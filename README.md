# Have I got everything (HIGE) server

A REST API for Have I got everything app.

## Local development

Prerequisites: Docker

Copy `.env.example` to `.env` and fill the data out.

Install dependencies, and run the Docker container:

```bash
make up
```

Run migrations:

```bash
make migrate
```

Start the server:

```bash
make start
```
