
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class PythonOrgSearch(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome('/Users/ZhiyuZhu/Documents/CS 242/FinalProject/chromedriver')


    def test_register(self):
        driver = self.driver
        driver.get("http://localhost:63342/FinalProject/StartPage.html?_ijt=8746aiod0o1qtcke44n4k5j5qm")
        self.assertIn("Animation Go", driver.title)
        driver.find_element_by_name("sign_in_button").click()

        a = driver.find_element_by_name('username')
        a.send_keys('fayina')

        driver.find_element_by_name("click_sign_in").click()
        self.assertIn('Animation Personal Profile Page', driver.title)


        c = driver.find_element_by_name("comment_bar")
        self.assertIn('TODAY COMMENT', c.text)

        b = driver.find_element_by_name("ghibli_studio")
        self.assertIn('Ghibli ジブリ', b.text)

        b = driver.find_element_by_name("aniplex_studio")
        self.assertIn('Aniplex アニプレックス', b.text)

        b = driver.find_element_by_name("deen_studio")
        self.assertIn('Deen スタジオディーン', b.text)

        b = driver.find_element_by_name("bones_studio")
        self.assertIn('Bones ボンズ', b.text)











    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()