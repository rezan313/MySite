from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import models

def index(request):
    latest_qustion_list =models.Qustion.objects.order_by('-pup_date')
    context={'latest_qustion_list':latest_qustion_list}
    return render(request,'polls/index.html',context)
def detail(request, qustion_id):
    qustion=get_object_or_404(models.Qustion,pk=qustion_id)
    return render(request,'polls/detail.html',{'qustion':qustion})
def results(request, qustion_id):
    qustion=get_object_or_404(models.Qustion,pk=qustion_id)
    return render(request,'polls/results.html',{'qustion': qustion})

def vote(request, qustion_id):
    qustion = get_object_or_404(models.Qustion, pk=qustion_id)
    try:
        selected_choice = qustion.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'qustion': qustion,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(qustion.id,)))
# Create your views here.