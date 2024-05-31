#Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
# такие как адрес, название и ассортимент товаров.
# Ваша задача — создать класс `Store`, который можно будет использовать для создания различных магазинов.

class Store:
    def __init__(self, address, name, title, price):
        self.address = address
        self.name = name
        self.title = title
        self.price = price
        self.goods = {}

    def add_goods(self, title, price):
        self.goods[title] = price
        self.goods.update({title: price})
        print(f"Товар {title} добавлен в ассортимент магазина {self.name}")
    def get_title(self):
        print(f"Ассортимент магазина {self.name} \n", self.goods.keys())

    def remove_goods(self, title):
        self.goods.pop(title)
        print(f"\nТовар {title} удален из ассоритмента магазина {self.name}\n")

    def update_price(self, title, price):
        if title in self.goods:
            self.goods.update({title: price})
            print(f"\nЦена товара {title} изменена и составляет {price} руб. \n")
        else:
            print(f"Изменение цены недоступно: {title} отсуствует в ассортименте")

    def get_goods(self):
        print(f"\n--Сегодня в магазине {self.name} в продаже--")
        for title, price in self.goods.items():
            print(f"{title} - {price} руб.")
    def get_price_item(self, title):
        print(f"\nЦена товара {title} = {self.goods[title]} руб.")

# Пример использования
store = Store('г.Москва', '"Продукты"', 'Товар', 'Цена')
store.add_goods("Яблоко", 100)
store.add_goods("Апельсин", 200)
store.add_goods("Банан", 300)
store.get_title()
store.get_goods()
store.get_price_item("Банан")
store.add_goods("Груша", 500)
store.get_goods()
store.remove_goods("Банан")
store.update_price("Банан", 400)
store.update_price("Апельсин", 300)
store.get_goods()

store_2 = Store('г.Москва', '"Электроника"', 'Товар', 'Цена')
store_2.add_goods("Телевизор", 20000)
store_2.add_goods("Компьютер", 45000)
store_2.add_goods("Кофеварка", 35000)
store_2.get_goods()

store_3 = Store('г.Москва', '"Химия"', 'Товар', 'Цена')
store_3.add_goods("Средство для мытья пасуды", 50)
store_3.add_goods("Средство для прочистки труб", 200)
store_3.add_goods("Жироудалитель", 180)
store_3.get_goods()


