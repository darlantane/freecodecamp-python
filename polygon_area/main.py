import shape_area
from unittest import main


rect = shape_area.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

main(module='test_module', exit=False)