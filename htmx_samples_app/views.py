from django.shortcuts import render, get_object_or_404, redirect
from htmx_samples_app.models import Profile
from htmx_samples_app.forms import ProfileModelForm
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse

# Create your views here.
def show_info_view(request, pk):
    item = Profile.objects.get(pk = pk)
    context = dict(
        item = item,   
    )
    return render(request, 'htmx_samples_app/row.html', context)

def show_list(request):
    items = Profile.objects.all()
    context = dict(
        items = items,
    )
    return render(request, 'htmx_samples_app/base.html', context)


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileModelForm
    template_name = 'htmx_samples_app/edit_form.html'
    def get_success_url(self):
        return reverse_lazy('htmx_samples_app:show_info_view', kwargs={'pk': self.object.pk})
    
    