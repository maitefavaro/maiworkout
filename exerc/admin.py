from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(Treino)
admin.site.register(User)
admin.site.register(Exercicio)
#admin.site.register(User,UserAdmin)


# Register your models here.
