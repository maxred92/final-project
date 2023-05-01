from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from product.models import Things
from .models import Profile


from .forms import SignUpForm, CustomPasswordForm, UserEditForm, ProfileEditForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return redirect('/users/login/', {'profile': profile})
    else:
        form = SignUpForm()
    

    return render(request, 'users/signup.html', {
        'form': form
    })

def profile(request):
    things = Things.objects.filter(created_by=request.user)

    return render(request, 'users/profile.html', {
        'things': things,
    })


class CustomPasswordChange(PasswordChangeView):
    form_class = CustomPasswordForm
    template_name='users/password_change.html'
    success_url = reverse_lazy('users:password_change_done')

    def form_valid(self, form):
        form.save()
        self.request.session.flush()
        logout(self.request)
        return super().form_valid(form)

def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('users:profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'users/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})