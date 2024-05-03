from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from pytils.translit import slugify

from catalog.models import Product, BlogPost, Category


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


class BlogPostListView(ListView):
    model = BlogPost

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блоговая запись'
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication_sing=True)
        return queryset


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = [
        'title',
        'content',
        'preview',
        'publication_sing',
        'number_of_views'
        ]
    template_name = 'catalog/blog_post_form.html'
    success_url = reverse_lazy('catalog:blogpost_form')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание блоговой записи'
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = [
        'title',
        'content',
        'preview',
        'publication_sing',
        'number_of_views'
    ]
    template_name = 'catalog/blog_post_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование блоговой записи'
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('catalog:blogpost_detail', kwargs={'pk': self.object.pk})


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blogpost_detail.html'
    success_url = reverse_lazy('catalog:blogpost_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        blogpost_item = self.get_object()
        context['blogpost_item'] = blogpost_item
        context['title'] = f'Запись в блоге #{blogpost_item.id}'
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:blogpost_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление блоговой записи'
        return context
