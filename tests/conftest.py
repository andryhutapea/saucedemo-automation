# # Report with allure report
#
# import pytest
# import os
# from datetime import datetime
# from selenium import webdriver
# import allure
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser-mode",
#         action="store",
#         default="headed",
#         help="Choose between 'headed' or 'headless'"
#     )
#
#
# @pytest.fixture
# def driver(request):
#     browser_mode = request.config.getoption("--browser-mode")
#     options = webdriver.ChromeOptions()
#
#     if browser_mode == "headless":
#         options.add_argument("--headless=new")  # For modern Chrome versions
#         options.add_argument("--disable-gpu")
#         options.add_argument("--window-size=1920,1080")
#
#     options.add_argument("--start-maximized")
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture(autouse=True)
# def attach_driver_to_request(driver, request):
#     request.node.funcargs["driver"] = driver
#
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     driver = item.funcargs.get("driver", None)
#
#     if rep.when == "call" and driver:
#         name = item.name
#         timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         status = "passed" if rep.passed else "failed"
#         screenshot_dir = os.path.abspath("reports/screenshots")
#         os.makedirs(screenshot_dir, exist_ok=True)
#         filename = f"{name}_{status}_{timestamp}.png"
#         filepath = os.path.join(screenshot_dir, filename)
#
#         driver.save_screenshot(filepath)
#
#         # Attach screenshot to Allure
#         with open(filepath, "rb") as image_file:
#             allure.attach(
#                 image_file.read(),
#                 name=f"{name} - {status}",
#                 attachment_type=allure.attachment_type.PNG
#             )
# end Code


# # Report with report.html

# import pytest
# import os
# import base64
# from datetime import datetime
# from selenium import webdriver
#
#
# @pytest.fixture
# def driver(request):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")
#
#     browser_mode = request.config.getoption("--browser")
#     if browser_mode == "headless":
#         options.add_argument("--headless=new")
#         options.add_argument("--disable-gpu")
#         options.add_argument("--window-size=1920,1080")
#
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="headed", help="headed or headless")
#
#
# @pytest.fixture(autouse=True)
# def attach_driver_to_request(driver, request):
#     request.node.funcargs["driver"] = driver
#
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     from pytest_html import extras
#
#     outcome = yield
#     rep = outcome.get_result()
#     driver = item.funcargs.get("driver", None)
#
#     if rep.when == "call" and driver:
#         screenshot_dir = os.path.abspath("reports/screenshots")
#         os.makedirs(screenshot_dir, exist_ok=True)
#
#         test_name = item.name
#         status = "passed" if rep.passed else "failed"
#         timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         filename = f"{test_name}_{status}_{timestamp}.png"
#         filepath = os.path.join(screenshot_dir, filename)
#
#         driver.save_screenshot(filepath)
#
#         # Encode image to base64
#         with open(filepath, "rb") as f:
#             encoded_img = base64.b64encode(f.read()).decode("utf-8")
#
#         html = f'<div><strong>{status.upper()}</strong><br><img src="data:image/png;base64,{encoded_img}" alt="{filename}" style="width:400px;height:auto;" /></div>'
#
#         if hasattr(rep, "extra"):
#             rep.extra.append(extras.html(html))
#         else:
#             rep.extra = [extras.html(html)]

# end


# # Combine report.html & allure reports

import pytest
import os
import base64
from datetime import datetime
from selenium import webdriver
import allure
from pytest_html import extras


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="headed", help="headed or headless"
    )


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()

    browser_mode = request.config.getoption("--browser")
    if browser_mode == "headless":
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# Agar fixture driver bisa digunakan di hook makereport
@pytest.fixture(autouse=True)
def attach_driver_to_request(driver, request):
    request.node.funcargs["driver"] = driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    driver = item.funcargs.get("driver", None)

    if rep.when == "call" and driver:
        test_name = item.name
        status = "passed" if rep.passed else "failed"
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        screenshot_dir = os.path.abspath("reports/screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)

        filename = f"{test_name}_{status}_{timestamp}.png"
        filepath = os.path.join(screenshot_dir, filename)

        driver.save_screenshot(filepath)

        # --- Attach to Allure ---
        with open(filepath, "rb") as image_file:
            allure.attach(
                image_file.read(),
                name=f"{test_name} - {status}",
                attachment_type=allure.attachment_type.PNG
            )

        # --- Attach to pytest-html ---
        with open(filepath, "rb") as f:
            encoded_img = base64.b64encode(f.read()).decode("utf-8")
        html = f'<div><strong>{status.upper()}</strong><br><img src="data:image/png;base64,{encoded_img}" style="width:400px;height:auto;" /></div>'

        extra = getattr(rep, "extra", [])
        extra.append(extras.html(html))
        rep.extra = extra
# # End Code







