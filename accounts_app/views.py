from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

def home(request):
	return render(request, "homepage.html")
def register_request(request):
	return render(request, "register.html")
def login_request(request):
	return render(request, "login.html")