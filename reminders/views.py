from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReminderForm
from .models import Reminder
from django.contrib.auth.decorators import login_required


@login_required
def new_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect('reminders:reminder_list')
    else:
        form = ReminderForm()
    return render(request, 'reminders/new_reminder.html', {'form': form})


@login_required
def reminder_list(request):
    reminders = Reminder.objects.filter(user=request.user)
    return render(request, 'reminders/reminder_list.html', {'reminders': reminders})


@login_required
def delete_reminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk, user=request.user)
    if request.method == 'POST':
        reminder.delete()
        return redirect('reminders:reminder_list')