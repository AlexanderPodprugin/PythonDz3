"""
����� Vector3D
�������� ������ �������� ������� ��������� � ���������� ������������ (x,y,z).
����������� ������ ���� ����������� ������:
� ���������� ������� � ������ � ������� ��������� (����� __str __),
� �������� �������� ���������� `+` (����� __add__),
� ��������� �������� ���������� `-` (����� __sub__),
� ��������� ������������ ���������� `*` (����� __mul__),
"""
class Vec():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod

    def __add__(self, other):
        return (self.x + other, self.y + other, self.z + other)


    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)


    def __sub__(self, other):
        return (self.x - other, self.y - other,self.z - other)


Vect = Vec(11,12,3)