from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from employees.models import Employee

# Create your views here.

def employee_details(request, pk):
    # try:
    #     employee = Employee.objects.get(pk=pk)
    #     print(employee)
    # except:
    #     raise Http404
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        'employee': employee
    }
    return render(request , 'employee_detail.html',context)