from django import forms
from assentos_app.models import Vendas

class VendasForm(forms.ModelForm):
    # filme = forms.HiddenInput()

    # assento = forms.HiddenInput()
    
    # forma_pagamento = forms.CharField(
    #     label = 'Forma de Pagamento',
    #     required=True,
    #     max_length=70,
    #     widget= forms.Select(
    #         attrs={
    #             'placeholder':'Forma de Pagamento',
    #             'name': 'forma_pagamento'
    #         }
    #     )
    # )
    class Meta:
        model = Vendas

        fields = ['forma_pagamento']
        # exclude = ['filme', 'assento']

        widgets = {
            'filme': forms.TextInput(
                attrs={
                    'name': 'filme',
                    'id':'filme'
                    }
            ),
            'assento': forms.TextInput(
                attrs={
                    'name': 'assento',
                    'id':'assento'
                    }
            ),
            'forma_pagamento': forms.Select(),
        }

        labels = {
            'forma_pagamento': 'Forma de Pagamento'
        }