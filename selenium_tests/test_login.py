from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login():
    # Setup WebDriver
    driver = webdriver.Chrome()
    
    try:
        # Navigate to Taskcafe
        driver.get("http://localhost:3333")
        
        # Wait for page to load
        wait = WebDriverWait(driver, 10)
        
        # Test 1: Check if login page loads
        email_field = wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        print("✓ Login page loaded successfully")
        
        # Test 2: Check if register link exists
        register_link = driver.find_element(
            By.XPATH, "//a[contains(text(),'Register')]"
        )
        print("✓ Registration link present")
        
        # Take screenshot
        driver.save_screenshot("login_page.png")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()
