from .models import User

def get_all_users():
    return User.objects.all()

def get_user_by_id(user_id: int):
    return User.objects.filter(id=user_id).first()
