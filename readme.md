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

If you like tmux sessions or just want to launch server with no container
just run make:
```
make run_prod
```

Run tests if needed (requires python venv)
```
make run_tests
```
 
