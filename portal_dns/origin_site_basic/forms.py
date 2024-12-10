from django.forms import Form, CharField, EmailField



class CheckReg(Form):
    name = CharField(max_length=100, label="Your Name")
    email = EmailField(label="Your Email")