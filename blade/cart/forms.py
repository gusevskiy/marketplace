from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,  # Минимальное значение
        max_value=10,  # Максимальное значение (можно изменить)
        initial=1,  # Значение по умолчанию
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'style': 'width: 60px; height: 42px'
        }),  # Виджет для ввода числа
        label=""  # Убираем метку
    )
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
