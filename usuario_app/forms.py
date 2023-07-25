from django import forms
from usuario_app.models import ImagemUsuario

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
                raise forms.ValidationError('espaços não são permitidos')
            else:
                return nome

    def clean_senha2(self):
        senha1 = self.cleaned_data.get('senha1')
        senha2 = self.cleaned_data.get('senha2')

        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError('as senhas não são iguais.')
            else:
                return senha2

class ImagemUsuarioForm(forms.ModelForm):
    class Meta:
        model = ImagemUsuario
        #coloquei qualquer coisa pra ele funcionar
        exclude=['']
        
        widgets = {
            # 'nome': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Ex.: Tom Cruise'
            #         }
            # ),
            'categoria': forms.Select(
                attrs={
                    'placeholder': '-- categoria --'
                    }
                    ),
            'foto': forms.FileInput(attrs={'class': 'file-input', 'title': 'Escolha a imagem', 'data-filename-placement': 'outside'}),
            #dar uma olhada..
            'usuario': forms.Select()
        }
        
        labels = {
            'nome': 'Nome Completo',
            'categoria': 'Categoria',
            'foto': 'Imagem',
            'usuario': 'Usuario'
        }













