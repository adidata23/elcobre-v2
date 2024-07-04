import pytest
from utilities.report_pdf import PDF


@pytest.mark.login_page_tests
class TestLoginPage:

    def test_login_success1(self, base, pages):
        pages.login_page.inputUsername("standard_user")
        pages.login_page.inputPassword("secret_sauce")
        pages.login_page.clickLogin()
        assert pages.login_page.url_success_login() == "https://www.saucedemo.com/inventory.html"
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success1", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data1", False)

    def test_login_success2(self, base, pages):
        pages.login_page.inputUsername('problem_user')
        pages.login_page.inputPassword("secret_sauce")
        pages.login_page.clickLogin()
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success2", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data2")

    def test_login_success3(self, base, pages):
        pages.login_page.user_login("locked_out_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success3", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data3")

    def test_login_success4(self, base, pages):
        pages.login_page.user_login("performance_glitch_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success4", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data4")

    def test_login_success5(self, base, pages):
        pages.login_page.user_login("error_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success5", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data5")

    def test_login_success6(self, base, pages):
        pages.login_page.user_login("visual_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success6", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data6")

    def test_login_success7(self, base, pages):
        pages.login_page.inputUsername("standard_user")
        pages.login_page.inputPassword("secret_sauce")
        pages.login_page.clickLogin()
        assert pages.login_page.url_success_login() == "https://www.saucedemo.com/inventory.html"
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success7", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data7")

    def test_login_success8(self, base, pages):
        pages.login_page.inputUsername('problem_user')
        pages.login_page.inputPassword("secret_sauce")
        pages.login_page.clickLogin()
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success8", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data8")

    def test_login_success9(self, base, pages):
        pages.login_page.user_login("locked_out_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success9", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data9")

    def test_login_success10(self, base, pages):
        pages.login_page.user_login("performance_glitch_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success10", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data10")

    def test_login_success11(self, base, pages):
        pages.login_page.user_login("error_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success11", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data11")

    def test_login_success12(self, base, pages):
        pages.login_page.user_login("visual_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success12", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data12")

    def test_login_success13(self, base, pages):
        pages.login_page.inputUsername('problem_user')
        pages.login_page.inputPassword("secret_sauce")
        pages.login_page.clickLogin()
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success13", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data13")

    def test_login_success14(self, base, pages):
        pages.login_page.user_login("locked_out_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success14", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data14")

    def test_login_success15(self, base, pages):
        pages.login_page.user_login("performance_glitch_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success15", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data15")

    def test_login_success16(self, base, pages):
        pages.login_page.user_login("error_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success16", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data16")

    def test_login_success17(self, base, pages):
        pages.login_page.user_login("visual_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success17", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data17")

    def test_login_success18(self, base, pages):
        pages.login_page.inputUsername('problem_user')
        pages.login_page.inputPassword("secret_sauce")
        pages.login_page.clickLogin()
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success18", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data18")

    def test_login_success19(self, base, pages):
        pages.login_page.user_login("locked_out_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success19", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data19")

    def test_login_success20(self, base, pages):
        pages.login_page.user_login("performance_glitch_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success20", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data20")

    def test_login_success21(self, base, pages):
        pages.login_page.user_login("error_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success21", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data21")

    def test_login_success22(self, base, pages):
        pages.login_page.user_login("visual_user", "secret_sauce")
        base.func_take_screenshot_pass(screenshot=True, desc1="Login success22", desc2="image descriptions")
        base.ss.write_scenario_txt("Login with valid data22")


pdf = PDF(pdf_filename="Testing PDF.pdf",
          # param_path="data//param.txt",
          # result_path="data//scenario_result.txt",
          cvpg_subtitle="Liquid Management - Cash Distribution",
          cvpg_author="Automation Team",
          cvpg_tcid="Cash Distribution Thru to Casa Thru - Fix - Immediate",
          header_author="Automation Team",
          header_tcid="Cash Distribution Thru to Casa Thru - Fix - Immediate")
pdf.data_reader()
pdf.generate_report()
