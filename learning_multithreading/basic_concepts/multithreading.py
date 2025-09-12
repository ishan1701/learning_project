import concurrent.futures
import logging
from dataclasses import dataclass
from datetime import datetime
from time import sleep
from typing import List


@dataclass
class Data:
    id: int
    name: str


def call_data_class(number: int):
    print(f"Sleeping for {number} seconds")
    sleep(number)
    data_obj = []
    for i in range(number):
        data_obj.append(Data(id=i, name=f"{i}_as_string"))
    return data_obj


# Example function to be applied to each element
def process_element(element):
    print("processing element ", element)
    start_time = datetime.now()
    # Simulate some work (like IO-bound task)
    return_values = call_data_class(number=element)
    # for return_value in return_values:
    #     print(return_value.id, return_value.name)
    # print(return_values)
    end_time = datetime.now()
    execution_time = end_time - start_time
    print(
        f"execution time is for element {element} is {execution_time}, start time is {start_time}, end time is {end_time}"
    )
    return execution_time


if __name__ == "__main__":
    # List of elements
    elements = [
        {1: "a"},
        {2: "b"},
        {3: "c"},
        {4: "d"},
        {5: "e"},
        {6: "f"},
        {7: "g"},
        {8: "h"},
        {9: "i"},
        {10: "j"},
    ]
    # for i in range(500):  # Adjust the number of elements as needed
    #     elements.append(i)

    # Using ThreadPoolExecutor for multithreading
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Map the process_element function to each element in the list
        # results = list(executor.map(process_element, elements))
        # retrun_value = list(executor.map(process_element, elements))
        executor.map(process_element, elements)
