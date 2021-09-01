from django.contrib import admin
from major.models import MajorPost
from accounts.models import User

admin.site.register(MajorPost)
admin.site.register(User)
