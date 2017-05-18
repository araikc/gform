import json
import os

from django.shortcuts import render, redirect, render_to_response
from gform.forms import UserCreationForm

from django.conf import settings

def create_user(request):
    fields_file = os.path.join(settings.PROJECT_ROOT, 'gform', 'fields.json')
    json_data=open(fields_file).read()
    extra_fields = json.loads(json_data).keys()
    form = UserCreationForm(request.POST or None, extra=extra_fields)
    if form.is_valid():
        for (clabel, cvalue) in form.extra_data():
            save_answer(request, clabel, cvalue)
        return redirect("create_user_success")

    return render_to_response("signup/form.html", {'form': form})
# Create your views here.
