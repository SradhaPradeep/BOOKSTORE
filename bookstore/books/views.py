from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q
from q import q
from .models import Book, Cart, CartItems


# Create your views here.


class BookList(ListView):
    model = Book  # models le table name
    template_name = 'booklist.html'


class BookDetails(DetailView):
    model = Book
    context_object_name = 'blist'
    template_name = 'bookdetails.html'


class SearchResultListView(ListView):
    model = Book
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(Q(title=query) | Q(author=query))


class BookCheckout(DetailView):
    model = Book
    template_name = 'checkout.html'


@login_required()
def cart(request):
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
        cart_items = CartItems.objects.filter(cart=cart_obj)
    else:
        cart_obj = None
        cart_items = []
    context = {
        'cart': cart_obj,
        'cart_items': cart_items
    }
    return render(request, 'cart/mycart.html', context)


@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart_qs = Cart.objects.filter(user=request.user)

    if cart_qs.exists():
        cart_obj = cart_qs.first()
    else:
        cart_obj = Cart.objects.create(user=request.user, total_price=Decimal("0.00"))

    try:
        cart_item, created = CartItems.objects.get_or_create(book=book, cart=cart_obj)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        cart_obj.total_price += book.price
        cart_obj.save()
    except Exception as e:
        # Handle the exception, e.g., log it or return an error response
        pass

    return redirect('mycart')


@login_required()
def remove_from_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
        cart_item_qs = CartItems.objects.filter(book=book, cart=cart_obj)
        if cart_item_qs.exists():
            cart_item = cart_item_qs.first()
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
            cart_obj.total_price = Decimal(str(book.price))
            cart_obj.save()
        return redirect('mycart')
