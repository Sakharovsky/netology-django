from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):

    try:
        sort = request.GET.get("sort")
    except TypeError:
        sort = None
    
    if sort == 'min_price':
        sort = 'price'
    elif sort == 'max_price':
        sort = '-price'
    else:
        sort = 'name'

    phones = Phone.objects.order_by(sort).all()
    phone_list = (
        {
            'name': phone.name,
            'image': phone.image,
            'price': phone.price,
            'slug': phone.slug
            }
            for phone in phones
        )
    template = 'catalog.html'
    context = {
        'phones': phone_list
        }
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.filter(slug=slug).first()
    if phone:
        template = 'product.html'
        context = {
            'phone': {
                'name': phone.name,
                'image': phone.image,
                'price': phone.price,
                'release_date': phone.release_date,
                'lte_exists': phone.lte_exists
            }
        }
        return render(request, template, context)
    else:
        return HttpResponse('Упс... Не можем найти такую модель телефона.')
