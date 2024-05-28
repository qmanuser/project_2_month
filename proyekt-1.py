
from datetime import datetime
user_info = {"ism": "Bobur", "familia": "Temurov", "password": 1111, "card_number": "8600530447633627", "card_balance": 2200000}



def russian_balance_display():
    bottom = input(f"""
        {user_info["card_balance"]} сумм на вашем балансе
        Хотите воспользоваться другой услугой?
            1. Да
            2. Нет
                >>> """)

    if bottom == "1":
        return russian_services()

    elif bottom == "2":
        return main()

    else:
        print("Ошибка, просто нажмите указанные кнопки!")
        return russian_balance_display()

def russian_balance_check():
    print("Спасибо, что выбрали нас!")
    check = f"""
                        CHECK
                Баланс: {user_info["card_balance"]}
                Карта: {12 * "*" + user_info["card_number"][-4::]}
                Время: {datetime.now()}
            """
    print(check)
    return main()


def russian_service_add_money():
    pass
def russian_services_sms():
    pass
def russian_services_cash():
    pass

def russian_services_balance():
    print("<<<<<<<<<Balance>>>>>>>>")
    bottom = input("""
                   1. Просмотр на экране
                   2. просмотр на чеке    
                    >>> """)
    if bottom == "1":
        return russian_balance_display()

    elif bottom == "2":
        return russian_balance_check()

    else:
        print("такого типа услуг не существует!")
        return russian_services_balance()

def russian_services():
    bottom = input("""
            <<<< Russian >>>>>
            Выберите тип услуги:
                 1. Посмотреть баланс
                 2. Выдача наличных
                 3. SMS-уведомление
                 4. Заполнение карты
                 0. Вернуться назад
                    >>> """)
    if bottom == "1":
        return russian_services_balance()
    elif bottom == "2":
        return russian_services_cash()
    elif bottom == "3":
        return russian_services_sms()
    elif bottom == "4":
        return russian_service_add_money()

    elif bottom == "0":
        print("Спасибо, что выбрали нас!")
        return main()

    else:
        print("такого типа услуг не существует!")
        return russian_services()





def english_balance_display():
    bottom = input(f"""
        Your balance is {user_info["card_balance"]} sum
        Do you want to use another service?
            1. Yes
            2. No
                >>> """)

    if bottom == "1":
        return english_services()

    elif bottom == "2":
        return main()

    else:
        print("Error, just press the indicated buttons!")
        return english_balance_display()

def english_balance_check():
    print("Thank you for choosing us!")
    check = f"""
                        CHECK
                Balance: {user_info["card_balance"]}
                Card: {12 * "*" + user_info["card_number"][-4::]}
                Time: {datetime.now()}
            """
    print(check)
    return main()


def english_services_balance():
    print("<<<<<<<<<Balance>>>>>>>>")
    bottom = input("""
                1. View on the display
                2. View at the check     
                    >>> """)
    if bottom == "1":
        return english_balance_display()

    elif bottom == "2":
        return english_balance_check()

    else:
        print("This type of service does not exist")
        return english_services_balance()

def english_services_cash():
    pass

def english_services_sms():
    pass


def english_service_add_money():
    pass

def english_services():
    bottom = input("""<<<
    select the type of service you need:
    1. View the balance
    2. Get cash
    3. Turn on SMS notification
    4. Add money
    5. Go back to menu
    >>> """)
    if bottom == "1":
        return english_services_balance()
    elif bottom == "2":
        return english_services_cash()
    elif bottom == "3":
        return english_services_sms()
    elif bottom == "4":
        return english_service_add_money()

    elif bottom == "0":
        print("Thank you for choosing us!")
        return main()

    else:
        print("This type of service does not exist")
        return english_services()
def uzbek_balance_display():
    bottom = input(f"""
    Sizning balansingiz {user_info["card_balance"]} so'm
    Boshqa xizmatdan foydalanishni istaysizmi?
        1. Ha
        2. Yo'q
            >>> """)

    if bottom == "1":
        return uzbek_services()

    elif bottom == "2":
        return main()

    else:
        print("Xatolik, faqat ko'rsatilgan tugmalarni bosing!")
        return uzbek_balance_display()

def uzbek_balance_check():
    print("Bizni tanlaganiz uchun tashakkur")
    check = f"""
                    CHECK
            Balance: {user_info["card_balance"]}
            Karta: {12 * "*" + user_info["card_number"][-4::]}
            Vaqt: {datetime.now()}
        """
    print(check)
    return main()

def uzbek_services_cash():
    pass


def uzbek_services_balance():
    print("<<<<<<<<<Balance>>>>>>>>")
    bottom = input("""
            1. Ekranda ko'rish
            2. Chekda ko'rish     
                >>> """)
    if bottom == "1":
        return uzbek_balance_display()

    elif bottom == "2":
        return uzbek_balance_check()

    else:
        print("Bunday xizmat turi mavjud emas")
        return uzbek_services_balance()


def uzbek_services_sms():
    pass

def uzbek_service_add_money():
    pass

def uzbek_services():
    bottom = input("""
        <<<< Uzbek >>>>>
        Xizmat turini tanglang:
            1. Balanceni ko'rish
            2. Naqt pul yechish
            3. SMS Xabarnoma
            4. Kartani to'ldirish
            0. Ortga qaytish
                >>> """)
    if bottom == "1":
        return uzbek_services_balance()
    elif bottom == "2":
        return uzbek_services_cash()
    elif bottom == "3":
        return uzbek_services_sms()
    elif bottom == "4":
        return uzbek_service_add_money()

    elif bottom == "0":
        print("Bizni tanlaganiz uchun tashakkur!")
        return main()

    else:
        print("Bunday xizmat turi mavjud emas")
        return uzbek_services()
def uzbek():
    password = int(input(" <<< Iltimos 'PIN CODE' ni kiriting! >>> "))
    if password == user_info["password"]:
        return uzbek_services()
def english():
    password = int(input(" <<< PLEASE ENTER A PASSWORD! >>> "))
    if password == user_info["password"]:
        return english_services()

def russian():
    password = int(input(" <<< Пожалуйста, введите пароль! >>> "))
    if password == user_info["password"]:
        return russian_services()
def main():
    language = input("""
    Choose a language:
    1: Uzbek
    2: English
    3: Russian
    >>>
    """)
    if language == '1':
        return uzbek()
    elif language == '2':
        return english()
    elif language == '3':
        return russian()
    else:
        print("Bunday til mavjud emas!")
        return main()
if __name__ == '__main__':
    main()