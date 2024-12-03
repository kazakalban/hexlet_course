"""
Цель упражнения — написать функцию collect_indexes(). Эта функция должна:

    Принимать на вход коллекцию — некий итератор или итерируемый элемент
    Возвращать словарь или подобную ему коллекцию. Ключом будет элемент 
    коллекции, а значением для ключа — список индексов коллекции,
    по которым встречается этот элемент
"""


from collections import defaultdict


def collect_indexes(items):
    final_dict = defaultdict(list)
    index = 0
    for item in items:
        final_dict[item].append(index)
        index += 1
    return final_dict


def test_collect_indexes():
    assert not collect_indexes([])
    assert collect_indexes([1]) == {1: [0]}
    assert collect_indexes([1, 2]) == {1: [0], 2: [1]}
    assert collect_indexes('lol') == {'l': [0, 2], 'o': [1]}
    assert collect_indexes('coco') == {'c': [0, 2], 'o': [1, 3]}


test_collect_indexes()