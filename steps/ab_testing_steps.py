from behave import step


@step("Page title is A/B Test Variation 1")
def step_impl(context):
    displayed_value = context.page.get_page_title()
    expected_value_1 = "A/B Test Variation 1"
    expected_value_2 = "A/B Test Control"
    if not displayed_value == expected_value_1 and not displayed_value == expected_value_2:
        raise AssertionError(f"{displayed_value} is not equal {expected_value_1} or {expected_value_2}")