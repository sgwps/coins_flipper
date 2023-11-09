from typing import Any
from django import forms


class MachineParams(forms.Form):
    def clean(self):
        cleaned_data = super().clean()
        coin_number = cleaned_data.get("coin_number")
        exits_to_continue = cleaned_data.get("exits_to_continue")
        exits_event_happened = cleaned_data.get("exits_event_happened")

        if 2 ** coin_number > exits_to_continue + exits_event_happened:
            raise forms.ValidationError("The numbers are not valid.")

        return cleaned_data

    coin_number = forms.IntegerField(label="Coin number: ", min_value=1, max_value=15)
    exits_to_continue = forms.IntegerField(label="Exits to continue: ")
    exits_event_happened = forms.IntegerField(label="Exits to continue: ")


