from django.shortcuts import get_object_or_404, render

from .models import Category, Product, PosterView


def product_all(request):
    template_name = 'store/home.html'
    products = Product.products.all()
    banners = PosterView.objects.all()
    context = {
        "products":products,
        "banners":banners
    }
    return render(request, template_name, context)
    # products = Product.products.all()
    # return render(request, 'store/home.html', {'products': products})
    


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})
