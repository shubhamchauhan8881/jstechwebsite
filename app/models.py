from django.db import models

# Create your models here.
class UserQuery(models.Model):
    created_at  = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    service_type = models.CharField(max_length= 12, choices=[
        ("webd", "Website Developement"),
        ("webr","Website Redesign"),
        ("appd", "App Developement"),
        ("dataA", "Data Analysis"),
        ("cv", "Computer Vision"),
        ("ml", "Machine Learning"),
        ("nlp", "NLP Engineering"),

        ])
    message = models.CharField(max_length=1500)

    def __str__(self):
        return self.name + ' ' + self.phone

class Feedback(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' ' + self.email
    

class Blogs(models.Model):  
    created_at = models.DateTimeField(auto_now_add=True)

    is_published = models.BooleanField(default=False)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/blogs", null=True, blank=True)
    content = models.TextField(max_length=10000)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40)
    message = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="media/testimonial")
    display = models.BooleanField(default=False)
    url = models.URLField(blank=True, null=True)


class Team(models.Model):

    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/team/")

    def __str__(self):
        return self.name


class Projects(models.Model):

    name = models.CharField(max_length=50)
    url = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=600)
    image = models.ImageField(upload_to="media/projects")

    def __str__(self):
        return self.name


class TelegramClients(models.Model):
    name = models.CharField(max_length= 100)
    chat_id = models.CharField(max_length= 50)

    class Meta:
        verbose_name = 'telegram client'

    @staticmethod
    def all():
        return TelegramClients.objects.all()
    def __str__(self):
        return self.name