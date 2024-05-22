def task11():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = 0

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} специализируется на кухне {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

        def update_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.restaurant_name} обновлен: {self.rating}.")

    newRestaurant = Restaurant("Новый Ресторан", "Итальянская")

    print(f"Название ресторана: {newRestaurant.restaurant_name}")
    print(f"Тип кухни: {newRestaurant.cuisine_type}")
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

    restaurant1 = Restaurant("Ресторан 1", "Французская")
    restaurant2 = Restaurant("Ресторан 2", "Японская")
    restaurant3 = Restaurant("Ресторан 3", "Испанская")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

    restaurant1.update_rating(4.5)


task11()