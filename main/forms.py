from django import forms

from .models import SportTuri, SportCenter



class SearchForm(forms.Form):
    q = forms.CharField(max_length=255, label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Qidiruv"}))


class SportTuriCreateForm(forms.ModelForm):
    class Meta:
        model = SportTuri
        fields = ['nomi', 'photo']

        widgets = {
            "nomi": forms.TextInput(attrs={"class": "form-control pl-0"}),
            "photo": forms.FileInput(attrs={"class": "form-control pl-0 pb-2", "type": "file"}),
        }

        labels = {
            "photo": "Rasm"
        }
        

class SportCenterCreateForm(forms.ModelForm):
    class Meta:
        model = SportCenter
        fields = '__all__'


        widgets = {
            "nomi": forms.TextInput(attrs={"class": "form-control mb-2"}),
            "sport_turi": forms.Select(attrs={"class": "form-control mb-2"}),
            "manzil": forms.TextInput(attrs={"class": "form-control mb-2"}),
            "telfon": forms.TextInput(attrs={"class": "form-control mb-2"}),
            "opens": forms.TimeInput(attrs={"class": "form-control mb-2", "type": "time"}),
            "closes": forms.TimeInput(attrs={"class": "form-control mb-2", "type": "time"   }),
            "photo": forms.FileInput(attrs={"class": "form-control mb-2 pl-0 pb-3", "type": "file"}),
            "latitude": forms.TextInput(attrs={"class": "form-control mb-2"}),
            "longtitude": forms.TextInput(attrs={"class": "form-control mb-2"}),
        }

        labels  = {
            "opens": "Ochiladi",
            "closes": "Yopiladi",
            "latitude": "Kenglik",
            "longtitude": "Uzunlik",
            "photo": "Rasm",
            "is_active": "Active",
        }
