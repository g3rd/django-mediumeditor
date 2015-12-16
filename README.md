# Django Medium Editor
Adds [Medium Editor](https://yabwe.github.io/medium-editor/) to [Django](https://www.djangoproject.com/).

## Supported Environments

* Django 1.9
* Python 3.4

## Installation

1. Install **django-mediumeditor**
    
    via PyPi:
    ```
    pip install django-mediumeditor
    ```
    via GIT:

    ``` 
pip install git+https://github.com/g3rd/django-mediumeditor.git
    ```

2. Install app
    ```
    INSTALLED_APPS = [
        ...
        'mediumeditor',
    ]
    ```

## Usage

### Django Admin

Add to Admin class

```
from mediumeditor.admin import MediumEditorAdmin

@admin.register(MyModel)
class MyModelAdmin(MediumEditorAdmin, admin.ModelAdmin):
    ...
    mediumeditor_fields = ('my_text_field', )
    ...
```

### Forms

**NOTE:** This is untested

1. Override the Widget for the field

    ```
    from mediumeditor.widgets import MediumEditorTextarea
    
    class MyForm(forms.ModelForm):
        ...
        class Meta:
            model = MyModel
            widgets = {
                'my_text_field': MediumEditorTextarea(),
            }
    ```

2. In the ```<head>``` of the template
    ```
    {{ form.media }}
    ```

## Contributing

[Take out some bugs](https://github.com/g3rd/django-mediumeditor/issues)

[Report issues or feature requests](https://github.com/g3rd/django-mediumeditor/issues)


## License
MIT: https://github.com/g3rd/django-mediumeditor/blob/master/LICENSE
