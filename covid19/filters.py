import django_filters
from django_filters import DateFilter, CharFilter
from .models import *
from django_filters.widgets import RangeWidget
from django import forms


class CovidRecordFilter(django_filters.FilterSet):
    """
    Student name: Van Phuc Tan Le
    Student number: 040985238

    This class initializes the filter based on CovidRecord Form.
    It sets up how the filter will work:
    1/ date: the date will be filtered by from-to range.
    2/ name in English: is filtered if user's input contains the keyword
    that matches with data
    3/ name in France: is filtered if user's input contains the keyword
    that matches with data

    -> Return None
    """
    date = django_filters.DateFromToRangeFilter(
        widget=RangeWidget(attrs={'type': 'date'}))
    # start_date = DateFromToRangeFilter(
    #     field_name='date', lookup_expr='gte', widget=RangeWidget(attrs={'type': 'date'}))
    # end_date = DateFilter(
    #     field_name='date', lookup_expr='lte', widget=DateInput(attrs={'type': 'date'}))
    nameEN = CharFilter(field_name='nameEN', lookup_expr='icontains')
    nameFR = CharFilter(field_name='nameFR', lookup_expr='icontains')

    class Meta:
        """
        Student name: Van Phuc Tan Le
        Student number: 040985238

        This class determines the model will be filtered (CovidRecord)
        Determines the fields will be filtered (name in English, 
        name in France, and from-to date range)
        -> Return None
        """
        model = CovidRecord
        fields = ['nameEN', 'nameFR']
        #exclude = ['uid', 'rate_tested', 'rate_total']
