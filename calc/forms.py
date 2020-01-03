from django import forms

from  .models import Trip

class Tripform(forms.ModelForm):
    """"
    destinations = forms.CharField(label = 'Destinations', max_length=100)
    firstname = forms.CharField(label = 'FirstName', max_length=100)
    lastname = forms.CharField(label = 'LastName', max_length=100)
    email = forms.EmailField()
    phone = forms.IntegerField()
    gender = forms.CharField(label = 'Gender', max_length=100)
    emergencycontact = forms.IntegerField()
    country = forms.CharField(label = 'country', max_length=100)
    date = forms.DateField()
    numberofadult = forms.IntegerField()
    question = forms.CharField(label = 'Comment', max_length=1000)
    """

    class Meta():
        model =Trip
        fields = [
            'destinations',
            'firstname',
            'lastname',
            'email',
            'phone',
            'gender',
            'emergencycontact',
            'country',
            'date',
            'numberofadult',
            'question'
        ]
