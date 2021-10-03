from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, TextInput
from restaurantapp.models import Client



class LoginForm(AuthenticationForm):

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class RegisterView(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username','first_name' , 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-group'

    phonenumber = CharField(
        label='Phone number', widget= TextInput,max_length=15
    )

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        result = super().save(commit)
        phonenumber = self.cleaned_data['phonenumber']
        profile = Client(phonenumber=phonenumber,user = result)
        if commit:
            profile.save()
        return result
