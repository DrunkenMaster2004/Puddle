from django.shortcuts import render,redirect
from item.models import Category, Item
from .forms import SignupForm
# Create your views here.
def index(request):
    items = Item.objects.filter(is_Sold=False)
    catergories = Category.objects.all()
    return render(request, './core/index.html', {
        'items':items,
        'categories':catergories,
    })

def contact(request):
    return render(request, './core/contact.html')

def sp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    form = SignupForm()
    return render(request, './core/sp.html',{
         'form':form,
    })