from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, userlogin
from .models import Items, CartItem, Order



# Create your views here.
#starting homepage
def homepage(request):
    all_items = Items.objects.all()
    return render(request, 'homepage.html', {'all_items':all_items})


#signup page
def signupRecord(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginurl')
    else:
        form=UserCreationForm()
    return render(request,'signuppage.html',{'form':form})

#login page
def loginRecord(request):
    if request.method=='POST':
        form=userlogin(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('homeurl')
    else:
        form=userlogin()
    return render(request, 'loginpage.html',{'form':form})


#logout page
def userlogout(request):
    logout(request)
    return render(request,'homepage.html')


#adding to cart
def add_to_cart(request, product_id):
    product = Items.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    
    cart_item.quantity = 1
    cart_item.save()
    return redirect('mycarturl')

#mycart page
def mycart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'mycart.html', {'cart_items':cart_items, 'total_price':total_price})

#removing from cart
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('mycarturl')

#add fooditems to order
def add_to_order(request, item_id):
    item = get_object_or_404(Items, id=item_id)
    order, created = Order.objects.get_or_create(user=request.user)
    order.items.add(item)
    order.total_price = sum(item.price for item in order.items.all())
    order.save()
    return redirect('myorderurl')

#myorders page
def myorders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,'myorders.html', {'orders':orders}) 


