from django.urls import path

from .views import BookList, BookDetails, SearchResultListView, BookCheckout, add_to_cart, cart,remove_from_cart

urlpatterns = [
    path('', BookList.as_view(), name='blist'),
    path('books/<int:pk>/', BookDetails.as_view(), name='details'),
    path('search/', SearchResultListView.as_view(), name='search'),
    path('checkout/<int:pk>/', BookCheckout.as_view(), name='checkout'),
    path('cart/', cart, name='mycart'),
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),  # function ayond as_view venad,just fun mathram import--
    path('remove_from_cart/<int:book_id>/', remove_from_cart, name='remove_from_cart'),

]
