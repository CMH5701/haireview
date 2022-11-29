from django import forms
from .models import Question, Answer
from django_summernote.widgets import SummernoteWidget


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['q_title', 'question', 'q_photo', 'hashtags']
        
        labels = {
			'q_title' : '제목',
            'question': '질문',
            'q_photo': '사진',
            'hashtags': '해시태그'
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'a_photo']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': '댓글을 입력하세요'})
        }
        labels = {
			'text' : '내용',
            'a_photo': '사진'
        }
