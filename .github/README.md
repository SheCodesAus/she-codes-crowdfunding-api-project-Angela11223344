# Project title: 'MichelangLEGO Designs'
# Life-sized Lego
​
Donate your old lego bricks to build life-sized things! (Think the pyramids, Big Ben, a space rocket...etc)
Target audience:
Anyone from ages 4 - 99.
--> Parents who are tired of standing on/hoovering up pieces of lego.
--> Grandparents who have downsized and no longet have space to store lego.
--> Children who want to make some space for more new lego/cooler sets.
--> Adults who want to make space for more new lego/cooler sets.

​
## Features

--> Create a user account
--> Update the information in your user account
--> Create a project
--> Submit a pledge to your chosen project
--> Search for keywords in 'Project List'
--> Search for keywords in 'Pledge List'
​
### User Accounts
​
- [X] Username: Rusty
- [X] Email Address: RustyDog@mail.com
- [X] Password: dog
​
### Project
​
- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
- Pledge
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
- User
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
​
### Implement suitable permissions
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [X] Limit who can create --> Only a logged in user can create a new project
  - [X] Limit who can retrieve --> Anyone can have a look at the projects
  - [X] Limit who can update --> Only the creator of the project can update
  - [X] Limit who can delete --> Only the creator of the project can delete
- Pledge
  - [X] Limit who can create --> A logged in user can create a pledge for a project
  - [X] Limit who can retrieve --> Anyone can have a look at the list of pledges
  - [X] Limit who can update --> Only the creator of the pledge can update
  - [X] Limit who can delete --> Only the creator of the pledge can delete
- Pledge
  - [ ] Limit who can retrieve
  - [ ] Limit who can update
  - [ ] Limit who can delete
​
### Implement relevant status codes
​
- [ ] Get returns 200
- [ ] Create returns 201
- [X] Not found returns 404
​
### Handle failed requests gracefully 
​
- [X] 404 response returns JSON rather than text
​
### Use token authentication
​
- [X] impliment /api-token-auth/
​
## Additional features
​
- [X] Search bar.
​
Implement a search bar so that users can search by project name keyword.
​
- [X] Update password.
​
Allow users to update their passwords.
​
- [ ] {Title Feature 3}
​
{{ description of feature 3 }}
​
### External libraries used
​
- [X] django-filter --> Used to create search bar for 'Project List' and 'Pledge List'. 
​
​
## Part A Submission
​
- [ ] A link to the deployed project.
- [ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a token being returned.
- [ ] Your refined API specification and Database Schema.
​
### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
​
1. Create User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"email": "not@myemail.com",
	"password": "not-my-password"
}'
```
​
2. Sign in User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"password": "not-my-password"
}'
```
​
3. Create Project
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/projects/ \
  --header 'Authorization: Token 5b8c82ec35c8e8cb1fac24f8eb6d480a367f322a' \
  --header 'Content-Type: application/json' \
  --data '{
	"title": "Donate a cat",
	"description": "Please help, we need a cat for she codes plus, our class lacks meows.",
	"goal": 1,
	"image": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Dollar_bill_and_small_change.jpg",
	"is_open": true,
	"date_created": "2023-01-28T05:53:46.113Z"
}'