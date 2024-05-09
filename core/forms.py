from django import forms
from django.core.exceptions import ValidationError


class AgendaForm(forms.Form):
    nome = forms.CharField(max_length=150)
    telefone = forms.CharField(max_length=20)
    cpf = forms.CharField(max_length=30)
        
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if telefone.startswith(('19', '16')):
            return telefone
        raise ValidationError('DDD válido somente o 19')
    
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        # Remove formatting characters from the CPF
        cpf = ''.join(filter(str.isdigit, cpf))
        if len(cpf) != 11:
            raise ValidationError('Esse campo precisa ter 11 números')
        return cpf
