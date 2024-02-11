from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User as AuthUser

class Company(models.Model):
    name = models.CharField(max_length=100)
    employees = models.IntegerField(default=0)  # For simplicity, assuming number of employees
    # Other fields...

class Client(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=15)  # Assuming phone number is string for simplicity
    # Other fields...

class ClientUsers(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)