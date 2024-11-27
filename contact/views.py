from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            form.save()
            # Redirect to the about page (homepage) after successful submission
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'about/contact.html', {'form': form})
