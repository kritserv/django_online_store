from django import forms
from products.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class HeadphoneForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))

    QUERY_FIELDS = [
        "is_in_stock",
        "is_on_sale",
        "is_bluetooth",
        "is_waterproof",
        "has_noise_cancelling",
        "has_microphone",
        "color",
        "headphone_type",
        "port",
        "frequency_response",
    ]

    FORM = []
    try:
        for q in QUERY_FIELDS:
            CHOICES = []
            for x in Headphone.objects.values(q).distinct().order_by(q):
                CHOICES.append((x[q], x[q]))

            FORM.append(
                forms.MultipleChoiceField(
                    widget=forms.CheckboxSelectMultiple, choices=CHOICES, required=False
                )
            )

        product_available, on_sale, is_bluetooth, is_waterproof, has_noise_cancelling, has_microphone, color, headphone_type, port, frequency_response = FORM
    except:
        None