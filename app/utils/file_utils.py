from fastapi import HTTPException
from shutil import copyfileobj


def save_image(image, file_path):
    """
    Save an uploaded image file to a specified path on the server.

    This function takes an uploaded image object and a file path as input.
    The image is written to the file in the specified path. If an input/output
    error occurs during this process, an HTTPException with status code 500 is thrown, indicating an
    status code 500, indicating a server error.

    Parameters:
    image (UploadFile): a FastAPI UploadFile object representing the uploaded image.
    file_path (str): The path to the file where the image will be saved.

    Raises:
    HTTPException: An HTTP exception with status code 500 is thrown if an I/O error occurs.

    Returns:
    None: The function does not return any value. The image is saved in the specified path.

    """
    try:
        with open(file_path, "wb") as buffer:
            copyfileobj(image.file, buffer)
    except IOError as e:
        raise HTTPException(status_code=500, detail=f"Error saving image: {e}")
