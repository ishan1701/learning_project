Resource: https://www.youtube.com/watch?v=EgpLj86ZHFQ


1. pip3 install pytest
2. pip3 install pytest-mock


## To run the tests via pytest create file test_file.py
so for example if I want to test the function inside app.py, I need to create a file named test_app.py so that 
pytest can indentify the which function to refer while running the tests.

3.  pytest test_app.py -s 
   This command will print the print statement added in the test file. Also the print statement preset in the actual file if present

## what is test driven development

## how to write test case for a function that raise an exception
I have a scenario where I have the below code in a function
`raise TypeError('Type is not implemented')`

Now to write a simple assert for the above will be
```angular2html
def test_function_name():
    with pytest.raises(expected_exception='TypeError', match='Type is not implemented')
```

## how to write unit stest for a  class and its methods?

