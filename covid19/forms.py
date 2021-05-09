from django import forms
from covid19.models import CovidRecord


class DateInput(forms.DateInput):
    """
    Student name: Van Phuc Tan Le
    Student number: 040985238

    This class determines the input type of date.
    It will give the ability of date-picker for the date field
    in the form.

    -> Return None
    """
    input_type = 'date'


class Covid19Form(forms.ModelForm):

    class Meta:

        """
        Student name: Van Phuc Tan Le
        Student number: 040985238

        This class creates the form for user's input.
        Whenever it is called, the form of all fields will be propmted
        and formatted based on CovidRecord model.

        -> Return None
        """
        model = CovidRecord
        fields = '__all__'
        widgets = {'date': DateInput()}
        labels = {
            'uid': 'Id',
            'nameEN': 'Province name in EN',
            'nameFR': 'Province name in FR',
            'date': 'Record Date',
            'num_confirmed': 'Confirm cases',
            'num_probable': 'Probable cases',
            'num_death': 'Number of death',
            'num_total': 'Total cases',
            'num_tested': 'Tested cases',
            'rate_tested': 'Tested rate',
            'num_today': 'Number of cases today',
            'rate_total': 'Rate in total',
        }

    def __init__(self, *args, **kwargs):
        """
        Student name: Van Phuc Tan Le
        Student number: 040985238

        This function lets developer customize the data fields of the form
        Ex: We can change the date field from type input 
        to a date-picker

        -> Return None
        """
        super(Covid19Form, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['class'] = 'datepicker'
        # self.fields['date'].required = False
