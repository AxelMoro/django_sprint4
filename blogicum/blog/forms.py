from .models import Post, Comment, User


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('text',)


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'
