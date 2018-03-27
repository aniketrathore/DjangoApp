from django.shortcuts import render
from Registration.form import UserForm, UserProfileInfoForm, DeleteUser, UpdateUserPass
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    model = User.objects.order_by()
    return render(request, 'htmls/index.html', {'key1': model})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'htmls/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_update_password(request):
    form = UpdateUserPass
    if request.method == "POST":
        form = UpdateUserPass(request.POST)

        if form.is_valid():
            var = form.cleaned_data['username']
            var2 = form.cleaned_data['password']
            u = User.objects.get(username__exact=var)
            u.set_password(str(var2))
            u.save()
            return render(request, 'htmls/index.html')
        else:
            return HttpResponse("Could't Update, Try Again")

    else:
        return render(request, 'htmls/update_pass.html', {'key': form})


def user_delete(request):
    form = DeleteUser
    if request.method == "POST":
        form = DeleteUser(request.POST)

        if form.is_valid():
            var = form.cleaned_data['username']
            var2 = str(var)
            User.objects.filter(username=var2).delete()
            return render(request, 'htmls/index.html')

    else:
        return render(request, 'htmls/delete_user.html', {'key': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            return HttpResponse("Invalid Login Details, Refresh Page To Login Again.")

    else:
        return render(request, 'htmls/login.html', {})


def api_list(request):
    return render(request, 'htmls/api_list.html')
