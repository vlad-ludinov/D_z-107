import pytest
from main import Student


class TestStudent:

    @pytest.fixture
    def student(self):
        return Student("Иван Иванов", "subjects.csv")

    def test_create_student_name_not_str(self):
        with pytest.raises(TypeError):
            Student(123, "subjects.csv")

    def test_create_student_name_is_alpha(self):
        with pytest.raises(ValueError):
            Student("Иван123 Иванов", "subjects.csv")

    def test_create_student_name_is_upper(self):
        with pytest.raises(ValueError):
            Student("иван иванов", "subjects.csv")

    def test_full_name(self, student):
        assert student.name == "Иван Иванов"

    def test_add_grade(self, student):
        student.add_grade("Математика", 4)
        assert student.subjects.get("Математика").get("grade") == 4

    def test_add_grade_no_subject(self, student):
        with pytest.raises(ValueError):
            student.add_grade("Философия", 4)

    def test_add_grade_not_int(self, student):
        with pytest.raises(TypeError):
            student.add_grade("Математика", "4")

    def test_add_grade_out_range(self, student):
        with pytest.raises(ValueError):
            student.add_grade("Математика", 6)

    def test_get_average_grade(self, student):
        student.add_grade("История", 5)
        student.add_grade("Математика", 4)
        assert student.get_average_grade() == 4.5

    def test_add_test_score_no_subject(self, student):
        with pytest.raises(ValueError):
            student.add_test_score("Философия", 60)

    def test_add_test_score_not_int(self, student):
        with pytest.raises(TypeError):
            student.add_test_score("Математика", "60")

    def test_add_test_score_out_range(self, student):
        with pytest.raises(ValueError):
            student.add_test_score("Математика", 102)

    def test_get_average_test_score(self, student):
        student.add_test_score("История", 60)
        student.add_test_score("История", 90)
        assert student.get_average_test_score("История") == 75.0

    def test_str(self, student):
        student.add_grade("История", 4)
        student.add_grade("Математика", 5)
        assert student.__str__() == "Студент: Иван Иванов\nПредметы: Математика, История"
