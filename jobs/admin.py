from django.contrib import admin
from .models import Company,addJob,userApply,company_schedule

# Register your models here.

admin.site.register(Company)
admin.site.register(addJob)
admin.site.register(userApply)
admin.site.register(company_schedule)
