# TP-market
# Electronics Marketplace

A modern e-commerce platform focused on mobile phones, PCs, and tablets. Built with Django (REST API) and Next.js (TypeScript), this project demonstrates a full-stack marketplace with admin product management and user product browsing/filtering.

## Features

- User registration and login (email-based)
- Browse products by name, type (mobile, PC, tablet), and price range
- Product detail pages with images and specifications
- Admin panel for uploading/editing products and images
- Secure JWT authentication
- Responsive, modern UI

## Tech Stack

- **Backend:** Django, Django REST Framework, PostgreSQL, SimpleJWT
- **Frontend:** Next.js, TypeScript, Tailwind CSS, React Query
- **Deployment:** Render/Railway (backend), Vercel/Netlify (frontend)

## Getting Started

### Backend
1. Clone the repo and navigate to `backend/`
2. Create a virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Set up PostgreSQL and configure environment variables
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Start the server: `python manage.py runserver`

### Frontend
1. Navigate to `frontend/`
2. Install dependencies: `npm install`
3. Create a `.env.local` file with the backend API URL
4. Start the dev server: `npm run dev`

## Folder Structure

```
repo-root/
├── backend/   # Django API
└── frontend/  # Next.js app
```

## Contribution Guidelines
- Fork the repo and create a feature branch
- Commit your changes with clear messages
- Open a pull request for review

## License
This project is licensed under the MIT License. 
