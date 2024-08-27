from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django import forms
from .models import *
from Account.models import *
from django.views import View
from .forms import NewTraineeModel
from django.urls import reverse_lazy


def list(request):
    trainees = Trainee.objects.all()
    context = {'trainees': trainees}
    return render(request, 'trainee/list.html', context)

def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, pk=id)

    if request.method == 'POST':
        form = NewTraineeModel(request.POST, request.FILES, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            context = {
                'form': form,
                'error': 'Invalid data'
            }
            return render(request, 'trainee/update.html', context)
        
    form = NewTraineeModel(instance=trainee)
    context = {
        'form': form,
    }
    return render(request, 'trainee/update.html', context)

    
def delete_trainee(request, id):
    if request.method == 'POST':
   
        success = Trainee.deleteEachTrainee(id)
        if success:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Trainee not found'}, status=404)

    trainee = get_object_or_404(Trainee, pk=id)
    return render(request, 'trainee/delete.html', {'trainee': trainee})
    

def show_details_trainee(request, id):
    trainee = Trainee.get_trainee_details(id)
    return render(request, 'trainee/showDetails.html', {'trainee': trainee})


class NewTrainee(View):
    def get(self, request):
        form = NewTraineeModel()
        return render(request, 'trainee/formCreate.html', {'form': form})

    def post(self, request):
        form = NewTraineeModel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')  
        else:
            return render(request, 'trainee/formCreate.html', {'form': form, 'errors': form.errors})