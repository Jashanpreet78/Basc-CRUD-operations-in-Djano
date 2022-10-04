
from django import forms
from .models import User

class AddUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('task_name','description','created_date','finished_date','status')
        widgets={
            'task_name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'created_date':forms.DateInput(attrs={'class':'form-control'}),
            'finished_date':forms.DateInput(attrs={'class':'form-control'}),
            'status':forms.TextInput(attrs={'class':'form-control'}),
        }
