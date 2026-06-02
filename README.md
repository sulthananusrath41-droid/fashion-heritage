# Fashion Heritage. Historical Womens Gowns Explorer


## Distinctiveness and Complexity

- Fashion Heritage is a platform that teaches people about culture.

- It lets users look at womens gowns from various countries and times.

- I think this project stands out from CS50W projects.

- It meets complexity requirements in ways and Fashion Heritage does it well.

- The platform shows gowns from around the world.

- Users can explore womens clothing, on Fashion Heritage.

### Why It Is Distinctive

Fashion Heritage is really different from websites. It is not a place where you can talk to friends like on a network. It is also not a place where you can buy things like on an e-commerce site. You will not see things like followers or posts or even a shopping cart on Fashion Heritage.

It is actually a website that teaches people about the history of womens clothes from around the world. The people who made Fashion Heritage wanted to show everyone how clothes have changed over time. They picked eleven important dresses from eleven different countries like England and France and China and India and Korea and Japan and the United States and Russia and Portugal and Greece and Spain.

These dresses are from a long time ago. Almost 1,600 years ago, starting from a time called the Byzantine Period in 330 AD and going all the way to the Victorian Era which ended in 1901. Fashion Heritage is unique because it is the project that teaches people about history and clothes from different cultures in this way. No other project is, like Fashion Heritage.

### Why It Is Complex

- Fashion Heritage is a lot more complicated than the projects in this course.

- It is complicated in ways.

- **First** the database design is really advanced.

- The application has 5 custom Django models.

- These models are Gown, Comment, Like, Save and UserProfile.

- The Gown model has a lot of fields.

- These fields include the name of the gown the country it's from the era it is from the designer, the history of the gown

- the cultural significance of the gown and an image field that uses Django ImageField with the Pillow library.

- The Comment, Like and Save models all use ForeignKey relationships that connect to both the Gown model and Djangos built-in User model.

- Managing these relationships correctly across all the views was not easy.

- It needed a lot of planning.

- **Second** the JavaScript code is more advanced than the code in the projects.

- The Like button and the Save button both use the JavaScript Fetch API.

- They use it to send POST requests to Django API endpoints without reloading the page.

- Django returns JSON responses.

- JavaScript reads these responses. Uses them to update the button text on the screen in real time.

- All API calls include CSRF token handling.

- This is to protect against -site request forgery attacks.

- **Third** the search feature is really cool.

- It uses Django Q objects to search across three model fields at the same time.

- These fields are the name, the country and the era.

- It does all this in a database query.

- So if a user types India or Victorian or Mughal they can find matching gowns away.

- **Fourth** setting up image uploading was not easy.

- It was done using Django ImageField and the Pillow library.

- Setting up MEDIA_ROOT MEDIA_URL and serving media files correctly needed a lot of configuration in settings.py.

- **Fifth** the application has an user authentication system.

- This system includes registration, login and logout.

- All the interactive features like liking, saving and commenting are protected.

- Only logged in users can use them.

- Finally the application looks great on devices.

- It uses Bootstrap 4 to make it mobile responsive.

- The homepage shows gowns in a multi-column card grid, on desktop.

- It switches to a column on mobile.

- This was tested on a mobile device.

- It was also tested using Chrome DevTools with a Galaxy S8 simulation.

- The Fashion Heritage application works well on mobile devices.

- The Fashion Heritage application is really advanced.

- The Fashion Heritage application has a lot of features.


## Files

- **models.py**. This file has all the 5 Django models.

The Gown model has fields for name, country, era, designer, history, cultural significance and image.

The Comment model links to Gown and User. Has text content.

The Like model links to Gown and User.

The Save model links to Gown and User.

The UserProfile model extends the default Django User model.

- **views.py**. This file has all view functions for the application.

The index view is for the homepage.

The gown_detail view is for gown pages.

The like_gown API endpoint returns JSON.

The save_gown API endpoint returns JSON.

The saved_gowns view shows the users saved collection.

The search view uses Q objects.

The login, logout and register views are for user authentication.

- **urls.py**. This file has all URL patterns for the fashion_heritage app.

It includes paths for the homepage, detail pages like and save API endpoints saved gowns page, search page, login, logout and register.

- **admin.py**. This file registers all 5 models with the Django admin panel.

This allows gowns and user content to be managed through the admin interface.

- **templates/fashion_heritage/layout.html**. This is the base template that all other templates inherit from.

It has a Bootstrap 4 CDN link, a navigation bar with a search box, login/logout links and a block content area.

- **templates/fashion_heritage/index.html**. This is the homepage template.

It shows all gowns in a Bootstrap card grid layout with name, country and era displayed on each card.

- **templates/fashion_heritage/gown_detail.html**. This is the individual gown detail page.

It shows the image, full history, cultural significance like button save button and comments section with JavaScript Fetch API functionality.

- **templates/fashion_heritage/login.html**. This is the login page.

It has username and password fields and a link to the registration page.

- **templates/fashion_heritage/register.html**. This is the registration page.

New users can create an account, with username, email and password.

- **templates/fashion_heritage/saved_gowns.html**. This page shows all gowns that the currently logged in user has saved to their collection.

- **templates/fashion_heritage/search.html**. This is the search results page.

It displays gowns matching the users search query across name, country and era fields.

- **capstone/settings.py**. This is the Django project settings file.

It includes apps, database configuration, static files configuration and media files configuration with MEDIA_ROOT and MEDIA_URL.

- **capstone/urls.py**. This is the project URL configuration.

It includes the fashion_heritage app URLs and configures media file serving during development.

- **media/gowns/**. This folder contains all gown images.

These images are served through Djangos media file system.

- **requirements.txt**. This file lists all Python packages required to run the application.

It includes Django and Pillow.


## How to Run

1. First you need to get a copy of the project from GitHub. You do this by cloning the repository.

2. Next you install the Python packages. You can do this by running `pip install -r requirements.txt` in your terminal.

3. After that you need to set up your database. You do this by running `python manage.py migrate`.

4. Then you create an user account. This is called a superuser account. You create it by running `python manage.py createsuperuser`.

5. Now you can start the development server. You do this by running `python manage.py runserver`.

6. To see the application you go to `http://127.0.0.1:8000` in your web browser.

7. To add gowns with images you go to `http://127.0.0.1:8000/admin`. You log in with your superuser account.


## Additional Information

- This project needs the Pillow library to upload images. It is listed in `requirements.txt`. Gets installed automatically.

- The project uses SQLite as its database. This is because SQLite is simple and works on different systems.

- The project uses Bootstrap 4. It loads it from a CDN in the `layout.html` base template.

- To use features like Like, Save and Comments you need to be logged in. If you are not logged in you get redirected to the login page.

- Only an admin superuser can add gowns with images. They do this through the Django admin panel.

- The application already comes with 11 gowns. These gowns are, from England, France, China, India, Korea, Japan, United States, Russia, Portugal, Greece and Spain. They cover 1,600 years of fashion history.

- The application works well on mobile phones. We actually tested it on a mobile phone and also used Chrome DevTools to see how it looks on a Galaxy S8.

- We used Bootstrap 4 to make sure the application is responsive. This means that when you use the application, on a phone the cards will stack on top of each other.. When you use it on a desktop the cards will be arranged in three columns.