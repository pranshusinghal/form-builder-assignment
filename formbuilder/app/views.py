from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

# Complete your SignUp view below:
class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

def logout_view(request):
  logout(request)
  return redirect("home")

@login_required
def home(request):
  context = {"name": request.user}
  return render(request, "app/home.html", context)
