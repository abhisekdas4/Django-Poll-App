from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import PollModel
from .forms import PollModelForm


def home(request):
    qs = PollModel.objects.all()
    context = {'qs': qs}
    return render(request, 'poll/index.html', context)


def create(request):
    poll = PollModel()
    form = PollModelForm()

    if request.method == 'POST':
        form = PollModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            HttpResponseRedirect('/')

    context = {'form': form}
    return render(request, 'poll/create.html', context)


def vote(request, pk):
    poll = PollModel.objects.get(id=pk)
    context = {'poll': poll}

    if request.method =='POST':
        if request.POST.get('poll') == 'option1':
            poll.option_one_count += 1
        elif request.POST.get('poll') == 'option2':
            poll.option_two_count += 1
        elif request.POST.get('poll') == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')


        poll.save()
        HttpResponseRedirect('/result/', poll.id)


    return render(request, 'poll/vote.html', context)


def result(request, pk):
    poll = PollModel.objects.get(id=pk)
    context = {'poll':poll}
    return render(request, 'poll/result.html', context)
