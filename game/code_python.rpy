init python:
    class Item:
        def __init__(self, name):
            # Название предмета
            self.name = name
    
    class Inventory:
        def __init__(self):        
            # Список предметов (Приватная переменная)
            self.__items = []
            # Количество предметов в инвентаре
            self.count = 0

        # Добавление предмета
        def add(self, item):
            if(isinstance(item, Item)):
                self.__items.append(item)
                self.count += 1
            return None
        
        # Удаление предмета
        def remove(self, item):
            if(isinstance(item, Item)):
                self.__items.remove(item)
                self.count -= 1
            return None

        # Проверка предмета на наличия
        def has_item(self, item):
            if(isinstance(item, Item)):
                if(item in self.__items): return True
                else: return False
            return None

        # Получение предмета по индексу
        def get_item(self, index):
            if(isinstance(index, int)):
                return self.__items[index]
            return None

    class CollectionItem:
        # Коллекция всех возможных предметов
        __collectionItem = {"Ручка": Item("Ручка"),
                            "Тетрадь": Item("Тетрадь")}
        
        # Для получения предмета по названию
        @staticmethod
        def get_item_str(name_item):
            if(isinstance(name_item, str)):
                return CollectionItem.__collectionItem.get(name_item)
            return None

        # Для получения предмета по ключу
        @staticmethod
        def get_item_int(id_item):
            if(isinstance(id_item, int)):
                values = list(CollectionItem.__collectionItem.values())
                count = len(values)
                if(id_item >= 0 and id_item < count):
                    return values[id_item]
            return None