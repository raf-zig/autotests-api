from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise (TypedDict):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнений.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа создания упражнения.
    """
    exercise: Exercise

class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа получения упражнения.
    """
    exercise: Exercise

class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа обновления упражнения.
    """
    exercise: Exercise

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения упражнений.
    """
    exercises: list[Exercise]


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнений.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Метод возвращает данные созданного упражнения.

        :param request: CreateExerciseRequestDict
        :return: данные созданного упражнения
        """
        response = self.create_exercise_api(request)
        return response.json()

    def get_exercises(self, request: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод возвращает  упражнения.

        :param request: GetExercisesQueryDict
        :return: все упражнения
        """
        response = self.get_exercises_api(request)
        return response.json()

    def get_exercise(self, query: str) -> GetExerciseResponseDict:
        """
        Метод возвращает упражнения определенного курса.

        :param query: id курса
        :return: упражнения курса
        """
        response = self.get_exercise_api(query)
        return response.json()

    def update_exercise(self, query: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод возвращает обновленное упражнение.

        :param query: id упражнения
        :param request: UpdateExerciseRequestDict
        :return: обновленное упражнение
        """
        response = self.update_exercise_api(query, request)
        return response.json()

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))