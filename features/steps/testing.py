from behave import *


@given("we run behave")
def step_impl(context):
    pass


@when("we have a passing test case")
def step_impl(context):
    assert True is not False


@then("behave will pass the test case")
def step_impl(context):
    assert context.failed is False
