# users/forms.py

from django.contrib.auth.forms import UserCreationForm

class CustomerUserCreationsForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", )