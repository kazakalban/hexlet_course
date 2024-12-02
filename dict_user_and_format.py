"""В этой практике вам нужно реализовать две функции:

    Функцию make_user(), которая должна принимать два параметра — имя пользователя и возраст. Функция должна вернуть словарь с ключами 'name' и 'age', по которым должны быть сохранены соответствующие значения
    Функцию format_user(), которая принимает словарь — результат вызова функции make_user(). Она должна вернуть строку вида 'Phil, 25'

phil = make_user('Phil', 25)
type(phil)
# <class 'dict'>
format_user(phil)
# Phil, 25"""


def make_user(user_name: str, user_age: int) -> dict[str, str | int]:
    """
    Создает словарь с данными пользователя. 
    """
    user_data = {
        'name': user_name,
        'age': user_age
    }
    return user_data


def format_user(user_data: dict) -> str:
    """
    Форматирует данные пользоваталя в строку
    """
    return f"{user_data['name']}, {user_data['age']}"


phil = make_user('Phil', 25)
print(type(phil))

print(format_user(phil))