import pytest
from unittest import mock
from learning_pytest.src.mocking_example import get_frm_json_placeholder


@mock.patch('requests.get')
def test_get_frm_json_placeholder(mock_get_frm_url):
    ## creating an mock object and creating the property

    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id':'ded', 'name':'fffrf'}

    ##assiging the
    mock_get_frm_url.return_value = mock_response

    returned_output =  get_frm_json_placeholder('https://jsonplaceholder.typicode.com/users')
    print(f' the returned is {returned_output}')

    assert returned_output == {'id':'ded', 'name':'fffrf'}