# FSND Capstone API Backend

Final Project for the Udacity Fullstack Nanodegree

## Casting Agency

### Overview

This project consists of a Casting Agency App. The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process. The goal of this project is to practice and get a better insight of how full stack delevoping is.

### Motivation for project

This project sums up all the effort made during this Nanodregree where I learned many different technologies and the basics of how FE and BE interact with each other. I believe this project is the stepping stone that will allow me to dive into the deepths of the web development world and I'm really exited to get this jorney started as a Full Stack Developer. The project itself will definetly have a lot of potential improvements, but that's what developing means for me, always having room for making things better, more efficient and simpler.

### Installing Dependencies

#### Python 3.8.3

Follow instructions to install the version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

It's good practise to work within a virtual environment whenever using Python. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

```
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we use to handle cross origin requests from the frontend server.

## Database Setup

Create a new database in Postgress:

```
createdb capstone
```

With Postgres running, restore the database

```
psql capstone < Capstone_data.sql
```

## Running the server locally

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```
source setup.sh
```

## Testing

To run the tests, run:

```
dropdb test_app && createdb test_app
psql test_app < Capstone_data.sql
python3 test_app.py
```

#### RBAC

Each endpoint is access controlled using Auth0's Role Based Access Control
(RBAC), with the exception of one publicly accessible endpoint. Specifics on
each role and the permissions granted to each are below this file

## Live server can be found in

> Base URL `https://capstonea.herokuapp.com/`

## API Reference

### Getting Started

1. Base URL : Backend app is hosted on https://capstonea.herokuapp.com/
2. Authentication : Role based authentication using AUTH0

### Error Handling

Errors are returned as JSON objects in the following format:

```json
{
  "success": False,
  "error": 404,
  "message": "Resource Not Found"
}
```

The API will return these error types when requests fail:

- 400: bad request
- 404: Resource not found
- 422: unprocessable
- 500: Internal Server Error

If the route requires authentification and the request fails, it will return:

- 401: "authorization_header_missing"
- 400: "invalid_claims"
- 403: "unauthorized"

### Roles and Permissions

## Permissions

| Permissions   | Details                       |
| ------------- | ----------------------------- |
| get:movies    | Gets access to all movies     |
| get:actors    | Gets access to all actors     |
| post:actors   | Can add actors to the DB      |
| post:movies   | Can add movies to the DB      |
| delete:actors | Can delete actors from the DB |
| delete:movies | Can delete movies from the DB |
| patch:actors  | Can modify actors from the DB |
| patch:movies  | Can modify movies from the DB |

## Roles

| Role               | Permissions                                                                                         |
| ------------------ | --------------------------------------------------------------------------------------------------- |
| Casting Assistant  | get:movies get:actors                                                                               |
| Casting Director   | get:movies get:actors post:actors delete:actors patch:actors patch:movies                           |
| Executive producer | get:movies get:actors post:actors post:movies delete:actors delete:movies patch:actors patch:movies |

### Endpoints

#### GET /

No authentication required. This is to check if the APP is up and running.

```json
{
  "Message": "'Hi There",
  "success": true
}
```

#### GET /actors (Auth required)

Returns details of all actors.

Sample output:

```json
{
  "actors": [
    { "age": 54, "gender": "male", "id": 7, "name": "Otilio" },
    { "age": 45, "gender": "male", "id": 9, "name": "pepe Gotera" }
  ],
  "status": true
}
```

#### GET /actors/<actor_id> (Auth required)

Returns actor details for the given id.

Sample output:

```json
{
  "actors": {
    "age": 25,
    "gender": "female",
    "id": 1,
    "name": "Dany"
  },
  "success": true
}
```

#### GET /movies (Auth required)

Returns details of all movies.

Sample output:

```json
{"movies": [{ "actor_id": 4, "id": 13, "release date": "Wed, 25 Dec 2020 22:55:56 GMT", "title": "random title" }, {"actor_id": 1, "id": 8, "release date": "Thu, 25 Mar 2021 11:55:11 GMT", "title": avengers vs godzilla" }],"status": true }
```

#### GET /movies/<movie_id> (Auth required)

Returns movies details for the given id.

Sample output:

```json
{
  "movies": {
    "id": 1,
    "releasedate": "20-07-2015",
    "title": "Frozen"
  },
  "success": true
}
```

#### POST /actors (Auth required)

Add a new actor.

Sample input:

```json
{
  "name": "John",
  "age": "26",
  "gender": "male"
}
```

#### POST /movies (Auth required)

Add a new movie.

Sample input:

```json
{
  "title": "Toy Story",
  "releasedate": "20-07-2015"
}
```

#### PATCH /actors/<actor_id> (Auth required)

Update the existing actor.

Sample input:

```json
{
  "name": "Dany",
  "age": "25"
}
```

#### PATCH /movies/<movie_id> (Auth required)

Update the existing movie.

Sample Input:

```json
{
  "title": "Frozen"
}
```

#### DELETE /actors/<actor_id> (Auth required)

Delete the existing actor.

Sample Output:

```json
{
  "deleted_actor_id": 35,
  "message": "Actor successfully deleted!",
  "success": true
}
```

#### DELETE /movies/<movie_id> (Auth required)

Delete the existing movie.

Sample Output:

```json
{
  "deleted_movie_id": 34,
  "message": "Movie successfully deleted!",
  "success": true
}
```

### AUTHORS

Ahmad Alsobhi

## Acknowledgements

I want to thank Udacity for providing the framework and guidelines for this great project.

## Test tokens:

#### Casting assistant

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBLRFh0NUVXY3l1aGxVcm9jZkR3TiJ9.eyJpc3MiOiJodHRwczovL2FobWFkMC5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDkzMzI5MDA5ODI1MzU5NzcwNjYiLCJhdWQiOlsiY2Fwc3RvbmUiLCJodHRwczovL2FobWFkMC5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk3MTE4MzkzLCJleHAiOjE1OTcxMjU1OTMsImF6cCI6Impjd1NOSzB0aVdTOWJ0WTAxblRHWnZzTTFydnBSMWc0Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.kmQe8VfcJXmcXn-gkwjyjTfFufT5oHeetyEy2YvlKRvU-4qEoyU7i3uOjCc1iWcU95r9B-JOynqcjzD4frXT4kNu8Xr4nmh7fInKo2klI2wC7JN_oIyLTvc8M2kgHlMl63DYW7vP76R3pBbwctAb9AlhsKQlwgomPQV4Hcf2UKiJogN36hkmRIM75qf-FFvFk_NOJlYf1C1USkdhL1Yjswsoa3o_oSnzuv301rC_gs0xjWJyd_II0CwBbV8OK427SQr2MFxe85avQTI1puL1BND0JWrcRWWcZLasRBEpLfJFvM3baXVl-ghg14QRjYa9J1mvQoKwYuzFILZ51Ufw_g`

#### Casting director

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBLRFh0NUVXY3l1aGxVcm9jZkR3TiJ9.eyJpc3MiOiJodHRwczovL2FobWFkMC5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTU5MDE2Nzc0Mjk1OTkxODI0OTMiLCJhdWQiOlsiY2Fwc3RvbmUiLCJodHRwczovL2FobWFkMC5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk3MTIwNDgyLCJleHAiOjE1OTcxMjc2ODIsImF6cCI6Impjd1NOSzB0aVdTOWJ0WTAxblRHWnZzTTFydnBSMWc0Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.aWvx8LRde4JdknPML5uISNdRaxSgBcGygGZbVsaVE-WvkxcMhJmbNfYtz5YU1GB6iJGsC1XFY3wA7hAyHq5-rlTRjvPcCKa4ZYwisT2B-_03nGm1TPtZkpogzySIpbDZZKUv6F6l2LDtJlKDiPjmqOgU9TUqOWJv9_0lXz1mVwEACDHvmI-OoOlkR3r9a3mXanr4-Wv2gp71nVA0oop31HJLd5LEz6YbcLk87Mi1W7RrtEEjHz5niy7DVfk5fSOmOlSM6mhx6phptm0l0EFCGqPe1JjwIJpsNv3gKvSg6Xnt7P1Kc_W8GCQBMv_CvgG2eo_uPzeOhteFe_MM1vJ91g`

#### Executive producer

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBLRFh0NUVXY3l1aGxVcm9jZkR3TiJ9.eyJpc3MiOiJodHRwczovL2FobWFkMC5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDE3ODQzNDAxMDEzMzIzMjczNjMiLCJhdWQiOlsiY2Fwc3RvbmUiLCJodHRwczovL2FobWFkMC5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk3MTIwNzM5LCJleHAiOjE1OTcxMjc5MzksImF6cCI6Impjd1NOSzB0aVdTOWJ0WTAxblRHWnZzTTFydnBSMWc0Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.EwjJsFrMdLLbPX2gTfZK0MiXLyGJcIyfi2lPhVc2KWWaJU4vY9d-pOTQEivTMbhXJGWbN6U5wxegTxH7IjKtRhjKzwp0cXWh_0c_Sa_ID9U4YiRVmahp1IAsYbfD4tNn2vHIoKZ6vNjqPkVIGovdd5JcKlkRygejAsgcMvxvHzKcjzhDyWiTWliVQfmrywMvHdG4aLU9u413C5ERgYGtnGrJv1yUd2FYsN-MOKe2pmfZkOY5n2sjk8jO6ll7uw7UIdsEsHOHc1HKYnC6v5j1V30OYjIWlq4mYBquit6XOJocO_7g-eAfzHJ9N_B5tWav7nOp27EjBx-olHjVWS4K-Q`
