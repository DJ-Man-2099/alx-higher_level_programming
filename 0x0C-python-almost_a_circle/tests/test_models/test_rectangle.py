

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(10, 5, 2, 3)

    def test_area(self):
        result = self.rectangle.area()
        self.assertEqual(result, 50)

    def test_display(self):
        # Redirect stdout to a StringIO object
        # to capture the output of the display method
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        self.rectangle.display()

        sys.stdout = sys.__stdout__
        expected_output = "\n\n\n"+"  " + "#" * 10 + "\n" + \
                          "  " + "#" * 10 + "\n" + \
                          "  " + "#" * 10 + "\n" + \
                          "  " + "#" * 10 + "\n" + \
                          "  " + "#" * 10 + "\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        result = str(self.rectangle)
        expected_output = "[Rectangle] (3) 2/3 - 10/5"
        self.assertEqual(result, expected_output)

    def test_update_args(self):
        self.rectangle.update(1, 20, 30, 4, 5)
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 20)
        self.assertEqual(self.rectangle.height, 30)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 5)

    def test_update_kwargs(self):
        self.rectangle.update(width=20, height=30, x=4, y=5)
        self.assertEqual(self.rectangle.width, 20)
        self.assertEqual(self.rectangle.height, 30)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 5)

    def test_to_dictionary(self):
        result = self.rectangle.to_dictionary()
        expected_output = {
            "x": 2,
            "y": 3,
            "id": 4,
            "height": 5,
            "width": 10
        }
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
