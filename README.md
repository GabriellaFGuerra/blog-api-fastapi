# FastAPI Blog API

This is a simple blog API built with FastAPI and SQLAlchemy, using SQLite as the database. It allows you to perform CRUD operations on blog posts, including managing tags for each post.

## Features

- **Create, Read, Update, Delete (CRUD) operations for blog posts.**
- **Tagging system for posts (tags are stored as a comma-separated string in the database and handled as lists in the API).
**
- **Uses Pydantic for data validation and serialization.**
- **SQLite database for easy setup.**

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/GabriellaFGuerra/blog-api-fastapi.git
```

2. **Navigate to the project directory:**
```bash
cd blog-api-fastapi
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
## Running the Application

## Running the Application

1. **Start the FastAPI development server:**
```bash
uvicorn main:app --reload
```
2. **Access the API documentation:**

   - Open your browser and go to `http://127.0.0.1:8000/docs` to access the Swagger UI documentation.
   - You can also access the ReDoc documentation at `http://127.0.0.1:8000/redoc`.

## API Endpoints

- **GET `/`:** Get all posts.
- **POST `/post`:** Create a new post.
- **GET `/post/{id}`:** Get a post by ID.
- **PUT `/post/{id}`:** Update a post by ID.
- **DELETE `/post/{id}`:** Delete a post by ID.
- **GET `/posts/{tags}`:** Get posts by tag (comma-separated list of tags).

## Data Model

**Post:**

- `id` (int): Primary key
- `title` (str): Title of the post
- `content` (str): Content of the post
- `tags` (str): Comma-separated string of tags
- `created_at`
 (datetime): Timestamp of post creation
- `updated_at` (datetime): Timestamp of last update

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
