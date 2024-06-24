import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--API_KEY", action="store"
    )

@pytest.fixture
def API_KEY(request):
    return request.config.getoption("--API_KEY")