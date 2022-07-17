'''Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
не использовать random.randint и вообще библиотеку random
Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды)
- для задания случайности'''

from datetime import datetime


def random(_min, _max):
    d = _max - _min
    ms = datetime.today().microsecond / (10 ** 6)
    
    return _min + int(d * ms)


rnd = random(0, 100)
print(rnd)