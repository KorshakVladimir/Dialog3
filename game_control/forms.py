# -*- coding: utf-8 -*-

from django import forms
from . models import Game

class GameForm(forms.ModelForm):
    error_css_class = 'error_form_add_game'
    class Meta:
        
        model = Game
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'add_game_form, form-control'}),
        }

    def clean_name(self):
        data = self.cleaned_data['name']
        unic_name = Game.objects.filter(name = data)
        if unic_name :

            raise forms.ValidationError("Игра \" %s \" уже существует" % data )


        return data 
