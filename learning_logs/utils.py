from django.shortcuts import render, get_object_or_404
from django.http import Http404


def check_topic_owner(topic, request):
    if topic.owner != request.user:
        raise Http404
    return True


class ObjDetailMixin:
    model = None
    template = None
    obj_param = None

    def get(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        if check_topic_owner(obj.__getattribute__(self.obj_param), request):
            return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

