#CalorieCounter
def calories_of_food_item(item):
    table_of_calories={"apple":100,"twinkie":500}
    return table_of_calories.get(item,0)
 if item=="apple":
     return 100
if item=="twinkie":
    return 500
total_cals=0
while true:
    food_item=input("Enter food: ")
    calories=
    calories_of_food_item(food_item)
    total_cals+=calories
    print("The calories for ",food_item," are ", calories)
print("Total calories are ", total_cals)

