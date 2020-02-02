from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

# Create your views here.

class LoginView(View):
    def get(self, request, *args,**kwargs):
        context ={'parm1':'hello', 'parm2': 'django', 'auth':request.user.is_authenticated}
        return render(request, 'registration/login.html', context=context)
