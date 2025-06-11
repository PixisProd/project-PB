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


async def render_template(template_str: str, values: dict) -> str:
    template = jinja_env.from_string(template_str)
    return template.render(values)
