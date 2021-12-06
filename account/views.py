from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from account.forms import RegistrationForm
from django.contrib import messages


# Create your views here.
class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations! Registration Successful!")
            form.save()
        return render(request, 'account/register.html', {'form': form})


@login_required
def profile(request):
    # addresses = Address.objects.filter(user=request.user)
    # orders = Order.objects.filter(user=request.user)
    # return render(request, 'account/profile.html', {'addresses': addresses, 'orders': orders})
    return render(request, 'account/profile.html')
