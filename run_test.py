import unittest



class SomeTests(unittest.TestCase):
    @repeat(10)
    def test_me(self):
        print("You will see me 10 times")

if __name__ == '__main__':
    unittest.main()