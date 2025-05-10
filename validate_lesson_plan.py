import yaml

def validate_lesson_plan(plan_str):
    try:
        plan = yaml.safe_load(plan_str)
        assert 'title' in plan and 'objectives' in plan and 'activities' in plan
    except Exception as e:
        return f"Invalid lesson plan format: {e}"
    return "Valid format"
