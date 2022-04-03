from django.forms import ModelForm, BooleanField
from .models import Post


class ProductForm(ModelForm):
    check_box = BooleanField(label='Ало, Галочка!')

    class Meta:
        model = Post
        fields = ['news_type', 'post_title', 'post_text', 'author', 'check_box']