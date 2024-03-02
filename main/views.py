from django.shortcuts import render
from . import models

def index(request):
    about_me = models.AboutMe.objects.last()
    educations = models.Education.objects.all()
    skills = models.Skill.objects.all()
    experiences = models.Experience.objects.all()
    profiles = models.Profile.objects.all()
    portfolios = models.Portfolio.objects.all()
    clients = models.Client.objects.all()
    contact = models.Contact.objects.all()
    introduce = models.Introduce.objects.first()

    context = {
        'about_me':about_me,
        'educations':educations,
        'skills':skills,
        'experiences':experiences,
        'profiles':profiles,
        'portfolios':portfolios,
        'clients':clients,
        'contact':contact,
        'introduce':introduce

    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        models.Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        # contact = models.Contact(email=email, name=name, subject=subject, message=message)
        # contact.save()
    return render(request, 'index.html', context)
