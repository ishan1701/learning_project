from pathlib import Path
import json
file_name='some_file.jsonl'

def not_loading_to_memory():
    with open(Path(__file__).parent.parent.joinpath('data', file_name), 'r') as file:
        for line in file:
            data = json.loads(line)
            yield data['email_address']




def it_loading_to_memory():
    with open(Path(__file__).parent.parent.joinpath('data', file_name), 'r') as file:
        data = json.load(file)  #this will load the data in whole memory
    for line in data:
        yield line['email_address']

