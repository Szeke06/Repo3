from django.forms import ModelForm
from .models import game , Test


class GameForm(ModelForm):
    class Meta :
        model = game
        fields = '__all__'


class TestForm(ModelForm):
    class Meta :
        model = Test
        fields ='__all__'

