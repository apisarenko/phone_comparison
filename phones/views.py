from django.shortcuts import render
from .models import Apple, Digma, Vertex


def show_catalog(request):
    template = 'catalog.html'
    list_phone = (Apple, Digma, Vertex)
    list_context = []
    for model in list_phone:
        ddd = model.objects.select_related('phone')
        list_context.append(ddd)
    context = {}
    context['objects'] = list_context

    return render(
        request,
        template,
        context
    )
