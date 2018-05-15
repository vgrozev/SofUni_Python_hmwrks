
price_per_kg_vegies = float(input())
price_per_kg_fruits = float(input())
total_kg_vegies = int(input())
total_kg_fruits = int(input())

vegies = price_per_kg_vegies * total_kg_vegies
fruits = price_per_kg_fruits * total_kg_fruits

sum = vegies + fruits
sum_in_eur = sum / 1.94

print(sum_in_eur)
