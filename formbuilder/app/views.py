from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Form, FormConfig
from .forms import FormCreateForm

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

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

class FormList(LoginRequiredMixin, ListView):
  model = Form

class FormCreate(LoginRequiredMixin, CreateView):
  model = Form
  template_name = "app/create_form.html"
  form_class = FormCreateForm

@login_required
def edit_form(request, form_id):
    form = Form.objects.get(id=form_id)
    input_fields = form.inputfield_set.all()
    select_fields = form.selectfield_set.all()
    # select fields and corresponding options map
    select_options_map = {}
    for field in select_fields:
      select_options_map[(field.field_name, field.label)] = field.option_set.all()

    if request.method == 'POST':
      # if form gets submitted, then save the entered details inside FormConfig Table
      payload = {}
      for key, value in request.POST.items():
        if key != "csrfmiddlewaretoken":
          payload[key] = False if value=="on" else value
      # saving the form details inside `FormConfig` Table
      form_config = FormConfig()
      form_config.form = form
      form_config.payload = payload
      form_config.save()
      # upon saving config, redirect to `formlist` URL
      return redirect('formlist')

    return render(request, 'app/edit_form.html', 
                {
                'form': form, 
                'input_fields': input_fields, 
                'select_options_map': select_options_map
                }
            )

class FormDelete(LoginRequiredMixin, DeleteView):
  model = Form
  template_name = "app/delete_form.html"
  success_url = "/form/list"