# Online Selling Portal (Team Acraiders)

A Django-based online marketplace where users can register as customers, list products, negotiate with buyers, manage requests/orders, and track deliveries.

## Video Demo
- [Watch the demo video](https://drive.google.com/file/d/1V4zVgM_VplvDZ85e0qP1BjyR3E91XWWR/view?usp=sharing)

## Project Overview
This project implements an end-to-end selling portal with:
- Custom email-based authentication.
- Product listing with category support and multiple images.
- Cart and checkout flow.
- Buyer/seller request negotiation (with chat-like messaging).
- Order and delivery tracking.
- Profile/address management.

## Tech Stack
- **Backend:** Django
- **Database:** SQLite (default in development)
- **Frontend:** Django Templates + static CSS/JS
- **Python libraries:** crispy forms, phone number handling, dotenv, Pillow, etc.

## Repository Structure
```text
online-selling-portal-team-acraiders/
├── ecom/
│   ├── ecom/                  # Django project settings and URLs
│   ├── store/                 # Main marketplace app (users, products, requests, orders)
│   ├── cart/                  # Shopping cart app
│   ├── media/                 # Uploaded product images
│   ├── static/                # CSS/JS/assets
│   ├── manage.py
│   └── requirements.txt
├── README.md
├── OSP-SRS.pdf
├── OSP-test-plan.pdf
├── OSP-test-compliance-report.pdf
└── OSP-project-presentation.pptx
```

## Core Features

### Authentication and Users
- Custom `User` model using **email as the login identifier**.
- Registration/login flows for customers.
- Password update flow with email notification.

### Product and Catalog
- Categories with dedicated browsing.
- Product listings include:
  - name, manufacturer, description
  - base/sale price
  - quantity
  - city and shipping constraints
  - up to 5 images

### Buying and Selling Workflow
- Buyer can create requests for a product.
- Seller can accept/reject requests.
- Buyer and seller can negotiate with request-linked chat messages.
- Accepted requests become orders.
- Seller can view deliveries and expanded order details.

### Cart
- Session-backed cart implementation.
- Add, update, and remove product quantities.

### Profile and Address
- Customer profile page.
- Address capture used for fulfillment and delivery checks.

## Data Model (High Level)
Main entities in `store`:
- `User` (custom auth model)
- `Customer`
- `Manager`
- `Category`
- `Product`
- `Address`
- `Request`
- `Chat`
- `Order`
- `Issue`

## Getting Started (Local Setup)

### 1) Prerequisites
- Python 3.10+
- pip
- virtualenv (recommended)

### 2) Clone and enter project
```bash
git clone <your-fork-or-repo-url>
cd online-selling-portal-team-acraiders
```

### 3) Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate      # Windows (PowerShell)
```

### 4) Install dependencies
```bash
pip install -r ecom/requirements.txt
```

### 5) Configure environment variables
Create a `.env` file inside the `ecom/` directory (same level as `manage.py`) and add:
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
```

> If email is not needed in your local run, you can still start the app; email sends are configured with `fail_silently=True` in current logic.

### 6) Run migrations
```bash
cd ecom
python manage.py migrate
```

### 7) Create a superuser (optional, for admin)
```bash
python manage.py createsuperuser
```

### 8) Start development server
```bash
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

## Running Tests
From `ecom/` directory:
```bash
python manage.py test
```

## Important Notes
- Current default configuration uses:
  - `DEBUG=True`
  - `ALLOWED_HOSTS=['*']`
- Do **not** use these values in production.
- Replace secret keys, hardcoded credentials, and configure secure deployment settings before production use.

## API/Architecture Notes
- This codebase is primarily server-rendered (Django templates), not a separate SPA frontend.
- Business logic is mostly located in `store/views.py` and model definitions in `store/models.py`.

## Documentation Artifacts
The repository also includes:
- Software requirements specification (`OSP-SRS.pdf`)
- Test plan (`OSP-test-plan.pdf`)
- Test compliance report (`OSP-test-compliance-report.pdf`)
- Project presentation (`OSP-project-presentation.pptx`)

## Contribution Guide (Suggested)
1. Create a feature branch.
2. Make focused changes with clear commit messages.
3. Run tests locally.
4. Open a pull request with:
   - problem statement
   - solution summary
   - testing evidence

## License
No explicit license file is currently present in this repository. Add a `LICENSE` file if you want to define usage terms.
