from django.form import ModelForm 
from .models import Comment



class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ['body']