from django import forms
from . import models

class MyWidget(forms.CharField):
    def __init__(self, label, widget, max_length=50, extra_class=None,  **kwargs):
        super(MyWidget, self).__init__(label=label, widget=widget(attrs= {"class": f"{extra_class} contact-form-input"  if extra_class else "contact-form-input" }), **kwargs)


class ContactForm(forms.Form):
    name = MyWidget(label="Name", widget=forms.TextInput, max_length=50)
    phone = MyWidget(label="Phone", widget=forms.TextInput, max_length=50)
    
    email = MyWidget(label="Email", widget=forms.EmailInput, max_length=100)
    service_type = forms.ChoiceField( widget=forms.Select(attrs={"class":"contact-form-input"}),choices = [
        ("webd", "Website Developement"),
        ("webr","Website Redesign"),
        ("appd", "App Developement"),
        ("dataA", "Data Analysis"),
        ("cv", "Computer Vision"),
        ("ml", "Machine Learning"),
        ("nlp", "NLP Engineering"),
    ])
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={"class":"contact-form-input", "rows":3}), max_length=100)

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if len(phone) != 10 or phone[0] in ["0",'1','2','3','4','5'] or not phone.isdigit():
            raise forms.ValidationError("Invalid phone number.")
        return phone

    
    def save(self):
        data = self.cleaned_data
        try:
            models.UserQuery.objects.create(
                **data
            )
        except:
            return False
        return True


