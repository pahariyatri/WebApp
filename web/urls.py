from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('search', SearchResultsView.as_view(), name='search_results'),
]
"""
urlpatterns = [
    path("",views.index, name="Home"),
    path("index",views.index, name="index"),


    #path("destination", views.offers, name="offers"),
    #path("destination/details/<str:pk_test>", views.details, name="details"),
    path('search', SearchResultsView.as_view(), name='search_results'),
    path('adventure', views.adventure, name='adventure'),
    path('solo', views.solo, name='solo'),
    path('group', views.group, name='group'),
    path('religous', views.religous, name='religous'),
    path('wateractivities', views.wateractivities, name='wateractivities'),
    path('nature', views.nature, name='nature'),
    path('family', views.family, name='family'),
    path('romantic', views.romantic, name='romantic')

    #path('index', HomePageView.as_view(), name='home'),
]
"""