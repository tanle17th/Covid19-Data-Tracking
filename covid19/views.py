from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .forms import Covid19Form
from .models import CovidRecord
import csv
import io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .filters import CovidRecordFilter
# Create your views here.


def covid19_list(request):
    """
    Student name: Van Phuc Tan Le
    Student number: 040985238

    This function calls all objects of the database
    and passes to covid19_list.html the data

    -> Return render the html file and pass through the list of objects
    """
    records = CovidRecord.objects.all()

    myFilter = CovidRecordFilter(request.GET, queryset=records)
    records = myFilter.qs

    context = {'covid19_list': records, 'myFilter': myFilter}
    return render(request, 'covid19/covid19_list.html', context)


def covid19_form(request, id=0):
    """
    Student name: Van Phuc Tan Le
    Student number: 040985238

    This function takes request and id from any url calls it.
    There are two situations:
    1/ Request type is GET: It returns the form
       - If no id is passed, return the empty form for create.
       - If an id is passed, return the form with associate object for update
    -> Return render the html form file and pass through the form

    2/ Request type is POST: It posts data typed in the form
        - If id = 0, user is creating new record
        - If id != 0, user is getting desired update record 
        and pass new data with an instance to save the data
    -> Return redirect to the list
    """
    if request.method == 'GET':
        if id == 0:
            form = Covid19Form()
        else:
            covid19 = CovidRecord.objects.get(pk=id)
            form = Covid19Form(instance=covid19)
        return render(request, 'covid19/covid19_form.html', {'form': form})
    else:
        if id == 0:
            form = Covid19Form(request.POST)
        else:
            covid19 = CovidRecord.objects.get(pk=id)
            form = Covid19Form(request.POST, instance=covid19)
        if(form.is_valid):
            form.save()
        return redirect('/covid19/list')


def covid19_delete(request, id):
    """
    Student name: Van Phuc Tan Le
    Student number: 040985238

    This function get a Covid Record object by the id (pk)
    and call delete function to delete
    -> Return redirect to the list
    """
    covid19 = CovidRecord.objects.get(pk=id)
    covid19.delete()
    return redirect('/covid19/list')


@permission_required('admin.can_add_log_entry')
def upload_csv(request):
    """
    Student name: Van Phuc Tan Le
    Student number: 040985238

    This function takes a csv file chosen by user, read the file,
    delete all current records in the list, loop through the indexes
    in the file and create_or_update record in the list.
    -> Return redirect to the list
    """
    if request.method == 'GET':
        return render(request, 'covid19/covid19_list.html', 'Test')

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file.')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    CovidRecord.objects.all().delete()
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = CovidRecord.objects.update_or_create(
            uid=column[0],
            nameEN=column[1],
            nameFR=column[2],
            date=column[3],
            num_confirmed=column[5],
            num_probable=column[6],
            num_death=column[7],
            num_total=column[8],
            num_tested=column[9],
            rate_tested=column[12],
            num_today=column[13],
            rate_total=column[15],
        )
    context = {}
    return redirect('/covid19/list')
