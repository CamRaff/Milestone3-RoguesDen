# CamRaff - Milestone Project 3 - Rogues Den

![displays](readme_images/displays.png)

Here is a link to the deployed site: [Rogues Den](https://rogues-den-mp3-918bccafa7f4.herokuapp.com/)

---

# Contents

- [Automated](#automated)

    - [W3C HTML Validator](#w3c-html-validator)

    - [CSS Jigsaw](#css-jigsaw)


---

# Automated

## W3C HTML Validator

To test all of the HTML pages in my site, I used the [W3C HTML Validator](https://validator.w3.org/). The results for each page were as follows:

### Home

The initial test showed no errors.

<img src="testing_images/w3c_html/w3c-html-home.png" alt="home page html test" height="200">

### Login

The initial test brought up errors due to having class attributes set separately, as shown below:

<img src="testing_images/w3c_html/w3c-html-login.png" alt="login page html test" height="300">

After rectifying this issue the results were as follows:

<img src="testing_images/w3c_html/w3c-html-login-fixed.png" alt="login page html second test" height="200">

### Register

The initial test brought up the same error as the login page with class attributes set separately:

<img src="testing_images/w3c_html/w3c-html-register.png" alt="register page html test" height="400">

After rectifying this issue the results were as follows: 

<img src="testing_images/w3c_html/w3c-html-register-fixed.png" alt="register page html second test" height="200">

### Characters

The initial test showed no errors.

<img src="testing_images/w3c_html/w3c-html-characters.png" alt="characters page test" height="200">

### View Character

The initial test showed no errors.

<img src="testing_images/w3c_html/w3c-html-view-character.png" alt="view character page test" height="200">

### Edit Character

The initial test showed no errors.

<img src="testing_images/w3c_html/w3c-html-edit-character.png" alt="edit character page test" height="200">

### Profile

The initial test showed no errors.

<img src="testing_images/w3c_html/w3c-html-profile.png" alt="profile page test" height="200">

## CSS Jigsaw

To test the CSS used in the site, I used [CSS Jigsaw](https://jigsaw.w3.org/css-validator/). There were no issues flagged by the test:

<img src="testing_images/css-jigsaw.png" alt="css test" height="100">

## JavaScript Validator

To test the custom JavaScript used in the site, I used [JSHint](https://jshint.com/). The test results were as follows:

<img src="testing_images/jshint-test.png" alt="javascript test" height="300">

The undefined variable being flagged is related to the Materialize framework that I used. 

## Python Validator

To test the Python used in the site, I used the [CI Python Linter](https://pep8ci.herokuapp.com/). The results for each module were as follows:

### __init__.py

The initial test flagged some minor issues like extra blank lines needed, and also flagged an issue with imports being in the wrong place, however they were needed there for app initialization so I had to add "# noqa" beside those lines of code. See below: 

<img src="testing_images/pylint/init-pylint.png" alt="init python lint" height="400">

### auth.py

The initial test flagged quite a lot of "line too long" issues. I rectified the line lengths and the result was as follows:

<img src="testing_images/pylint/auth-pylint.png" alt="auth python lint" height="400">