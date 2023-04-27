# webfortune
## To set up Docker container:
`docker build -t cowsay .`\n
`docker run cowsay`\n
When you run these commands a flask server will be running on your IP on port 5000.\n
To kill the server run:\n
`docker ps`\n
`docker kill <name of container>`\n

## To run locally:\n
`python3 -m venv env`\n
`source env/bin/activate`\n
`pip install -r requirements.txt`\n
`flask run`\n
After these commands are run a web server will be running on localhost port 5000\n
To kill the server:\n
`ctrl + c`\n
