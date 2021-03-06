from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from cgm.models import UserProfile #, Comment #, Message, Picture
#from csn.models import Event, Group
import hashlib

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'login', 'required':''})) # Tj change forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password', 'required':''})) # Tj Styling forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

    def clean(self):
        email = self.cleaned_data.get('email')
        try:
            u = User.objects.get(email=email)
        except User.DoesNotExist:
            return self.cleaned_data

        self._errors['email'] = [u'Email is already in use']
        return self.cleaned_data

class SettingsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('url', 'gender', 'birthdate', 'bio',)

    def clean(self):
        super(forms.ModelForm, self).clean()
        if ' ' in self.cleaned_data.get('url'):
            self._errors['url'] = [u'URL cannot contain spaces.']
        return self.cleaned_data

#class GroupForm(forms.ModelForm):
#    def __init__(self, *args, **kwargs):
#        try:
#            user = kwargs.pop('user')
#            super(GroupForm, self).__init__(*args, **kwargs)
#            friends = user.get_profile().friends.all()
#            choices = [(x.pk, x.get_profile()) for x in friends]
#            self.fields['members'].widget = FilteredSelectMultiple('Friends',
#                    False, choices=choices)
#        except KeyError:
#            # if user isn't set, prevent any chance of the widget
#            # being populated with all users.
#            super(GroupForm, self).__init__(*args, **kwargs)
#            self.fields['members'].queryset = User.objects.none()
#
#    class Meta:
#        model = Group

class ChangePassForm(forms.Form):
    old_pass = forms.CharField(widget=forms.PasswordInput)
    new_pass1 = forms.CharField(widget=forms.PasswordInput)
    new_pass2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        super(forms.Form, self).clean()
        pass1 = self.cleaned_data.get('new_pass1')
        pass2 = self.cleaned_data.get('new_pass2')
        if pass1 != pass2:
            self._errors['new_pass1'] = [u'Passwords do not match.']
        return self.cleaned_data

#class MessageForm(forms.ModelForm):
#    class  Meta:
#        model = Message
#        fields = ('recipient', 'subject', 'body')
#        widgets = {
#            'body': forms.Textarea(attrs={'cols': 80, 'rows': 7}),
#        }

 #   def clean(self):
 #       super(forms.ModelForm, self).clean()
 #       subject = self.cleaned_data.get('subject')
 #       if subject.isspace():
 #           self.cleaned_data['subject'] = 'No Subject'

  #      recipient = self.cleaned_data.get('recipient')
  #      author = self.instance.author
  #      if recipient not in author.get_profile().friends.all():
  #          self._errors['url'] = [u'User not in your friends.']

#        return self.cleaned_data

#class CommentForm(forms.ModelForm):
#    class Meta:
#        model = Comment
#        fields = ('post', 'public')
#        widgets = {
#            'post': forms.Textarea(attrs={'cols': 80, 'rows': 7}),
#        }

#class AlbumForm(forms.Form):
#    name = forms.CharField()

#class PictureForm(forms.ModelForm):
#    class Meta:
#        model = Picture
#        fields = ('image', 'caption',)

#class EventForm(forms.ModelForm):
#    class Meta:
#        model = Event
#        fields = ('title', 'description', 'datetime')

#class SearchForm(forms.Form):
#    name = forms.CharField(required=False)
#    email = forms.EmailField(required=False)

#    def clean(self):
#        name = self.cleaned_data.get('name')
#        #If name field is set, verify it is correct
#        if len(name) > 0:
#            name_l = name.split(' ')
#            if len(name_l) != 2:
#                self._errors['name'] = [u'Use first name and last name']
#        return self.cleaned_data