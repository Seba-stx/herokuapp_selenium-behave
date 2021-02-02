from behave import step


@step("User clicks A/B Testing")
def step_impl(context):
    context.page.click_ab_testing()


@step("User clicks Add/Remove Elements")
def step_impl(context):
    context.page.click_add_remove_element()


@step("User clicks Form Authentication")
def step_impl(context):
    context.page.click_form_authentication()


@step("User clicks Dropdown")
def step_impl(context):
    context.page.click_dropdown()


@step("User clicks JavaScript Alerts")
def step_impl(context):
    context.page.click_js_alerts()