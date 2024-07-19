from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import app
import threading

# Global driver
driver = None

@given('I am on the registration page')
def step_given_on_registration_page(context):
    global driver

    # Initialize the Flask app in test mode
    context.app = app.create_app()
    context.app.config['TESTING'] = True
    context.app.config['WTF_CSRF_ENABLED'] = False

    # Start the Flask server in a separate thread
    context.server_thread = threading.Thread(target=context.app.run, kwargs={'use_reloader': False})
    context.server_thread.start()

    # Initialize the Selenium WebDriver
    driver = webdriver.Chrome()  # or webdriver.Firefox()
    driver.implicitly_wait(10)

    # Wait for the server to start
    time.sleep(1)

    driver.get('http://127.0.0.1:5000')

@when('I register with a valid username and password')
def step_when_register_valid(context):
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    submit = driver.find_element(By.NAME, 'submit')

    username.send_keys('validuser')
    password.send_keys('password')
    submit.click()

@when('I register with an invalid username')
def step_when_register_invalid(context):
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    submit = driver.find_element(By.NAME, 'submit')

    username.send_keys('fail')
    password.send_keys('password')
    submit.click()

@then('I should see a success message')
def step_then_see_success_message(context):
    message = driver.find_element(By.ID, 'message')
    assert 'Registration successful!' in message.text

@then('I should see an error message')
def step_then_see_error_message(context):
    message = driver.find_element(By.ID, 'message')
    assert 'Registration failed. Try again.' in message.text

def after_scenario(context, scenario):
    # Teardown code to quit the browser and stop the server
    driver.quit()
    context.server_thread.join()
