from django import forms
from .models import Review, R_comment 
from django_summernote.widgets import SummernoteWidget

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['r_title','r_body', 'r_location',  'r_receipt', 'hashtags' ]
        labels = {
            'r_title' : '제목',
            'r_body' : '내용',
            'r_location' : '위치',
            'r_receipt' : '영수증',
            'hashtags' : '해시태그',
        }

class r_commentForm(forms.ModelForm) :
    class Meta :
        model = R_comment
        fields = ['text','rc_photo']
        labels = {
			'text' : '내용',
            'rc_photo': '사진'
        }