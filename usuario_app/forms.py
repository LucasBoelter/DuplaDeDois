from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label = 'Nome de Login',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs= {
                'placeholder': 'ex: Tom Cruise',
            }
        )
    )

    senha = forms.CharField(
        label = 'Senha',
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                'placeholder':'sua senha',
            }
        )
    )