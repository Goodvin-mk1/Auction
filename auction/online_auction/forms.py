from django.forms import Form, ModelForm, EmailInput, TextInput, Textarea

from .models import FeedBack, Lot, Bet


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


class LotForm(ModelForm):
    class Meta:
        model = Lot
        fields = ('name', 'category', 'image', 'description')


class BetForm(ModelForm):
    class Meta:
        model = Bet
        fields = ('user', 'event', 'bet')


