document.body.addEventListener('htmx:afterSwap', function(event) {
    const response = event.detail?.xhr?.response; // Безопасный доступ к свойствам
    if (response) {
        const data = JSON.parse(response);

        if (data.status === 'success') {
            // Обновляем количество товаров в корзине
            const cartTotalElement = document.getElementById('cart-total');
            if (cartTotalElement) {
                cartTotalElement.textContent = `Товаров в корзине: ${data.cart_total}`;
            }
        } else if (data.status === 'error') {
            console.error('Ошибка при добавлении товара:', data.errors);
        }
    }
});