import json
from models.base import Base
from models.rectangle import Rectangle


r1 = Rectangle(10, 7, 2, 8)
r2 = Rectangle(2, 4)
Rectangle.save_to_file([r1, r2])
