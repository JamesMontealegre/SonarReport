from dataclasses import dataclass


@dataclass
class AuthUser:
    user_id: int
    role: str
    permissions: list[str]

    def has_permission(self, permission: str) -> bool:
        return permission in self.permissions

    def has_permissions(self, permissions: list[str]) -> bool:
        return any(self.has_permission(permission) for permission in permissions)


@dataclass
class GenericResponseListEntity:
    count: int
    data: list[dict]


@dataclass
class GenericResponseEntity:
    data: dict