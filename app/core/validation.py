
from fastapi import HTTPException

from app.core.config import settings


def validate_image_upload(image):
    """
    Validates an uploaded image based on its extension and size.

    This function checks if the file extension of the uploaded image is in the list of allowed file extensions,
    and if the file size does not exceed the maximum limit set. If any of these validations fail, an HTTPException exception is thrown with a
    HTTPException exception is thrown with an appropriate status code and detail message.

    Args:
        image: An uploaded image object, which includes the image file and associated metadata.

    Raises:
        HTTPException: thrown if the file extension is not allowed or if the file size exceeds the maximum limit.
    """
    allowed_extensions = settings.EXTENTIONS_FILE_LIST
    file_extension = image.filename.split(".")[-1].lower()
    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=400, detail=f"File extension '{file_extension}' is not allowed.")

    max_file_size = settings.MAX_FILE_SIZE_MG * 1024 * 1024  # MAX_FILE_SIZE_MG=5 ->5MB
    if len(image.file.read()) > max_file_size:
        raise HTTPException(status_code=413, detail="The image is too large.")

    image.file.seek(0)
