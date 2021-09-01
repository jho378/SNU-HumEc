from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, authenticate


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # 중복저장 방지
            user.set_password(form.cleaned_data["password"])  # 비밀번호 암호화
            user.save()
            return redirect("accounts:done")
    else:
        form = SignupForm()
    ctx = {
        "form": form
    }
    return render(request, "accounts/signup.html", ctx)


def done(request):
    return render(request, "accounts/done.html")


def signin(request):  # django 내장 login 함수와 이름 겹치지 않게
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("core:core")

        ctx = {
            "form": form,
            "error": "아이디나 비밀번호가 일치하지 않습니다.",
        }
        return render(request, "accounts/login.html", ctx)
    else:
        form = LoginForm()
    ctx = {
        "form": form
    }
    return render(request, "accounts/login.html", ctx)
