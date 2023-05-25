from django import forms

from .models import Things

class AddThingForm(forms.ModelForm):
    """ Class for adding a product to the site """
    
    class Meta:
        model = Things
        fields = (
            "category",
            "name",
            "description",
            "price",
            "image",
        )
        widgets = {
            "category": forms.Select(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            ),
            "name": forms.TextInput(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            ),
            "description": forms.Textarea(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            ),
            "price": forms.TextInput(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            ),
            "image": forms.FileInput(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            ),
        }


class EditThingForm(forms.ModelForm):
    """ Class for editing a product on the site """

    class Meta:
        model = Things
        fields = ("category", "name", "description", "price", "image", "is_sold")
        widgets = {
            "category": forms.Select(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            ),
            "name": forms.TextInput(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            ),
            "description": forms.Textarea(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            ),
            "price": forms.TextInput(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            ),
            "image": forms.FileInput(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            ),
        }
