def introspection_info(obj):
    """
    Функция для проведения интроспекции объекта и сбора его подробной информации.
    :param obj: Обект для интроспекции
    :return: Словарь с информацией об объекте
    """
    info = {'type': type(obj).__name__, 'module': obj.__class__.__module__, 'attributes': [], 'methods': [] }

    attributes = dir(obj)
    for attr in attributes:
        if not attr.startswith('__') and not attr.endswith('__'):
            try:
                if callable(getattr(obj, attr)):
                    info['methods'].append(attr)
                else:
                    info['attributes'].append(attr)
            except Exception:
                pass

    if hasattr(obj, '__doc__'):
        info['docstring'] = obj.__doc__

    if isinstance(obj, type):
        info['base_classes'] = [base.__name__ for base in obj.__bases__]
    return info

number_info = introspection_info(42)
print("Информация о числе:")
print(number_info)

class Person:
     """Класс,предстовляющий человека."""
     def __init__(self, name, age):
         self.name = name
         self.age = age

     def say_hello(self):
         return  f"Приветб меня зовут {self.name}"
person = Person("Алиса", 30)
person_info = introspection_info(person)
print("\nИнформация об объекте Person:")
print(person_info)

def example_function(x, y):
    """Пример функции для демонсрации интроспекциию"""
    return x + y

func_info = introspection_info(example_function)
print("\nИнформаия о функции:")
print(func_info)