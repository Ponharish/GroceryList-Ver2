from django import forms

class GroceryForm(forms.Form):
    def __init__(self, *args, fields_to_add=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fieldNames = []
        flag = 0
        notes_field_options = None
        if fields_to_add:
            for field_name, field_options in fields_to_add.items():
                if field_name == "notes":
                    notes_field_options = field_options
                    flag = 1
                else:
                    self.fieldNames.append({
                        "field_name": field_name,
                        "english_name": field_options.get("english_name", ""),
                        "tamil_name": field_options.get("tamil_name", "")
                    })
                    self.fields[field_name] = forms.CharField(
                        max_length=field_options.get("max_length", 100),
                        required=field_options.get("required", False),
                        initial=field_options.get("initial", ""),
                        widget=field_options.get("widget", forms.TextInput()),
                        label=field_options.get("english_name", ""),
                    )
            if flag == 1:
                self.fieldNames.append({
                    "field_name": "notes",
                    "english_name": "notes",
                    "tamil_name": ""
                })
                self.fields["notes"] = forms.CharField(
                    max_length=notes_field_options.get("max_length", 200),
                    required=notes_field_options.get("required", False),
                    widget=notes_field_options.get(
                        "widget", forms.Textarea(attrs={'rows': 5, 'cols': 50})
                    ),
                    label=notes_field_options.get("label", "Notes"),
                )
        