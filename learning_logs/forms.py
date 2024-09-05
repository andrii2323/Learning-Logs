from django import forms

from .models import Topic, Entry, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': 'Category Name'}
        widgets = {'name': forms.TextInput(attrs={'size': 40})}


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'category']
        labels = {'text': '', 'category': 'Category'}
        widgets = {
            'text': forms.TextInput(attrs={'size': 40}),
            'category': forms.Select()
        }


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}