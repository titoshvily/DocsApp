from django import forms
from .models import Workshop, Doc, Orders, Process, Stuff


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.name} (№{obj.id_number})" if obj.id_number else obj.name


class WorkshopForm(forms.Form):
    workshop = forms.ModelChoiceField(
        queryset=Workshop.objects.all(),
        label="Выберите цех",
        widget=forms.Select(attrs={"class": "form-control"}),
    )


class DocForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = "__all__"

        responsible_not = CustomModelChoiceField(
            queryset=Stuff.objects.all(),
            widget=forms.Select(attrs={"class": "form-control"}),
            required=False,
        )
        widgets = {
            'responsible_not': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'evp_class': forms.SelectMultiple(attrs={'class': 'form-control'}),
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = [
            "name",
            "id_doc",
            "workshop",
            "evp_class",
            "group",
            "release_date",
            "mayor",
            "responsible_not",
            "responsible",
            "process",
            "link",
        ]
        widgets = {
            "release_date": forms.DateInput(attrs={"type": "date"}),
        }


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = [
            "action",
            "type",
            "name_doc",
            "responsible_process",
            "date_deadline",
            "release_date",
            "status_procces",
            "comment",
            "link",
        ]

        widgets = {
            "date_deadline": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "release_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }
