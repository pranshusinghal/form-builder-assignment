# Generated by Django 4.1.7 on 2023-03-30 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_field_field_name_alter_form_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payload', models.JSONField()),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.form')),
            ],
        ),
    ]