import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:

    def test_successful_login(self, driver):
        driver.get("http://localhost:3000/admin")
        # cibler les champs de formulaire
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        # login et mot de passe        
        email_input.send_keys("l.sohouenou@it-akademy.fr")
        password_input.send_keys("Yvannah@2020")
        login_button.click()
    
        WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))
        
        assert "Dashboard" in driver.title