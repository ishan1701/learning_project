from rectangle import Rectangle
from circle import Circle
from point import Point


class ShapeFactory:
    '''
    Purpose: Factory class to create shape
    '''

    @staticmethod
    def create(shape: str, **kwargs):
        '''
        Purpose: Factory class to create shape
        '''

        if shape == 'rectangle':
            first_point: Point = Point(x=kwargs.get('first_point_x'), y=kwargs.get('first_point_y'))
            second_point = Point(x=kwargs.get('second_point_x'), y=kwargs.get('second_point_y'))
            return Rectangle(first_point, second_point)

        if shape == 'circle':
            first_point: Point = Point(x=kwargs.get('first_point_x'), y=kwargs.get('first_point_y'))
            second_point = Point(x=kwargs.get('second_point_x'), y=kwargs.get('second_point_y'))
            return Circle(first_point, second_point)

        else:
            raise NotImplementedError(f'{shape} not implemented')
