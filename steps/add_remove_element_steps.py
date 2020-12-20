from behave import step


@step("Page title is Add/Remove Elements")
def step_impl(context):
    displayed_value = context.page.get_page_title()
    expected_value = "Add/Remove Elements"
    assert displayed_value == expected_value, \
        f"Displayed value: '{displayed_value}' is not equal to Expected value: '{expected_value}' "


@step("User clicks Add Element button")
def step_impl(context):
    context.page.click_add_element_button()


@step("User verifies if Delete button appeared")
def step_impl(context):
    delete_button = context.page.get_delete_button()
    if delete_button is True:
        pass
    else:
        raise AssertionError(f"Delete button is not visible")


@step("User clicks Delete Element button")
def step_impl(context):
    context.page.click_delete_button()


@step("User verifies if Delete button disappeared")
def step_impl(context):
    delete_button = context.page.check_if_delete_button_available()
    if delete_button is True:
        pass
    else:
        raise AssertionError(f"Delete button is still visible on teh page")
