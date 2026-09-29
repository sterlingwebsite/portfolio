# Portfolio Website

## Overview

As a software engineer, I built this portfolio website to demonstrate my ability to create full-stack web applications using Django and Python. This project allowed me to deepen my understanding of the Model-View-Template (MVT) architecture, database design with Django's ORM, and creating dynamic, interactive web interfaces. The application showcases my software engineering projects in a professional, filterable gallery format that potential employers and collaborators can browse.

## Description

This is a Django-based portfolio web application that displays software engineering projects with dynamic filtering and search capabilities. The app runs on a local Django development server and allows visitors to browse a gallery of projects, filter by category or search terms, and view detailed information about each project.

**To start the server:**
python manage.py runserver

Then open your browser and navigate to `http://127.0.0.1:8000/` to see the portfolio homepage.

## Purpose

I created this software to build a professional portfolio platform that highlights my technical projects and skills. The application demonstrates proficiency in web development fundamentals including database design, dynamic content rendering, URL routing, user input handling, and responsive web interfaces. This portfolio serves as both a learning tool and a showcase for my software engineering capabilities.

## Web Pages

**Homepage (Portfolio Gallery)** - The main landing page displays all projects in a card-based layout. Users can search projects across all fields (title, description, tech stack, category, and GitHub links) using the search bar. Category filter buttons allow quick filtering by project type (Testing, Study, Finance). The page dynamically updates to show matching results and displays a count of projects found. Users can click on any project title to navigate to the detailed project page.

**Project Detail Page** - Each project has its own dedicated page showing complete information including the full description, technology stack used, and a direct link to the GitHub repository. This page is dynamically generated based on the project ID in the URL. Users can easily return to the portfolio homepage using the "Back to Portfolio" link.

**Contact Page** - A contact form page (to be implemented) where visitors can reach out with inquiries or collaboration opportunities.

The app uses URL parameters (`/project/<id>/`) to dynamically route to individual projects and query parameters (`?search=` and `?category=`) to filter the gallery without requiring page reloads.

## Development Environment

**Tools:**

- Visual Studio Code (code editor)
- Git (version control)
- Python 3.11
- Django 5.2.17

**Languages & Libraries:**

- Python 3.11
- Django 5.2.17 (web framework with built-in ORM)
- SQLite (database - included with Django)
- HTML5 (template markup)
- CSS3 (styling)

## Useful Websites

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Models & Database](https://docs.djangoproject.com/en/5.2/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/5.2/topics/http/views/)
- [Django Templates](https://docs.djangoproject.com/en/5.2/topics/templates/)
- [Django Admin Interface](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/)

## Future Work

- Implement the contact form with email notifications
- Add image upload and display functionality for project thumbnails
- Create user authentication for admin content management
- Implement pagination for large project lists
- Enhance styling with CSS framework (Bootstrap or Tailwind)
- Add project sorting options (by date, popularity, tech stack)
- Deploy to production server (Heroku, AWS, or similar)
- Add comment/feedback system on project detail pages
