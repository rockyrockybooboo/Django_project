from django import forms
from .models import Membar
class MembarForm(forms.ModelForm):
  class Meta:
    model = Membar
    fields = ['name' , 'age' , 'email' , 'passwd']