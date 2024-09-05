from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry, Category
from .forms import TopicForm, EntryForm, CategoryForm


def index(request):
    """Main page 'Журналу спостережень'."""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Represent all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Added a new topic"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id, owner=request.user)
    if request.method != 'POST':
        topic.delete()
        return redirect('learning_logs:topics')
    return render(request, 'learning_logs/delete_topic.html', {'topic': topic})


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


@login_required
def categories(request):
    """Represent all categories"""
    categories = Category.objects.filter(owner=request.user)
    context = {'categories': categories}
    return render(request, 'learning_logs/categories.html', context)


@login_required
def new_category(request):
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.owner = request.user
            new_category.save()
            return redirect('learning_logs:categories')

    context = {'form': form}
    return render(request, 'learning_logs/new_category.html', context)

@login_required
def category_topics(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = category.topics.filter(owner=request.user).order_by('date_added')
    context = {'category': category, 'topics': topics}
    return render(request, 'learning_logs/category_topics.html', context)

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id, owner=request.user)
    if request.method != 'POST':
        category.delete()
        return redirect('learning_logs:categories')
    return render(request, 'learning_logs/delete_category.html', {'category': category})