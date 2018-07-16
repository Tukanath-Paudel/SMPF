from django.shortcuts import render,redirect
from stock.forms import RegistrationForm
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def enquiry(request):
    return render(request, 'accounts/enquiry.html')

def index(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method =='GET':
        context={
            'form': RegistrationForm(),
        }
        return render(request, 'accounts/regform.html', context)
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/login')
        else:
            return render(request, 'accounts/regform.html',{'form': form})





