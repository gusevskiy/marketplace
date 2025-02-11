from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser



#  создадим собственный класс для формы регистрации
#  сделаем его наследником предустановленного класса UserCreationForm
class CreationForm(UserCreationForm):
    agree_to_privacy = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(),
        label='Согласие с обработкой персональных данных',
        error_messages={'required': 'Вы должны согласиться с обработкой персональных данных.'}
    )
    class Meta(UserCreationForm.Meta):
        # укажем модель, с которой связана создаваемая форма
        model = CustomUser
        # укажем, какие поля должны быть видны в форме и в каком порядке
        fields = ('first_name', 'last_name', 'email', 'agree_to_privacy')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.agreed_to_privacy = self.cleaned_data['agree_to_privacy']
        if commit:
            user.save()
        return user  # Убедитесь, что возвращается объект пользователя