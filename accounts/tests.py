from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver

class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path='<Chromドライバ配置場所>')

    @classmethod
    def testDownClass(cls):
        cls.selenium.quit()
        super().testDownClass()

    def test_login(self):
        # ログインページを開く
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('sccount_login')))

        # ログイン
        username_input = self.selenium.find_element_by_name("login")
        username_input.send_keys('<ユーザー登録済みのメールアドレス>')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('<ログインパスワード>')
        self.selenium.find_element_by_class_name('btn').click()

        # ページのタイトルの検証
        self.assertEquals('日記一覧｜Private Diary', self.selenium.title)