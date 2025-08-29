from django import forms
from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['nome', 'sobrenome', 'age', 'salary', 'bio', 'photo']

        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'age': 'Idade',
            'salary': 'Salário (R$)',
            'bio': 'Biografia',
            'photo': 'Foto de Perfil',
        }

        help_texts = {
            'age': 'Digite sua idade em anos.',
            'salary': 'Informe seu salário mensal.',
            'bio': 'Escreva uma breve descrição sobre você.',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Ex: João', 'class': 'form-control'}),
            'sobrenome': forms.TextInput(attrs={'placeholder': 'Ex: Silva', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'bio': forms.Textarea(attrs={'placeholder': 'Fale um pouco sobre você...', 'class': 'form-control', 'rows': 4}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 0:
            raise forms.ValidationError("A idade não pode ser negativa.")
        return age

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary < 0:
            raise forms.ValidationError("O salário não pode ser negativo.")
        return salary