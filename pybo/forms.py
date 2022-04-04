from django import forms
from pybo.models import Answer, Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject', 'content']
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': 'Answer sheet',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }