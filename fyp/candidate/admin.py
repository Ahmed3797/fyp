from django.contrib import admin
from .models import candidate,Skill,Eduaction,CVSubmission,ApprovedCandidate

# Register your models here.
admin.site.register(candidate)
admin.site.register(Skill)
admin.site.register(Eduaction)
admin.site.register(CVSubmission)
admin.site.register(ApprovedCandidate)