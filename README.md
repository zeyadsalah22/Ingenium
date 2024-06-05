# Ingenium Club Website

This is the repository for the Ingenium club website developed for the Egypt-Japan University of Science and Technology (E-JUST). The website was implemented using the Django framework, HTML, CSS, JavaScript, and Bootstrap.

## Table of Contents
- [Overview](#overview)
- [Pages](#pages)
  - [Home Page](#home-page)
  - [Committee Pages](#committee-pages)
- [Technologies Used](#technologies-used)
- [Database Models](#database-models)
- [Django Functions](#django-functions)
- [Website](#website)

## Overview
The Ingenium club website provides information about the club, its events, and its committees. It includes a general description of the club, details about the highboard, information on events like Artsmania, and an application form for new members.

## Pages

### Home Page
The Home Page includes:
- A general description and information about the club
- Information about the highboard of the club
- Details about the Artsmania event held over two years
- An application form for becoming a member of the club

### Committee Pages
Each committee (Drama, Music, Art, Photography, etc.) has its own page featuring:
- FAQs about the committee
- Photos related to the committee's activities

## Technologies Used
- Django
- HTML
- CSS
- JavaScript
- Bootstrap

## Database Models
The project uses the following database models:

### High
- **order**: IntegerField
- **image**: CharField(max_length=64, default='ingenium.jpeg')
- **name**: CharField(max_length=150)
- **position**: CharField(max_length=150)
- **info**: TextField

### Image
- **order**: IntegerField
- **image**: CharField(max_length=64)
- **category**: CharField(max_length=64)

### Question
- **order**: IntegerField
- **question**: TextField
- **answer**: TextField
- **category**: CharField(max_length=64)

## Django Functions
The project includes the following Django views and functions:

### Index View
- **URL**: `/`
- **Function**: `index`
- **Description**: Displays the home page with general club information and highboard details.

### Committee Views
Each committee has a dedicated view that displays related images and FAQs. The views are:
- `drama`
- `music`
- `art`
- `photography`
- `design`
- `media`
- `logistics`
- `hr`
- `pr`
- `literature`

All committee views follow the same pattern:
- **URL**: `/committee_name/`
- **Function**: `committee_name`
- **Description**: Displays the committee page with images and FAQs.

## Website
To visit the website, follow [this link](https://ingenium.onrender.com/).
