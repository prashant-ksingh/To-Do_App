from django import forms
from .models import User,Todo


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
