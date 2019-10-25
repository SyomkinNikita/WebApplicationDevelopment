# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.data = []
        strings = []
        for i in items:
            if isinstance(i, str):
                if 'ignore_case' in kwargs.keys() and kwargs['ignore_case'] is True:
                    if i.lower() not in strings:
                        strings.append(i.lower())
                        self.data.append(i)
                else:
                    if i not in self.data:
                        self.data.append(i)
            else:
                if i not in self.data:
                    self.data.append(i)

    def __next__(self):
        if not self.data:
            raise StopIteration
        return self.data.pop(0)

    def __iter__(self):
        return self
