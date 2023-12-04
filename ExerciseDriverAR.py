from ProgramExerciseAR import Food

def list_of_obj():
    obj_list = []
    num_items = int(input("Enter the number of items: "))
    while num_items < 1:
        print("Number of items must be at least 1.")
        num_items = int(input("Enter the number of items: "))
    for _ in range(num_items):
        name = input("Enter the name of the item: ").title()
        name.title()
        amount = float(input("Enter the amount of the item in pounds: "))
        while amount <= 0:
            print("Amount must be greater than 0.")
            amount = float(input("Enter the amount of the item in pounds: "))
        food_item = Food(name, amount)
        obj_list.append(food_item)
    return obj_list


def display_list(obj_list):
    for food_item in obj_list:
        print(food_item)

def calc_total_cost(obj_list):
    total_cost = 0
    for food_item in obj_list:
        total_cost += food_item.cost_of_ordered()
    return total_cost

def main_function():
  items_list = list_of_obj()
  display_list(items_list)
  total_cost = calc_total_cost(items_list)
  print(f"Total cost of all items: ${total_cost:.2f}")

main_function()