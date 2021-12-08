class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return 'Circle with area ' + str(self.pi * self.radius ** 2)
  
  def circumference(self):
    return 'Circle with circumference ' + str(self.pi * 2 * self.radius)
  
  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)

#Exa.-

medium_pizza = Circle(12)
teacher_desk = Circle(36)
round_room = Circle(11460)

print(Circle.area(medium_pizza))
print(Circle.circumference(medium_pizza))
print(Circle.__repr__(medium_pizza))

print(Circle.area(teacher_desk))
print(Circle.circumference(teacher_desk))
print(Circle.__repr__(teacher_desk))

print(Circle.area(round_room))
print(Circle.circumference(round_room))
print(Circle.__repr__(round_room))
