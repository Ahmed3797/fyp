from django import forms

USER_CHOICES = [
    ('candidate', 'Candidate'),
    ('company', 'Company'),
]

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=USER_CHOICES, widget=forms.RadioSelect)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
             self.add_error('password',"Passwords do not match")

        return cleaned_data
    


    