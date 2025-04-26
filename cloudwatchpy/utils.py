import uuid
import os
from typing import Optional

def generate_request_id() -> str:
    """Generate a unique request ID for tracing."""
    return str(uuid.uuid4())

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Read environment variable with fallback default."""
    return os.getenv(key, default)

def get_client_ip(headers: dict, fallback_ip: Optional[str] = None) -> Optional[str]:
    """Extract real client IP from headers (used in proxies, middlewares)."""
    x_forwarded_for = headers.get("x-forwarded-for")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()
    return fallback_ip
