# LAP 4 Final Project - TwigElites 

## Table of Contents

- [Description](#description)
- [Links](#links)
- [Team Organisation](#team-organisation)
- [Installation & Usage](#installation--usage)
- [Technologies](#technologies)
- [Testing](#testing)
- [File Structure](#file-structure)
- [Routes](#routes)
- [Contributors](#contributors)


## Description
TwigElites is a fullstack project that aims to ...

## Links
Client deployed via [Netlify]()  
Server deployed via [Heroku]()  
Final presentation available on [Canva]()  
Initial pitch and MVP available on [Gist](https://docs.google.com/presentation/d/16tDXMa6T90nQuIeHiOVL1EjXnzEruMd3iTHaqYEd8R8/edit#slide=id.g1475814baf8_2_106)  
Planning and delivery on [Trello](https://trello.com/b/TGevNNhf/lap4-project)
Wireframes designs on [Figma](https://www.figma.com/file/Fmrp2VgyvgsnlRUpHIqdQU/Untitled?node-id=0%3A1)  

## Team Organisation

| Team Member     | Role |
|----------|------|
| [Reece Thatcher]()    | Back End Developer    |
| [Florencia Pezcara]() | FullStack Developer   |
| [Saamiya Yousuf]()   | Back End Developer and Testing      |
| [Taro Schenekr]()  | Front End Developer and Testing    |


## Installation and Usage
To run locally:  

Server:
1. Run `cd server` in terminal to enter server directory
2. Run `pipenv shell` to enter virtual enviroment
3. Run `pipenv install` to install all dependencies
4. Run `pipenv run start` to start Flask App

## Technologies

What technologies we used in the backend

![Flaks](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white) ![Postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white) ![Git](https://img.shields.io/badge/-Git-%23F05032?style=flat&logo=git&logoColor=%23ffffff) ![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github)![VS Code](http://img.shields.io/badge/-VS%20Code-007ACC?style=flat&logo=visual-studio-code&logoColor=ffffff) ![Markdown](https://img.shields.io/badge/-Markdown-000000?style=flat&logo=markdown)

## Testing
- `git checkout testing` -> this branch is used for testing
- Whilst in the main folder:
    - `pipenv run shell`
    - `pipenv run test`

## File Structure

File structure for our `app` folder:

- app
    - database
        - db.js
    - models
        - twiglet.js
        - user.py
    - routes
        - auth.js
        - main.js
        - socket_io.py
        - twiglet.py
    - __init__.py

## Routes

#### All of TwigElites routes - GET requests

| **URL**        | **HTTP Verb** | **Action**     |
| -------------- | ------------- | -------------- |
| /              | GET           | homepage       |
| /twiglets      | GET           | gets all twiglets |
| /twiglets/twiglet_id  | GET    | gets twiglets by id |
| /twiglets/user/id  | GET    | gets all twiglets by user from id |
| /auth/users    | GET            | get users who have an account |

