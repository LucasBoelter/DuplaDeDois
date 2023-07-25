from django import forms
from assentos_app.models import Vendas

class VendasForm(forms.ModelForm):
    class Meta:
        model = Vendas

        fields = ['forma_pagamento', 'assento', 'filme']


        widgets = {
            'filme': forms.HiddenInput(
                attrs={
                    'name': 'filme',
                    'id':'filme'
                    }
            ),
            
            'assento': forms.HiddenInput(
                attrs={
                    'name': 'assento',
                    'id':'assento'
                    }
            ),

            'forma_pagamento': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

        labels = {
            'forma_pagamento': 'Forma de Pagamento'
        }