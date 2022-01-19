from behave import *


@given('User entered the url')
def step_impl(context):
    print('STEP: Given User entered the url')


@when('user emter user name')
def step_impl(context):
    print(u'STEP: When user emter user name')


@then('user enter the passwords')
def step_impl(context):
    print(u'STEP: Then user enter the passwords')


@then('user clicks on submit button')
def step_impl(context):
    print(u'STEP: Then user clicks on submit button')
