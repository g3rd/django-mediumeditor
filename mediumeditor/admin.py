from mediumeditor.widgets import MediumEditorTextarea


class MediumEditorAdmin(object):

    def formfield_for_dbfield(self, db_field, **kwargs):

        if not hasattr(self, 'mediumeditor_fields'):
            raise ValueError('mediumeditor_fields is required on model')

        if db_field.name in self.mediumeditor_fields:
            return db_field.formfield(widget=MediumEditorTextarea())
        return super(MediumEditorAdmin, self).formfield_for_dbfield(
            db_field, **kwargs)
