from app.db.repositories import UserRepository
from app.schemas.user import UserResponse,UserRequest,UserUpdate

class UserService:
    def __init__(self):
        self.repo = UserRepository()
    
    def get_user_by_username(self,username:str) -> UserResponse:
        user_db = self.repo.get_user_by_username(username=username)
        if not user_db:
            return None
        user_response = UserResponse(
            id=str(user_db.id),
            username=user_db.username,
            email=user_db.email,
            rol=user_db.rol
        )
        return user_response
    
    def create_user(self,user_request: UserRequest) -> UserResponse | None:
        user = self.repo.create_user(user_request=user_request)
        
        if not user:
            return None
        
        user.id = str(user.id)
        return UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            rol=user.rol
        )
    
    def update_user(self,user_update: UserUpdate, username: str):
        username = username.upper()
        user = self.repo.update_user(user_update=user_update,username=username)
        
        if not user:
            return None
        
        user.id = str(user.id)
        return UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            rol=user.rol
        )
        
    def delete_user(self,username: str) -> bool:
        username = username.upper()
        
        user_deleted = self.repo.delete_user(username=username)
        
        if not user_deleted:
            return None
        
        return True
