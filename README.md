# Thoughts Project API

A Django REST Framework API that serves as a learning management system with integration to Project Gutenberg's digital library.

## Features

- **User Management**: Custom user model with roles and profiles
- **Course Management**: Create and manage courses with readings and assignments
- **Reading Integration**: 
  - Direct integration with Project Gutenberg's library via Gutendex API
  - Search Gutenberg books
  - Fetch book details and content
- **Social Features**:
  - Like system for entries
  - Share functionality
  - Tag system for organizing content
- **Privacy Controls**: Private/public entry management

## API Endpoints

### Gutenberg Integration
```http
GET /api/gutenberg/books/{gutenberg_id}/   # Get specific book details
GET /api/gutenberg/search?q={query}        # Search Gutenberg library
GET /api/gutenberg/text?url={text_url}     # Fetch book content
```

### Authentication
```http
POST /api/login/                # Login user
POST /api/register/            # Register new user
GET /api/profile/              # Get user profile
```

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd thoughtsproject
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python3 manage.py migrate
```

5. Load initial data:
```bash
./seed_database.sh
```

6. Start the development server:
```bash
python3 manage.py runserver
```

## Technology Stack

- Django
- Django REST Framework
- SQLite (Development)
- Requests library for API integration
- Project Gutenberg (via Gutendex API)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your license here]