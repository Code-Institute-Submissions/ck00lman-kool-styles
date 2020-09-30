from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_favorites(request):
    """ A view that renders the favorites contents page """

    return render(request, 'favorites/favorites.html')

def add_to_favorites(request, item_id):
    """ Add a quantity of the specified product to favorites """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    favorites = request.session.get('favorites', {})

    if size:
        if item_id in list(favorites.keys()):
            if size in favorites[item_id]['items_by_size'].keys():
                favorites[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {favorites[item_id]["items_by_size"][size]}')
            else:
                favorites[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your favorites')
        else:
            favorites[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your favorites')
    else:
        if item_id in list(favorites.keys()):
            favorites[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {favorites[item_id]}')
        else:
            favorites[item_id] = quantity
            messages.success(request, f'Added {product.name} to your favorites')

    request.session['favorites'] = favorites
    return redirect(redirect_url)
    

def adjust_favorites(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    favorites = request.session.get('favorites', {})

    if size:
        if quantity > 0:
            favorites[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {favorites[item_id]["items_by_size"][size]}')
        else:
            del favorites[item_id]['items_by_size'][size]
            if not favorites[item_id]['items_by_size']:
                favorites.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your favorites')
    else:
        if quantity > 0:
            favorites[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {favorites[item_id]}')
        else:
            favorites.pop(item_id)
            messages.success(request, f'Removed {product.name} from your favorites')

    request.session['favorites'] = favorites
    return redirect(reverse('view_favorites'))


def remove_from_favorites(request, item_id):
    """Remove the item from the shopping favorites"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        favorites = request.session.get('favorites', {})

        if size:
            del favorites[item_id]['items_by_size'][size]
            if not favorites[item_id]['items_by_size']:
                favorites.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your favorites')
        else:
            favorites.pop(item_id)
            messages.success(request, f'Removed {product.name} from your favorites')

        request.session['favorites'] = favorites
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)