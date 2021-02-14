from behave import step, runner
from value_assertion import compare_expected_value_with_displayed


@step("Page title is Login Page")
def step_impl(context):
    displayed_title = context.page.get_page_title()
    expected_title = "Login Page"
    assert displayed_title == expected_title, \
        f"Displayed value: '{displayed_title}' is not equal to Expected value: '{expected_title}' "


@step("User logs in")
def step_impl(context):
    context.page.input_username()
    context.page.input_password()
    context.page.click_login()


@step("Successful log in message pop up")
def step_impl(context: runner.Context) -> None:
    context.page_error_list = []
    displayed_log_in_message = context.page.get_log_in_message()
    expected_log_in_message = "You logged into a secure area!"
    assert displayed_log_in_message == expected_log_in_message, \
        f"Displayed message: {displayed_log_in_message} is not equal expected message: {expected_log_in_message}"


@step("User logs out")
def step_impl(context):
    context.page.click_logout()


@step("Successful log out message pop up")
def step_impl(context):
    displayed_log_out_message = context.page.get_log_out_message()
    expected_log_out_message = "You logged out of the secure area!"
    assert displayed_log_out_message == expected_log_out_message, \
        f"Displayed message: {displayed_log_out_message} is not equal expected message: {expected_log_out_message}"
