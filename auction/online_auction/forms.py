from django.forms import Form, ModelForm, EmailInput, TextInput, Textarea, DecimalField

from .models import FeedBack, Lot, Bet, Event


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


class BetForm(Form):
    class Meta:
        model = Bet
        fields = ('bet',)
        widgets = {
            'bet': DecimalField(
                error_messages={
                    'required': 'Please enter your name'
                }

            )
        }


class AuctionAddForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'buyout_price', 'start_price', 'end_date')
