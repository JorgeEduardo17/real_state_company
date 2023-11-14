import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.models.py_object_id import PyObjectId


@pytest.fixture
def test_client():
    """
    Creates and provides a test client for the FastAPI application.
    This client can be used to perform test requests to the application.
    :return:
    """
    with TestClient(app) as client:
        yield client


@pytest.fixture
def property_data():
    """
    Provides test data for a property.
    This data can be used for tests that require property data but do not require an identifier.
    :return:
    """
    return {
        "address": "Carrera 1 #1-1",
        "price": 1000,
        "code_internal": "001",
        "year": 2000,
        "id_owner": "JOED1"
    }


@pytest.fixture
def property_create_data(property_data):
    """
    Extends the 'property_data' data with an additional 'name' field.
    Useful for tests requiring property creation data.
    :param property_data:
    :return:
    """
    return {"name": "Property_name_1", **property_data}


@pytest.fixture
def property_data_with_id(property_create_data):
    """
    Adds a unique identifier to the property data.
    Useful for tests that require a property with an assigned identifier.
    :param property_create_data:
    :return:
    """
    return {"id": PyObjectId(), **property_create_data}


@pytest.fixture
def image_data_with_id(property_data_with_id):
    """
    Generates test data for an image associated with a property, including a unique identifier.
    Useful for tests related to loading and managing property images.
    :param property_data_with_id:
    :return:
    """
    file_name = "test_image.jpg"
    return {
        "_id": PyObjectId(),
        "id_property": property_data_with_id['id'],
        "file": f"app/images/{file_name}",
        "enable": True
    }


@pytest.fixture
def mock_property_repository_create(mocker):
    """
    Creates a mock for the 'create' method of the property repository.
    This allows to simulate and test this method without performing real operations on the database.
    :param mocker:
    :return:
    """
    return mocker.patch('app.repositories.property.PropertyRepository.create')


@pytest.fixture
def mock_property_repository_get(mocker):
    """
    Creates a mock for the 'get' method of the property repository.
    It allows to simulate the retrieval of properties without real access to the database.
    :param mocker:
    :return:
    """
    return mocker.patch('app.repositories.property.PropertyRepository.get')


@pytest.fixture
def mock_property_repository_update(mocker):
    """
    Creates a mock for the 'update' method of the property repository.
    Useful to test the update logic without affecting the real database.
    :param mocker:
    :return:
    """
    return mocker.patch('app.repositories.property.PropertyRepository.update')


@pytest.fixture
def mock_property_image_repository_add_property_image(mocker):
    """
    Creates a mock for the 'add_property_image' method of the property image repository.
    Makes it easy to test the image addition logic without interacting with the database.
    :param mocker:
    :return:
    """
    return mocker.patch('app.repositories.property_image.PropertyImageRepository.add_property_image')


@pytest.fixture
def mock_property_service(mocker):
    """
    Creates a mock for the service properties.
    This allows to simulate the service logic in the tests, avoiding external dependencies.
    :param mocker:
    :return:
    """
    return mocker.patch('app.repositories.property.PropertyService')
