from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Subcategory, Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-pill'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        subcategories = Subcategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for s in subcategories]

        self.fields['subcategory'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-danger rounded-pill'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        brands = Brand.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for b in brands]

        self.fields['brand'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-success rounded-pill'