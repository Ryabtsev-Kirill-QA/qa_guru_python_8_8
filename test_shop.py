"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def second_product():
    return Product("pencil", 50, "This is a pencil", 500)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        # Проверка, если продукта хватает
        assert product.check_quantity(product.quantity - 1) is True
        # Проверка, если продукта не хватает
        assert product.check_quantity(product.quantity + 1) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(100)
        # Проверка, что количество продукта после покупки уменьшилось
        assert product.quantity == 900

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product)
        # Проверка, что продукт появился в корзине
        assert product in cart.products

    def test_add_product_count(self, product, cart):
        cart.add_product(product)
        cart.add_product(product, buy_count=1)
        # Проверка, что количество продукта в корзине увеличилось
        assert cart.products.get(product) == 2

    def test_remove_product_all(self, product, cart):
        cart.add_product(product)
        cart.remove_product(product)
        # Проверка, что продукт удален из корзины
        assert product not in cart.products

    def test_remove_product_less(self, product, cart):
        cart.add_product(product, buy_count=5)
        cart.remove_product(product, remove_count=3)
        # Проверка, что продукт удален полностью при удалении больше, чем есть в корзине
        assert cart.products[product] == 2

    def test_remove_product_more(self, product, cart):
        cart.add_product(product, buy_count=10)
        cart.remove_product(product, remove_count=20)
        # Проверка, что продукт удален полностью при удалении больше, чем есть в корзине
        assert cart.products == {}

    def test_clear(self, product, cart):
        cart.add_product(product)
        cart.clear()
        # Проверка очистки корзины
        assert cart.products == {}

    def test_get_total_price(self, product, second_product, cart):
        cart.add_product(product, buy_count=5)
        cart.add_product(second_product, buy_count=10)
        # Проверка расчета полной стоимости товаров в корзине
        assert cart.get_total_price(product) == 500 + 500

    def test_buy(self, product, cart):
        cart.add_product(product, buy_count=5)
        cart.buy(5)
        # Проверка, что после покупки, количество товара в корзине уменьшилось на количество купленного
        assert cart.products.get(product) == 0

    def test_buy_more_than_available(self, product, cart):
        cart.add_product(product, buy_count=5000)
        # Проверка ошибки при покупке больше, чем есть на складе
        with pytest.raises(ValueError):
            cart.buy(5000)
