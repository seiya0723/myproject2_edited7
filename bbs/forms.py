from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model     = Topic
        fields   = [ "category","title","comment","price","salary","spending","pay_dt"]
