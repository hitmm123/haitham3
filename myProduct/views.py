# Create your views here.
from django.shortcuts import render, redirect

from .forms import ProductForm




def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Assuming you have a view named 'product_list'
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
