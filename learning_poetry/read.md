1. Install poetry
    Run pip3 install poetry
2. create the pyproject.toml file in your project directory.
    poetry init
3. Create the virtual environment.
    poetry install
    The above command also install any dependencies listed in the pyproject.toml file.
4. poetry env info
    
    Virtualenv
    Python:         3.10.9
    Implementation: CPython
    Path:           /Users/ishan.kumar/Library/Caches/pypoetry/virtualenvs/learning-project-EByPaHHD-py3.10
    Executable:     /Users/ishan.kumar/Library/Caches/pypoetry/virtualenvs/learning-project-EByPaHHD-py3.10/bin/python
    Valid:          True
    
    Base
    Platform:   darwin
    OS:         posix
    Python:     3.10.9
    Path:       /Library/Frameworks/Python.framework/Versions/3.10
    Executable: /Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10
    ➜  learning_project poetry env info -p
    /Users/ishan.kumar/Library/Caches/pypoetry/virtualenvs/learning-project-EByPaHHD-py3.10
5. poetry config virtualenvs.in-project true
    Now the virtual environment will be created inside the project folder itself. Delete the old one and run the following command to create a new one.
6. poetry install
7. poetry shell
    This command activates the virtual environment.
   Spawning shell within /Users/ishan.kumar/PycharmProjects/learning_project/.venv
   bin emulate bash -c '. /Users/ishan.kumar/PycharmProjects/learning_project/.venv/bin/activate'
8. deactivate
    This command will deactivate the virtual environment. Just simply type deactivate at the prompt.
9. poetry add requests
    The command will add new package to the pyproject.toml file and update the lock file as well.
10. poetry remove requests
     to remove the package from the project
11. poetry install. Sometimes the below error can occur and fixed using this command (poetry env use /Library/Frameworks/Python.framework/Versions/3.10/bin/python3)
    
    Current Python version (3.10.9) is not allowed by the project (^3.11).
    Please change python executable via the "env use" command.
    ➜  learning_project which python
    python not found
    ➜  learning_project which python3
    /Library/Frameworks/Python.framework/Versions/3.10/bin/python3
    ➜  learning_project poetry env use /Library/Frameworks/Python.framework/Versions/3.10/bin/python3
    
    Current Python version (3.10.9) is not allowed by the project (^3.11).
    Please change python executable via the "env use" command.
12. poetry env use /Library/Frameworks/Python.framework/Versions/3.10/bin/python3
    Using virtualenv: /Users/ishan.kumar/PycharmProjects/learning_project/.venv
13. poetry install
    Installing dependencies from lock file
14. sometimes while installing packages below error can come
    ```poetry install ```
    ```Installing dependencies from lock file```
    ```pyproject.toml changed significantly since poetry.lock was last generated. Run `poetry lock [--no-update]` to fix the lock file.```
run the below command to solve it
```poetry lock --no-update```
15. poetry add pytest-mock 
    This command will add new package. Run after python shell.
