from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_homepage_elements():
    driver = webdriver.Chrome()
    
    try:
        driver.get("http://localhost:3333")
        wait = WebDriverWait(driver, 10)
        
        # Test 3: Check for Taskcafe logo/brand
        brand_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(),'Taskcafe')]")
            )
        )
        print("✓ Taskcafe brand displayed")
        
        # Test 4: Check for login form elements
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(
            By.XPATH, "//button[@type='submit']"
        )
        
        print("✓ Login form elements present")
        driver.save_screenshot("homepage_elements.png")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_homepage_elements()
