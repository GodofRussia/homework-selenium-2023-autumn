from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    # parser.addoption('--debug_log', action='store_true')


@pytest.fixture(scope="session")
def config(request):
    browser = request.config.getoption("--browser")
    # debug_log = request.config.getoption('--debug_log')

    return {
        "browser": browser,
        #'debug_log': debug_log,
    }
