# Garden Gnome: A Description

# IMPORTANT LINKS
- Other Repo [CLIENT REPO]()
- Deployed Client [DEPLOYED CLIENT]()
- Deployed API [DEPLOYED API]()
# PLANNING STORY

# ERD
![ERD](./img/GardenGnomeERD.jpeg)
# USER ROUTE PATHS AND METHODS
|HTTP METHOD |URL PATH        |RESULT           |ACTION |
|:-----------|:---------------|:----------------|-------|
|GET         | /sign-in       |get one user     |sign-in|
|POST        |/sign-up        |create user      |create |
|PATCH       |/change-password|update password  |update |
|DELETE      |/sign-out       |sign-out         |destroy |
# POST ROUTE PATHS AND METHODS
|HTTP METHOD |URL PATH        |RESULT           |ACTION |
|:-----------|:---------------|:----------------|-------|
|GET         |/posts-all      |list of all posts|index or list|
|GET         |/post/:id       |read single post |show |
|POST        |/create-post    |create post      |create |
|PATCH       |/update-post/:id|update post      |update |
|DELETE      |/post/:id       |delete post      |destroy |

# COMMENT ROUTE PATHS AND METHODS
|HTTP METHOD |URL PATH                |RESULT           |ACTION |
|:-----------|:-----------------------|:----------------|-------|
|POST        |/post/:id               |create comment   |create |
|PATCH       |/post/:postId/:commentId|update comment   |update |
|DELETE      |/post/:postId/:commentId|delete comment   |destroy |
# TECHNOLOGIES USED
- Python
- Django
- PostgresSQL
# UNSOLVED PROBLEMS

