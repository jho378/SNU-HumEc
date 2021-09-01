from django import forms
from . import models


class SignupForm(forms.ModelForm):
    # 필드명 오버라이드
    name = forms.CharField(label="이름")
    phone = forms.CharField(label="전화번호")
    username = forms.CharField(label="ID(마이스누 메일)")
    password1 = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ("name", "phone", "username", "password", "password1")
        widgets = {
            "password": forms.PasswordInput(),
        }

    def clean_password1(self):
        pw = self.cleaned_data.get("password")
        pw1 = self.cleaned_data.get("password1")

        if pw != pw1:
            raise forms.ValidationError("*비밀번호가 일치하지 않습니다")
        return pw1
