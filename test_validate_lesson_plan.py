import unittest
from validate_lesson_plan import validate_lesson_plan

class TestLessonPlanValidation(unittest.TestCase):
    def test_valid_plan(self):
        valid_plan = """
        title: Math Lesson
        objectives: Learn addition
        activities:
          - Addition with objects
        """
        self.assertEqual(validate_lesson_plan(valid_plan), "Valid format")

    def test_invalid_plan(self):
        invalid_plan = """
        title: Math Lesson
        activities:
          - Addition with objects
        """
        self.assertIn("Invalid lesson plan format", validate_lesson_plan(invalid_plan))

if __name__ == '__main__':
    unittest.main()
