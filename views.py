from django.shortcuts import render,get_object_or_404
from django.shortcuts import render,redirect
from .models import blog
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from bloging.settings import EMAIL_HOST_USER
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

@login_required
def home(request):
	return redirect('login')

def loginview(request):
	username=request.POST['username']
	password=request.POST['password']
	user=authenticate(request,username=username,password=password)
	if user is not None:
		login(request, user)
		return  redirect('add')
	else:
		return render(request,"login.html")	
										

def logout_view(request):
	logout(request)
	return redirect('login')


def sign_up(request):
	form=UserCreationForm(request.POST)
	if request.method=="POST":
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password1')
			user=authenticate(request,username=username,password=password)
			login(request,user)
			return redirect('home')
	else:
		form=UserCreationForm()
	return render(request,'registration/sign_up.html',{'form':form})


def Resethome(request):
	return render(request,'registration/ResetPassword.html')


def resetPassword(request):
	responseDic={}
	try:
		username=request.POST['uname']
		recepient=request.POST['email']
		pwd=request.POST['password']
		subject="Password reset"
		try:
			user=User.objects.get(username=username)
			if user is not None:
				user.set_password(pwd)
				user.save()
				message="Your Password Was Changed"
				send_mail(subject,message, EMAIL_HOST_USER, [recepient])
				responseDic["errmsg"]="Password Reset Successfully"
				return render(request,"registration/ResetPassword.html",responseDic)
		except Exception as e:
			print(e)
			responseDic["errmsg"]="Email doesnot exist"
			return render(request,"registration/ResetPassword.html",responseDic)
	except Exception as e:
			print(e)
			responseDic["errmsg"]="Failed to reset password"
			return render(request,"registration/ResetPassword.html",responseDic)

def blogview(request):
	bglist=blog.objects.all()
	return render(request,"blogadmin.html",{'blg':bglist})
		
def add1(request):
	responseDic={}
	try:
		title=request.POST['title']
		body=request.POST['body']
		bglist=blog(title=title,body=body)
		bglist.save()
		responseDic["msg1"]="Blog added"
		return render(request,"blogadmin.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Blog cannot be added"
		return render(request,"blogadmin.html",responseDic)

def edit1(request):
	try:
		title=request.POST['title']
		newtitle=request.POST['newtitle']
		bglist=blog.objects.get(id=1)
		bglist.title=newtitle
		bglist.save()
		
		return render(request,"blogadmin.html",{'msg3':"Titile updated"})
	except Exception as e:
		return render(request,"blogadmin.html",{'msg3':"Title can not be updated"})

def edit2(request):
	try:
		body=request.POST['body']
		newbody=request.POST['newbody']
		bglist=blog.objects.get(id=1)
		bglist.body=newbody
		bglist.save()
		
		return render(request,"blogadmin.html",{'msg4':"Content updated"})
	except Exception as e:
		return render(request,"blogadmin.html",{'msg4':"Content can not be updated"})

def dltblog1(request):
	try:
		title=request.POST['title']
		body=request.POST['body']
		bglist=blog.objects.filter(title=title,body=body)
		bglist.delete()
		return render(request,"blogadmin.html",{'msg5':"Blog Deleted"})
	except Exception as e:
		return render(request,"blogadmin.html",{'msg5':"Blog can not be Deleted"})


def blogview1(request):
	bglist=blog.objects.all()
	return render(request,"index.html",{'blg1':bglist})


def header(request):
	return render(request,"header.html")

def index(request):
	return render(request,"index.html")

