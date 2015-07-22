# -*- coding: utf-8 -*-

from django import forms
from . models import Game

class GameForm(forms.ModelForm):
	
    class Meta:
        
        model = Game
        fields = ('name',)
        widgets = {
            'name': TextInput(attrs={'class': 'add_form_status'}),
        }

    def clean(self):
    	new_name = self.cleaned_data.get('name')
        # if (self.cleaned_data.get('email') !=
        #     self.cleaned_data.get('confirm_email')):

        #     raise ValidationError(
        #         "Email addresses must match."
        #     )

        return self.cleaned_data    
