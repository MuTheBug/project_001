from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite


class MyOwnSite(AdminSite):
    site_title = "Foo Admin"
    site_header = '9Th Grade administration'


myapp_admin_site = MyOwnSite(name='myapp_admin')

myapp_admin_site.register(Chapter, )
myapp_admin_site.register(Text, )
myapp_admin_site.register(TextQuestion, )
myapp_admin_site.register(TFQuestions, )
myapp_admin_site.register(Multiples, )
myapp_admin_site.register(MakeQuestions, )
myapp_admin_site.register(Paragraphs, )
myapp_admin_site.register(CorrectTheMistake, )
myapp_admin_site.register(CTMistake,)
# Attach your models to it using the usual my_admin_site.register()
# Attach it to the URLconf
