# Capstone-Project
#Day 1
#Library Management System API

A Django REST Framework backend for managing library resources, including books, users, and transactions.

#Current Progress

#Completed Some Features (books App)

 #Project Initialization
  - Created Django project (`library_api`)
  - Created apps: `books`, `users`, `transactions`
  
 #Books Management
  - Implemented Book model with all required fields
  - Created BookSerializer for data validation
  - Implemented BookViewSet with CRUD operations
  - Added filtering capabilities:
    - Filter by availability (`available_only=true`)
    - Search by title, author, or ISBN
  - Set up proper permissions (IsAuthenticatedOrReadOnly)
#Users Management
- Implemented Custom User model extending AbstractUser
- Added fields:
  - Username (unique), Email (unique)
  - Date of Membership, Active Status
- Created UserSerializer with proper field validation
- Implemented UserViewSet with controlled CRUD operations
- Configured JWT authentication endpoints:
  - `/api/auth/token/` - Obtain tokens
  - `/api/auth/token/refresh/` - Refresh tokens

#Transactions System
- Implemented Transaction model with:
  - User (ForeignKey), Book (ForeignKey)
  - Checkout Date (auto), Deadline (14 days default)
  - Return Date (nullable), Status flags
- Created TransactionSerializer with read-only fields
- Implemented TransactionViewSet with custom actions:
  - `POST /transactions/checkout/` - Check out a book
  - `POST /transactions/<id>/return/` - Return a book
- Added business logic:
  - Automatic copy availability updates
  - Duplicate checkout prevention
  - Overdue book tracking

#API Features
- RESTful endpoints following best practices
- Comprehensive error handling

