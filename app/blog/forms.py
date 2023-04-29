from django import forms

from .models import Post

from users.utils import set_widgets_class


@set_widgets_class
class PostCreationForm(forms.ModelForm):
    form_title = 'Publish new post'
    submit_text = 'Submit'

    class Meta:
        model = Post
        fields = ('title', 'text')

    def save(self, commit=True, **kwargs):
        user = kwargs.pop('user', None)
        if not user or not user.is_authenticated:
            raise Exception

        self.instance.author = user
        super().save()
