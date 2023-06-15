price = 10        #цена одной книги     
discount_percentage = 40   #процент скидки
shipping_cost_1 = 2      #стоимость доставки за первый экземпляр
shipping_cost_2 = 1.50    #стоимость доставки за каждый дополнительный
number_of_books = -1       #количество купленных экземпляров

discounted_price = price - (price * (discount_percentage / 100))  #вычисляем стоимость с учетом процента скидки
price_final = discounted_price * number_of_books

if number_of_books == 1:          #тут расчитываем стоимость в зависимости от количества купленных книг
    total = discounted_price + shipping_cost_1
    print (f'Общая стоимость с доставкой составляет {total:.2f} руб')
elif number_of_books > 1:
    total = discounted_price * number_of_books + (shipping_cost_1 + (shipping_cost_2 * (number_of_books - 1)))
    print (f'Общая стоимость с доставкой составляет {total:.2f} руб')
else:
    print ("Стоимость расчитывается от одной и более купленных книг")

