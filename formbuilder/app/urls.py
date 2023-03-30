from django.urls import path, include

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("account/", include("django.contrib.auth.urls"), name="login"),
  path("logout/", views.logout_view, name="logout"),
  path("signup/",  views.SignUp.as_view(), name="signup"),
  path("form/list", views.FormList.as_view(), name="formlist"),
  path("form/create", views.FormCreate.as_view(), name="formcreate"),
  path('form/update/<int:form_id>/', views.edit_form, name='formupdate'),
  path("form/delete/<pk>", views.FormDelete.as_view(), name="formdelete"),
]