from django.db import models
from PIL import Image






class Food(models.Model):

    ALL_FOOD = 'ALL_FOOD'
    BAKERY = 'BAKERY'
    SEA_FOOD = 'SEA_FOOD'
    CHICKEN = 'CHICKEN'
    PIZZA = 'PIZZA'
    BURGER='BURGER'

    CATEGORY = [
        (ALL_FOOD, "All food"),
        (BAKERY, "Bakery"),
        (SEA_FOOD, "Sea food"),
        (CHICKEN, "Chicken"),
        (PIZZA, "Pizza"),
        (BURGER, "Burger"),
    ]

    food_name= models.CharField(max_length=50,null=False, blank=False)
    category=models.CharField(choices=CATEGORY, max_length=50, default=ALL_FOOD)
    image=models.ImageField(default="default.jpg",upload_to="foods")
    duration=models.DurationField()
    rating=models.DecimalField(max_digits=5,decimal_places=1)
    amount=models.DecimalField(max_digits=20,decimal_places=2)
    favourite=models.BooleanField()
    calorie=models.IntegerField()
    about=models.TextField(max_length=500)


    def filter_Category(self,category_type):
        return self.filter(category=category_type).all()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.image.path)




