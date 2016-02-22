from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import render

from .forms import ContactForm, SignUpForm


# Create your views here.
def home(request):
    title = 'Welcome'
    # if request.user.is_authenticated():
    #     title = "My Title %s" %(request.user)

    # add a form here :)

    # if request.method == "POST":
    #     print(request.POST)

    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form

    }
    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)
        instance.save()
        context = {
            'title': 'ThankYou'
        }
        # print(instance.email)
        # print(instance.timestamp)

    return render(request, "index.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
        #     print(key)
        #     print(form.cleaned_data.get(key))
        form_email = form.cleaned_data.get("email")
        form_name = form.cleaned_data.get("name")
        subject = form.cleaned_data.get("subject")
        form_message = form.cleaned_data.get("message")
        # print (email,name,subject,message)
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'vamagithub@gmail.com']
        contact_message ="%s: %s via %s"%(
            form_name ,
            form_message,
            form_email)

        send_mail(subject,
                  contact_message,
                  from_email ,
                  to_email,
                  fail_silently=False)       #SEE THIS MAKE IT TRUE IT DOESNOT WORK


    context = {
        "form": form,
    }
    return render(request,"forms.html",context)