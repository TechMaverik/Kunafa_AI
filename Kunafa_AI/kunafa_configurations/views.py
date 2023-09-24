from django.shortcuts import render
from kunafa_configurations.forms import IPCameraForm
from .models import IPCamera

# Create your views here.
def load_main_page(request):
    status=False
    ip_form=IPCameraForm
    all_data=IPCamera.objects.all()
    if request.POST:
        form = ip_form(request.POST)
        if form.is_valid():
            form.save()
            status=True
    context={
        'form':ip_form,
        'status':status,
        'all_data':all_data}
    return render(request,"index.html",context)

def kill(request):
    IPCamera.objects.all().delete()
    context={'delete':'deleted'}
    return render(request,"deleted.html",context)
