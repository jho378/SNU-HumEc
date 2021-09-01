from django.shortcuts import render, redirect
from .forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # 중복저장 방지
            user.set_password(form.cleaned_data["password"])  # 비밀번호 암호화
            user.save()
            return redirect("accounts:done")

    form = SignupForm()
    ctx = {
        "form": form
    }
    return render(request, "accounts/signup.html", ctx)


def done(request):
    return render(request, "accounts/done.html")
