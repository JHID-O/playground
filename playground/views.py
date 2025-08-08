from django.shortcuts import render, redirect
from .forms import PlaygroundModelForm
from .models import PlaygroundModel
import csv
from django.http import HttpResponse

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

def playground_table(request):
    phn_query = request.GET.get('phn', '')
    playground_data = []
    if phn_query:
        playground_data = PlaygroundModel.objects.filter(PHN=phn_query).order_by('PHN')
    return render(request, 'playground_table.html', {
        'playground_data': playground_data,
        'phn_query': phn_query
    })
    
def download_phn(request):
    phn_query = request.GET.get('phn', '')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="playground_{phn_query}.csv"'
    writer = csv.writer(response)
    writer.writerow(['Month', 'Year', 'PHN', 'Surname', 'Given Name', 'Middle Name', 'PS', 'ES', 'Status'])
    data = PlaygroundModel.objects.filter(PHN=phn_query).order_by('PHN')
    for item in data:
        writer.writerow([item.month, item.year, item.PHN, item.surname, item.given_name, item.middle_name, item.ps, item.es, item.status])
    return response