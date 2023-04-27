from django.shortcuts import render
from posts.models import Product
from posts.forms import ProductCreateForm, ReviewCreateForm

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products' : products
        }
        return render(request, 'products/products.html', context=context)

def product_detail_view(request):
    if request.method == 'GET':
        review = Product.objects.get(id=id)

        context = {
            'review': review,
            'comments': review.comment_set.all()
        }
    return render(request, 'products/detail.html', context=context)

def product_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)
    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                product_image=form.cleaned_data.get('product_image'),
                product_name=form.cleaned_data.get('product_name'),
                product_description=form.cleaned_data.get('product_description'),
                product_rate=form.cleaned_data.get('product_rate'),
                product_availability=form.cleaned_data.get('product_availability')

            )

            return redirect('/products/')

    return render(request, 'products/create.html', context={
        'form': form
    })

def review_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ReviewCreateForm
        }
        return render(request, 'products/create.html', context=context)
    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ReviewCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                text=form.cleaned_data.get('text'),
                product= form.cleaned_data.get('product')

            )

            return redirect('/products/')

    return render(request, 'products/create.html', context={
        'form': form
    })