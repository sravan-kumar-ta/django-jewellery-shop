from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.all_categories, name="all-categories"),
    path('categories/<slug:slug>/', views.category_products, name="category-products"),
    path('<slug:c_slug>/<slug:p_slug>/', views.detail, name="product-detail"),
]
