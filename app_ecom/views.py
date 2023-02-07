from django.shortcuts import render, HttpResponse
from .models import Product


# Create your views here.

def index(request):
    product_id = Product.product_id
    product_name = Product.product_name
    product_category = Product.product_category
    product_sub_category = Product.product_sub_category
    price = Product.price
    desc = Product.desc
    image = Product.image


    all_products = []
    category_types = []
    category_products = Product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in category_products}
    for cat in cats:
        cat_types = Product.objects.filter(product_category=cat)
        category_types.append(cat)

    for p in Product.objects.all():
        all_products.append(p)

    # print('prods', all_products)
    # print('cats', category_types)

    context = {
        'product' : all_products,
        'categories' : category_types,
    }

    return render(request, 'app_ecom/index.html', context)

def services(request):
    return render(request, 'app_ecom/services.html')

def contact(request):
    return render(request, 'app_ecom/contact.html')

def about(request):
    return render(request, 'app_ecom/about.html')

def cart(request):
    all_products = []
    all_products_names = []
    all_products_price = []
    all_products_ids = []

    all_products_images = []

    for p in Product.objects.all():
        all_products.append(p)
        all_products_names.append(p.product_name)
        all_products_ids.append(p.id)
        all_products_price.append(p.price)

        all_products_images.append(p.image.url)
        # p.image_url.url

    import json
    all_products_names = json.dumps(all_products_names)
    all_products_images = json.dumps(all_products_images)


    context = {
        'products' : all_products,
        'all_products_ids' : all_products_ids, 
        'all_products_names' : all_products_names, 
        'all_products_price' : all_products_price,

        'all_products_images' : all_products_images, 
    }

    # print(all_products_ids)
    # print(list(all_products_names), type(all_products_names))
    # print(all_products_price)

    print(list(all_products_images))

    return render(request, 'app_ecom/cart.html', context)

def product_view(request, p_id):
    product = Product.objects.filter(id=p_id)
    return render(request, "app_ecom/product_view.html", {'product' : product[0]})
    