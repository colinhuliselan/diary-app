# Diary app

Simple app for keeping a diary. Consists of:

- `FastAPI` (`python`) backend
- `nginx` reverse proxy
- Simple `html` frontend
- `mongodb` database

## Run

- Copy `.env.template` to `.env` files in `backend` and `database` dirs.
- From root:

```
docker compose build
docker compose up
```

- Naviate to http://localhost
