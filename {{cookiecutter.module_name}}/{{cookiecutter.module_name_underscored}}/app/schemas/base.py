"""Base Schemas file contained useful class and functions."""
import datetime
from typing import List, Literal, Optional, Union

from pydantic import BaseModel, root_validator
from tortoise.models import Q


class QueryFilter(BaseModel):
    """Query Filter is Pydantic class for build filter_by."""

    field: str
    operator: Literal["in", "contains", "icontains", "gt", "lte", "gte", "lt", "eq"]
    value: Union[str, int, datetime.date]

    @root_validator
    def validate_value(_, values) -> None:  # noqa: N805
        """Validate value on Pydantic step.

        Args:
            values -  value that we validate
        """
        operator, value = values.get("operator"), values.get("value")
        if not value.isdigit() and operator in {"gt", "lte", "gte", "lt", "eq"}:
            raise ValueError("Some error")

        return values


def generate_filters(filter_by: List[QueryFilter]) -> List[Q]:
    """Generate result from filters element that contains data."""
    result = []
    for fi in filter_by:
        k = fi.field
        v = fi.value
        chuck_f: Optional[Q] = None
        match fi.operator:
            case "contains":
                k = f"{k}__contains"
                chuck_f = Q(**{k: v})
            case "gt":
                k = f"{k}__gt"
                chuck_f = Q(**{k: v})
            case "gte":
                k = f"{k}__gte"
                chuck_f = Q(**{k: v})
            case "lt":
                k = f"{k}__lt"
                chuck_f = Q(**{k: v})
            case "lte":
                k = f"{k}__lte"
                chuck_f = Q(**{k: v})
            case "icontains":
                k = f"{k}__icontains"
                chuck_f = Q(**{k: v})
            case "in":
                k = f"{k}__in"
                chuck_f = Q(**{k: v})
            case "eq":
                chuck_f = Q(**{k: v})
        if chuck_f:
            result.append(chuck_f)
    return result
