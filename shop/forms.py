from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "لطفا نام کاربری را وارد کنید  "}),
        label="Username",
        validators=[
            validators.MaxLengthValidator(limit_value=20, message="Username must be at most 20 characters."),
            validators.MinLengthValidator(8, message="Username must be at least 8 characters.")
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': "ایمیل را وارد کنید "}),
        label="Email",
        validators=[validators.MaxLengthValidator(limit_value=20, message="Invalid email.")]
    )

    class Meta:
        model = User
        fields = ['first_name', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password and re_password and password != re_password:
            raise forms.ValidationError("Passwords do not match.")

    def save(self):
        user_name = self.cleaned_data["user_name"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        User.objects.create_user(username=user_name, email=email, password=password)
