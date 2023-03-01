# TD7A4

**CCC2**

## Context

Build a docker stack based on a Flask app and MongoDB images (very ugly btw, no css or tag, just to understand docker and its functionalities)

## Dependencies

- docker, docker-compose plugin

## Configure environment

```bash
# Create a volume to save our data
docker create volume flask_mongo
```

## Launch the stack

```bash
# Launch the server
docker compose up
```

The flask app is available on `http://localhost:5000`, you can go to `/text` endpoint to check the content of the fiel `text-content.txt`, you can change it to anything you want, it will update the content on the web app by refreshing it.

