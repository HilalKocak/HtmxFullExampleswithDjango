from django.shortcuts import render
from htmx_samples_app.models import Profile
# Create your views here.
def click_to_edit_view(request):
    item = Profile.objects.get()
    context = dict(
        item = item,   
    )
    
    return render(request, 'htmx_samples_app/base.html', context)