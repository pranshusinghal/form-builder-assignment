from django.db import models

""" Form and Field are in One to Many relationship """
class Form(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return '/form/list'

    def __str__(self):
        return "Form - " + self.name

class Field(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    required = models.BooleanField(default=False)

class InputField(Field):
    TYPE_CHOICES = (
        ('text', 'Text'),
        ('email', 'Email'),
        ('number', 'Number'),
        ('checkbox', 'Checkbox'),
    )

    label = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='text')
    placeholder = models.CharField(max_length=200, default="", null=True, blank=True)
    regex = models.CharField(max_length=200, default="", null=True, blank=True)
    regexErrorMessage = models.CharField(max_length=200, default="", null=True, blank=True)
    value = models.CharField(max_length=200)

class SelectField(Field):
    TYPE_CHOICES = (
        ('singleSelect', 'singleSelect'),
    )
    label = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='text')

class Option(models.Model):
    select_field = models.ForeignKey(SelectField, on_delete=models.CASCADE)
    label = models.CharField(max_length=200)
    value = models.CharField(max_length=200)