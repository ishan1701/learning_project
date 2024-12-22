1. The pathlib mudule in python provides an object-oriented way of working with file paths. It provides a Path class that represents a path to a file or directory, and allows you to perform various operations on it such as joining paths together, getting the parent directory, checking if a path exists, etc.

2. Typically, you use pathlib.Path, and it automatically selects the appropriate subclass based on your operating system.

3. **Pathlib is more powwefull than os as it Path are considred as objects and allows for the operations like joining the path, creating the file, reading the file, searching for a file with extensions, deleting the file**
4. 
```
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
   ```

5. ```
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
```
