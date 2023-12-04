class Food:
    def __init__(self, name, amount):
        self.__name = name
        self.__amount = amount
        self.__price = self.price_per_pound()

    def price_per_pound(self):
        name = self.__name.title()
        if self.__name == "Dry Cured Iberian Ham":
            price = 117.80
        elif self.__name == "Wagyu Steaks":
            price = 450
        elif self.__name == "Matsutake Mushrooms":
            price = 272
        elif self.__name == "Kopi Luwak Coffee":
            price = 306.50
        elif self.__name == "Moose Cheese":
            price = 487.20
        elif self.__name == "White Truffles":
            price = 3600
        elif self.__name == "Blue Fin Tuna":
            price = 3603
        elif self.__name == "Le Bonnotte Potatoes":
            price = 270.81
        else:
            price = 0
        return price

    def cost_of_ordered(self):
        cost = self.__amount * self.__price
        return cost

    def __str__(self):
        return f"Price per pound for {self.__name} is {self.__price}"