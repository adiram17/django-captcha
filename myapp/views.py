from django.shortcuts import render
from .forms import CaptchaTestForm

def home(request):
    if request.method=="POST":
        form=CaptchaTestForm(request.POST)
        if form.is_valid():
            print("Captcha validation success")
        else:
            print("Captcha validation failed")
    form=CaptchaTestForm()
    return render(request,"home.html",{"form":form})