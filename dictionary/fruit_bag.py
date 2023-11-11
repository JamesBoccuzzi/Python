a = {'james' : [1,2,3],
     'frank' : {'black' : 'red'}}

total = 0

fruitPrices = {'banana' : 3.25,
               'apple' : 2.5,
               'orange' : 4,
               'pommogranite' : 8.25}

fruitBag = {'banana' : 5,
            'apple' : 9,
            'pommogranite' : 3}

for fruit, quantity in fruitBag.items():
    quantity = quantity * fruitPrices[fruit]
    total = total + quantity
    print(quantity)
print('The total price is', total)
    