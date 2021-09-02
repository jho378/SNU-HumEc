from django.contrib import admin
from complaint.models import Complaint, ComplaintComment

admin.site.register(Complaint)
admin.site.register(ComplaintComment)
