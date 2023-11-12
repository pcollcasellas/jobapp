from django.shortcuts import render
from django.template import loader # noqa

from app.models import JobPost


# Create your views here.
def job_list(request):
    jobs = JobPost.objects.all()
    context = {'jobs': jobs}
    return render(request, 'app/job_list.html', context)


def job_detail(request, id):
    job = JobPost.objects.get(id=id)
    context = {'job': job}
    print(context)
    return render(request, 'app/job_detail.html', context)
