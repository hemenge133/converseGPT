import pytest
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv

load_dotenv()

def test_html_client():
    current_path = os.path.abspath(os.path.dirname(__file__))
    html_file_path = os.path.join(current_path, '..', 'src', 'index.html')

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(f"file://{html_file_path}")
    
    # Get API Key from environment and handle input prompt
    api_key = os.environ['OPENAI_API_KEY']
    alert = WebDriverWait(driver, 30).until(expected_conditions.alert_is_present())
    alert.send_keys(api_key)
    alert.accept()

    # Find the input box and the send button find_element(by=By.CSS_SELECTOR, value=css_selector)
    input_box = driver.find_element(by=By.CSS_SELECTOR, value='input[type="text"].flex-grow[placeholder="Type a message..."]')
    send_button = driver.find_element(by=By.ID, value="send-button")  # Replace with correct ID

    # Type text and click the send button
    input_box.send_keys("Hello World")
    send_button.click()

    # Wait until chat bubble is populated
    wait = WebDriverWait(driver, 5)
    ai_chat_bubble = wait.until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".chat-bubble-ai"))
    )

    # Check the response - replace with the correct logic to find the response
    response = ai_chat_bubble.text
    assert len(response) > 0

    driver.close()
