# Yokiyo
Fun Olympics is a web application that allows users to be in the loop of what is going on in the summer olympics. The user login and creates their profile which determines the kind of information they get from the various venues and faciiities.Your comments and feedback are highly welcome.


## Features (User Stories)
This app that allows users to post their neigb=hbourhood and see others posted by others.

- [x] A user can register their accounts and sign in.
- [x] A user can read blogs on the home page.
- [x] Once signed in a user can comment on a blog post or news using their accounts.
- [x] Once signed in a user can see their venues.
- [x] Once signed in a user can see their facilities around different venues.
- [x] Once signed in a user can see the different schedules of events in different facilities in the venue.
- [x] Once signed in a user can comment on a blog post.

- [x] Once signed in User can rate other neighbourhoods and businesses.

## Screenshot

![A screenshot of the app page](https://github.com/Hillarydalie/jiraniwatch/blob/master/static/images/jirani.png "App Page")

## Getting Started

These instructions will help get you started on your own copy of the project up and running on your local machine for development and testing purposes. 
This has also been deployed on a live development server for this project. The notes on how to deploy your own project to a live server will be in the link below.	

### Prerequisites

You will need to have the following. 

```
- [x] Python version 3.6 - Readily available on any linux distro/windows or mac system one may be using.
- [x] A code editor of your choice. I personally used sublime for this project, but other good freebee ones are Atom and VS Code.
- [x] Terminal. We will run most of our apps from the terminal. Good knowledge in using the terminal is a plus. To start the terminal CTRL + ALT + T for linux. For those on windows one can use git bash.
- [x] Dependencies required will be installed in the next stage.
```

### Installing

This is a step by step series of instruction that will tell you how to get a development env running and any other installations required.

- [ ] Cloning the repository from the link. Open terminal and run the following command.
```
git clone https://github.com/hillarydalie/jiraniwatch.git
```
- [ ] When the cloning is complete, enter to the folder cloned by running this command.

```
cd jiraniwatch/
```
- [ ] Create a virtual environment by running either of the two commands. <preffered_environment_name> replace this with your environment name.
```
*pip install virtualenv*, when complete then run *virtualenv <preffered_environment_name>* or *python3 -m venv virtual*
```
- [ ] Activate the virtual environment by running the following command.
```
source <preffered_environment_name>/bin/activate
```
- [ ] We will then install all the dependencies used in the project simply by running the requirements.txt file as follows.
```
pip install -r requirements.txt
```
- [ ] The last thing is to test and make sure everything is running fine. We shall use this command.
```
python3.6 manage.py runserver
```
Now we are ready to work on the project on our local server.


## Running the tests

An important aspect in python is writing tests to ensure our tests fail then writing code to ensure the tests pass. This has already been done. In order for you to run the tests you shall run the following code.

``` python3.6 manage.py tests```

Ensure all the tests ran and pass. If you need to add any features in the models, write the test, run the test to see if it fails, then write the code to ensure the test now passes. This is a good practise.

## Bugs

No bugs have so far been reported as of 22nd of May 2020. If you find any do not hesitate to contact me. 
[GitHub](http://hillarydalie.github.com), [Mail](emacode@yahoo.chr)

## Technologies Used in Project

* [Python](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language.
* [Django](https://www.djangoproject.com/) - This is a python framework used for most of this project.
* [HTML5](https://www.w3schools.com/html/html5_intro.asp) - Mark up language for web pages.
* [CSS3](https://www.w3schools.com/css/default.asp) - Used to style HTML pages.
* [BOOTSTRAP](https://getbootstrap.com/)- Bootstrap is an open source toolkit for developing with HTML,CSS and JS.
* [POSTGRESQL](https://www.postgresql.org/) - Used as our relational database management system for our  Project.
* [JQuery](https://www.jquery.com/) - A javascript library used for addding javascript functionality to webpages.
* [HEROKU](https://www.jquery.com/) - Heroku is a cloud platform as a service which I used this as a development server.

## Future Implementations

* [SEO Optimization](#) - Optimise the site for good ads and high list on search engines.
* [Payment Gateway](#) - Optimise the site to be able to transact payments for the lessons online.
* [Booking Engine](#) - Optimise the booking system. Add to calender and give notifications.

## Contributors

This is my sole work. No contirbutors in this project. If you have forked and used this repository, kindly add my profile link in your list of contributors.

## Authors

* **Emmanuel Kwizera Rudasubwa**


## License

This project license is auto-generated by github under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Additional Knowledge

* Youtube Tutorials
* W3Schools.
* Django Project Documentation.
* Bootstrap Documentation.

										Copyright Reserved  (c) 2020

