from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

class FacebookScraper():
    def setUp(self):
        # opens firefox
        self.driver = webdriver.Firefox()
        # opens facebook.com
        self.driver.get("https://wwww.facebook.com")

    def facebook_login(self):
        # update with your own details
        fb_uname = "insert your email"
        fb_upasee = "insert your password"

        emailFieldID = "email"
        passFieldID = "pass"
        loginButtonXpath = "//input[@value='Log In']"
        fbLogoXpath = "(//a[contains(@href, 'logo')])[1]"

        # retrieves input fields
        emailFieldElement = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        # clears and fills in input fields, then logs in
        emailFieldElement.clear()
        emailFieldElement.send_keys(fb_uname)
        passFieldElement.clear()
        passFieldElement.send_keys(fb_upasee)
        loginButtonElement.click()


    def scrape_text(self):
        # change scrape_url to vary the url that you want the text from
        scrape_url = "https://www.facebook.com/search/posts/?q=venue%20suggestions&filters_rp_location=%7B%22name%22%3A%22location%22%2C%22args%22%3A%22109248112428236%22%7D"
        self.driver.get(scrape_url)

        while True:
            # performs full page scroll and pauses
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            # change newsfeed_div_id to ID of newsfeed column
            newsfeed_div_id = "pagelet_loader_initial_browse_result"
            text = self.driver.find_element_by_id(newsfeed_div_id).text
            print(text)

            # performs full page scroll and pauses
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
