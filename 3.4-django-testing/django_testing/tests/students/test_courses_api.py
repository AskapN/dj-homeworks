import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


URL = "/api/v1/courses/"

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    course = course_factory(_quantity=1)
    course_id = course[0].id
    response = client.get(f'{URL}{course_id}/')
    data = response.json()
    assert response.status_code == 200
    assert data['name'] == course[0].name

@pytest.mark.django_db
def test_get_all_courses(client, course_factory):
    course = course_factory(_quantity=10)
    response = client.get(URL)
    data = response.json()
    assert response.status_code == 200
    assert len(data) == len(course)
    for idx, c in enumerate(data):
        assert c['name'] == course[idx].name

@pytest.mark.django_db
def test_filter_courses(client, course_factory):
    i = 3
    course = course_factory(_quantity=10)
    response = client.get(URL, {'id': course[i].id, 'name': course[i].name})
    assert response.status_code == 200
    assert course[i].id == response.json()[0]['id']
    assert course[i].name == response.json()[0]['name']

@pytest.mark.django_db
def test_post_course(client, course_factory):
    count = Course.objects.count()
    name = "test_course"
    response = client.post(URL, data = {'name': name})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1

@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.patch(f'{URL}{course[0].id}/', data = {'name': course[0].name})
    assert response.status_code == 200

@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.delete(f'{URL}{course[0].id}/')
    response2 = client.get(f'{URL}{course[0].id}/')
    assert response.status_code == 204
    assert response2.status_code == 404
