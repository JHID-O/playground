from django.shortcuts import render, redirect
from .forms import PlaygroundModelForm

def add_playground(request):
    if request.method == 'POST':
        form = PlaygroundModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playground_home')  # or any page you want
    else:
        form = PlaygroundModelForm()
    return render(request, 'add_playground.html', {'form': form})

def home(request):
    return render(request, 'playground_1.html')