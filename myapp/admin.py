from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Company, Client, ClientUsers

admin.site.register(Company)
admin.site.register(Client)
admin.site.register(ClientUsers)