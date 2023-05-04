from django.db.models import Q
from django.shortcuts import render
from posts.models import Product
from posts.forms import ProductCreateForm, ReviewCreateForm, CommentCreateForm
from posts.constants import PAGINATION_LIMIT

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products[PAGINATION_LIMIT * (page-1):PAGINATION_LIMIT * page]

        if search:
            products = products.filter(Q(product_name__icontains=search),
                                       Q(product_description__icontains=search))


        context = {
            'products': products,
            'user': request.user
            'pages': range(1, max_page+1)
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

    if request.method == 'POST':
        post = Post.objects.get
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                post=post
            )
            return redirect(f'/products/{id}')

        context={
            'post': post,
            'form': form,
            'comments': post.comment_set.all()
        }
        return render(request, '/products/detail.html', context=)

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