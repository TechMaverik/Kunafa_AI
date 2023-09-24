from django.shortcuts import render
from kunafa_configurations.forms import RemindersForm

# Create your views here.
def load_main_page(request):
    status=False
    rem_form=RemindersForm
    if request.POST:
        form = rem_form(request.POST)
        if form.is_valid():
            form.save()
            status=True
    return render(request,"index.html",{'form':rem_form,'status':status})
