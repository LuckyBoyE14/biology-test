"""
В модуле определены все сущности БД

FILE: db/models.py
"""
from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.sqlite import BLOB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class ClassRoom(Base):
    """
    Таблица с названиями классов
    """
    __tablename__ = "classes"

    id: Mapped[int] = mapped_column(primary_key=True,
                                    comment="ID класса")
    name: Mapped[str] = mapped_column(String,
                                      comment="Название класса")

    users: Mapped[List["User"]] = relationship(
        back_populates="classroom", cascade="all, delete-orphan"
    )


class User(Base):
    """
    Таблица в которой хранятся данные пользователей, включая админов/учителей
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True,
                                    comment="ID пользователя")
    class_id: Mapped[Optional[int]] = mapped_column(ForeignKey("classes.id"),
                                                    comment="Класс ученика")
    name: Mapped[str] = mapped_column(String,
                                      comment="Имя пользователя")
    surname: Mapped[str] = mapped_column(String,
                                      comment="Фамилия пользователя")
    rating: Mapped[int] = mapped_column(default=0, comment="Рейтинг пользователя")
    password: Mapped[str] = mapped_column(String,
                                          comment="Пароль пользователя")

    is_admin: Mapped[bool] = mapped_column(
        default=False,
        comment="Является ли пользователь админом"
    )

    classroom: Mapped["ClassRoom"] = relationship(back_populates="users")

    def __repr__(self) -> str:
        return (
            f"User(id={self.id!r}, name={self.name!r}, "
            f"surnname={self.surname!r})"
        )


class Category(Base):
    """
    Таблица с наименованиями тем
    """
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True,
                                    comment="ID темы")
    name: Mapped[str] = mapped_column(String,
                                      comment="Наименование темы теста")
    image: Mapped[Optional[bytes]] = mapped_column(BLOB,
                                         comment="Иконка для кнопки")

    asks: Mapped[List["Ask"]] = relationship(
        back_populates="category", cascade="all, delete-orphan"
    )


class Ask(Base):
    """
    Таблица с вопросами
    """
    __tablename__ = "asks"

    id: Mapped[int] = mapped_column(primary_key=True,
                                    comment="ID вопроса")
    cat_id: Mapped[int] = mapped_column(ForeignKey("categories.id"),
                                        comment="Категория вопроса")
    text: Mapped[str] = mapped_column(String,
                                      comment="Текст вопроса")
    category: Mapped["Category"] = relationship(back_populates="asks")

    answers: Mapped[List["Answer"]] = relationship(
        back_populates="ask", cascade="all, delete-orphan"
    )


class Answer(Base):
    """
    Таблица с ответами
    """
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(primary_key=True,
                                    comment="ID ответа")
    ask_id: Mapped[int] = mapped_column(ForeignKey("asks.id"),
                                        comment="ID вопроса")
    text: Mapped[str] = mapped_column(String,
                                      comment="Текст ответа")
    is_true: Mapped[bool] = mapped_column(comment="Правильный ли ответ")

    ask: Mapped["Ask"] = relationship(back_populates="answers")
