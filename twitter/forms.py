from django import forms


class MessageForm(forms.Form):
    content = forms.CharField(label="Message", max_length=160)
