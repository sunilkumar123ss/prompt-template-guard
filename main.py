"""Render a deliberately restricted subset of Python format templates."""
import argparse
import json
from pathlib import Path
import re
import string


def render_prompt(template,variables,allowed):
    if not isinstance(template,str) or not isinstance(variables,dict):
        raise ValueError("template must be a string and variables an object")
    allowed=set(allowed)
    if any(not isinstance(name,str) or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*",name) for name in allowed):
        raise ValueError("allowed fields must be simple identifiers")
    fields=set()
    try:parts=list(string.Formatter().parse(template))
    except ValueError as exc:raise ValueError(f"invalid template braces: {exc}") from exc
    for literal,field,format_spec,conversion in parts:
        if field is None:continue
        if field not in allowed or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*",field):
            raise ValueError(f"undeclared or unsafe placeholder: {field}")
        if format_spec or conversion is not None:
            raise ValueError("format specifications and conversions are disabled")
        fields.add(field)
    if set(variables) != fields:
        missing=sorted(fields-set(variables));extra=sorted(set(variables)-fields)
        raise ValueError(f"variable mismatch: missing={missing}, extra={extra}")
    if any(not isinstance(value,str) for value in variables.values()):
        raise ValueError("all values must be strings")
    return template.format_map(variables)

