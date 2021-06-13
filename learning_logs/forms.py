from django.forms import ModelForm, Textarea, TextInput
from .models import Topic, Entry


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        widgets = {'text': TextInput(attrs={'class': 'form-control'})}


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text']
        widgets = {'title': TextInput(attrs={'class': 'form-control'}),
                   'text': Textarea(attrs={'cols': 80, 'class': 'form-control'})}
