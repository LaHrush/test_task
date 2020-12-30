import pytest
from Helper import get_status_code, get_user_id, get_message, get_user_name, get_user_email, get_user_gender
from RestApi import RestApi
from data import testdata_with_empty_fields, testdata_with_all_fields
from models.UserModel import UserModel
from names.ErrorMessages import ErrorMessages
from names.ApiKeyNames import ApiKeyNames
from names.CallNames import CallNames



@pytest.mark.parametrize("users", testdata_with_empty_fields)
def test_create_user_with_empty_fields(users):

    responce = RestApi.post(resource=CallNames.CREATE_USER_PATH, payload=users)
    assert get_status_code(responce) == ApiKeyNames.UNPROCESSABLE_ENTITY
    assert get_message(responce) == ErrorMessages.CANT_BY_BLANK

@pytest.mark.parametrize("users", testdata_with_all_fields)
def test_create_user_with_all_fields(users):

    responce = RestApi.post(resource=CallNames.CREATE_USER_PATH, payload=users)
    assert get_status_code(responce) == ApiKeyNames.CREATED_STATUS_CODE
    assert get_user_name(responce) == users.name
    assert get_user_email(responce) == users.email
    assert get_user_gender(responce) == users.gender

def test_delete_user():
    # Create user
    responce = RestApi.post(resource=CallNames.CREATE_USER_PATH, payload=UserModel())
    assert get_status_code(responce) == ApiKeyNames.CREATED_STATUS_CODE
    user_id = get_user_id(responce)
    # Delete user
    responce = RestApi.delete(resource=CallNames.DELETE_USER_PATH + str(user_id))
    assert get_status_code(responce) == ApiKeyNames.NO_CONTENT
    # check deleted user
    responce = RestApi.get(resource=CallNames.GET_USER + str(user_id))
    assert responce.json()['data']['message'] == ErrorMessages.NOT_FOUND

def test_update_user_with_all_fields():
    # Create user
    responce = RestApi.post(resource=CallNames.CREATE_USER_PATH, payload=UserModel())
    assert get_status_code(responce) == ApiKeyNames.CREATED_STATUS_CODE
    user_id = get_user_id(responce)
    # Update user
    responce = RestApi.put(resource=CallNames.UPDATE_USER_PATH + str(user_id), payload=UserModel())
    assert get_status_code(responce) == ApiKeyNames.OK_STATUS_CODE
    # Check updated data
    assert get_user_name(responce) == UserModel().name
    assert get_user_email(responce) == UserModel().email
    assert get_user_gender(responce) == UserModel().gender

