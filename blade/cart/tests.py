from decimal import Decimal
from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from product.models import Product, Category
from .cart import Cart
from django.conf import settings


class CartTests(TestCase):
    def setUp(self):
        """Настройка тестовых данных."""
        # Создаем категорию с id=1
        self.category = Category.objects.create(name="Test Category")
        # Создаем товар, связанный с категорией
        self.product = Product.objects.create(
            name="Test Product",
            price=Decimal('10.00'),
            stock=2,
        )
        self.factory = RequestFactory()

    def _get_request(self):
        """Создает и возвращает запрос с сессией."""
        request = self.factory.get('/')
        middleware = SessionMiddleware(lambda req: None)
        middleware.process_request(request)
        request.session.save()
        return request

    def test_add_product(self):
        """Тест добавления товара в корзину."""
        request = self._get_request()
        cart = Cart(request)

        # Добавляем товар
        cart.add(self.product, quantity=1)

        # Проверяем, что товар добавлен
        self.assertIn(str(self.product.id), cart.cart)
        self.assertEqual(cart.cart[str(self.product.id)]['quantity'], 1)
        self.assertEqual(cart.cart[str(self.product.id)]['price'], '10.00')

    def test_remove_product(self):
        """Тест удаления товара из корзины."""
        request = self._get_request()
        cart = Cart(request)

        # Добавляем товар
        cart.add(self.product, quantity=2)

        # Удаляем товар
        cart.remove(self.product)

        # Проверяем, что товар удален
        self.assertNotIn(str(self.product.id), cart.cart)

    def test_update_quantity(self):
        """Тест обновления количества товара."""
        request = self._get_request()
        cart = Cart(request)

        # Добавляем товар
        cart.add(self.product, quantity=2)

        # Обновляем количество
        cart.add(self.product, quantity=3, override_quantity=True)

        # Проверяем, что количество обновлено
        self.assertEqual(cart.cart[str(self.product.id)]['quantity'], 3)

    def test_get_total_price(self):
        """Тест расчета общей стоимости корзины."""
        request = self._get_request()
        cart = Cart(request)

        # Добавляем два товара
        cart.add(self.product, quantity=2)
        cart.add(self.product, quantity=3)

        # Проверяем общую стоимость
        self.assertEqual(cart.get_total_price(), Decimal('50.00'))

    def test_clear_cart(self):
        """Тест очистки корзины."""
        request = self._get_request()
        cart = Cart(request)

        # Добавляем товар
        cart.add(self.product, quantity=2)

        # Очищаем корзину
        cart.clear()

        # Проверяем, что корзина пуста
        self.assertNotIn(settings.CART_SESSION_ID, request.session)

    def test_iteration(self):
        """Тест итерации по корзине."""
        request = self._get_request()
        cart = Cart(request)

        # Добавляем товар
        cart.add(self.product, quantity=2)

        # Проверяем итерацию
        for item in cart:
            self.assertEqual(item['product'], self.product)
            self.assertEqual(item['quantity'], 2)
            self.assertEqual(item['price'], Decimal('10.00'))
            self.assertEqual(item['total_price'], Decimal('20.00'))

    def test_length(self):
        """Тест подсчета количества товаров в корзине."""
        request = self._get_request()
        cart = Cart(request)

        # Добавляем товар
        cart.add(self.product, quantity=2)

        # Проверяем количество
        self.assertEqual(len(cart), 2)