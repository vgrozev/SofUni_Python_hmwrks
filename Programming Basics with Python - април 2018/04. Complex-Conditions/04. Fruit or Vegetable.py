product = input().lower()

if product == 'banana' or product == 'apple' or product == 'kiwi' or product == 'cherry' or product == 'lemon' or product == 'grapes':
    product = 'fruit'
elif product == 'tomato' or product == 'cucumber' or product == 'pepper' or product == 'carrot':
    product = 'vegetable'
else:
    product = 'unknown'

print(product)

