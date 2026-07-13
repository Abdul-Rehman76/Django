from django.db import models

# Create your models here. used to create database tables for the food app.
#in simple terms, a model is a Python class that defines the structure of a database table and the behavior of the data stored in that table. Each attribute of the class represents a field in the table, and each instance of the class represents a row in the table.
# we have to create an object of the model class to create a new record in the database. we can do this by calling the constructor of the model class and passing in the values for each field as keyword arguments. For example, to create a new Food object, we can do:
class Food(models.Model):

    def __str__(self):
        return self.food_description

    food_name = models.CharField(max_length=100)
    food_description = models.TextField()
    food_price = models.DecimalField(max_digits=6, decimal_places=2)
    # food_image = models.ImageField(upload_to='food_images/', null=True, blank=True)

    # def __str__(self):
    #     return self.food_name