from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from .models import CVSubmission

# class CVSubmissionForm(forms.ModelForm):
#     cv = forms.FileField(
#         validators=[
#             FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])
#         ]
#     )

#     class Meta:
#         model = CVSubmission
#         fields = ['cv']