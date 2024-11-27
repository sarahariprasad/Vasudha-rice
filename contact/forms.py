from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'w-100 form-control border-0 py-3 mb-4'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'w-100 form-control border-0 py-3 mb-4'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w-100 form-control border-0 py-3 mb-4'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-100 form-control border-0 mb-4'}))
    phone = forms.CharField(min_length=10,max_length=12, widget=forms.TextInput(attrs={'class': 'w-100 form-control border-0 py-3 mb-4', 'type': 'number', 'pattern': '[0-9]*'}))
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError("Phone number should contain only digits.")
        return phone
    class Meta:
         model = Contact
         fields = ['name', 'subject','email','phone', 'message']