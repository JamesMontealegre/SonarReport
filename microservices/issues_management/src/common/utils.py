# app/utils.py
from flask_jwt_extended import get_jwt
from src.common.enums import ExceptionsMessages
from src.common.exceptions import CustomException
from src.common.logger import logger
from src.models.entities import AuthUser


def format_exception_message(exception: Exception) -> str:
    cause = str(exception.__cause__) if exception.__cause__ else str(exception)

    if "DETAIL:" in cause:
        detail_message = cause.split("DETAIL:")[-1].strip()
        return detail_message.replace("\n", " ").capitalize()

    return cause


def decode_token(user_id: int) -> AuthUser:
    claims = get_jwt()
    role = claims.get("role")
    permissions = claims.get("permissions")
    if not role or not permissions:
        logger.error(ExceptionsMessages.ERROR_DECODING_TOKEN.value)
        raise CustomException(ExceptionsMessages.ERROR_DECODING_TOKEN.value)
    return AuthUser(user_id=user_id, role=role, permissions=permissions)
