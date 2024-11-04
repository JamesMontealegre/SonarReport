import os

JWT_ACCESS_TOKEN_EXPIRES = os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 900)
JWT_REFRESH_TOKEN_EXPIRES = os.getenv("JWT_REFRESH_TOKEN_EXPIRES", 2592000)
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret-key")
JWT_ACCESS_DELTA = os.getenv("JWT_ACCESS_DELTA", 1)
JWT_REFRESH_DELTA = os.getenv("JWT_REFRESH", 30)
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

if all([DATABASE_HOST, DATABASE_PORT, DATABASE_NAME, DATABASE_USER]):
    DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
else:
    DATABASE_URI = "sqlite:///local.db"

DISABLE_PERMISSIONS_VALIDATIONS = os.getenv("DISABLE_PERMISSIONS", "false").lower() == "true"
BACKEND_HOST = os.getenv("BACKEND_HOST", "localhost")
DAEMON_REQUEST_HEADER_VALUE = os.getenv("DAEMON_REQUEST_HEADER_VALUE")
