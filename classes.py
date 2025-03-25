class Restaurant:
    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name} and the cuisine type is {self.cuisine_type}")
    def open_restaurant(self):
        print("The restaurant is open")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavours):
        super().__init__(name, cuisine_type)
        self.flavours = flavours
    def describe_flavours(self):
        print("The flavours in the ice cream stand are ", self.flavours)

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
class Admin(User):
    def __init__(self, first_name, second_name, privileges):
        super().__init__(first_name, second_name)
        self.privileges = Privileges(privileges)

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privilege(self):
        print(self.privileges)

restaurant = Restaurant("Manaswini's Restaurant", "Asian")
# print("Name of the restaurant is ",restaurant.restaurant_name)
# print("Type of cuisine sold here is ", restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
restaurant1 = Restaurant("Restaurant1", "Chinese")
restaurant2 = Restaurant("Restaurant2", "Thai")
restaurant3 = Restaurant("Restaurant3", "French")
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()

ice_cream = IceCreamStand("Buskin Robins", "Ice Cream", ["Vanilla", "Butterscotch", "Chocolate"])
ice_cream.describe_flavours()

admin_user = Admin("Manaswini", "Gogineni", ["can add", "can delete" "can post", "can get"])
admin_user.privileges.show_privilege()

