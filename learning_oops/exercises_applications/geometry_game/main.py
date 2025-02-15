from shape_factory import ShapeFactory
from random import randint
from point import Point

if __name__ == '__main__':
    # shape = 'circle'
    # first_point_x = randint(-100, 100)
    # first_point_y = randint(-100, 100)
    #
    # second_point_x = randint(-100, 100)
    # second_point_y = randint(-100, 100)
    #
    # assert first_point_x != second_point_x, 'point should be different'
    # assert first_point_y != second_point_y, 'point should be different'
    #
    # shape = ShapeFactory.create(shape=shape, first_point_x=first_point_x, first_point_y=first_point_y,
    #                             second_point_x=second_point_x, second_point_y=second_point_y)
    #
    # print(shape)
    # print(shape.shape)
    # print(shape.first_point)
    # print(shape.second_point)
    #
    # print(f'the area is {shape.area}')
    #
    # new_point = Point(x=randint(-110, 110), y=randint(-110, 110))
    #
    # print(f'{shape.if_point_lies(new_point)} as the new point is {new_point}')
    #
    # #########################rectangle##############

    print('_______________REC___________________')

    shape = 'rectangle'
    first_point_x = randint(1, 100)
    first_point_y = randint(1, 100)

    second_point_x = randint(first_point_x + 1, 100)
    second_point_y = randint(first_point_y + 1, 100)

    assert first_point_x != second_point_x, 'point should be different'
    assert first_point_y != second_point_y, 'point should be different'

    shape = ShapeFactory.create(shape=shape, first_point_x=first_point_x, first_point_y=first_point_y,
                                second_point_x=second_point_x, second_point_y=second_point_y)

    print(shape)
    print(shape.shape)
    print(shape.first_point)
    print(shape.second_point)

    print(f'the area is {shape.area}')

    new_point = Point(x=randint(first_point_x, first_point_y), y=randint(second_point_x, second_point_y))

    print(f'{shape.if_point_lies(new_point)} as the new point is {new_point}')
    print(f'the perimeter of {shape.shape_type} is {shape.perimeter}')

    shape.create_shape()

