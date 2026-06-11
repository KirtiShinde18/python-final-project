# Flask Blog API

A simple Blog Management API built with Flask and JSON file storage. This project demonstrates basic CRUD operations using Flask routes and a local JSON database.

<p align="center">
  <img 
    src="/hero.png" 
    width="90%" 
    style="border-radius:15px; overflow:hidden;"
  />
</p>

## Features

* View all blog posts
* Create a new blog post
* Delete an existing blog post
* Store blog data in a local JSON file (`db.json`)
* Simple Flask backend

## Project Structure

```text
project/
│
├── app.py
├── db.json
├── templates/
│   └── index.html
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-blog-api.git
cd flask-blog-api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

#### Mac/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install flask
```

## Running the Application

```bash
python app.py
```

The server will start at:

```text
http://127.0.0.1:5000
```

## API Endpoints

### Get All Posts

**GET**

```http
GET /posts
```

Response:

```json
[
  {
    "id": 1,
    "title": "My First Blog",
    "desc": "Blog description",
    "hero": "image-url"
  }
]
```

---

### Create New Post

**POST**

```http
POST /posts
```

Request Body:

```json
{
  "title": "My Blog",
  "desc": "Blog description",
  "hero": "image-url"
}
```

Response:

```json
{
  "message": "Blog created successfully"
}
```

---

### Delete Post

**DELETE**

```http
DELETE /posts/1
```

Response:

```json
{
  "message": "Blog remove successfully"
}
```

## Database Format

The application uses a local JSON file (`db.json`) for storage.

Example:

```json
{
  "posts": []
}
```

## Technologies Used

* Python
* Flask
* JSON
* HTML

## Future Improvements

* Update blog posts
* Search functionality
* SQLite database integration
* User authentication
* RESTful API validation

## Author

Kirti Shinde

Built with Flask 🚀
