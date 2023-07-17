from django import forms
from .models import Iha,RentRecord, User

class IhaCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Iha
        fields = "__all__"

class IhaUpdateForm(forms.ModelForm):
    class Meta:
        model = Iha
        fields = '__all__'


class IhaRentForm(forms.ModelForm):
    user_rent = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None, to_field_name='username')
    class Meta:
        model = RentRecord
        fields =  ["user_rent",'iha','rental_start_date', 'rental_end_date']
        widgets = {
            'rental_start_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
            'rental_end_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
        }
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.fields['user_rent'].disabled = True
        


    def clean_rental_end_date(self):
        rental_start_date = self.cleaned_data.get('rental_start_date')
        rental_end_date = self.cleaned_data.get('rental_end_date')

        if rental_start_date and not rental_end_date:
            raise forms.ValidationError("Please provide a rental end date.")

        return rental_end_date

