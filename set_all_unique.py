"""
Вам предстоит реализовать функцию all_unique(). Эта функция должна 
принимать коллекцию и возвращать True, 
если элементы не повторяются (если элементов нет, 
то ничего не повторяется).
"""


def all_unique(items) -> bool:
    return True if len(items) == len(set(items)) else False

print(all_unique([1, 2, 3]))
print(all_unique([1, 2, 1]))