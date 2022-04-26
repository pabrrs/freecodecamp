class Rectangle:
  _width = None
  _height = None

  def __init__(self, width: int, height: int):
    self.set_width(width)
    self.set_height(height)

  def __str__(self):
    return f'Rectangle(width={self._width}, height={self._height})'
  
  def set_width(self, width):
    self._width = width

  def set_height(self, height):
    self._height = height
  
  def get_area(self):
    return (self._width * self._height)

  def get_perimeter(self):
    return (2 * self._width) + (2 * self._height)

  def get_diagonal(self):
    return (
      (self._width ** 2) + (self._height ** 2)
    ) ** 0.5

  def get_picture(self):
    if (self._width > 50) or (self._height > 50):
      return 'Too big for picture.'
    picture_form = ['*' * self._width] * self._height
    return '\n'.join(picture_form) + '\n'

  def get_amount_inside(self, form: 'Rectangle'):
    return int(self.get_area() / form.get_area())

class Square(Rectangle):
  _side = None
  def __init__(self, side):
    self.set_side(side)
  
  def __str__(self):
    return f'Square(side={self._side})'
    
  def set_side(self, side):
    self._side = side
    self._width = self._side
    self._height = self._side

  def set_width(self, width):
    self.set_side(width)
    
  def set_height(self, height):
    self.set_side(height)
