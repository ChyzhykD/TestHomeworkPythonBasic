import json


class JsonParser:
    def __init__(self, json_string):
        self.json_string = json_string

    def __enter__(self):
        self.data = json.loads(self.json_string)
        return self.data

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right
        if top_left.x > bottom_right.x:
            tmp = top_left.x
            top_left.x = bottom_right.x
            bottom_right.x = tmp
        elif top_left.y < bottom_right.y:
            tmp = top_left.y
            top_left.y = bottom_right.y
            bottom_right.y = tmp

    def contains(self, point):
        if (self.top_left.x <= point.x <= self.bottom_right.x and
                self.bottom_right.y <= point.y <= self.top_left.y):
            return True
        return False

    def __contains__(self, point):
        return self.contains(point)


if __name__ == '__main__':
    with JsonParser('"hello"') as res:
        assert res == "hello"

    with JsonParser('{"hello": "world", "key": [1,2,3]}') as res:
        assert res == {"hello": "world", "key": [1, 2, 3]}

    start_point = Point(1, 0)
    end_point = Point(7, 3)

    rect = Rectangle(start_point, end_point)
    assert rect.contains(start_point)
    assert not rect.contains(Point(-1, 3))
    assert start_point in rect
    assert Point(-1, 3) not in rect
