# Generated by Django 5.0.1 on 2024-01-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('Gender', models.CharField(max_length=25)),
                ('PhoneNumber', models.CharField(max_length=12)),
                ('DOB', models.CharField(max_length=50)),
                ('SelectMembershipplan', models.CharField(max_length=200)),
                ('SelectTrainer', models.CharField(max_length=55)),
                ('Reference', models.CharField(max_length=55)),
                ('Address', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=155)),
                ('price', models.IntegerField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('gender', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=25)),
                ('salary', models.CharField(max_length=25)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
