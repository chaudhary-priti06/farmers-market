from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


@login_required
def order_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    Order.objects.create(
        product=product,
        buyer=request.user,
        quantity=1
    )

    return redirect('home')
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
from django.contrib.auth.decorators import login_required

@login_required
def order_history(request):
    orders = Order.objects.filter(buyer=request.user)
    return render(request, 'orders.html', {'orders': orders})



