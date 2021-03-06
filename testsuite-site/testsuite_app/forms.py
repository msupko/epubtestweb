from django.forms import ModelForm
from django import forms
from models import *
from django.forms.models import inlineformset_factory

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    def is_valid(self):
        return len(self.username) > 0 and len(self.password) > 0


class ReadingSystemForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = ReadingSystem
        fields = ('name', 'version', 'operating_system', 'locale', 'sdk_version')

class ResultForm(ModelForm):
   class Meta:
        model = Result
        fields = ('result', 'notes', 'publish_notes')
        
        # clear the 'result' label: it's visually distracting
        labels = {
            'result': '',
        }

        # use a custom text area
        widgets = {
            'notes': forms.Textarea(attrs={'cols': 40, 'rows': 3, 'title': 'Notes'}),
        }

ResultFormSet = inlineformset_factory(Evaluation, Result, extra=0, can_delete=False, form = ResultForm)
