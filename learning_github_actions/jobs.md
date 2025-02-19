### jobs are the list of steps which should be run something like a tasks

```
jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install Spectacles and dependencies
        run: |
          python -m pip install --upgrade pip
          pip install spectacles
```

Here is the explanation.
* ci: is the name of the job
* steps: tasks which are the part of the job

Now we can have 
* run - to run a command on the runner.
* uses- which are the third party actions that can be used

For example below
```
steps:
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install Spectacles and dependencies
        run: |
          python -m pip install --upgrade pip
          pip install spectacles
```
In the first step which is `uses`, we are setting up python via actions(marketplace).
And then in the second step is `run`, a command will be executed.



## Some common actions 
