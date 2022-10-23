from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class DataForm(forms.Form):
    date_time = forms.DateTimeField()
    arrival_departure = forms.CharField(max_length=1)  # change
    number_of_pass = forms.IntegerField()
    parking_place = forms.IntegerField()
    gate_number = forms.IntegerField()

    # threshold_value = forms.IntegerField(label='Пороговое значение', min_value=1, required=False)
    # crusher_slot_size = forms.IntegerField(label='Размер щели дробилки (мм)', min_value=1, required=False)
    # ore_data = forms.FileField(label='Данные', required=False)