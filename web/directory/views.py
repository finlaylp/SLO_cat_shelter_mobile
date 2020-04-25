from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect 

from .forms import ClientForm
from .models import Client

# Create your views here.
def index(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client(request):
    client_id = request.GET.get('id')
    print(client_id)
    client = Client.objects.get(id=client_id)
    return render(request, 'client.html', {'client': client})

def help(request):
    return render(request, 'help.html')

def add_client(request):
   if request.method == 'POST':
      form = ClientForm(request.POST)
      if form.is_valid():
         data = form.cleaned_data
         client = Client(first_name = data.get('first_name'),
                         last_name = data.get('last_name'),
                         birthday = data.get('birthday'),
                         location = data.get('location'))
         client.save()

         return HttpResponseRedirect('view_clients')
   else:
      form = ClientForm()

   return render(request, 'add_client.html', {'form': form})

def view_clients(request):
   clients = Client.objects.all()
   return render(request, 'view_clients.html', {'clients': clients})
