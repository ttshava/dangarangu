from django import forms

# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()

    class Meta:
        fields = ['name', 'stud', 'sex', 'dob', 'status', 'breed', 'cattle_colour', 'horn', 'conception']



