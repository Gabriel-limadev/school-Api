## 📎 Technologies

Project was developed with the following technologies:
- [Django-Rest-Framework](https://www.django-rest-framework.org/)

## 📎 Acquired knowledge
- I used this project to improve my knowledge about routes, views and filters

This is a project developed with the team **[Alura](https://www.alura.com.br/)**

<hr>

<p align="center">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="#installing">Installing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#using-the-api">Using</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#routes">Routes</a>—↴————↴——————↴
  <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="#routes-to-students">Students</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#routes-to-courses">Courses</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#routes-to-registrations">Registrations</a>
  <br>
 
<div align="center">
  <a href="https://www.python.org/downloads/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/djangorestframework?color=%2300C86F">
  </a>
  <a href="https://www.django-rest-framework.org/#requirements">
    <img alt="PyPI - Django Version" src="https://img.shields.io/pypi/djversions/djangorestframework?color=%2300C86F">
  </a>
  <a href="https://github.com/luigiMinardi/alurachallenge-backend/blob/main/LICENSE">
    <img alt="GitHub license" src="https://img.shields.io/badge/license-MIT-%2300C86F">
  </a>
  <a href="https://pypi.org/project/djangorestframework/">
    <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/djangorestframework">
  </a>
</div>

# English

## Installing

* First, clone the repository::

  ```bash
  git clone https://github.com/Gabriel-limadev/school-Api
  ```

* Then create a [Virtual Enviroment](https://outline.com/HaJ3zA) for you:

  ```bash
  python -m venv venv
  ```
  
* Activate Your `venv`:

  Mac/Linux:
  ```bash
  source .venv/bin/activate 
  ```
  Windows:
  ```cmd
  venv/Scripts/activate.bat
  ```

* Install all the requirements:

  ```bash
  pip install -r requirements.txt
  ```

* Make the Migrations:

  ```bash
  python manage.py makemigrations
  ```

* Run the DataBase Migration:

  ```bash
  python manage.py migrate
  ```

* Create a Super User:
  ```bash
  python manage.py createsuperuser
  ```

* Run your server:

  ```bash
  python manage.py runserver
  ```

Now you are ready to use it.

# Using the API

## Routes

### Routes to Students

#### POST /students/
###### The response code must be `201`.

Add a new student in the database.

##### Request Body:

```json
{
    "name": "Alisson Lima",
    "rg": "113851728",
    "cpf": "89113223003",
    "date_birth": "1995-06-05"
}
```

##### Response Body:

```json
{
    "id": 2,
    "name": "Alisson Lima",
    "rg": "113851728",
    "cpf": "89113223003",
    "date_birth": "1995-06-05"
}
```

#### PUT /students/:id/
###### The response code must be `200`.

Change all values in specified student in the database.

##### Request Body:

> *Changing the video we've **POST** earlier, at url `/students/2/`*
```json
{
    "id": 2,
    "name": "Alisson Araujo",
    "rg": "125531448",
    "cpf": "42186305003",
    "date_birth": "1995-06-05"
}
```

#### GET /students/
###### The response code must be `200`.

Getting all the students of the database.

##### Response Body:

```json
[
    {
        "id": 1,
        "name": "Gabriel Lima",
        "rg": "588991983",
        "cpf": "50555075869",
        "date_birth": "2001-07-18"
    },
    {
        "id": 3,
        "name": "Jaqueline Araujo",
        "rg": "485178904",
        "cpf": "73180001011",
        "date_birth": "2006-03-15"
    }
]
```

#### /students/ Query Params

#### Search

You can search students using the query param `search`.

##### Example 1:

> *Searching for student name Gabriel.*

Searching "Gabriel" doing `/students/?search=Gabriel`

##### Return:

> *Returns all of the students that match in the search.*
```json
[
    {
        "id": 1,
        "name": "Gabriel Lima",
        "rg": "484127214",
        "cpf": "61831202000",
        "date_birth": "2001-07-18"
    }
]
```

##### Example 2:

> *Searching for student name Guilherme.*

Searching "Guilherme" doing `/students/?search=Guilherme`

##### Return:

> *Returns an empty list of students because we didn't have any student that match in the database.*
```json
[]
```

### Routes to Courses

#### POST /courses/
###### The response code must be `201`.

Add a new course in the database.

##### Request Body:

```json
{
    "course_code": "CJsAN",
    "description": "Course JavaScript Advanced",
    "level": "A"
}
```

##### Response Body:

```json
{
    "id": 2,
    "course_code": "CJsAN",
    "description": "Course JavaScript Advanced",
    "level": "A"
}
```

#### PUT /course/:id/
###### The response code must be `200`.

Change all values in specified course in the database.

##### Request Body:

> *Changing the course we've **POST** earlier, at url `/courses/2/`*
```json
{
    "id": 2,
    "course_code": "CPyAN",
    "description": "Course Python Advanced",
    "level": "A"
}
```

#### GET /courses/
###### The response code must be `200`.

Getting all the courses of the database.

##### Response Body:

```json
[
    {
        "id": 1,
        "course_code": "CPyMA",
        "description": "Python Morning Advanced",
        "level": "A"
    },
    {
        "id": 2,
        "course_code": "CPyAN",
        "description": "Course Python Advanced",
        "level": "A"
    }
]
```

#### /courses/ Query Params

#### Search

You can search courses using the query param `search`.

##### Example 1:

> *Searching for course name Python.*

Searching "Python" doing `/courses/?search=Python`

##### Return:

> *Returns all of the courses that match in the search.*
```json
[
    {
        "id": 1,
        "course_code": "CPyMA",
        "description": "Python Morning Advanced",
        "level": "A"
    },
    {
        "id": 2,
        "course_code": "CPyAN",
        "description": "Course Python Advanced",
        "level": "A"
    }
]
```

##### Example 2:

> *Searching for course name Java.*

Searching "Java" doing `/courses/?search=Java`

##### Return:

> *Returns an empty list of courses because we didn't have any course that match in the database.*
```json
[]
```

### Routes to Registrations

#### POST /registrations/
###### The response code must be `201`.

Add a new registration in the database.

##### Request Body:

```json
{
    "period": "N",
    "student": 1,
    "course": 2
}
```

##### Response Body:

```json
{
    "id": 3,
    "period": "N",
    "student": 1,
    "course": 2
}
```

#### PUT /registrations/:id/
###### The response code must be `200`.

Change all values in specified registratio in the database.

##### Request Body:

> *Changing the registration we've **POST** earlier, at url `/registrations/3/`*
```json
{
    "id": 3,
    "period": "M",
    "student": 1,
    "course": 1
}
```

#### GET /registrations/
###### The response code must be `200`.

Getting all the registrations of the database.

##### Response Body:

```json
[
    {
        "id": 1,
        "period": "A",
        "student": 1,
        "course": 1
    },
    {
        "id": 2,
        "period": "M",
        "student": 1,
        "course": 1
    },
    {
        "id": 3,
        "period": "M",
        "student": 1,
        "course": 1
    }
]
```

### Detailed routes

#### GET /students/:id/registration/
###### The response code must be `200`.

returns all courses in a student.

##### Response Body:

```json
[
    {
        "course": "Python Morning Advanced",
        "period": "Afternoon"
    }
]
```

#### GET /courses/:id/registration/
###### The response code must be `200`.

returns all students in a course.

##### Response Body:

```json
[
    {
        "student": "Gabriel Lima"
    },
    {
        "student": "Jaqueline Araujo"
    },
]
```
