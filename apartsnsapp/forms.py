from django import forms
from .models import ApartsnsModel , CommentModel

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=50, error_messages={'required': '入力してください'})
    class Meta:
        model = ApartsnsModel
        fields = ('name','title' , 'content')

class CommentCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = CommentModel
        fields = ('name', 'text')