from django.shortcuts import render, get_object_or_404


class ObjDetailMixin:
    model = None
    template = None

    def get(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        return render(request, self.template, context={self.model.__name__.lower(): obj})
