from http import HTTPStatus
from io import BytesIO
from unittest import mock

from starlette.datastructures import UploadFile

from app.models.py_object_id import PyObjectId


class TestPropertyCreation:
    def test_create_property_success(self, test_client, property_create_data, property_data_with_id, mock_property_repository_create):
        """
           Tests successful creation of a property.
           - The insertion into the database is simulated, and it is verified that the endpoint response is successful
            (HTTP status code 200).
           - Checks that the returned data matches the sent data.
         """

        # SetUp
        mock_property_repository_create.return_value = property_data_with_id

        # Action
        response = test_client.post("/api/v1/property/create-property/", json=property_create_data)

        # Assertion
        assert response.status_code == HTTPStatus.OK
        for key in property_create_data:
            assert response.json()[key] == property_create_data[key]

    def test_create_property_invalid_input(self, test_client, property_data):
        """
            Verifies the system's response to invalid input when creating a property.
            - An incomplete or invalid data dictionary is passed.
            - The server response is expected to be an error (HTTP status code 422).
            - Checks if the response contains specific error messages for the missing or incorrect fields.
        """

        # SetUp
        property_in_data = property_data

        # Action
        response = test_client.post("/api/v1/property/create-property/", json=property_in_data)

        # Assertion
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
        errors = response.json().get('detail', [])
        assert any("name" in error.get('loc', []) for error in errors)

    def test_change_price_to_property_success(
            self, test_client, property_data_with_id, mock_property_repository_get, mock_property_repository_update
    ):
        """
            Tests the price change of an existing property.
            - An existing property is simulated, and its price is changed.
        """

        # SetUp
        price_in = 3500.0
        mock_property_repository_get.return_value = property_data_with_id
        mock_property_repository_update.return_value = {**property_data_with_id, "price": price_in}

        # Action
        response = test_client.put(f"/api/v1/property/change-price/{property_data_with_id['id']}?price_in={price_in}")

        # Assertion
        assert response.status_code == HTTPStatus.OK
        assert response.json()["price"] == price_in

    def test_change_price_to_property_not_found(self, test_client, mock_property_repository_get):
        """
            Tests price change for a property that does not exist.
            - An attempt is made to change the price of a nonexistent property.
        """

        # SetUp
        non_existent_property_id = PyObjectId()
        price_in = 3500.0
        mock_property_repository_get.return_value = None

        # Action
        response = test_client.put(f"/api/v1/property/change-price/{non_existent_property_id}?price_in={price_in}")

        # Assertion
        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
        assert "Property not found" in response.json().get("detail", "")

    def test_upload_image_to_property_success(
            self, test_client, property_data_with_id, image_data_with_id, mock_property_repository_get, mock_property_image_repository_add_property_image
    ):
        """
            Tests successful upload of an image to an existing property.
            - An existing property is simulated, and an image is uploaded for it.
            - Verifies that the file storage function is called correctly and that the endpoint response is successful (HTTP status code 200).
            - Checks that the response data matches the uploaded image data.
        """

        # SetUp
        file_name = image_data_with_id['file'].split('/')[-1]
        existing_image_data = image_data_with_id
        # Simular una imagen como un archivo en memoria
        image_content = BytesIO(b"fake image data")
        image = UploadFile(filename=file_name, content_type="image/jpeg", file=image_content)
        mock_property_repository_get.return_value = property_data_with_id
        mock_property_image_repository_add_property_image.return_value = image_data_with_id

        # Action
        with mock.patch('builtins.open', mock.mock_open()) as mocked_file:
            response = test_client.post(
                f"/api/v1/property/properties/{property_data_with_id['id']}/upload-image/",
                files={"image": (image.filename, image_content, image.content_type)}
            )

            # Assertion
            assert response.status_code == HTTPStatus.OK
            # Asegurarse de que la función open fue llamada para guardar la imagen
            file_path_call_arg = mocked_file.call_args[0][0]
            assert file_path_call_arg.startswith("app/images/")
            assert file_path_call_arg.endswith("-test_image.jpg")
            assert "wb" == mocked_file.call_args[0][1]

            response_data = response.json()
            assert response_data["_id"] == str(image_data_with_id["_id"])
            assert response_data["id_property"] == str(image_data_with_id["id_property"])
            assert response_data["file"] == image_data_with_id["file"]
            assert response_data["enable"] == image_data_with_id["enable"]

        image_content.close()

    def test_upload_image_to_property_unsuccess_property_not_found(self, test_client, mock_property_repository_get):
        """
            Tests uploading an image to a non-existent property.
            - Attempts to upload an image for a property that does not exist.
            - Verifies that the file storage function is not called and that the endpoint response indicates an error (HTTP status code 404).
        """

        # SetUp
        property_id = PyObjectId()
        # Simular una imagen como un archivo en memoria
        file_name = "test_image.jpg"
        image_content = BytesIO(b"fake image data")
        image = UploadFile(filename=file_name, content_type="image/jpeg", file=image_content)
        mock_property_repository_get.return_value = None

        # Action
        with mock.patch('builtins.open', mock.mock_open()) as mocked_file:
            response = test_client.post(
                f"/api/v1/property/properties/{property_id}/upload-image/",
                files={"image": (image.filename, image_content, image.content_type)}
            )

            # Assertion
            assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
            mocked_file.assert_not_called()

        image_content.close()
