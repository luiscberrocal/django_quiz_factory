from django import forms
from django.forms.widgets import RadioSelect, Textarea
import logging
logger = logging.getLogger(__name__)


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        logger.debug('*** QuestionForm.__init__ ***')
        super(QuestionForm, self).__init__(*args, **kwargs)
        if question:
            choice_list = [x for x in question.get_answers_list()]
            self.fields["answers"] = forms.ChoiceField(choices=choice_list,
                                                   widget=RadioSelect)


class EssayForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(EssayForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(
            widget=Textarea(attrs={'style': 'width:100%'}))
