from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, HttpResponse
from django.views import View
# Create your views here.
from . import forms
from django.contrib import messages
from . import models

class HomeView(View):
    def get(self, request, *args, **kwargs):
        testimonials = models.Testimonial.objects.all()
        contact_form = forms.ContactForm()
        return render(request, 'home.html', {"contact_form":contact_form, "testimonials":testimonials})

    def post(self, request, *args, **kwargs):
        f = forms.ContactForm(request.POST)
        if f.is_valid():
            if f.save():
                messages.success(request, "Form saved successfully. We will contact you soon.")
            else:
                messages.error(request, "Failed to save. Please try again")
            return redirect( request.META.get("HTTP_REFERER") )
        else:
            messages.warning(request,f.errors)
            return HttpResponseRedirect( f"/#contact")


class ContactUsView(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'contact.html')

    
class BlogsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blogs.html')

def GetPage(request, page_name):
    return render(request, f"components/{page_name}.html")

class FeedbackView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'feedback.html')
    
    def post(self, request, *args, **kwargs):
        name, message, rating, email  = request.POST.get('name'), request.POST.get('message'), request.POST.get('rating'), request.POST.get('email')
        if not (message or rating or name or email):
            err = "Please fill the form correctly."
            return render(request, 'feedback.html',{"error": err, "message": message, "email": email, "name": name})
        else:
            models.Feedback.objects.create(
                name = name,
                rating = rating,
                email = email,
                message = message
            )
            messages.success(request, f"Thank you {name} for your valuable feedback. It's truly appreciated and will help me improve!")
            return  redirect('feedback')
            
    
class CareersView(View):
    def get(self, request):
        return render(request, 'Careers.html')


class ProjectsView(View):
    def get(self, request):
        projects = models.Projects.objects.all()
        return render(request, 'Projects.html', {"projects": projects})

    
class Team(View):
    def get(self, request):
        teams = models.Team.objects.all()
        return render(request, 'Team.html', {"teams":teams})

    