import pytest


@pytest.mark.login_page_tests
class TestLoginPage2:

    def test_success1(self, base, pages):
        pages.login_page.inputUsername("standard_user")
        pages.login_page.inputPassword("secret_sauce")
        pages.login_page.clickLogin()
        assert pages.login_page.url_success_login() == "https://www.saucedemo.com/inventory.html"
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login1", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data1", False)

    def test_success2(self, base, pages):
        pages.login_page.inputUsername('problem_user')
        pages.login_page.inputPassword("secret_sauce")
        pages.login_page.clickLogin()
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login2", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data2")

    def test_success3(self, base, pages):
        pages.login_page.user_login("locked_out_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login3", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data3")

    def test_success4(self, base, pages):
        pages.login_page.user_login("performance_glitch_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login4", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data4")

    def test_success5(self, base, pages):
        pages.login_page.user_login("error_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login5", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data5")

    def test_success6(self, base, pages):
        pages.login_page.user_login("visual_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login6", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data6")

    def test_success7(self, base, pages):
        pages.login_page.inputUsername("standard_user")
        pages.login_page.inputPassword("secret_sauce")
        pages.login_page.clickLogin()
        assert pages.login_page.url_success_login() == "https://www.saucedemo.com/inventory.html"
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login7", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data7")

    def test_success8(self, base, pages):
        pages.login_page.inputUsername('problem_user')
        pages.login_page.inputPassword("secret_sauce")
        pages.login_page.clickLogin()
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login8", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data8")

    def test_success9(self, base, pages):
        pages.login_page.user_login("locked_out_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login9", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data9")

    def test_success10(self, base, pages):
        pages.login_page.user_login("performance_glitch_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login10", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data10")

    def test_success11(self, base, pages):
        pages.login_page.user_login("error_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login11", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data11")

    def test_success12(self, base, pages):
        pages.login_page.user_login("visual_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login12", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data12")

    def test_success13(self, base, pages):
        pages.login_page.inputUsername('problem_user')
        pages.login_page.inputPassword("secret_sauce")
        pages.login_page.clickLogin()
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login13", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data13")

    def test_success14(self, base, pages):
        pages.login_page.user_login("locked_out_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login14", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data14")

    def test_success15(self, base, pages):
        pages.login_page.user_login("performance_glitch_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login15", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data15")

    def test_success16(self, base, pages):
        pages.login_page.user_login("error_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login16", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data16")

    def test_success17(self, base, pages):
        pages.login_page.user_login("visual_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login17", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data17")

    def test_success18(self, base, pages):
        pages.login_page.inputUsername('problem_user')
        pages.login_page.inputPassword("secret_sauce")
        pages.login_page.clickLogin()
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login18", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data18")

    def test_success19(self, base, pages):
        pages.login_page.user_login("locked_out_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login19", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data19")

    def test_success20(self, base, pages):
        pages.login_page.user_login("performance_glitch_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login20", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data20")

    def test_success21(self, base, pages):
        pages.login_page.user_login("error_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login21", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data21")

    def test_success22(self, base, pages):
        pages.login_page.user_login("visual_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Testing 2 Module of Login22", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data22")
