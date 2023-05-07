from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from product.models import Things

from .forms import (CustomPasswordForm, ProfileEditForm, SignUpForm,
                    UserEditForm)
from .models import Profile

""" View for registering a user and creating a profile on the site """


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        profile_form = ProfileEditForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return redirect("/users/login/", {"profile": profile})
    else:
        form = SignUpForm()
        profile_form = ProfileEditForm()

    return render(
        request, "users/signup.html", {"form": form, "profile_form": profile_form}
    )


""" Presentation of the profile and its products """


def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    things = Things.objects.filter(created_by=request.user)

    return render(request, "users/profile.html", {"things": things, "profile": profile})


""" Change password view """


class CustomPasswordChange(PasswordChangeView):
    form_class = CustomPasswordForm
    template_name = "users/password_change.html"
    success_url = reverse_lazy("users:password_change_done")

    def form_valid(self, form):
        form.save()
        self.request.session.flush()
        logout(self.request)
        return super().form_valid(form)


""" Profile edit view """


def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("users:profile")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(
            request,
            "users/edit.html",
            {"user_form": user_form, "profile_form": profile_form},
        )
