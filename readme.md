# 9AI Python Developer Intern Assignment

Name: Chinmay Amrutkar
Email: chinmayaons1@gmail.com / chinmayma21@iitk.ac.in

### Build Instructions:

- Download the zip file from github
- Unzip the file to local system
- Run the command 'fastapi dev main.py'

### Data Model:

The blog posts use the following schema:

- \_id: BSON object
- blog: String
- likes: Integer
- comments: [String]

### Api End Points:

Note that all endpoints require data to be given in the request query, description of each parameter is given below for all endpoints

- GET /api/post:

  - id: String

- POST /api/post:

  - blog: String

- PUT /api/post:

  - id: String
  - blog: String

- DELETE /api/post

  - id: String

- POST /api/post/like

  - id: String

- POST /api/post/dislike

  - id: String

- POST /api/post/comment

  - id: String
  - comment: String
