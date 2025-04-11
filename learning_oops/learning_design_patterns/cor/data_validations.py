from abc import ABC, abstractmethod


class DataValidationHandler(ABC):

    def __init__(self):
        self.next_handler = None

    @abstractmethod
    def validate(self, data: dict):
        pass

    def set_next_handler(self, handler: 'DataValidationHandler'):
        self.next_handler = handler
        print(self.__class__.__name__)
        print(handler.__class__.__name__)
        print('___________________________')
        return handler

    def process(self, data: dict):
        print(self.next_handler)
        self.validate(data=data)
        if self.next_handler is not None:
            self.next_handler.process(data=data)




class DataQualityHandler(DataValidationHandler):
    def validate(self, data: dict) -> None:
        print('Inside DataQualityHandler')
        print(data)
        if data.get('id', None) is None or data.get('value', None) is None:
            raise ValueError('Data is missing required field')
        return None


class ClassificationHandler(DataValidationHandler):
    def validate(self, data: dict) -> None:
        print('Inside ClassificationHandler')
        if data.get('classification') == 'confidential':
            raise ValueError('Data cant be confidential')
        return None


class BusinessHandler(DataValidationHandler):
    def validate(self, data: dict) -> None:
        print('Inside BusinessHandler')
        if data.get('value') < 0:
            raise ValueError('Data cant be negative')
        return None

#client code
def main():
    dqh= DataQualityHandler()
    ch = ClassificationHandler()
    bh = BusinessHandler()

    #create the chain of handlers
    dqh.set_next_handler(ch).set_next_handler(bh)

    test_records = [
        # {"id": None, "value": 100, "classification": "public"},
        # {"id": "123", "value": 50, "classification": "confidential"},
        # {"id": "456", "value": -10, "classification": "public"},
        {"id": "789", "value": 200, "classification": "public"}
    ]
    for record in test_records:
        dqh.process(data=record)

if __name__ == '__main__':
    main()