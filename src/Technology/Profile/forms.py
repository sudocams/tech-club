from django import forms
from Profile.models import Applications

class ApplicationModelForm(forms.ModelForm):
    
    
    class Meta:
        model = Applications
        fields = ['name', 'number', 'email', 'admin_no', 'langauges', 'team', 'bio']
   

