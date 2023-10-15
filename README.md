
# Тестируем классы интернет-магазина
Вам нужно реализовать и протестировать классы интернет-магазина.
Все места, которые нужно дописать как в тестах, так и классах, отмечены `# TODO`.

При реализации обращайте внимание на типизацию аргументов методов и возвращаемых значений.
Так же обратите внимание на организацию тестов в файле с тестами:
- Тесты сгруппированы по классу, который они тестируют.
- Каждый тест называется именем соответствующего ему метода.

Вы можете начать как с реализации классов, так и с тестов.


# Дополнительные вопросы:
1. С чего проще начать выполнение домашнего задания: с тестов или с реализации классов?
2. Почему для хранения товаров в корзине используется словарь, а не список?
3. Зачем нужен __hash__ в классе Product? Изучите этот метод и объясните, почему он нужен.

# Ответы на вопросы:
1. Проще было начинать с классов и потом уже на них писать проверки
2. Используется словарь, тк при работе с корзиной нас будет интересовать количество для конкретного товара
   т.е. связка ключ:значение
3. Хэшируемость делает объект пригодным для использования в качестве ключа словаря, 
   тк эта структура данных используют значение хэша внутри