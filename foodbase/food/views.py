
from rest_framework.permissions import IsAuthenticated
from .serializers import FoodSerializer
from rest_framework.generics import ListAPIView
from .models import Food

class FoodListView(ListAPIView):
    
    queryset = Food.objects.all()
    #permission_classes= (IsAuthenticated,)
    serializer_class=FoodSerializer


class FoodCategoryView(ListAPIView):
    
    serializer_class=FoodSerializer

    def get_queryset(self):
        category_type=self.kwargs['category']
        return Food.objects.filter(category=category_type)





