import configuration
import behave
from behave import runner

from parsers import register_type_parsers

register_type_parsers()

'''
The fixture before test running gets value from base_url and assigns 
the value to context.base_url.
The same happens with context.driver
The arrow at the end of the function determines type, it's called type annotation.
Thanks to this PyCharm gives us a hint what type is expected
'''


def before_all(context: runner.Context) -> None:
    context.base_url = behave.use_fixture(configuration.base_url, context)


def before_scenario(context: runner.Context, scenario) -> None:
    context.driver = behave.use_fixture(configuration.driver, context)


def after_scenario(context: runner.Context, scenario) -> None:
    context.driver.close()
