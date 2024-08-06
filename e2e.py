import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_scores_service():
    chrome_options = Options()
    # Add any required Chrome options here if needed
    # chrome_options.add_argument("--headless")  # Run in headless mode if required

    service = Service(ChromeDriverManager().install())
    driver_chrome = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver_chrome.get("http://127.0.0.1:8777/")
        # Use WebDriverWait to wait for the element to be present
        score = WebDriverWait(driver_chrome, 10).until(
            EC.presence_of_element_located((By.ID, "score"))
        )
        # Check if the score is within the expected range
        if 0 <= int(score.text) <= 1000:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver_chrome.quit()

def main_function():
    if test_scores_service():
        sys.exit(0)
    else:
        sys.exit(-1)

if __name__ == "__main__":
    main_function()
