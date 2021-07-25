from typing import Optional, Any, Dict
from fastapi import HTTPException


class InvalidDateError(HTTPException):

    status_code: int = 400
    headers: Optional[Dict[str, Any]] = {}

    def __init__(self, detail: Any) -> None:
        super().__init__(self.status_code, detail=detail, headers=self.headers)


class ActivityNotFound(HTTPException):

    status_code: int = 404
    headers: Optional[Dict[str, Any]] = {}

    def __init__(self, detail: Any) -> None:
        super().__init__(self.status_code, detail=detail, headers=self.headers)
