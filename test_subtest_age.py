import unittest
from age import categorize_by_age

class TestIsChild(unittest.TestCase):

    def test_child_age(self):
        for age in range(0, 9):  # 0–8 (ตามรูป)
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"{age} is considered as a child.")
                self.assertEqual(result, "Child")

if __name__ == "__main__":
    unittest.main(verbosity=2)