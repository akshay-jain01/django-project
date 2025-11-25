from .models import User

def create_user(data: dict) -> User:
    return User.objects.create(**data)

def update_user(user: User, data: dict) -> User:
    for field, value in data.items():
        setattr(user, field, value)
    user.save()
    return user

def delete_user(user: User) -> None:
    user.delete()
