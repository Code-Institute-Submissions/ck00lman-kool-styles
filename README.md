
# Code Institute Full Stack Frameworks with Django

# Welcome to Kool Style E-Commerce Website

## Project Objectives
This ecommerce website provides and facilitates user with shopping for any trending and/or variety of Styles they might be looking for. 
Product(s) include but are not limited to clothing, home decor, kitchen essentials, etc.. This website is an extention of the "Boutique Ado", it has a similar look and feel, however with multiple new options and funcitonalities. Any user can browse, look, select, register, add to favorites and purchase items. 


## Deployed Link
The Kool Styles Website is available [here](https://kool-styles.herokuapp.com/)

## User Exprience & User Interface
The color scheme I used was adopted from the mini project "Boutique Ado", however I've customized it by adding a "Dark Magenta" color scheme, so the user would have an enjoyable and colorful UI. on this website is chosen to be bright and cheery to give customers a bright and cheerful experience when they shop. The font selection of `font-family: "Helvetica Neue", Helvetica, sans-serif;` has maintained a modern/classic look in order to facilitate legibility.

### User and Staff Accounts for quick access:
> Staff  
> username:  staff1  
> password: koolstyle297
>
> User
> username: newuser  
> password: koolstyle123  
>  
> User 2 
> username: user1  
> password: koolstyle123


### Account & Access: How it works:
Customer: A customer is able to register for an account in which he/she will receive a confirmation email after completing the [registration form](https://kool-styles.herokuapp.com/accounts/login/). A customer has the ability of Adding and Updating their Profile information, adding/updating Shopping Bag and Favourites. 

Staff: A staff is able to login to the [Admin Dashboard](https://kool-styles.herokuapp.com/admin). Where he/she will have the ability of Adding and Updating product information (category, subcategory, brand, size, etc..) and verifying order information, however a product CRUD functionality is also possible if the Staff Member is logged in on the website directly. THe Staff memeber will be presented with the option to "Edit" or "Delete" Products.


## User Stories
### eCommerce Option
1. As a user of the ecommerce website, a user would like to be able to browse through various products.
2. As a user, he/she should be able to query/search for products, either by sorting categories or in a search bar.
3. As a user, he/she should be able to view product details(image, description, attributes/options, etc.) when selected. 
4. A user should be able to add a product to the shopping cart and checkout whenever they choose to.
5. A user should also be able to remove products from the shopping bag and/or favorites.
6. A user should see immediately what product they have just added to their shopping bag, what they've removed, total product count and the grand total.

## Wireframes
The wireframes for this project can be found [here](https://github.com/ck00lman/kool-styles/blob/master/wireframes.pdf).

## Kool Styles Functionalities & Features (Home Page)
* Navigation Bar
- At the top of the homepage, user will find the navbar, which will facilitate navigationt of the website. User will be able to Register or Login/Logout, see their Favorites, Shopping Bag and Search for products.
pages and also the shopping cart page.

* A simplistic approach in which the user is presented a clean and modern home page. 
- The User is greeted with a background image, welcome text and shop styles button, allowing the user to navigate to the products page.

b. Features that allow users to navigate to other pages
* At the top of the homepage, there is a navbar to allow users to navigate to Directory, Product Category and SignUp or Login/Logout
pages and also the shopping cart page.

c. Features that allow users to view shopping bag and favorites.
* On the right of the navigation bar, there is a favorites and a shopping bag icon which navigates to the user's favorites or shopping cart contents.

### Products page
Search Feature
* On the products page the user will be able to filter the products (Ascending or Descending) based on:
- Price
- Rating
- Name
- Category
- Brand

Cards Display
* All products will be illustrated in a card view, to enhance and facilitate the users overall experience.

Permission Based Features
* If the user is logged in as a superuser/staff or has permissions to perform CRUD functions, the user would be able to see
the edit or delete a product.

### User Account Management Page
* The account management pages are fully managed by Django-AllAuth

### Shopping Bag Page
Shopping Bag Feature(s)
* Upon visiting the website for the first time the users will see an empty shopping bag if no products are added.
* If the user adds products to the bag, the users will be able to see product count amount in the red badge on top to the righ of the shopping bag, when the bag is selected the user will be redirected to the SHopping Bag page.
* There are also buttons that allow the user to increase (+) or decrease (-) the quantity of the item to purchase.
* On the bottom right the user will be able to see the Total (excluding shipping), Shipping cost/fee and Grand Total.

### Shopping Bag Page
Shopping Bag Feature(s)
* Upon visiting the website for the first time the users will see the Favourites option at the top right.
* If the user adds products to their favorites, the users will be able to see product count amount in the red badge on top to the righ of the heart shape, when their favorites is selected the user will be redirected to the Favorites page.
* There are also buttons that allow user to increase or decrease the quantity of the item to purchase.
* On the bottom right the user will be able to see the Total (excluding shipping), Shipping cost/fee and Grand Total.

### NavBar & Footer
Navigation Bar 
* On the navigation bar and footer, when a relevant link is selected the user is redirected to the assiged `href`url.

## Technologies Used
The technologies used for this project are:
1. [Django(Release 3.1.1)](https://docs.djangoproject.com/en/3.1/releases/3.1.1/). Django is a Python Web Framework that encourages rapid
development and clean design.
2. [Python(Release 3.8.5)](https://www.python.org/downloads/release/python-385/). Python is the programming language that Django 
is built on.
3. [HTML5](https://html.spec.whatwg.org/). HTML is the markup language that structures the webpage documents.
4. [CSS3](https://www.w3.org/TR/2001/WD-css3-roadmap-20010523/). Cascading style sheet is the language that presents and styles 
the HTML documents.
5. [Javascript and JQuery](https://developer.oracle.com/sg/javascript/). Javascript and Jquery is used primarily to do DOM 
manipulation and it is the main engine to serve interactivity and event handling to the webpages.
6. [Bootstrap (Release 4.5)](https://getbootstrap.com/docs/4.5/getting-started/introduction/). Bootstrap is the layout framework
used to organize the website's display.
7. [Git and Github](https://github.com/)  
Github is an online hosting service for software development that utilizes Git for version control.
8. [Gitpod](https://www.gitpod.io/)  
Gitpod is an online IDE that can be launched in Github. I used it to start developing with the Code Institute Starter Template.
9. [Stripe](https://stripe.com/en-sg). Stripe is a financial software service provider that provides the API for software developers
to integrate payment into their websites and mobile apps.
10. [Google Fonts](https://fonts.google.com/)
is used for body and in paragraph tags. Google Font Delius Swash Caps is used in the navbar brand/logo name.
11. [Font Awesome](https://fontawesome.com/) FontAwesome is an icon set and toolkit that provides many different icons in many different formats for use in development.
12. [Heroku](https://heroku.com/) Heroku is a Cloud Application Platform, which offers platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. 

### Django Libraries
1. [Django-AllAuth](https://django-allauth.readthedocs.io/en/latest/overview.html) is a Django Library that manages authentication, 
registration, account management as well as 3rd party (social) account authentication and security related actions.
2. [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) is Django package that provides DRY Django Forms. Used to create the User registration, checkout, profile updating, etc..

### Database
The database used in the project is PostgreSQL from the Heroku Platform Resources. PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance.

## Testing
Due to unforseen circumstances I was able only able to test the project manually. 

## Project challenges.
In this project I learned alot in a short time span. I was challenged and decided to take the challenge and add additional funcitonalities and styling to Code Institute's "Boutique Ado" Project. It might look very similar,however I managed to understand how to use Python as a Server Side Language, PostgreSQL and Django. The most successful achievements were connecting to AWS, adding Stripe Payment option and Deploying to Heroku.


## Deployment
### Running the project locally.
The project was developed in GitPod.
In order to facilitate the deployment of this project locaaly please follow the below guidelines:
The steps I went through to run the project locally are as follows:

1. Create an account on [Gitpod](https://www.gitpod.io/).
2. Sign up or Sign In to [github](https://github.com/) account.
3. Sign up or sign in to [gitpod](https://www.gitpod.io/) account and link it to your github account.
4. Go to your github profile page and create a new repository using the 
[Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)
5. The project folder will be available on the personal github or in the dropdown list from the create a new repository page.
6. After successfully creating the repository you will find at the top right of the new repository a green Gitpod button.
8. Once the project has fully loaded in the browser, a Visual Studio Code-like editor with a terminal will be seen.
9. Please install the following requirements:  
    a. pip3 install django==3.1.1  
    b. pip3 install django-allauth  
    c. pip3 install django-crispy-forms
10. Set up the environment variables as follows:  
    a. Create a .env file  
    b. Create a .gitignore file to list the names of files to be omitted from git.  
    c. In the .env file, place the Django Secret Key, and the Stripe Publishable Key, Stripe Secret Key and Stripe Endpoint Secret.  
    d. The initial coding is done using SQLite. On deploy after obtaining the database url, the production database url is to be 
    inserted into the .env file too.
11. It is important to generate the requirements.txt:
```console
$ pip3 freeze --local > requirements.txt
```
12. Setting up Django  
a. To start a new project, enter the following command in the terminal:
```console
$ django-admin startapp `<project_name>` .
```
b. To start a new app withing this project, enter the following command in the terminal:
```console
$ django-admin startapp `<app_name>`
```
c. How to programmatically setup the database via Django, running this command will illustrate the actions that will be taking place:
```console
$ python3 manage.py migrate --plan
```
d. How to programmatically setup the database via Django:
```console
$ python3 manage.py migrate
```
d. Creating migration files for the database, running this command will illustrate the actions that will be taking place:
```console $ python3 manage.py makemigrations --dry-run
```
f. Creating migration files for the database:
```console
$ python3 manage.py makemigrations
```
g. To create superuser:
```console
$ python3 manage.py createsuperuser
```
h. Adding Products:
```console
$ python3 manage.py loaddata categories
```
i. Adding Products:
```console
$ python3 manage.py loaddata subcategories
```
j. Adding Products:
```console
$ python3 manage.py loaddata brands
```
k. Adding Products:
```console
$ python3 manage.py loaddata products
```

13. Data was populated with the data provided in the mini project and via the admin dashboard.

14. In order to run the project locally, run the following command in the terminal:
```console
$ python3 manage.py runserver
```

## How To Deploy on Heroku
1. By installing the following dependencies via the terminal:
```console
$ pip3 install gunicorn
$ pip3 install psycopg2
$ pip3 install Pillow
$ pip3 install whitenoise
$ pip3 install dj_database_url
```

2. Sign up for Heroku account

3. Login Heroku in the terminal

```console
$ heroku login -i

```

4. Type in the below to create a heroku app, where `<the_name_of_the_project>` is the name of the project to be deployed.  

```console
$ heroku create <name_of_the_project>

```
Or you can also create it online:
Create an App on Heroku(before creating an app make sure your GitHub account is connected with your Heroku Account):
    - Navigate to [New Heroku App](https://dashboard.heroku.com/new-app)
    - Type app name 
    - Choose region (choose region closes to you)
    - Click create app button.

5. then create a remote repository by typing in 

```console
$ git remote -v
```

6. Create a Procfile with the content "web gunicorn `<name of the project>`.wsgi:application
8. Update the allowed host in settings.py to the newly created heroku app domain name.
```ALLOWED_HOSTS = ['<name of the project>.herokuapp.com', 'localhost']
```
9. Freeze all project dependencies by keying in to the terminal 

```console
$ pip3 freeze --local > requirements.txt 
```
10. Add STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

11. Finally push the project to git as below:

```console
$ git add.
$ git commit -m <deployment message>
$ git push heroku master
```

## Setting Up the Database for Production.
1. Add import dj_database_url to settings.py
2. Change the databases setting in settings.py to get the default database url from env variable as below:
```
DATABASES = {'default': dj_database_url.parse(os.environ["DATABASE_URL"])}
```
3. Run database migrate again to setup the database:
```console
$ python3 manage.py migrate
```
4. It is important to setup a superuser account and populate the database data within the sequence described in section "Running the project locally
12c-12k."
5. Do NOT forget to set the following environment variables:
 - create file env.py in the main folder of the app or you can set them up in your Heroku App Dashboard Settings
 - set variables for  EMAIL_PASSWORD, EMAIL_ADRESS, SECRET_KEY, STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY, STRIPE_WH_KEY, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and HOSTNAME


## Persisting Bugs


## Acknowledgements and Credits
### Images
## Credits

* Google Fonts: https://fonts.google.com
* Materializecss: https://materializecss.com
* Pixabay: https://www.pixabay.com
* Pexels: https://www.pexels.com
* Color Hex: http://www.color-hex.com
* Pine Tools: https://pinetools.com
* Pixlr Photo Editor: https://pixlr.com
* Photo Resizer: https://www.photoresizer.com
* jQuery: https://code.jquery.com/
* W3Newbie Tutorials: https://w3newbie.com/w3newbie-tutorials/
* W3School (HTML and CSS): https://www.w3schools.com/default.asp
* Code Institute Modules: Course Resources from all Modules 
* Stackoverflow: https://stackoverflow.com/ 
* GitHub: https://www.github.com
* GitPod: https://www.gitpod.io
* Animate.CSS: https://animate.style/

### Media
* Pixabay: https://www.pixabay.com
* Google: https://www.google.com
* Pexels: https://www.pexels.com
* Poster My Wall: https://www.postyermywall.com
* Link Picture: https://www.linkpicture.com


### Data
1. Code Institute "Boutique Ado" Fixture Files. 

## Design Ideas
1. The Design Ideas are orginally from Code Institute "Boutique Ado". 


## Disclaimer
Any content but limited to such as images, information used in this project/website is purely for educational purpose.