import allure
import pytest
from selenium import webdriver

_driver = None
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('lang=en_US')


def pytest_addoption(parser):
    '''
    Add pytest argument --browser
    '''

    parser.addoption(
        '--browser', action='store', default='chrome', help='browser option: chrome or firefox'
    )


@pytest.fixture(scope='session')
def driver(request):
    global _driver
    name = request.config.getoption('--browser')
    if _driver is None:
        if name == 'chrome':
            _driver = webdriver.Chrome(options=options)
        elif name == 'firefox':
            _driver = webdriver.Firefox()
        else:
            _driver = webdriver.Chrome(options=options)
        _driver.set_window_position(1000,0)
    print('STARTING BROWSER: %s' % name)

    yield _driver
    # _driver.quit()


@pytest.fixture(scope="session", autouse=True)
def pre_setup():
    # clean 'failures' file everytime when run the new test
    with open('failures', encoding='utf-8', mode='w') as file:
        file.truncate()


# do a screenshot everytime when a test fails
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    Get each test case result hook function
    :param item:
    :param call:
    :return:
    '''
    # Get hook function result
    outcome = yield
    rep = outcome.get_result()
    # only find calls (test cases) with failure, no setup/teardown included
    if rep.when == 'call' and rep.failed:
        with open('failures', "a") as f:
            f.write(rep.nodeid + "\n")
        # Take screenshot in allure report
        if hasattr(_driver, 'get_screenshot_as_png'):
            with allure.step('Capture failure screenshot...'):
                allure.attach(_driver.get_screenshot_as_png(), 'fail_screen_shot', allure.attachment_type.PNG)
