from behave import runner


def compare_expected_value_with_displayed(
        context: runner.Context,
        expected_value: str,
        displayed_value: str
) -> None:
    if not expected_value == displayed_value:
        context.page_error_list.append(
            f"Compared values are incorrect for question: {context.step.name}. Expected value: {expected_value}, displayed value: {displayed_value}"
        )
