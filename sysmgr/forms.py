from django import forms
from models import User
from sysmgr import tools

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["password"] = forms.CharField(max_length=16, widget=forms.PasswordInput)

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.password = tools.Cryptor().encrypt(user.password)
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'
