from django.utils import timezone
from django import forms
from .models import Interview, Question


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['name','description','image', 'application_end_date']
    
    widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'name':forms.TextInput(attrs={'placeholder':'Enter the name of the Interview'})
        }
    
    def __init__(self, *args, **kwargs):
        super(InterviewForm, self).__init__(*args, **kwargs)

        # Set the input format for date fields
        
        
    def clean(self):
        cleaned_data = super().clean()
        
        application_end_date = cleaned_data.get('application_end_date')
        

        if application_end_date :
            now = timezone.now()
            current_date = now.date()
            
            if application_end_date < current_date:
                self.add_error('application_end_date', 'Application end date must be in the future.')

        return cleaned_data
    

class InterviewDateForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date >= end_date:
                self.add_error('start_date', "Start date must be before end date.")
                self.add_error('end_date', "End date must be after start date.")

            interview = self.instance
            if start_date < interview.application_end_date:
                self.add_error('start_date', "Start date must be before application end date.")

        return cleaned_data
    

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [ 'question_text', 'answer','image']

QuestionFormSet = forms.modelformset_factory(Question, form=QuestionForm, extra=1)
