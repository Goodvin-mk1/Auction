from django.forms import Form, ModelForm, EmailInput, TextInput, Textarea

from .models import FeedBack


class FeedBackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = ('message', 'email')
        widgets = {
            'email': EmailInput(
                attrs={
                    'type': 'email',
                    'name': 'email',
                    'class': 'form-control',
                    'id': 'email',
                    'placeholder': 'Ваш email',
                    'required': True
                }
            ),
            'message': Textarea(
                attrs={
                    'name': 'message',
                    'class': 'form-control',
                    'rows': '5',
                    'placeholder': 'Ваше сообщение',
                    'required': True
                }
            )
        }


