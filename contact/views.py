from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name= request.POST.get('name','')
            email= request.POST.get('email','')
            content= request.POST.get('content','')

            emailsend= EmailMessage(
                "systems ivek: nuevo mensaje",
                "De {}<{}>\n\nEscribio:\n\n{}".format(name,email,content),
                "no_contestar@inbox.mailtrap.io",
                ["contacto@systemsivek.com"],
                reply_to=[email]
            )
            try:
                #salio chido
                emailsend.send()
                return redirect(reverse('contact')+"?ok")
            except:
                #algo la cague
                return redirect(reverse('contact')+"?fail")
           

    return render(request,'contact/contact.html', {'form':contact_form})