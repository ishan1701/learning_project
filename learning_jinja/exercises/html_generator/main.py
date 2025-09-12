from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from learning_jinja.models.html_model import HTMLCustom
from learning_jinja.utils.utiils import read_frm_yaml


def _get_template():
    yaml_file_path = Path(__file__).parent.parent.joinpath("input.yaml")
    input_yaml = read_frm_yaml(yaml_file_path)
    print(input_yaml)
    title = input_yaml["title"]

    user_data = [
        HTMLCustom(
            title=title,
            user_name=user["name"],
            user_role=user["role"],
            is_active=user["is_active"],
        )
        for user in input_yaml["users"]
    ]

    users = [user.serialize() for user in user_data]
    return {"users": users, "title": title}

    # return template


def main():
    data: dict = _get_template()
    template_dir = Path(__file__).parent.parent.parent.joinpath("templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("input.html.j2")
    output = template.render(data)

    print(output)


if __name__ == "__main__":
    main()
