from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/product_list_basic.html'


#def home(request):
#    products = Product.objects.all()
#    context = {"products": products}
#    return render(request, 'catalog/product_list_basic.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


#def product_detail(request, pk):
#    product = Product.objects.get(pk=pk)
#    context = {"product": product}
#    return render(request, 'catalog/product_detail.html', context)


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'




#def contacts(request):
#    if request.method == 'POST':
#        name = request.POST.get('name')
#        phone = request.POST.get('phone')
#        message = request.POST.get('message')
#        print(f'{name} ({phone}): {message}')
#    return render(request, 'catalog/contacts.html')
