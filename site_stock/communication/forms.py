from django import forms

from .models import Message

class MessageForm(forms.ModelForm):
    """ Class for adding a comment with a user """
    
    class Meta:
        model = Message
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            )
        }
