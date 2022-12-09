from django import forms
from .models import Option

class VoteForm(forms.Form):
    choice = forms.MultipleChoiceField(label = "科目",widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Option
        fields = "__all__"

    def __init__(self,categories=None,*args,**kwargs):
        self.base_fields['choice'].choices = categories
        super().__init__(*args,**kwargs)    