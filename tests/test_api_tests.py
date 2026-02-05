""" tests file container """
import json
from pprint import pprint
import random
import string

import requests
from requests import Response

import pytest

@pytest.mark.smoke
@pytest.mark.api
def test_request_all_posts(base_api_url):
    """Sends GET requests for all posts info"""
    response: Response = requests.get(f'{base_api_url}/posts', timeout=2)
    assert response.status_code == 200, \
        f"response status was not 200 but instead: {response.status_code}"
    response_dict: dict = json.loads(response.text)
    ids_list = [post['id'] for post in response_dict]
    assert ids_list == sorted(ids_list), \
        "response was not sorted in ascending order"

@pytest.mark.api
def test_request_post_with_id(base_api_url, post_id):
    """Retrieves a single post by it's ID using GET request"""
    post_id = int(post_id)
    response: Response = requests.get(f'{base_api_url}/posts/{post_id}', \
        timeout=2)
    assert response.status_code == 200, \
        f"response status was not 200 but instead: {response.status_code}"
    response_dict: dict = json.loads(response.text)
    print(response_dict['id'])
    assert response_dict['userId'] == 10, \
        f"post userId was not 10 but instead: {response_dict['userId']}"
    assert response_dict['id'] == post_id, \
        f"post id was not {post_id} but instead: {response_dict['id']}"
    assert response_dict['title'], "post title was empty"
    assert response_dict['body'], "post body was empty"

@pytest.mark.api
def test_request_post_not_found(base_api_url, post_error_id):
    """Sends GET request for a non-existing post and expects 404"""
    post_id = int(post_error_id)
    response: Response = requests.get(f'{base_api_url}/posts/{post_id}', \
        timeout=2)
    assert response.status_code == 404, \
        f"response status was not 404 but instead: {response.status_code}"
    response_dict: dict = json.loads(response.text)
    assert 'body' not in response_dict, "response body was not empty"

@pytest.mark.smoke
@pytest.mark.api
def test_create_post_with_user_id(base_api_url, user_id):
    """Creates a new post using POST request"""
    user_id = int(user_id)
    random_title = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    random_body = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    post_data = {
        "title": random_title,
        "body": random_body,
        "userId": user_id
    }
    response: Response = requests.post(f'{base_api_url}/posts', \
        json=post_data, timeout=2)
    assert response.status_code == 201, \
        f"response status was not 201 but instead: {response.status_code}"
    response_dict: dict = json.loads(response.text)
    assert response_dict['userId'] == user_id, \
        f"post userId was not {user_id} but instead: {response_dict['userId']}"
    assert response_dict['id'] == 101, \
        f"post id was not 101 but instead: {response_dict['id']}"
    assert response_dict['title'] == random_title, "post title was not as expected"
    assert response_dict['body'] == random_body, "post body was not as expected"

@pytest.mark.api
def test_get_user_info_by_id(base_api_url, user_id):
    """Retrieves user info by user ID using GET request"""
    user_id = int(user_id)
    response: Response = requests.get(f'{base_api_url}/users/{user_id}', \
        timeout=2)
    assert response.status_code == 200, \
        f"response status was not 200 but instead: {response.status_code}"
    response_dict: dict = json.loads(response.text)
    pprint(response_dict, depth=3, sort_dicts=False)
