from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label = 'Nome de Login',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs= {
                'placeholder': 'Ex: Tom Cruise',
            }
        )
    )

    senha = forms.CharField(
        label = 'Senha',
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                'placeholder':'Sua senha',
            }
        )
    )

class CadastroForms(forms.Form):
    nome_completo = forms.CharField(
        label= 'Nome Completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ex.: Tom Cruise',
            }
        )
    )

    email = forms.EmailField(
        label= 'E-mail',
        required=True,
        max_length=50,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Ex.: tom@cruise.com',
            }
        )
    )

    senha1 = forms.CharField(
        label = 'Senha',
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                'placeholder':'Senha',
            }
        )
    )

    senha2 = forms.CharField(
        label = 'Confirme a senha',
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                'placeholder':'Senha',
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_completo')

        if nome:
            nome = nome.strip()

            if ' ' in nome:
                raise forms.ValidationError('espaços n são permitidos')
            else:
                return none


















