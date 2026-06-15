from pages.login_page import LoginPage
import pytest


@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("standard_user", "secret_sauce", True),
        ("problem_user", "secret_sauce", True),
        ("performance_glitch_user", "secret_sauce", True),
        ("error_user", "secret_sauce", True),
        ("visual_user", "secret_sauce", True),
        ("locked_out_user", "secret_sauce", False)
    ]
)
def test_login(driver, username, password, expected):
    login = LoginPage(driver)
    login.open()

    login.login(username, password)

    if expected:

        assert "inventory" in driver.current_url

    else:

        assert "Epic sadface" in login.get_error_message()
