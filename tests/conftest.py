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
        # options.add_argument("--window-size=1920,1080")

    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# Agar fixture driver bisa digunakan di hook make report
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







