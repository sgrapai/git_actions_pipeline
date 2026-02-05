"""Conftest file"""
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--base_api_url",
        action="store",
        default="",
        help="base api url",
    )
    parser.addoption(
        "--post_id",
        action="store",
        default="99",
        help="a post id number",
    )
    parser.addoption(
        "--post_error_id",
        action="store",
        default="150",
        help="a post id number that doesn't exist",
    )
    parser.addoption(
        "--user_id",
        action="store",
        default="1",
        help="a user id number",
    )

@pytest.fixture
def base_api_url(request):
    return request.config.getoption("--base_api_url")

@pytest.fixture
def post_id(request):
    return request.config.getoption("--post_id")

@pytest.fixture
def post_error_id(request):
    return request.config.getoption("--post_error_id")

@pytest.fixture
def user_id(request):
    return request.config.getoption("--user_id")
