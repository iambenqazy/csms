from django.contrib import admin
from .models import StudentDetail, HouseName, ClassName, Programs, Subjects

# Register your models here.
admin.site.register(StudentDetail)
admin.site.register(HouseName)
admin.site.register(ClassName)
admin.site.register(Programs)
admin.site.register(Subjects)
