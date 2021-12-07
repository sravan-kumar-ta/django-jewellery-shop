from .models import Cart


def cart_menu(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        context = {
            'cart_items': cart_items,
        }
    else:
        context = {}
    return context
