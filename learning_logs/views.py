from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def check_topic_owner(topic, request):
    if topic.owner != request.user:
        raise Http404
    return True


def index(request):
    # homepage
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    # All topics page
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context=context)


@login_required
def topic(request, topic_id):
    # one topic with all entries
    topic = Topic.objects.get(id=topic_id)
    if check_topic_owner(topic, request):
        entries = topic.entry_set.order_by('-date_added')
        context = {'topic': topic, 'entries': entries}
        return render(request, 'learning_logs/topic.html', context=context)


@login_required
def new_topic(request):
    # create new topic
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def entry(request, entry_id):
    # one entry
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if check_topic_owner(topic, request):
        context = {'topic': topic, 'entry': entry}
        return render(request, 'learning_logs/entry.html', context=context)


@login_required
def new_entry(request, topic_id):
    # create new entry
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            if check_topic_owner(new_entry.topic, request):
                new_entry.save()
                return redirect('learning_logs:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


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
                return redirect('learning_logs:topic', topic_id=topic.id)
        context = {'entry': entry, 'topic': topic, 'form': form}
        return render(request, 'learning_logs/edit_entry.html', context)
