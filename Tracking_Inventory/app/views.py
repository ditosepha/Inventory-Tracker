from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import AddItem
# Create your views here.
def ladning_page(request):
    return render(request, 'index.html')

def inventory(request):
    items = Item.objects.all()
    if request.method == "POST":
        form = AddItem(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else: 
        form = AddItem()
    context = {
        "items": items,
        "form": form,
    }
    return render(request, 'inventory.html', context)

def delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
    return redirect('inventory')
