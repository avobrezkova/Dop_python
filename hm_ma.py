class MyMap:  # Класс MyMap, представляет структуру данных "карта"
    def __init__(self, size,
                 method='chaining'):  # Метод инициализации класса. Принимает размер карты и метод разрешения коллизий
        self.size = size
        self.map = [None] * size
        self.method = method

    def hash_fun(self, key):  # Метод для вычисления хеш-функции от ключа
        return hash(key) % self.size

    def insert(self, key, value):  # Метод для добавления элемента в карту
        index = self.hash_fun(key)

        if self.method == 'chaining':  # Проверка метода разрешения коллизий
            if self.map[index] is None:
                self.map[index] = [(key, value)]
            else:
                self.map[index].append((key, value))
        elif self.method == 'open addressing':
            while self.map[index] is not None:
                index = (index + 1) % self.size
            self.map[index] = (key, value)

    def search(self, key):  # Метод для поиска элемента по ключу
        index = self.hash_fun(key)

        if self.method == 'chaining':
            if self.map[index] is not None:
                for k, v in self.map[index]:
                    if k == key:
                        return v
        elif self.method == 'open addressing':
            initial_index = index
            while self.map[index] is not None:
                k, v = self.map[index]
                if k == key:
                    return v
                index = (index + 1) % self.size
                if index == initial_index:  # Проверка на зацикливание
                    break

        return None

# Пример использования
my_map = MyMap(10, 'chaining')  # Создание экземпляра структуры данных map с методом разрешения коллизий через цепочки
my_map.insert('key1', 'value1')
my_map.insert('key2', 'value2')
print(my_map.search('key1'))  # Выводит 'value1'

my_map_open_address = MyMap(10, 'open addressing')  # Создание экземпляра структуры данных map с методом разрешения коллизий через открытую адресацию
my_map_open_address.insert('key1', 'value1')
my_map_open_address.insert('key2', 'value2')
print(my_map_open_address.search('key2'))  # Выводит 'value2'