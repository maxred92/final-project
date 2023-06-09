from django import forms

from store.tasks import send_feedback_email_task

class FeedbackForm(forms.Form):
    """ Class for creating a feedback form """
    
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={"placeholder": "Your email address"}),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={"class": "w-full py-4 px-6 rounded-xl border"}),
    )

    def send_email(self):
        """ Function to send a message to the user about receiving feedback """
        
        send_feedback_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["message"]
        )
