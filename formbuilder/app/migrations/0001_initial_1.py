# Generated by Django 4.1.7 on 2023-03-29 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SelectField',
            fields=[
                ('field_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.field')),
                ('label', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('singleSelect', 'singleSelect')], default='text', max_length=20)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.form')),
            ],
            bases=('app.field',),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('select_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.selectfield')),
            ],
        ),
        migrations.CreateModel(
            name='InputField',
            fields=[
                ('field_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.field')),
                ('label', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('text', 'Text'), ('email', 'Email'), ('number', 'Number'), ('checkbox', 'Checkbox')], default='text', max_length=20)),
                ('placeholder', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('regex', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('regexErrorMessage', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('value', models.CharField(max_length=200)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.form')),
            ],
            bases=('app.field',),
        ),
    ]
