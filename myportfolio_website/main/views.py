#main/views.py


from django.shortcuts import render, get_object_or_404
from .models import About, Count, Skill, Interest, Testimonial, Summary, Education, VoluntaryExperience, ProfessionalExperience, Service, Portfolio

def index(request):
    about = About.objects.first()
    counts = Count.objects.all()
    skills = Skill.objects.all()
    interests = Interest.objects.all()
    testimonials = Testimonial.objects.all()
    summary = Summary.objects.first()  # Fetch summary
    education = Education.objects.all()  # Fetch education
    voluntary_experience = VoluntaryExperience.objects.all()  # Fetch voluntary experience
    professional_experience = ProfessionalExperience.objects.all()  # Fetch professional experience
    services = Service.objects.all()  # Fetch services
    portfolios = Portfolio.objects.all()

    context = {
        'about': about,
        'counts': counts,
        'skills': skills,
        'interests': interests,
        'testimonials': testimonials,
        'summary': summary,
        'education': education,
        'voluntary_experience': voluntary_experience,
        'professional_experience': professional_experience,
        'services': services,
        'portfolios': portfolios,
    }

    return render(request, 'index.html', context)


def portfolio_details(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    return render(request, 'portfolio-details.html', {'portfolio': portfolio})


