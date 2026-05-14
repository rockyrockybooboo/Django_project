from django.shortcuts import render , redirect
from .models import Membar
from .forms import MembarForm
# Create your views here.
def home(request):
  Membars = Membar.objects.all
  return render(request , 'website/home.html' , {'Membars': Membars})

def register(request):
  if request.method == 'POST':
    form = MembarForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('/')
  else:
    form = MembarForm()
   

  
  return render(request , 'website/Register_form.html' , {'form' : form})

# This is a comment 
