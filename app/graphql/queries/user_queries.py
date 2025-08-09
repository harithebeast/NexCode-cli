import strawberry
from typing import List
from sqlalchemy.orm import Session
from app.models.user import User
from app.graphql.types.user_type import UserType
from app.database.db_session import get_db

@strawberry.type
class Query:
    @strawberry.field
    def users(self, info) -> List[UserType]:
        db: Session = next(get_db())
        users = db.query(User).all()
        return [UserType(id=user.id, username=user.username, email=user.email) for user in users]
