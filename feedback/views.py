from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
from django.contrib.auth.decorators import login_required


def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback/feedback_list.html', {'feedbacks': feedbacks})


@login_required
def new_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('feedback:feedback_thanks')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/new_feedback.html', {'form': form})


@login_required
def feedback_thanks(request):
    return render(request, 'feedback/feedback_thanks.html')
