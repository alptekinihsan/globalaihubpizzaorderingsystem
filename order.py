import datetime
import csv


class Pizza:
    def __init__(self, description,cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost



class Klasik (Pizza):
    def __init__(self):
        self.description = "Klasik Pizza"
        self.cost = 15.0


class Margarita (Pizza):
    def __init__(self):
        self.description = "Margarita Pizza"
        self.cost = 18.0


class TurkPizza (Pizza):
    def __init__(self):
        self.description = "Turk Pizza"
        self.cost = 20.0


class SadePizza (Pizza):
    def __init__(self):
        self.description = "Sade Pizza"
        self.cost = 25.0


class Decorator(Pizza):
    def __init__(self, component,description, cost):
        self.component = component
        self.description = description
        self.cost = cost

    def get_cost(self):
        return self.component.get_cost () +Pizza.get_cost (self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Zeytinli', 1.5)


class Mantarlar(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Mantarli', 2.0)



class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Keci Peynirli',2.75)


class Et(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Etli',3.0)


class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Soganli', 2.0)


class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Misirli', 1.5)


def main():
    # Menü
    with open('Menu.txt', 'r') as f:
        print(f.read())

    # Pizza seçimi
    pizza_choice = int(input("Lütfen bir pizza seçiniz: "))
    while pizza_choice not in [1, 2, 3, 4]:
        pizza_choice = int(input("Lütfen geçerli bir pizza seçiniz: "))

    # Sos seçimi
    topping_choice = int(input("Lütfen bir sos seçiniz: "))
    while topping_choice not in [11, 12, 13, 14, 15, 16]:
        topping_choice = int(input("Lütfen geçerli bir sos seçiniz: "))

    # Pizza ve sos nesneleri
    if pizza_choice == 1:
        pizza = Klasik()
    elif pizza_choice == 2:
        pizza = Margarita()
    elif pizza_choice == 3:
        pizza = TurkPizza()
    else:
        pizza = SadePizza()
    if topping_choice == 11:
        pizza = Zeytin(pizza)
    elif topping_choice == 12:
        pizza = Mantarlar(pizza)
    elif topping_choice == 13:
        pizza = KeciPeyniri(pizza)
    elif topping_choice == 14:
        pizza = Et(pizza)
    elif topping_choice == 15:
        pizza = Sogan(pizza)
    else:
        pizza = Misir(pizza)


    # Toplam fiyatı hesapla

    total_cost = pizza.get_cost()
    print(f"Toplam Fiyat: {total_cost:.2f} TL")

    # Müşteri bilgilerini alın
    name = input("İsim: ")
    tc = input("TC Kimlik Numarası: ")
    cc_num = input("Kredi Kartı Numarası: ")
    cc_pss = input("Kredi Kartı Password: ")
    time = datetime.datetime.now ()

    # Sipariş özetini yazdırın
    print("\nSipariş Özeti:")
    print(f"Pizza: {pizza.get_description()}")
    print(f"Toplam Fiyat: {total_cost:.2f} TL")
    print(f"İsim: {name}")
    print(f"TC Kimlik Numarası: {tc}")
    print(f"Kredi Kartı Numarası: {cc_num}")
    print(f"Kredi Kartı CVV: {cc_pss}")



    def write_to_database(name, tc, card, cardpassword, desc, ordering_date):
        with open ('Orders_Database.csv', mode='a', newline='') as orders_file:
            writer = csv.writer (orders_file)
            writer.writerow ([name, tc, card, cardpassword, desc, ordering_date])

    write_to_database (name, tc, cc_num, cc_pss,pizza.get_description(), time)


"""
    def save_order_summary(order_summary, filename):
        with open (filename, mode='a', newline='') as file:
            writer = csv.writer (file)
            writer.writerow (['Name', 'TC', 'CreditCard', 'CreditCardPassword', 'Description', 'Ordering Date'])
            for summary in order_summary:
                writer.writerow (
                    [summary['name'], summary['tc'], summary['card'], summary['cardpassword'], summary['desc'],summary['ordering_date']])

    order_summary = [
        {'name': name, 'tc': tc, 'card': cc_num, 'cardpassword': cc_pss, 'desc': pizza.get_description(),'ordering_date':time},]

    save_order_summary (order_summary, 'Orders_Database.csv')
"""



if __name__ == "__main__":
    main()

