from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

        widgets = {
        'category':forms.Select(attrs={##This will give some format to the form

            'class':INPUT_CLASSES

        }),
        'name':forms.TextInput(attrs={##This will give some format to the form

            'class':INPUT_CLASSES

        }),
        'description':forms.TextInput(attrs={##This will give some format to the form

            'class':INPUT_CLASSES

        }),
        'price':forms.TextInput(attrs={##This will give some format to the form

            'class':INPUT_CLASSES

        }),
        'image':forms.FileInput(attrs={##This will give some format to the form

            'class':INPUT_CLASSES

        })

        
        }
