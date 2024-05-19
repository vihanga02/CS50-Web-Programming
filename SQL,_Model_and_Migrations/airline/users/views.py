from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
def login_request(request):
    return render(request, "user/login.html") 