import time

from behave import *
from selenium.webdriver.common.by import By

@given("I have Cucumber installed")
def step_impl(context):
    print("Important message")

@when("Winter season is coming")
def step_impl(context):
    print("Prepare for impact")

@then("All tests should passed")
def step_impl(context):
    print("Good job")



@given("I go to autocomplete page")
def step_impl(context):
    context.browser.get("https://formy-project.herokuapp.com/")
    time.sleep(3)
    context.browser.find_element(By.LINK_TEXT,"Autocomplete").click()
    time.sleep(3)

@when('I type ko')
def step_impl(context):
    context.browser.find_element(By.ID,"locality").send_keys("Cluj-Napoca")
    time.sleep(3)


@then('Cluj-Napoca should be available')
def step_impl(context):
    print("Good job")
    time.sleep(3)



@given("I access google.ro")
def step_impl(context):
    context.browser.get("https://www.google.ro")
    time.sleep(2)

@when("I type 'Coronavirus' in textfield")
def step_impl(context):
    button = context.browser.find_element(By.CSS_SELECTOR, "#L2AGLb")
    button.click()
    time.sleep(3)
    search_bar = context.browser.find_element(By.NAME, "q")
    search_bar.send_keys("Coronavirus")
    time.sleep(2)
    search_bar.submit()
    time.sleep(2)

@then("I want to see the news regarding the subject")
def step_impl(context):
    print("Step executed")


@given("I enter https://www.herokuapp.com")
def step_impl(context):
    context.browser.get("https://the-internet.herokuapp.com/login")

@when("I enter correct credentials")
def step_impl(context):
    user = (By.ID, "username")
    pwd = (By.ID, "password")
    btn = (By.CLASS_NAME, "radius")
    context.browser.find_element(*user).send_keys("tomsmith")  # we open the tuple and access it with *
    context.browser.find_element(*pwd).send_keys("SuperSecretPassword!")
    context.browser.find_element(*btn).click()
    time.sleep(3)

@then("I access the site info")
def step_impl(context):
    logout_btn = (By.CLASS_NAME, "button")
    context.browser.find_element(*logout_btn).click()


@when(u'I type "{location}"')
def step_impl(context,location):
    context.browser.find_element(By.ID, "autocomplete").send_keys(location)


@then(u'I will see the "{results}"')
def step_impl(context,results):
    time.sleep(2)
    message = context.browser.find_element(By.CSS_SELECTOR,"body > div.pac-container.hdpi > div > div:nth-child(2) > span").text
    assert message == "This page can't load Google Maps correctly."
    print("The selected location is in" + results )
    time.sleep(3)

@given("I access https://www.openstreetmap.org")
def step_impl(context):
    context.browser.get("https://www.openstreetmap.org")

@when("I type an address in the text field")
def step_impl(context):
    searchbar = context.browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[1]/div/div[1]/input")
    go_btn = context.browser.find_element(By.CSS_SELECTOR, "#sidebar > div.search_forms > form.search_form.px-1.py-2 > div > div.col > div > div.input-group-append > input")
    searchbar.send_keys("Kogalniceanu Street Bucharest")
    time.sleep(3)
    go_btn.click()
    time.sleep(3)

@then("I want it to be shown on the map")
def step_impl(context):
    print("Address shown")


@given("I access https://www.openstreetmap.org and after I press route button")
def step_impl(context):
    context.browser.get("https://www.openstreetmap.org")
    route_btn = context.browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[2]/a")
    route_btn.click()

@when("I type in two locations, one in every text field and I press GO")
def step_impl(context):
    from_bar = context.browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[2]/div[2]/div[2]/input")
    to_bar = context.browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[2]/div[3]/div[2]/input")
    calculate_btn = context.browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[2]/div[4]/div[2]/input")
    from_bar.send_keys("Bucharest")
    to_bar.send_keys("Lengerich")
    time.sleep(3)
    calculate_btn.click()


@then("The distance should be shown on the screen")
def step_impl(context):
    time.sleep(5)
    distance = context.browser.find_element(By.XPATH, "//*[@id='sidebar_content']/p[1]")
    print(distance.text)


