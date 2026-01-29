import pytest

# 2. Create a custom command-line option using pytest_addoption
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against: dev, qa, prod"
    )

@pytest.fixture
def get_env(request):
    return request.config.getoption("--env")