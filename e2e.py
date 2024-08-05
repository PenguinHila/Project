import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_scores_service():
    chrome_options = Options()

    # Optionally add any necessary options here
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("http://127.0.0.1:5000/")
        score_element = driver.find_element(By.ID, "score")
        score_value = int(score_element.text)

        if 0 <= score_value <= 1000:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit()


def main_function():
    if test_scores_service():
        sys.exit(0)
    else:
        sys.exit(-1)


if __name__ == "__main__":
    main_function()