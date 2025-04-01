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

