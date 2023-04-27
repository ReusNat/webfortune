# webfortune
## To set up Docker container:
`docker build -t cowsay .`
`docker run cowsay`
When you run these commands a flask server will be running on your IP on port 5000.
###To kill the server run:
```
docker ps
docker kill <name of container>
```
## To run locally:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
flask run
```
After these commands are run a web server will be running on localhost port 5000
###To kill the server:
`ctrl + c`
