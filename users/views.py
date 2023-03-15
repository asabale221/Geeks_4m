from django.shortcuts import render
from .forms import UserReqistrationForm

class Register:
    pass

def register(request):
    if request.method == "POST":
        user_form = UserReqistrationForm
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return render(request, "registration/register_done.html", {"user": new_user})
    else:
        user_form = UserReqistrationForm()
    return render(request, "registration/register.html", {"form": user_form})