from django import forms
from . models import Answer,Game

class AnswerForm(forms.ModelForm):
    class Meta:
        
        model = Answer
        fields = ('text_answer',)


