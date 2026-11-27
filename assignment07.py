def calculate_calories(carbs, fats, proteins):
    total = (carbs * 4) + (fats * 9) + (proteins * 4)
    return total

carbs = float(input("Enter carbs in grams: "))
fats = float(input("Enter fats in grams: "))
proteins = float(input("Enter proteins in grams: "))

calories = calculate_calories(carbs, fats, proteins)

print("Total calorie intake:", calories)