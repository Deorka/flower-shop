from django.core.exceptions import ValidationError


def validate_number_or_range_str(value: str, field_name: str):
    msg = f'Некорректное значение поля {field_name}: ожидается строка с числом или двумя числами через дефис'
    if not value.isnumeric():
        try:
            value_splitted = value.split('-')
            if not (value_splitted[0].isnumeric() and value_splitted[1].isnumeric()) or len(value_splitted) > 2:
                raise ValidationError(msg)
        except IndexError:
            raise ValidationError(msg)
