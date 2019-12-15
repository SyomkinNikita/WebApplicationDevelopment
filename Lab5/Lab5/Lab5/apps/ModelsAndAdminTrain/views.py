from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from Lab5.Lab5.apps.ModelsAndAdminTrain.form import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                my_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=my_password)
                login(request, user)
                return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
