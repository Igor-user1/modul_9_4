first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'a')
        for data in data_set:
            file.write(str(data) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        import random
        word = random.choice(self.words)
        return word


first_ball = MysticBall('Да', 'нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
