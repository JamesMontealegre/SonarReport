from enum import Enum


class ExceptionsMessages(str, Enum):
    # User-related errors
    USER_NOT_REGISTERED = "User not registered."
    USER_NOT_AUTHORIZED = "User not authorized."
    USER_NOT_FOUND = "User not found."
    INVALID_PASSWORD = "Invalid password."

    # Token-related errors
    TOKEN_NOT_FOUND = "Token not found."
    ERROR_DECODING_TOKEN = "Error decoding token."

    # Resource-related errors
    RESOURCE_NOT_FOUND = "Resource not found."
    RESOURCE_EXISTS = "Resource already exists."

    # Parameter-related errors
    INVALID_PARAMETER = "Invalid parameter."

    # General errors
    ERROR = "Something went wrong. Please try again later."


class MarshmallowCustomValidationMessages(Enum):
    MISSING_DATA = "Missing {field}."
    INVALID_DATA = "Not a valid {field}."
    GENERIC_ERROR = "Error in {field}."