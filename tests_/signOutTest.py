import time
from pages_.navigationBar import NavigationBar
from tests_.baseTest import BaseTestWithLogin
from pages_.signInPage import LoginPage


class SignOut(BaseTestWithLogin):

    def test_for_sign_out(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.move_mouse_to_account_and_lists_container()
        navigationBarObj.click_on_sign_out_button()
        time.sleep(5)
        loginPageObj = LoginPage(self.driver)
        textOfSignIn = loginPageObj.get_sign_in_text()
        self.assertEqual(textOfSignIn, "Sign in")
