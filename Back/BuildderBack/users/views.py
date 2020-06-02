
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate, login , get_user
# Needed to Search
from django.contrib.auth.models import User

from django.db.models import Q

from .forms import UserForm, LoginForm
from .models import B_User

def user_list(request):
    queryset_list = B_User.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) 
        ).distinct()
    sessionName =""
    user_logged = request.session.get('user')
    if user_logged:
        userFirtsName = B_User.objects.get(email = user_logged)
        sessionName = userFirtsName.first_name
    context={
        "user_list":queryset_list,
        "title": "User List",
        "user_logged": sessionName
    }
    return render(request, "user_list.html",context)


def user_create(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.password = make_password(form.data['password'])
        instance.save()
        messages.success(request,"Register sucess")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form":form,
    }
    return render(request, "user_form.html",context)

def user_detail(request, user_id = None):
    instance = get_object_or_404(B_User, user_id = user_id)
    context = {
        "instance":instance,
    }
    return render(request, "user_detail.html",context)
    

def user_edit(request, user_id=None):
    if not request.user.is_staff or not  request.user.is_superuser:
        raise Http404
    
    instance = get_object_or_404(B_User, user_id = user_id)
    # if not request.user == instance.user:
    #         raise Http404
    form = UserForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.password = make_password(form.data['password'])
        instance.save()
        messages.success(request, "User Updated", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context = {
        "instance": instance,
        "form": form
    }
    return render(request,"user_form.html",context)


def user_delete(request, user_id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(B_User, user_id = user_id)
    instance.delete()
    messages.success(request,"Deleted")
    return redirect("users:list")

def user_login(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():

        authenticate(email =form.data['email'],password=form.data['password'])
        request.session['user'] = form.data['email']
        return redirect("users:list")
        
        # userget = get_object_or_404(B_User, email= form.data['email'])
        # encrypted = userget.password
        # if check_password(request.POST['password'],encrypted):
        #     return redirect("users:list")
    context = {
        "form":form
    }
    return render(request,"user_login.html",context)

def user_logout(request):
    try:
        del request.session['user']
        request.session.flush()
    except KeyError:
        pass
    return HttpResponse("<h1>Logout</h1>")

