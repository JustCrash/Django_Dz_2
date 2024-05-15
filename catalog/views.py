from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.forms import inlineformset_factory
from catalog.forms import ProductForm, VersionForm
from django.urls import reverse_lazy
from pytils.translit import slugify

from catalog.models import Product, BlogPost, Contacts, Version


class HomeListView(ListView):
    model = Product
    template_name = "catalog/product_list_basic.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Каталог товаров"
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_item"] = self.get_object()
        context["title"] = f'Продукт #{context["product_item"].name}'
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_from.html"
    success_url = reverse_lazy("catalog:product_list_basic")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Создание продукта"
        return context

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid()


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_from.html'
    success_url = reverse_lazy('catalog:product_list_basic')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = ProductFormset(instance=self.object)
        context['title'] = 'Изменить продукт'
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list_basic')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить продукт'
        return context


class ContactsView(TemplateView):
    model = Contacts
    template_name = "catalog/contacts.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        return context


class BlogPostListView(ListView):
    model = BlogPost

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Блоговая запись"
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication_sing=True)
        return queryset


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ["title", "content", "preview", "publication_sing", "number_of_views"]
    template_name = "catalog/blogpost_from.html"
    success_url = reverse_lazy("catalog:blogpost_from")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Создание блоговой записи"
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "content", "preview", "publication_sing", "number_of_views"]
    template_name = "catalog/blogpost_from.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактирование блоговой записи"
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("catalog:blogpost_detail", kwargs={"pk": self.object.pk})


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "catalog/blogpost_detail.html"
    success_url = reverse_lazy("catalog:blogpost_list")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        blogpost_item = self.get_object()
        context["blogpost_item"] = blogpost_item
        context["title"] = f"Запись в блоге #{blogpost_item.id}"
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "catalog/blogpost_delete.html"
    success_url = reverse_lazy("catalog:blogpost_list")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Удаление блоговой записи"
        return context
