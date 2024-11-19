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

The initial test flagged some minor issues like extra blank lines needed, and also flagged an issue with imports being in the wrong place, however they were needed there for app initialisation so I had to add "# noqa" beside those lines of code. See below: 

<img src="testing_images/pylint/init-pylint.png" alt="init python lint" height="400">

### auth.py

The initial test flagged quite a lot of "line too long" issues. I rectified the line lengths and the result was as follows:

<img src="testing_images/pylint/auth-pylint.png" alt="auth python lint" height="400">

### models.py

The initial test flagged the same as above. I rectified the lengths and the result was as follows:

<img src="testing_images/pylint/models-pylint.png" alt="models python lint" height="400">

### routes.py

The initial test flagged the same as above. After rectifying the lengths the result was as follows:

<img src="testing_images/pylint/routes-pylint.png" alt="routes python lint" height="400">

## Lighthouse

I used Lighthouse from [Google Dev Tools](https://developer.chrome.com/docs/) to test the performance, accessibility, best practices and SEO of the website on both desktop and mobile, the results were as follows:

### Desktop

#### Home

<img src="testing_images/lighthouse/desktop/home-desktop.png" alt="lighthouse home page test for desktop" height="200">

#### Login

<img src="testing_images/lighthouse/desktop/login-desktop.png" alt="lighthouse login page test for desktop" height="200">

#### Register

<img src="testing_images/lighthouse/desktop/register-desktop.png" alt="lighthouse register page test for desktop" height="200">

#### Characters

<img src="testing_images/lighthouse/desktop/characters-desktop.png" alt="lighthouse characters page test for desktop" height="200">

#### Add Character

<img src="testing_images/lighthouse/desktop/add-character-desktop.png" alt="lighthouse add character page test for desktop" height="200">

The accessibility being lower on this page is due to labels not being set for select options. I rectified this with aria-labels.

#### View Character

<img src="testing_images/lighthouse/desktop/view-character-desktop.png" alt="lighthouse view character page test for desktop" height="200">

#### Edit Character

<img src="testing_images/lighthouse/desktop/edit-character-desktop.png" alt="lighthouse edit character page test for desktop" height="200">

#### Profile

<img src="testing_images/lighthouse/desktop/profile-desktop.png" alt="lighthouse profile page test for desktop" height="200">

The accessibility and SEO being lower on this page is due to a lack of alt text for the profile image. I added some alt text.

### Mobile

There was an accessibility issue on all pages due to a lack of a label for the side navigation provided by Materialize. I rectified this with an aria-label.

#### Home

<img src="testing_images/lighthouse/mobile/home-mobile.png" alt="lighthouse home page test for mobile" height="200">

#### Login

<img src="testing_images/lighthouse/mobile/login-mobile.png" alt="lighthouse login page test for mobile" height="200">

#### Register

<img src="testing_images/lighthouse/mobile/register-mobile.png" alt="lighthouse register page test for mobile" height="200">

#### Characters

<img src="testing_images/lighthouse/mobile/characters-mobile.png" alt="lighthouse characters page test for mobile" height="200">

#### Add Character

<img src="testing_images/lighthouse/mobile/add-character-mobile.png" alt="lighthouse add character page test for mobile" height="200">

The accessibility being lower on this page is due to labels not being set for select options. I rectified this with aria-labels.

#### View Character

<img src="testing_images/lighthouse/mobile/view-character-mobile.png" alt="lighthouse view character page test for mobile" height="200">

#### Edit Character

<img src="testing_images/lighthouse/mobile/edit-character-mobile.png" alt="lighthouse edit character page test for mobile" height="200">

#### Profile

<img src="testing_images/lighthouse/mobile/profile-mobile.png" alt="lighthouse profile page test for mobile" height="200">

The accessibility and SEO being lower on this page is due to a lack of alt text for the profile image. I added some alt text.