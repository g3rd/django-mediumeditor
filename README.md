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
    from mediumeditor.widget import MediumEditorTextarea
    
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

## Todo

Since this is a very new project, 

- [ ] Pypi
- [ ] Documentation
- [ ] Clean-up Django admin display
    - Toolbar style
    - Anchor configuration toolbar
    - Bold to use ```<strong>```
    - Italic to use ```<em>```
    - Inline styles do not inherit Django Admin (see H2 and unordered lists)
- [ ] Expand Django support to 1.8
- [ ] Expand Python support to 2
- [ ] Tests!
- [ ] Configure the toolbar - globally
- [ ] Configure the toolbar - per form
- [ ] Configure the toolbar - per field

## License
MIT: https://github.com/g3rd/django-mediumeditor/blob/master/LICENSE