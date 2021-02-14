from behave import step, given, runner
from pages import get_starting_page
from constants.constants import EmptyList


@step('the user is redirected to the "{page_type:PageType}"')
def step_impl(context: runner.Context, page_type) -> None:
    context.page = page_type(context.driver)


@given("User is on the webpage")
def step_impl(context):
    context.page = get_starting_page(context.driver, context.base_url)


@step("the user is able to check error list")
def step_impl(context: runner.Context) -> None:
    if context.page_error_list != EmptyList.EMPTY_LIST:
        raise AssertionError(context.page_error_list)


