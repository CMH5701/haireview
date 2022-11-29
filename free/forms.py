from django import forms
from free.models import Free, P_comment
from django_summernote.widgets import SummernoteWidget


class FreeForm(forms.ModelForm):
    class Meta:
        model = Free
        fields = ['p_title', 'p_body', 'p_photo', 'hashtags']
     
        labels = {
            'p_title': '제목',
            'p_body': '내용',
            'p_photo': '사진',
            'hashtags': '해시태그'
        }


class p_commentForm(forms.ModelForm):
    class Meta:
        model = P_comment
        fields = ['text', 'p_photo']
        labels = {
			'text' : '내용',
            'p_photo': '사진'
        }