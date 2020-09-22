from django.shortcuts import render

# Create your views here.

def all_products(request):
    """ This view will illustrate all products, including functionalities such as Sorting and Searching """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)