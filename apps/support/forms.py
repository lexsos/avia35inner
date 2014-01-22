from django import forms

from .models import Comment, Ticket


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'text'}),
        }


class TicketForm(forms.ModelForm):

    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'text'})
    )

    class Meta:
        model = Ticket
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title'}),
        }
