from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите название статьи', 'class': 'post-create__add-title'}),
        }
