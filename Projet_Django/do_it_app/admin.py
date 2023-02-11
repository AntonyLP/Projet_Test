from django.contrib import admin

from do_it_app.models.profile import Profile
from do_it_app.models.task import Task

# Register your models here.
admin.site.register(Task)
admin.site.register(Profile)
