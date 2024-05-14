from django.contrib import admin
from . models import company,Interview,Question,User_Answer,Report

# Register your models here.
admin.site.register(company)
admin.site.register(Interview)
admin.site.register(Question)
admin.site.register(User_Answer)
admin.site.register(Report)
