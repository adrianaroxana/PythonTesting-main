scope = 1
if scope == 0:
    li = [1, 2, 3, 4, 5]
    li2 = ['a', 'b', 'c']
    li3 = ['a', 'b', 2, 4, 'c', 5]
    print(li)
    print(li[2])
    print(li[7])


elif scope == 1:
    amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
    print(amazon_cart[0:2])
    amazon_cart[0] = 'laptop'
    print(amazon_cart)
    print(amazon_cart[1:3])
    print(amazon_cart[0::2])
    new_cart = amazon_cart
    new_cart[0] = 'gum'
    print(new_cart)

    amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
    new_cart = amazon_cart[:]
    new_cart[0] = 'gum'
    print(new_cart)
    print(amazon_cart)

else:
    print('tba')