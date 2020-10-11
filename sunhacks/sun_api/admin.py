from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Achievement,User,Fork,Course,Roadmap
# Register your models here.
#admin.site.register(User)
admin.site.register(Roadmap)
admin.site.register(Course)
admin.site.register(Achievement)
admin.site.register(Fork)
admin.site.register(User,UserAdmin)