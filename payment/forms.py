from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    full_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'w-100 form-control border-0 py-3 mb-4'}))
    phone = forms.CharField(min_length=10,max_length=12, widget=forms.TextInput(attrs={'class': 'w-100 form-control border-0 py-3 mb-4', 'type': 'number', 'pattern': '[0-9]*'}))
    post_code = forms.CharField(min_length=6,max_length=6, widget=forms.TextInput(attrs={'class': 'w-100 form-control border-0 py-3 mb-4', 'type': 'number', 'pattern': '[0-9]*'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'w-100 form-control border-0 py-3 mb-4'}))
    state = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'w-100 form-control border-0 py-3 mb-4'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-100 form-control border-0 mb-4'}))
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError("Phone number should contain only digits.")
        return phone
    class Meta:
        model = Order
        fields = ['full_name','phone','post_code','city','state','address','payment_method']
        widgets = {
            'payment_method': forms.RadioSelect,
        }