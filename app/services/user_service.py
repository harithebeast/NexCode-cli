from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def get_user(self, user_id: int):
        return self.user_repo.get_user_by_id(user_id)
