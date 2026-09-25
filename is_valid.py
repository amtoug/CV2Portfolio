import json
from Schema import Portfolio


def is_valid_json(response):

    try:
        return json.loads(response)

    except json.JSONDecodeError:
        return False


def validate_schema(response):

    try:
        Portfolio.model_validate(response)
        return True

    except Exception:
        return False