from pathlib import Path
from random import randint


def _basic_concept():
    #absolute paths
    p=Path(__file__)
    print(p)
    print(p.resolve())
    print(p.absolute())

    print('______RELATIVE PATH_________')
    path = Path('abc/isit.txt')
    print(path)
    print(path.resolve()) # abs path

    print(path.parent.parent.absolute()) # abs path both are same
    print(path.resolve().name)
    print(path.stem)
    print(path.is_file())
    print(path.parent.is_dir())
    print(path.parent.parent)# will retrun .
    print(path.parent.parent.absolute()) #wil return abs path
    print(path.parent.parent.resolve())  #wil return abs path
    print(path.parent.parent.is_dir())


def _opening_file(file_name: str, dir_name: str):
    p = Path(__file__).parent.joinpath(dir_name, file_name)

    if p.exists():
        print('file_exists')
        with open(p, 'r') as file:
            contents = file.read()
        print(contents)
    else:
        raise FileNotFoundError('file does not exist')

def _iterating_over_directory(dir_name: str):

    #relative path
    p = Path(dir_name) # relative path
    print(p)
    print(p.parent.parent)
    if not p.exists():
        raise FileNotFoundError('directory does not exist')

    #absolute path
    p = Path(__file__).parent.joinpath(dir_name)
    print(f'the absoute  path is {p}')


    for file in p.iterdir():
        print('________START___________')
        print(file)
        print(file.parent)
        print(file.name)
        print(file.absolute())
        print(file.is_dir())
        print(file.resolve())
        # _opening_file(file_name=file.name, dir_name=dir_name)
        with open(file, 'r') as file:
            contents = file.read()
            print(contents)

        print('________END___________')

def _creating_new_file(dir_name, file_name):
    p=Path(__file__).parent.joinpath(dir_name,file_name)
    print(p)
    if p.exists():
        print('file_exists')

    else:
        with open(p, 'w') as file:
            file.write('somevalue')


def _creating_directory(dir_name: str, file_name):
    p = Path(__file__).parent
    print(p)
    print(p.parent)

    if p.joinpath(dir_name).exists():
        print(f'{dir_name} already exists')
        raise FileExistsError('Directory already exists')

    else:
        print(p.joinpath(dir_name))
        p.joinpath(dir_name).mkdir()
        with open(p.joinpath(dir_name, file_name), 'w+') as f:
            f.write('Hello World\n')


if __name__ == '__main__':
    _basic_concept()
    # _creating_directory(dir_name='dir_name',file_name='file.txt')
    # _opening_file(dir_name='dir_name', file_name='file.txt')
    #
    # _creating_new_file(dir_name='dir_name', file_name=f'file_{randint(1,10)}.txt')
    # _iterating_over_directory(dir_name='dir_name')
