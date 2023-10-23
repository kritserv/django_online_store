from django import forms
from products.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ClothForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))

    QUERY_FIELDS = [
        "is_in_stock",
        "is_on_sale",
        "color",
        "gender",
        "cloth_type",
        "size",
    ]

    FORM = []
    try:
        for q in QUERY_FIELDS:
            CHOICES = []
            for x in Cloth.objects.values(q).distinct().order_by(q):
                CHOICES.append((x[q], x[q]))

            FORM.append(
                forms.MultipleChoiceField(
                    widget=forms.CheckboxSelectMultiple, choices=CHOICES, required=False
                )
            )

        product_available, on_sale, color, gender, cloth_type, size = FORM
    except:
        None