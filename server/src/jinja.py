from jinja2 import Environment, meta


jinja_env = Environment(
    variable_start_string='((',
    variable_end_string='))',
    trim_blocks=True,
    lstrip_blocks=True,
)


async def parse_vars(template: str) -> list[str]:
    parsed = jinja_env.parse(template)
    return list(meta.find_undeclared_variables(parsed))