from django import forms

from .models import ApartsnsModel

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100, error_messages={'required': '入力必須です！！！！'})

    class Meta:
        model = ApartsnsModel
        fields = ('title' , 'content' , 'author' , 'images')