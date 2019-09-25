from django.urls import path
from . import views
urlpatterns=[
   path('products/', views.product_list),
   path('ordername/', views.order_name),
   path ('smaller/', views.lowest_price),
   path('biggest/', views.biggest_price)
]