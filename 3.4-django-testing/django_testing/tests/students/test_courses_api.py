from django.urls import reverse
import pytest

from students.models import Course

def test_example():
    assert True, "Just test example"

# создание и получение 1ого курса
@pytest.mark.django_db
def test_detail_course(client, course_factory):
    course_factory(_quantity=1)
    course_item = Course.objects.first()
    url = reverse("courses-detail", args=(course_item.id, ))
    # url = 'http://127.0.0.1:8000/api/v1/courses/'
    response = client.get(url)
    print(response.data)
    assert response.status_code == 200
    assert response.data.get("id") == course_item.id
    assert response.data.get("name") == course_item.name

# получение списка курсов
@pytest.mark.django_db
def test_list_course(client, course_factory):
    course_factory(_quantity=10)
    url = reverse("courses-list")
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 10

# проверяем фильтрации списка курсов по id
@pytest.mark.django_db
def test_filter_course_id(client, course_factory):
    course_factory(_quantity=10)
    course_item = Course.objects.first()
    url = reverse("courses-list")
    filters = {"id": course_item.id}
    response = client.get(url, data=filters)
    print(response.data)
    assert response.status_code == 200
    assert response.data[0].get("id") == course_item.id

# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_filter_course_name(client, course_factory):
    course_factory(_quantity=10)
    course_item = Course.objects.first()
    url = reverse("courses-list")
    filters = {"name": course_item.name}
    response = client.get(url, data=filters)
    print(response.data)
    assert response.status_code == 200
    assert response.data[0].get("name") == course_item.name

# тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    new_item = {
        "name": "ABOBA",
        "students": []
    }
    url = reverse("courses-list")
    response = client.post(url, new_item)
    course_item = Course.objects.filter(id=response.data.get("id")).first()
    print(response.data)
    assert response.status_code == 201
    assert response.data.get("name") == new_item["name"]
    assert response.data.get("name") == course_item.name

# тест успешного обновления курса
@pytest.mark.django_db
def test_patch_course(client, course_factory):
    course_factory(_quantity=10)
    course_item = Course.objects.first()
    new_item = {
        "name": "ABOBA",
    }
    url = reverse("courses-detail", args=(course_item.id, ))
    response = client.patch(url, new_item)
    course_item = Course.objects.filter(id=course_item.id).first()
    print(response.data)
    assert response.status_code == 200
    assert response.data.get("name") == new_item["name"]
    assert response.data.get("name") == course_item.name


# тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course_factory(_quantity=10)
    course_item = Course.objects.first()
    url = reverse("courses-detail", args=(course_item.id, ))
    response = client.delete(url)
    course_item = Course.objects.filter(id=course_item.id).first()
    print(response.data)
    assert response.status_code == 204
    assert response.data is None
    assert course_item is None