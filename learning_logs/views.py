from django.shortcuts import redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.core.paginator import Paginator
from .utils import *


def index(request):
    # homepage
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    # All topics page
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    return render(request, 'learning_logs/topics.html', context={'topics': topics})


@login_required
def read_topic(request, id):
    topic = get_object_or_404(Topic, id=id)
    entries = topic.entries.all()
    paginator = Paginator(entries, 10)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {'page': page,
               'topic': topic,
               'is_paginated': is_paginated,
               'next_url': next_url,
               'prev_url': prev_url}
    return render(request, 'learning_logs/topic.html', context=context)


class TopicCreate(LoginRequiredMixin, ObjCreateMixin, View):
    model_form = TopicForm
    template = 'learning_logs/new_topic.html'

    def post(self, request):
        form = self.model_form(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
        return render(request, self.template, context={'form': form})


@login_required
def edit_entry(request, entry_id):
    # edit entry
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if check_topic_owner(topic, request):
        if request.method != 'POST':
            form = EntryForm(instance=entry)
        else:
            form = EntryForm(instance=entry, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('learning_logs:topic', id=topic.id)
        context = {'entry': entry, 'topic': topic, 'form': form}
        return render(request, 'learning_logs/edit_entry.html', context)


class EntryDetail(LoginRequiredMixin, ObjDetailMixin, View):
    model = Entry
    template = 'learning_logs/entry.html'


class EntryCreate(LoginRequiredMixin, View):
    def get(self, request, topic_id):
        form = EntryForm()
        topic = Topic.objects.get(id=topic_id)
        return render(request, 'learning_logs/new_entry.html', context={'form': form, 'topic': topic})

    def post(self, request, topic_id):
        form = EntryForm(data=request.POST)
        topic = Topic.objects.get(id=topic_id)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', id=topic_id)
        return render(request, 'learning_logs/new_entry.html', context={'form': form, 'topic': topic})
