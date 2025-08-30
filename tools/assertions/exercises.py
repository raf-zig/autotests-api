from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseSchema
from tools.assertions.base import assert_equal


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