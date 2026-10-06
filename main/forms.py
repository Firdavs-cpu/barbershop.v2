from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'date':forms.DateTimeInput(attrs={
                'type': 'datetime-local'
            })
        }