"""AdminUser model for admin management service."""
from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from cloudsound_shared.models.base import Base, UUIDMixin, TimestampMixin


class AdminUser(Base, UUIDMixin, TimestampMixin):
    """Represents an administrator account."""

    __tablename__ = "admin_users"

    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(255), nullable=True)
    role = Column(String(50), nullable=False, default="admin")
    tenant_id = Column(UUID(as_uuid=True), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)

    def __repr__(self) -> str:
        return f"<AdminUser(id={self.id}, email='{self.email}', role='{self.role}')>"

