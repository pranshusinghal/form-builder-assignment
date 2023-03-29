from django.contrib import admin
from .models import Form, InputField, SelectField, Option

admin.site.register(Form)
admin.site.register(InputField)
admin.site.register(SelectField)
admin.site.register(Option)