from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from django.views.generic import CreateView, ListView, View

from estate.forms import EmailForm
from estate.models import PropertyModel


class HomeView(CreateView):
    template_name = 'estate/index.html'
    form_class = EmailForm
    success_url = '/'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'
        return context

class SearchView(ListView):
    model = PropertyModel
    template_name = 'estate/properties.html'



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("search")
        if query is not None:
            object = PropertyModel.objects.filter(
                Q(zipcode__icontains=query)
            )
        else:
            object = PropertyModel.objects.all()
        context['title'] = 'Results'
        context['object_list'] = object
        context['search'] = query
        return context

def search_property(request):
    search_text = request.GET.get('search')
    print(search_text)
    if not search_text:
        print(search_text)
        search_text = ""
    results = PropertyModel.objects.filter(zipcode__icontains=search_text)
    context = {'results':results}

    return render(request, 'estate/search_results.html', context)

def property(request, property_slug):
    property = get_object_or_404(PropertyModel, slug=property_slug)
    print(property)
    return render(request, 'estate/single_property.html', {'property':property})
