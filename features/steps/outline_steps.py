from behave import *


@when('user enter user "{name}"')
def step_impl(context, name):
    print(u'STEP: When user emter user ' + name)
