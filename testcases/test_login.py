
class TestLoginPage:

    def test_login_success1(self, base, login):
        login.inputUsername("standard_user")
        login.inputPassword("secret_sauce")
        login.clickLogin()
        base.ss.write_scenario_txt("Login with valid data1", False)
        assert login.url_success_login() == "https://www.saucedemo.com/inventory.html"
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success1", desc2="")

    def test_login_success2(self, base, login):
        base.ss_obj.write_scenario_txt("Login with valid data2", False)
        login.inputUsername('problem_user')
        login.inputPassword("secret_sauce")
        login.clickLogin()
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success2", desc2="")

    def test_login_success3(self, base, login):
        base.ss_obj.write_scenario_txt("Login with valid data3", False)
        login.user_login("locked_out_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success3", desc2="")

    def test_login_success4(self, base, login):
        base.ss_obj.write_scenario_txt("Login with valid data4", False)
        login.user_login("performance_glitch_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success4", desc2="")

    def test_login_success5(self, base, login):
        base.ss_obj.write_scenario_txt("Login with valid data5", False)
        login.user_login("error_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success5", desc2="")

    def test_login_success6(self, base, login):
        base.ss_obj.write_scenario_txt("Login with valid data6", False)
        login.user_login("visual_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success6", desc2="")
