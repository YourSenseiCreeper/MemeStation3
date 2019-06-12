
# Test of the buttons and their actions
# Test of the registration system?
# Test of Error404 (Don't have it rn)
# Test of adding an meme and the proper text
# Test of using buttons without permissions?
import unittest

import memes.views

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.widget = Meme('The widget')

    def tearDown(self):
        self.widget.dispose()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class UserLoggedInTestCase(TestCase):

    def test_log_in(self):
        c = Client()
        response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        self.assertEqual(response.status_code, 200)

    def test_log_out(self):
        c = Client()
        response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        self.assertIsNotNone(response.status_code)
        response2 = c.post('/logout/')
        self.assertIsNone(response2.status_code)

if __name__ == '__main__':
    unittest.main()

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)



