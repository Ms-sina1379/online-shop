# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.core import validators
# from django.contrib.auth.models import User
#
# class register_form(UserCreationForm):
#     first_name = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': "لطفا نام کاربری را وارد کنید  "}),
#         label="Username",
#         validators=[
#             validators.MaxLengthValidator(limit_value=20, message="Username must be at most 20 characters."),
#             validators.MinLengthValidator(8, message="Username must be at least 8 characters.")
#         ]
#     )
#
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'placeholder': "ایمیل را وارد کنید "}),
#         label="Email",
#         validators=[validators.MaxLengthValidator(limit_value=20, message="Invalid email.")]
#     )
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'email', 'password1', 'password2']
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         re_password = cleaned_data.get("re_password")
#
#         if password and re_password and password != re_password:
#             raise forms.ValidationError("Passwords do not match.")
#
#     def save(self):
#         user_name = self.cleaned_data["user_name"]
#         email = self.cleaned_data["email"]
#         password = self.cleaned_data["password"]
#         User.objects.create_user(username=user_name, email=email, password=password)
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "Enter username"}),
        label="Username",
        validators=[
            validators.MaxLengthValidator(limit_value=20, message="Username must be at most 20 characters."),
            validators.MinLengthValidator(8, message="Username must be at least 8 characters.")
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': "Enter email"}),
        label="Email",
        validators=[validators.MaxLengthValidator(limit_value=20, message="Invalid email.")]
    )

    class Meta:
        model = User
        fields = ['first_name', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user