import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    '''测试name_function.py中的函数'''

    def test_first_last_name(self):
        formatted_name = get_formatted_name('jainis', 'joplin')
        self.assertEqual(formatted_name, 'Jainis Joplin')

    def test_first_last_name_with_middle_name(self):
        formatted_name = get_formatted_name('jainis', 'joplin', 'jainis')
        self.assertEqual(formatted_name, 'Jainis Jainis Joplin')

if __name__ == '__main__':
    unittest.main() 