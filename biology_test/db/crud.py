from json import loads
from typing import Any
from hashlib import md5

from PyQt5.QtCore import QBuffer, QByteArray, QFile, QIODevice
from PyQt5.QtGui import QPixmap

from sqlalchemy import Engine, select, update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker

from .models import (
    Base,
    Answer,
    Ask,
    Category,
    User,
    ClassRoom,
)
from biology_test.main_rc import *


class Interface:
    """
    В классе содержаться все функции для работы с БД, а также
    производится их первичное заполнение тестами исходя из требований ТЗ
    """

    def __init__(self, engine: Engine):
        self.__session_maker = Interface.__create_session_maker(engine)
        Base.metadata.create_all(engine)
        self.__fill_db()

    @staticmethod
    def __create_session_maker(engine: Engine):
        """
        Создание генератора сессий для подключения к БД
        """
        return sessionmaker(autocommit=False, autoflush=False,
                            expire_on_commit=False, bind=engine)

    def get_asks(self, category: str) -> list[dict[Any, Any]]:
        """
        Функция выдает список всех вопросов по теме
        """
        with self.__session_maker() as session:
            asks = session.execute(
                select(
                    Ask
                ).join(Category)
                .where(Category.name.is_(category))
            ).mappings().all()
            return [
                {
                    "text": ask["Ask"].text,
                    "answers": [
                        {
                            "text": answer.text,
                            "is_true": answer.is_true
                        } for answer in ask["Ask"].answers
                    ]
                } for ask in asks
            ]

    def get_categories(self):
        """
        Функция выдает список всех тем
        """
        with self.__session_maker() as session:
            cats = session.execute(
                select(Category.__table__.columns)
            ).mappings().all()
            return cats

    def get_classes(self) -> list[str]:
        with self.__session_maker() as session:
            classes = session.scalars(select(ClassRoom))
            classes = [classroom.name for classroom in classes]
        return classes

    def update_rating(self, score: int, name: str, surname: str):
        """
        Обновление данных для пользователя
        """
        with self.__session_maker() as session:
            query = (
                update(User)
                .where(User.name.is_(name))
                .where(User.surname.is_(surname))
                .values(rating=score)
            )
            session.execute(query)
            session.commit()

    def get_user(self, name: str, surname: str,
                 password: str, classroom: str) -> dict[Any, Any]:
        """
        Функция проверяет есть ли юзер, и возвращает данные по нему,
        если нет то создает. В случае не совпадения пароля
        вызывает ошибку
        """
        with self.__session_maker() as session:
            try:
                query = (
                    select(User.__table__.columns,
                           ClassRoom.name.label("classroom"))
                    .join(ClassRoom, isouter=True)
                    .where(User.name.is_(name))
                    .where(User.surname.is_(surname))
                )
                user = session.execute(query).mappings().one()
                if user["password"] != md5(password.encode()).hexdigest():
                    user = None
                    raise KeyError("Не правильный пароль пользователя")
                print("Найден пользователь:", user)
                return user # type: ignore
            except NoResultFound:
                print("Создание нового пользователя")
                user = self.__create_user(name, surname, password, classroom)
                return user

    def __create_user(self, name: str, surname: str,
                      password: str, classroom: str) -> dict[Any, Any]:
        """
        Функция отвечает за содание новых пользователей
        """
        with self.__session_maker() as session:
            user = User(
                name=name,
                surname=surname,
                password=md5(password.encode()).hexdigest(),
                classroom=self.__get_class(classroom),
            )
            session.add(user)
            session.commit()
            query = (
                select(User.__table__.columns,
                       ClassRoom.__table__.columns)
                .join(ClassRoom, isouter=True)
                .where(User.name.is_(name))
                .where(User.surname.is_(surname))
            )
            user = session.execute(query).mappings().one()
            return user # type: ignore

    def __get_class(self, classroom: str) -> ClassRoom | None:
        """
        Функция возвращает объект класса
        """
        with self.__session_maker() as session:
            try:
                query = (
                    select(ClassRoom)
                    .where(ClassRoom.name.is_(classroom))
                )
                res = session.execute(query).scalar_one()
                return res
            except NoResultFound:
                return None

    # Далее идут все функции для создания БД
    def __fill_db(self):
        """
        Функция вычисляет заполнена БД или нет, если нет, то заполняет ее
        """
        with self.__session_maker() as session:
            try:
                query = select(User).where(User.name.is_("admin"))
                user = session.execute(query).one()
                print("Администратор системы:", user)
            except NoResultFound:
                print("База данных не создана")
                self.__create_admin()

    def __create_admin(self):
        """
        Создание администратора
        """
        with self.__session_maker() as session:
            print("Создание администратора системы...")
            user = User(name="admin", surname="admin", class_id=None,
                        password=md5(b"admin").hexdigest(), is_admin=True)
            session.add(user)
            session.commit()
            print("Администратор создан:", user)
            self.__create_categories()

    @staticmethod
    def read_start_data() -> list[dict[Any, Any]]:
        """Считывание json файла из ресурсов"""
        file = QFile(":/tests/static/categories.json")
        data = []
        if file.open(QIODevice.ReadOnly): # type: ignore
            data = loads(file.readAll().data().decode())
        file.close()
        # считывание картинок
        for idx, cat in enumerate(data):
            data[idx]["image"] = Interface.image_to_bytes(cat["image"])
        return data # type: ignore

    @staticmethod
    def image_to_bytes(url: str) -> bytes:
        """
        Функция загружает изображение из файла ресурсов для загрузки
        его в БД
        """
        img = QPixmap(url)
        ba = QByteArray()
        buff = QBuffer(ba)
        buff.open(QIODevice.WriteOnly) # type: ignore
        img.save(buff, "PNG")
        return ba.data()

    def __create_categories(self):
        """
        Создание тем для тестирования
        """
        with self.__session_maker() as session:
            for cat in Interface.read_start_data():
                asks = Interface.__create_asks(cat["asks"])
                category = Category(name=cat["name"], image=cat["image"],
                                    asks=asks)
                session.add(category)
                session.commit()

    @staticmethod
    def __create_asks(asks: list[dict[Any, Any]]) -> list[Ask]:
        """
        Создание для категории
        """
        result = []
        for ask in asks:
            answers = Interface.__create_answers(ask["answers"])
            result.append(Ask(text=ask["text"], answers=answers))
        return result

    @staticmethod
    def __create_answers(answers: list[dict[Any, Any]]) -> list[Answer]:
        """
        Создание ответов для вопросов
        """
        result = []
        for answer in answers:
            result.append(Answer(**answer))
        return result
