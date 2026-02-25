import json
from django.apps import apps
from django.db import models

schema = {}

def get_on_delete_name(on_delete):
    if not on_delete: return None
    if on_delete == models.CASCADE: return "CASCADE"
    if on_delete == models.PROTECT: return "PROTECT"
    if on_delete == models.SET_NULL: return "SET_NULL"
    if on_delete == models.SET_DEFAULT: return "SET_DEFAULT"
    if on_delete == models.SET: return "SET"
    if on_delete == models.DO_NOTHING: return "DO_NOTHING"
    if on_delete == models.RESTRICT: return "RESTRICT"
    return str(on_delete)

for model in apps.get_models():
    try:
        app_label = model._meta.app_label
        if app_label in ['admin', 'auth', 'contenttypes', 'sessions', 'messages', 'staticfiles', 'corsheaders', 'rest_framework', 'django_filters']:
            continue
            
        model_name = model.__name__
        table_name = model._meta.db_table
        
        fields_info = []
        has_soft_delete = False
        
        for field in model._meta.get_fields():
            try:
                if field.auto_created and not field.concrete:
                    continue
                    
                field_info = {
                    'name': field.name,
                    'type': field.get_internal_type() if hasattr(field, 'get_internal_type') else type(field).__name__,
                    'null': getattr(field, 'null', False),
                    'default': str(getattr(field, 'default', '')) if getattr(field, 'default', '') != models.fields.NOT_PROVIDED else 'None',
                    'unique': getattr(field, 'unique', False),
                    'primary_key': getattr(field, 'primary_key', False),
                    'db_index': getattr(field, 'db_index', False),
                    'is_relation': getattr(field, 'is_relation', False),
                    'related_model': field.related_model.__name__ if getattr(field, 'is_relation', False) and getattr(field, 'related_model', None) else None,
                    'on_delete': get_on_delete_name(getattr(field.remote_field, 'on_delete', None)) if getattr(field, 'is_relation', False) and hasattr(field, 'remote_field') else None,
                    'help_text': str(getattr(field, 'help_text', ''))
                }
                
                if field.name == 'is_deleted':
                    has_soft_delete = True
                    
                fields_info.append(field_info)
            except Exception as e:
                print(f"Error on field {field} of {model_name}: {e}")
            
        unique_together = getattr(model._meta, 'unique_together', [])
        constraints = [str(c) for c in getattr(model._meta, 'constraints', [])]
        indexes = [str(idx) for idx in getattr(model._meta, 'indexes', [])]
        
        schema[f"{app_label}.{model_name}"] = {
            'app': app_label,
            'model': model_name,
            'table_name': table_name,
            'has_soft_delete': has_soft_delete,
            'fields': fields_info,
            'unique_together': [str(u) for u in list(unique_together)] if unique_together else [],
            'constraints': constraints,
            'indexes': indexes
        }
    except Exception as e:
        print(f"Error on model {model}: {e}")

with open('schema_dump.json', 'w') as f:
    json.dump(schema, f, indent=2)

print(f"Dumped {len(schema)} models.")
