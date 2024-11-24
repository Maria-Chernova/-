from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    # Fetching students ordered by group
    students = Student.objects.all().order_by('group')

    context = {
        'object_list': students  # Pass the ordered students to the template
    }

    return render(request, template, context)