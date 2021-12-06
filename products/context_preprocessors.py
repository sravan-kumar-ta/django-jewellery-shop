from .models import Category


def store_menu(request):
    categories = Category.objects.all()
    context = {
        'categories_menu': categories,
    }
    return context
