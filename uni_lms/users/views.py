from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard:mainpage")
        else:
            return HttpResponse("No!")
    else:
        form = AuthenticationForm()
    return render(request, "loginpage.html", {'form': form })
    
def test_view(request):
    return render(request, "test.html", {})