from bson import ObjectId


class PyObjectId(ObjectId):
    """
    Custom class that extends MongoDB ObjectId for use in Pydantic models.

    This class allows the validation and serialization of MongoDB ObjectId in Pydantic models,
    facilitating its use in input and output operations, especially in RESTful APIs.

    Methods:
        __get_validators__: class method that returns the validators of the class.
        validate(cls, v): Validates and converts an entry into a valid MongoDB ObjectId.
        __modify_schema__(cls, field_schema): Modifies the Pydantic schema for this type.
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("ObjectId no válido")
        # Devuelve el ObjectId como una cadena
        return str(ObjectId(v))

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
