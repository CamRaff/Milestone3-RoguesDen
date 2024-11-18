# CamRaff - Milestone Project 3 - Rogues Den

![displays]()

Here is a link to the deployed site: []()

For my third Milestone Project on my course through Code Institute via UCP (University centre Peterborough), I thought it would be fun to create my own version of a Dungeons & Dragons character creation/storage site to allow people to keep track of the characters they have, whether it be few or many! In an ideal world, the site I have created would have the capability to allow for the creation of all race/class combinations, however, in order to ensure I can produce the best project I can within the time I have available, I have chosen to limit the race and class choices to those from the Player's Handbook (2014).

---

# Contents

- [User Experience](#user-experience-ux)

  - [User Stories](#user-stories)

- [Design and Development](#design-and-development)

  - [Wireframes](#wireframes)

    - [Desktop Views](#desktop-views)

    - [Mobile Views](#mobile-views)

  - [Images](#images)

  - [Typography and Color Scheme](#typography-and-color-scheme)

  - [Database Schema and User Journey](#database-schema-and-user-journey)

    - [Database Schema](#schema)

    - [User Journey](#journey)

---

# User Experience (UX)

## User Stories

### First Time Visitors

- I am new to Dungeons & Dragons and I want to find a website that will allow me to store my characters from my different campaigns.
- I want to find a website that is straight forward and easy to use. 
- I want to find a website which has a great vibe and cool visuals.

### Returning Visitors

- I want to be able to update my characters as I level up throughout my campaigns.

### Frequent Visitors

- I want to see if there are any new additions to character creation and other features on the site. 

---

# Design and Development

## Wireframes

Below you can find the inital mock-ups for all of the pages for the site on both desktop and mobile. The wireframes were all created using [Balsamiq](https://balsamiq.com/wireframes/).

### Desktop Views

- #### Home Page

<img src="readme_images/wireframes/home-page.png" alt="Home page image" height="400">

I wanted to keep the home page relatively simple as this is just an introduction, and all of the main focus should be on the character page.

- #### Login/Register Pages

<img src="readme_images/wireframes/login-page.png" alt="Login page image" height="400">

This is the login page which will either log you in or take you to register if not already registered. Clicking log in will take you to the characters page.

<img src="readme_images/wireframes/register-page.png" alt="Register page image" height="400">

This is the register page, very similar to the login page. Clicking submit will take you to the characters page.

- #### Profile Page

<img src="readme_images/wireframes/profile-page.png" alt="Profile page image" height="400">

This is the profile page where you can see your details, and from here update them if you wish. This is where you can logout from your account.

<img src="readme_images/wireframes/edit-account.png" alt="Edit profile page image" height="400">

This is a view of the edit account page.

- #### Character Pages

<img src="readme_images/wireframes/characters.png" alt="All characters page image" height="400">

This is the page where all of the users are stored and from here you can create, view, edit and delete the characters you create. The idea is to have the card that is displayed show the character name, an image of the race they picked, and have a drop down to display the stats of their character.

<img src="readme_images/wireframes/add-character.png" alt="Add characters page image" height="400">

This is the create/add character page, kept relatively simple.

<img src="readme_images/wireframes/character-page.png" alt="Character page image" height="400">

This is how the character will be displayed to the user after they have created them and clicked on the card visible on the character page.

<img src="readme_images/wireframes/edit-character.png" alt="Edit character page image" height="400">

This is the edit character page, very similar to the create/add character page, however the name and race of the character are not changeable once submitted.

<img src="readme_images/wireframes/erase-pop-up.png" alt="Image showing the erase character pop-up" height="400">

This is the defensive programming pop-up to check if they're sure and to notify them that their decision will be final.

### Mobile Views

- #### Home/Login/Register

<img src="readme_images/wireframes/mobile-views.png" alt="Image showing the home, login and register views on mobile" height="400">

- #### Profile/Edit Profile/Characters

<img src="readme_images/wireframes/mobile-views-2.png" alt="Image showing the profile, edit profile and all character views on mobile" height="400">

- #### New Character/Character/Edit Character

<img src="readme_images/wireframes/mobile-views-3.png" alt="image showing the add character, character and edit character views on mobile" height="400">

As you can see, the mobile views simply takes the desktop view and translates it more vertical than horizontal. The erase pop-up will appear the same on mobile as on desktop.

## Images

As I have gone with a Dungeons & Dragons style character creation/storage site, I decided for the site background to have a bit of a dark and grungy dungeon/vault style image. The image was created using the prompt "give me an image of a rogue's den" on [ChatGPT](https://chatgpt.com/)

<img src="rogues_den/static/images/background.webp" alt="Background image for desktop showing a dark and grungy cellar" height="400">

Just incase there were any issues displaying the above image on a smaller device, I also got the below created.

<img src="rogues_den/static/images/mobile-background.webp" alt="Background image for mobile showing a dark and grungy cellar" height="400">

As I was originally planning to give users the ability to change and upload their own profile image, I got [ChatGPT](https://chatgpt.com/) to create a blank profile picture as a place holder. Unfortunately I did not end up implementing the change feature but the blank image is visible on the user profiles and appears as below.

<img src="rogues_den/static/images/blank-profile-picture.webp" alt="Blank profile image" height="300">

### Race Images

The following are the images used as a display of character race. All of these images were acquired using AI from [Canva](https://www.canva.com/). 

#### Dragonborn

<img src="rogues_den/static/images/races/canva-dragonborn.webp" alt="Dragonborn image" height="300">

#### Dwarf

<img src="rogues_den/static/images/races/canva-dwarf.webp" alt="Dwarf image" height="300">

#### Elf

<img src="rogues_den/static/images/races/canva-elf.webp" alt="Elf image" height="300">

#### Gnome

<img src="rogues_den/static/images/races/canva-gnome.webp" alt="Gnome image" height="300">

#### Half-Elf

<img src="rogues_den/static/images/races/canva-half-elf.webp" alt="Half-Elf image" height="300">

#### Half-Orc

<img src="rogues_den/static/images/races/canva-half-orc.webp" alt="Half-Orc image" height="300">

#### Halfling

<img src="rogues_den/static/images/races/canva-halfling.webp" alt="Halfling image" height="300">

#### Human

<img src="rogues_den/static/images/races/canva-human.webp" alt="Human image" height="300">

#### Tiefling

<img src="rogues_den/static/images/races/canva-tiefling.webp" alt="Tiefling image" height="300">

### Favicon

I acquired an image from [ChatGPT](https://chatgpt.com/) that I was originally going to use for the Dragonborn race, however I was struggling to use ChatGPT to get images for the rest of the classes, so I decided to go with [Canva](https://www.canva.com/) for those, and kept the original Dragonborn image and used it to created the [Favicon](https://favicon.io/). The image is as follows:

<img src="rogues_den/static/favicon/apple-touch-icon.png" alt="Favicon image" height="300">

## Typography and Color Scheme

As this website had an image for a background, there wasn't much in the way of thought for a color scheme, as the image itself was quite dark due to the nature of the design. The only thing which required thought was what color the fonts would be, and a way to make the input and text boxes stand out slightly from the background itself. 

### Color Scheme

In order to allow for the background to be visible 99% of the time, I opted to use the rgba color format, leaving the red, blue and green options at 0, so they stayed clear, and then edited the opacity to make it slightly more opaque, leaving the background visible but also providing a background for the text. <br> The background was a little too light to provide contrast against the white text I'd decided upon, so I layered the background with rgba(0, 0, 0, 0.5) to give it more of a dark hint, and I added a background of rgba(0, 0, 0, 0.4) to the input and text boxes to provide that a background and further contrast for the text, while also allowing the background image to be visible. 

### Font and Color

To find a suitable font, I went to [Google Fonts](https://fonts.google.com/) and and after a bit of searching came across the 'Cinzel' font. I decided to go with this font as it provided a quite regal feel, which I thought went well with the Dungeons & Dragons vibe I was going for. 

<img src="readme_images/cinzel.png" alt="Cinzel font" height="150">

I believe this font was a good choice, as it is clear and easy to read, while also being very stylized and works well with the theme of the website. 

## Database Schema and User Journey

### Schema

In order to create the database schema, I used [DB Designer](https://erd.dbdesigner.net/login). The schema was as follows:

<img src="readme_images/db-schema.png" alt="database schema" height="400">

The database was relational, with the Users table linking to the Character table via "db.relationship" and the Character table using the users_id as a foreign key to link the characters created to that specific user. All of the tables created were done using [PostgreSQL](https://www.postgresql.org/).

### Journey

The below flowchart is designed to show the user journey, and I created it using [draw.io](https://www.drawio.com/).

<img src="readme_images/flowchart.png" alt="user journey" height="400">

The flowchart above shows the main navigational routes throughout the website. Naturally there are other links, but to keep the flow chart clear and readable I decided to only show the main routes. The home page is accessible from each page on the website via the title in the navigation bar. Before a user is verified, the navigation bar displays "Home", "Login" and "Register". Following logging in, the navigation bar displays "Characters" and "Profile".

## Features

The site contains a total of 9 pages and are as follows: 

- Home (open to everybody)
- Login (open to everybody)
- Register (open to everybody)
- Characters (requires authentication)
- Profile (requires authentication)
- View Character (requires authentication)
- Edit Character (requires authentication)
- Custom 404 (error page)
- Custom 500 (error page)