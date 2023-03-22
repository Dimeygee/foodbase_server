from django.urls import path
from .views import FoodListView, FoodCategoryView

urlpatterns = [
    path('', FoodListView.as_view(), name='allfood'),
    path('<str:category>/', FoodCategoryView.as_view(), name='foodcategory'),
]