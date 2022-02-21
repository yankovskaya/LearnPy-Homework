"""
Домашнее задание №1
Цикл for: Продажи товаров
* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""



sales_list = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def sales():
    for items_sold in sales_list[0]:
        iphone12 = (sales_list[0]["items_sold"])
        sum_iphone = sum(iphone12)
        print(f"Сумма продаж Iphone12: {sum_iphone}")
        print(f"Среднее количесво продаж Iphone12: {sum_iphone / len(iphone12)}")
        
        for items_sold in sales_list[1]:
            xiaomi = (sales_list[1]["items_sold"])
            sum_xiaomi = sum(xiaomi)
            print(f"Сумма продаж Xiaomi: {sum_xiaomi}")
            print(f"Среднее количесво продаж Xiaomi: {sum_xiaomi / len(xiaomi)}")
            
            for items_sold in sales_list[2]:
                samsung = (sales_list[2]["items_sold"])
                sum_samsung = sum(samsung)
                print(f"Сумма продаж Samsung: {sum_samsung}")
                print(f"Среднее количесво продаж Samsung: {sum_samsung / len(samsung)}")
                print(f"Cуммарное количество продаж всех товаров: {sum_iphone + sum_xiaomi + sum_samsung}")
                print(f"Cреднее количество продаж всех товаров: {(sum_iphone + sum_xiaomi + sum_samsung) / len(iphone12 + xiaomi+ samsung)}")
                return None
                
sales()
