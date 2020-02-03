from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

# Create your views here.

class LoginView(View):
    def get(self, request, *args,**kwargs):
        context ={'parm1':'hello', 'parm2': 'django', 'auth':request.user.is_authenticated}
        return render(request, 'registration/login.html', context=context)

def signup(request):
    if request.method == "POST":
        if request.POST["password1"]== request.POST["password_confirm"]:
            user =User.objects.create_user(
                username=request.POST["username"], password= request.POST["password1"])

            auth.login(request, user)
            return HttpResponseRedirect(reverse('book:login'))
        return render(request, "book/signup.html")
    return render(request, 'book/signup.html')

# Add facebook social login below