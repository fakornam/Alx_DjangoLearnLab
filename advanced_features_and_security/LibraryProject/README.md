# LibraryProject
It includes the default Django structure and configuration files.
## 📘 Django Admin Setup for Book Model

To manage books via Django Admin:

1. Ensure `bookshelf/models.py` defines the `Book` model.
2. Register and customize it in `bookshelf/admin.py`.
3. Run `makemigrations`, `migrate`, and `createsuperuser`.
4. Launch the admin panel at `/admin` and log in.
5. Use filters and search to manage book entries efficiently.