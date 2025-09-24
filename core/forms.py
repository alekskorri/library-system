from django import forms
from .models import Books


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'title',
            'author',
            'gener',
            'edition',
            'publication',
            'publisher',
            'price',
            'description',
            'image'
       ]

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'author': forms.TextInput(attrs={'class': 'form-control'}),
                'gener': forms.Select(attrs={'class': 'form-control'}),
                'edition': forms.DateInput(attrs={'class': 'form-control'}),
                'publication': forms.DateInput(attrs={'class': 'form-control'}),
                'publisher': forms.TextInput(attrs={'class': 'form-control'}),
                'price': forms.NumberInput(attrs={'class': 'form-control'}),
                'description': forms.Textarea(attrs={'class': 'form-control', "rows":"3"}),
                'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),

            }