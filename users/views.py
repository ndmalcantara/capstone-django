from audioop import reverse
from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import User
from django.core.paginator import Paginator
from django.db.models import Q 
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist





def index(request):
    user_list = User.objects.all().order_by('-id')
    paginator = Paginator(user_list, 5)

    page_number = request.GET.get('page')

    user_list = paginator.get_page(page_number)

    return render(request, 'Template/index1.html' {'page_obj': user_list})

def search(request):
    term = request.GET.get('search', '')
    user_list = User.objects.filter(Q (user_fname__icontains=term) | Q (user_lname__icontains=term)).order_by('-id')

    paginator = Paginator(user_list, 5)

    page_number = request.GET.get('page')

    user_list = paginator.get_page(page_number)

    return render(request, 'Template/index1.html' {'page_obj': user_list})

def add(request):
    return render(request, 'Template/add.html')

def processadd(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    position = request.POST.get('position')
    if request.FILES.get('image'):
        user_pic = request.FILES.get('image')
    else:
        user_pic = 'profile_pic/image.jpg'
    try:
        n = User.objects.get(user_email=email)
        # number already exists
        return render(request, 'Template/add.html' , {'error message' : "Duplicated email : " + email})
    except ObjectDoesNotExist
        user = User.objects.create(user_email=email, user_fname=fname, user_lname=lname, user_position=position, user_image=user_pic)
        user.save()
        return HttpResponseRedirect('/users')

def detail(request, profile_id):
    try:
        user= User.objects.get(pk=profile_id)
    except User.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'Template/detail.html', {'user': user})

def delete(request, profile_id):
    User.objects.filter(id=profile_id).delete()
    return HttpResponseRedirect('/users')

def edit(request, profile_id):
    try:
        user= User.objects.get(pk=profile_id)
    except User.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'Template/edit.html', {'user': user})

def processedit(request, profile_id):
    user= get_object_or_404(User, pk=profile_id)
    profile_pic = request.FILES.get('image')
    try:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        position = request.POST.get('position')
    except (KeyError, User.DoesNotExist):
        return render(request, 'Template/detail.html' , {
            'user': user,
            'error_message': "Problem updating record",
        })
    else:
        user_profile = User.objects.get(id=profile_id)
        user_profile.user_fname = fname
        user_profile.user_lname = lname
        user_profile.user_email = email
        user_profile.user_position = position
        if profile_pic:
            user_profile.user_image = profile_pic
        user_profile.save()
        return HttpResponseRedirect(reverse('users:detail', args=(profile_id,)))

