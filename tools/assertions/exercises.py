from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseSchema, GetExerciseResponseSchema, \
    CreateExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_internal_error_response


def assert_create_exercise_response(
    create_exercise_request: CreateExerciseRequestSchema,
    create_exercise_response: ExerciseSchema
    ):
    """
            Проверяет, что ответ на создание задания соответствует запросу на его создание.

            :param create_exercise_request: Запрос на создание задания.
            :param create_exercise_response: Ответ на создание задания.

        """
    assert_equal(create_exercise_request.title, create_exercise_response.title, "title")
    assert_equal(create_exercise_request.max_score, create_exercise_response.max_score, "max_score")
    assert_equal(create_exercise_request.min_score, create_exercise_response.min_score, "min_score")
    assert_equal(create_exercise_request.description, create_exercise_response.description, "description")
    assert_equal(create_exercise_request.estimated_time, create_exercise_response.estimated_time, "estimated_time")
    assert_equal(create_exercise_request.course_id, create_exercise_response.course_id, "course_id")
    assert_equal(create_exercise_request.order_index, create_exercise_response.order_index, "order_index")

def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
        Проверяет, что фактические данные задания соответствуют ожидаемым.

        :param actual: Фактические данные задания.
        :param expected: Ожидаемые данные задания.
        :raises AssertionError: Если хотя бы одно поле не совпадает.
        """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.order_index, expected.order_index, "order_index")

def assert_get_exercise_response(get_exercise_response: GetExerciseResponseSchema, create_exercise_response: CreateExerciseResponseSchema):
    """
        Проверяет, что данные задания при создании (create) и при запросе (get) совпадают.
        :param get_exercise_response: Ответ API при получении задания.
        :param create_exercise_response: Ответ API при создании задания.

    """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)

def assert_update_exercise_response(
        request: UpdateExerciseRequestSchema,
        response: UpdateExerciseResponseSchema):
    """
        Проверяет, что ответ на обновление задания соответствует данным из запроса.

        :param request: Исходный запрос на обновление задания.
        :param response: Ответ API с обновленными данными задания.
        :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")

def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(details='Exercise not found')
    assert_internal_error_response(actual, expected)