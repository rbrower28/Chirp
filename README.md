# Chirp - speak your mind!

Let the world know what you think! Chirp is a simple social media app
that allows you to write and post your thoughts for the world to see.
Be careful how much you write! Each post is limited to 200 characters.

Writing the code for this website has taught me a lot about web development.
I learned how to write dynamic pages using template folders and how to
include snippets of htmlcode, from headers to cards on the page.
I also learned how to connect to a sqlite database using Django models
and how to update and retrieve information to populate a webpage.

To test this website for yourself, begin by forking this repository.
Next, you want to make sure your software meets the requirements
listed in the requirements.txt file. Type this command in the terminal:

* **python3 manage.py runserver** for Macos
* **python manage.py runserver** for Windows

Once you are here, go to this url in your browser and you will have
access to the development site! Updates in the code will apply upon
refreshing the page.

* http://localhost:8000

{Describe your purpose for writing this software.} -->

## Code Demonstration and Walkthrough:

(Not made yet)
<!-- [Software Demo Video](http://youtube.link.goes.here) -->

# Web Pages

## Home Page

The home page has a header, nav-bar (on the left side)
and a decoration bar (on the right side). On the center of
the page you find a form that allows you to write and
submit a post. Under that form, you will find the 10 most
recent posts. These are dynamically filled by using a
Django model. This means that submitting a valid post on
top of the screen will place that new post right under
the form at the top. Each post has a link to it's own
dynamically generated page.

## Post Page

Each post made on Chirp is given a unique 5-character
identifier (slug) that becomes the custom url for the
individual page. The individual page has the same header,
navigation and decoration as the homepage (dynamically
written with django 'includes'). The main area of the page
has the original post at the top with larger font.
Underneath you will see any comments that have been left
on the post. The comments are displayed with the latest
on the top. Below the comments is a comment form where
you can submit your own. When a valid comment is sumbitted,
it is immediately placed at the bottom of the list, right
above the form.

# Login Page

This page uses a Django form model to populate a login
form. On here you login to your account, and if the login
is successful you are redirected to back to the homepage
and your username is displayed on the header.

# Development Environment

* Python - 3.9.4
* Django - 4.0.1

# Useful Websites

<!-- {Make a list of websites that you found helpful in this project} -->
* [Django 4.0 Documentation](https://docs.djangoproject.com/en/4.0/)
* [TutorialsPoint Django Walkthrough](https://www.tutorialspoint.com/django/index.htm)
* [W3Schools Django Resources](https://www.w3schools.com/django/index.php)

# Future Work

<!-- {Make a list of things that you need to fix, improve, and add in the future.} -->
* Item 1
* Item 2
* Item 3