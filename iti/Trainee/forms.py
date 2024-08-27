from django import forms
from django.db import models
from Account.models import Account
from .models import *

# class NewTrainee(forms.Form):
#     # trainee_id = models.AutoField(primary_key=True)
#     # name = forms.CharField(max_length=100, null=False)
#     # id_obj = forms.ChoiceField(choices=Account.getall())
#     # image = models.ImageField(upload_to='.images/', null=True, blank=True)


class NewTraineeModel(forms.ModelForm):
    class Meta:
        model=Trainee
        fields='__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter trainee name', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(NewTraineeModel, self).__init__(*args, **kwargs)
        self.fields['name'].required = True  
        self.fields['image'].required = True  
        self.fields['id_obj'].required = True