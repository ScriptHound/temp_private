+picture backend

Deploy

write .env and alembic.ini files for your server as them written in examples

Install docker
```
sudo apt install docker.io docker-compose
```

Start docker
```
sudo systemctl start docker
```
Also, dont forget to update firewall rules if needed.
At least some issues were met while deploying with firewalld.

Start service with Docker
```
docker-compose up --build
```

Don't forget to run migrations against db:
at docker backend container
```
docker exec -it <container name> bash
alembic upgrade head
```
or outside docker container

```
alembic upgrade head
```


If you like tmux sessions or just want to launch server with no container
just run make:
```
make run_prod
```

Run tests if needed (requires python venv)
```
make run_tests
```

If you want to see service in action you can use
demonstration.py script as follows
```
python demonstration.py --address "127.0.0.1" --port "80"
```

Common issues:

Access denied upon db/ directory
```
(CAUTION MIGHT BE DANGEROUS)
sudo chmod -R a+rwx db/
```
