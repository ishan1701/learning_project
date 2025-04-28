from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from learning_jinja.utils.utiils import read_frm_yaml
from learning_jinja.models.json_creator_model import APIConfig
from pydantic import ValidationError



def main():
    yaml_config = read_frm_yaml(file_path=Path(__file__).parent.parent.joinpath('inputs.yaml'))
    print(f'the confis is {yaml_config}')
    config: APIConfig|None=None
    try:
        config= APIConfig(**yaml_config['app_config'])
    except ValidationError as e:
        print(e)

    template_folder = Path(__file__).parent.parent.parent.parent.joinpath('templates')

    env = Environment(loader=FileSystemLoader(template_folder))

    template= env.get_template('input.json.j2')

    output= template.render(config=config)
    print(output)
    print(type(output))

    import json
    data = json.loads(output)
    print(data)
    print(type(data))

if __name__ == '__main__':
    main()