from django.forms import ModelForm, Textarea
from .models import Topic, Entry


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': Textarea(attrs={'cols': 80})}
