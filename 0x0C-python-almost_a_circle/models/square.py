#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialisation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string format"""
        my_list = "[" + str(self.__class__.__name__) + "]"
        my_list += " (" + str(self.id) + ") " + str(self.x) + "/" + str(self.y)
        my_list += " - " + str(self.width)
        return (my_list)

    @property
    def size(self):
        """getter"""
        return (self.width)

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        attr = ['id', 'size', 'x', 'y']
        for i in range(len(args)):
            if attr[i] == 'size':
                setattr(self, 'width', args[i])
                setattr(self, 'height', args[i])
            else:
                setattr(self, attr[i], args[i])
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        my_dic = {}
        attr = ['id', 'size', 'x', 'y']

        for key in attr:
            if key == 'size':
                my_dic[key] = getattr(self, 'height')
            else:
                my_dic[key] = getattr(self, key)

        return (my_dic)
