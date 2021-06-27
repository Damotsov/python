def foo(name, surname, date, city, email, phone):
    print(
        f'меня зовут-{name}, фамилия {surname},\n'
        f'я {date} года рождения,родился в городе {city},\n'
        f'мой Email:{email},мой номер телефона{phone}')


foo(name='Валентин', surname='Попов', date=1944, city='Пенза', email='popov@go.com', phone=9379992)
