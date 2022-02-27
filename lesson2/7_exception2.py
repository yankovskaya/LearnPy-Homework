def discounted(price, discount, max_discount=20):
    try:   
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if discount >= 100:
            raise ValueError("Максимальная скидка – 20%")
        if discount >= max_discount:
            return price
        else:
            return  price - (price * discount / 100)
    
    except(ValueError, TypeError):
        print("Ошибка")

discounted(100.0, 5, "10")
discounted("сто", "десять")
discounted("five", 5)
discounted("100", "4.5")
discounted(100, 2)
discounted(100, "3")
discounted("five", 5)
