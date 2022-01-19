import time

from behave import *


@given(u'User navigate to home page url')
def step_impl(context):

    context.driver.get('https://www.google.com')
    time.sleep(4)
    titles=context.driver.title
    assert 'Googles' in titles


@when(u'User enter the search box')
def step_impl(context):
    print("last step")


@then('user clicks on submit button click')
def step_impl(context):
    print(u'STEP: Then user clicks on submit button')

