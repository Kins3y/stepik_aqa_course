import unittest
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time

        browser = webdriver.Chrome()
        link = 'https://suninjuly.github.io/registration1.html'
        try:
            browser.get(link)
            pc1 = browser.find_element(By.CSS_SELECTOR, 'input')
            pc1.send_keys('Ivan')
            pc2 = browser.find_element(By.CSS_SELECTOR, '.first_block > .form-group.second_class > input')
            pc2.send_keys('Ivanov')
            pc3 = browser.find_element(By.CLASS_NAME, 'form-control.third')
            pc3.send_keys('Emailov@email.email')
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(1)
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            browser.quit()

    def test_abs2(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time

        browser = webdriver.Chrome()
        link = 'https://suninjuly.github.io/registration2.html'
        try:
            browser.get(link)
            pc1 = browser.find_element(By.CSS_SELECTOR, 'input')
            pc1.send_keys('Ivan')
            pc2 = browser.find_element(By.CSS_SELECTOR, '.first_block > .form-group.second_class > input')
            pc2.send_keys('Ivanov')
            pc3 = browser.find_element(By.CLASS_NAME, 'form-control.third')
            pc3.send_keys('Emailov@email.email')
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(1)
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!",  welcome_text)

        finally:
            browser.quit()

if __name__ == "__main__":
    unittest.main()