from django.db import models

""" Form and Field are in One to Many relationship """
class Form(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return '/form/list'

    def __str__(self):
        return "Form - " + self.name

class Field(models.Model):
    field_name = models.CharField(max_length=50, default="")
    required = models.BooleanField(default=False)

class InputField(Field):
    TYPE_CHOICES = (
        ('text', 'Text'),
        ('email', 'Email'),
        ('number', 'Number'),
        ('checkbox', 'Checkbox'),
    )
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='text')
    placeholder = models.CharField(max_length=50, default="", null=True, blank=True)
    regex = models.CharField(max_length=50, default="", null=True, blank=True)
    regexErrorMessage = models.CharField(max_length=50, default="", null=True, blank=True)

    def __str__(self):
        return "Input Field, Form: - " + self.form.name + ", Label: " + self.label + " - " + "Type: " + self.type

class SelectField(Field):
    TYPE_CHOICES = (
        ('singleSelect', 'singleSelect'),
    )
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='text')

    def __str__(self):
        return "Select Field, Form: - " + self.form.name + ", Label: " + self.label + " - " + "Type: " + self.type

class Option(models.Model):
    select_field = models.ForeignKey(SelectField, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.select_field.form.name + " Option: " + self.label

class FormConfig(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    payload = models.JSONField()

    def __str__(self):
        return "Form Config Data - " + self.form.name

