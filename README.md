signup
`curl --location "http://127.0.0.1:8000/signup/" --header "Content-Type: application/json" --data-raw "{\"email\": \"test@test.com\", \"password\": \"123\"}"`

signin
`curl --location "http://127.0.0.1:8000/signin/" --header "Content-Type: application/json" --data-raw "{\"email\": \"test@test.com\", \"password\": \"123\"}"`

me
`curl --location 'http://127.0.0.1:8000/me/' --header 'Authorization: Bearer <access_token_from_signin>`
