# API example application

	Simple example of application providing API to manage short notes / messages. Messages can be 
	read by anyone but edited only by authorised users.

## Deployment

	App is deployed at: https://daft-evox.herokuapp.com/

# API

	The API to the example app is described below.

## Get list of all messages

### Request

`GET /messages`

	curl -X 'GET' 'https://daft-evox.herokuapp.com/messages' -H 'accept: application/json'


### Response body

	[
	  {
	    "MessageID": 13,
    	"Body": "Henlo Worlnd",
 	   "Views": 0
  	},
  	{
   	 "MessageID": 12,
    	"Body": "Hallo Welt!",
    	"Views": 16
  	}
	]

## Get message specified by id

### Request

`GET /messages/{msg_id}`

	curl -X 'GET' 'https:/curl -X 'GET' \
 	'https://daft-evox.herokuapp.com/messages/13' \
  	-H 'accept: application/json'


### Response body

	{
  	"MessageID": 13,
  	"Body": "Henlo Worlnd",
  	"Views": 1
	}


## Get message specified by id

### Request

`GET /messages/{msg_id}`

	curl -X 'GET' 'https:/curl -X 'GET' https://daft-evox.herokuapp.com/messages/13 -H 'accept: application/json


### Response body

	{
	  "MessageID": 13,
	  "Body": "Henlo Worlnd",
 	  "Views": 1
	}


## Authorize to have access to create, edit and delete messages. Token is valid for 30 minutes

### Request

`POST /token`

	curl -X 'POST' https://daft-evox.herokuapp.com/token -H 'accept: application/json' -H 'Content-Type: application/x-www-form-urlencoded' -d 'grant_type=password&username=admin&password={Iaintgonnatellyou}&scope=&client_id=&client_secret='


### Response body

	{
	  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYyMTYzNDgzM30.YkaDyfywJRu739eTJHUGVUQJ-HkVIgG11VZQ7X05klM",
 	  "token_type": "bearer"
	}


## Create a new message

### Request

`POST /messages/create`

 	curl -X 'POST' 'https://daft-evox.herokuapp.com/messages/create?message_body=witam' -H 'accept: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYyMTYzNTA0MH0.aB_GhVF2HUE6WrV6i3-HX_OA4VPMveyL8bW3JcGueOE' -d

#### Request URL

https://daft-evox.herokuapp.com/messages/create?message_body=witam


### Response body

{
  "New Message Created with ID:": 15,
  "content": "witam"
}

## Edit message

### Request

`PATCH /messages/edit/{msg_id}`

curl -X 'PATCH' \
  'https://daft-evox.herokuapp.com/messages/edit/15?message_body=Guten%20Tag' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYyMTYzNTA0MH0.aB_GhVF2HUE6WrV6i3-HX_OA4VPMveyL8bW3JcGueOE'

Request URL
https://daft-evox.herokuapp.com/messages/edit/15?message_body=Guten%20Tag

### Response body

{
  "MessageID": 15,
  "Body": "Guten Tag",
  "Views": 0
}

## Delete message

### Request

`DELETE /messages/delete/{msg_id}`

curl -X 'DELETE' \
  'https://daft-evox.herokuapp.com/messages/delete/15' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYyMTYzNTA0MH0.aB_GhVF2HUE6WrV6i3-HX_OA4VPMveyL8bW3JcGueOE'

Request URL
https://daft-evox.herokuapp.com/messages/delete/15

### Response body
[
  "Message Successfully Deleted"
]