from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product


# Create your views here.
def home(request):
    categories = Category.objects.all()[:3]
    products = Product.objects.filter(is_active=True)[:8]
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'store/index.html', context)


def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'store/categories.html', {'categories': categories})


# def category_products(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     products = Product.objects.filter(is_active=True, category=category)
#     categories = Category.objects.all()
#     context = {
#         'category': category,
#         'products': products,
#         'categories': categories,
#     }
#     return render(request, 'store/category_products.html', context)

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(is_active=True, category=category)
    categories = Category.objects.all()

    paginator = Paginator(products, 3)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products_by_page = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products_by_page = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'products': products_by_page,
        'categories': categories,
    }
    return render(request, 'store/category_products.html', context)


def detail(request, c_slug, p_slug):
    product = get_object_or_404(Product, slug=p_slug)
    related_products = Product.objects.exclude(id=product.id).filter(is_active=True, category__slug=c_slug)
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'store/detail.html', context)


def wishlist(request, str1):
    print("sravan", str1)
    return redirect('')
