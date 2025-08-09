import strawberry
from sqlalchemy.orm import Session
from app.models.user import User
from app.database.db_session import get_db
from app.graphql.types.user_type import UserType

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, info, username: str, email: str) -> UserType:
        db: Session = next(get_db())
        user = User(username=username, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return UserType(id=user.id, username=user.username, email=user.email)
