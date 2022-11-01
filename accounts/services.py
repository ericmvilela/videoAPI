import dataclasses
from typing import TYPE_CHECKING
from . import models
import datetime
import jwt
from django.conf import settings
from django.db.models.fields.files import ImageFieldFile

if TYPE_CHECKING:
    from .models import User


@dataclasses.dataclass
class UserDataClass():
    name: str
    email: str
    username: str = None
    birthdate: datetime.date = None
    password: str = None
    teacher: bool = False
    profilePic: ImageFieldFile = None
    id: int = None

    @classmethod
    def from_instance(cls, user: "User") -> "UserDataClass":
        return cls(
            name=user.name,
            email=user.email,
            username=user.username,
            teacher=user.teacher,
            birthdate=user.birthdate,
            profilePic=user.profilePic,
            id=user.id
        )


def create_user(user_dc: "UserDataClass") -> "UserDataClass":
    instance = models.User(
        name=user_dc.name,
        email=user_dc.email,
        username=user_dc.username,
        teacher=user_dc.teacher,
        birthdate=user_dc.birthdate,
        profilePic=user_dc.profilePic,
        id=user_dc.id
    )

    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()

    return UserDataClass.from_instance(instance)


def user_email_selector(email: str) -> "User":
    user = models.User.objects.filter(email=email).first()

    return user


def user_username_selector(username: str) -> "User":
    user = models.User.objects.filter(username=username).first()

    return user


def create_token(user_id: int) -> str:
    payload = dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(days=30),
        iat=datetime.datetime.utcnow()
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')

    return token
