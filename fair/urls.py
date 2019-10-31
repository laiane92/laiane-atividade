from django.urls import path
from . import views
urlpatterns=[
   path('', views.home),
   path('products/', views.product_list),
   path('carrinho/', views.shop),
   path('<int:id>/comprar/', views.shopping_cart),
   path('show/', views.product_show)
   
]