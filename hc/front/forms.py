from django import forms
from hc.api.models import Channel


class NameTagsForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    tags = forms.CharField(max_length=500, required=False)

    def clean_tags(self):
        l = []

        for part in self.cleaned_data["tags"].split(" "):
            part = part.strip()
            if part != "":
                l.append(part)

        return " ".join(l)


class TimeoutForm(forms.Form):
    timeout = forms.IntegerField(min_value=60, max_value=2592000)
    grace = forms.IntegerField(min_value=60, max_value=2592000)


class AddChannelForm(forms.ModelForm):

    class Meta:
        model = Channel
        fields = ['kind', 'value']

    def clean_value(self):
        value = self.cleaned_data["value"]
        return value.strip()


class PriorityForm(forms.Form):

    CHOICES = ((1, 'Very low'),
               (0, 'Low'))

    priority = forms.ChoiceField(choices=CHOICES)

    def clean_value(self):
        return self.cleaned_data["priority"]


class StakeHolderForm(forms.Form):

    stakeholder_name = forms.CharField(max_length=100, required=True)
    stakeholder_email = forms.CharField(max_length=100, required=True)

    def clean_name(self):
        return self.cleaned_data["stakeholder_name"]

    def clean_email(self):
        return self.cleaned_data["stakeholder_email"]


class AddWebhookForm(forms.Form):
    error_css_class = "has-error"

    value_down = forms.URLField(max_length=1000, required=False)
    value_up = forms.URLField(max_length=1000, required=False)

    def get_value(self):
        return "{value_down}\n{value_up}".format(**self.cleaned_data)
