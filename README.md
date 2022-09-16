# MS AUTH

## About

This is a project for classes.

It was built using **Python**, **Flask**, **SQL Alchemy**, e **Docker**. O banco de dados
é **Postgres 14**.


### Docker (API)

To run the app **MS-AUTH** use Docker:

```bash
$ docker build -f .devops/Dockerfile -t ms-auth:v1.0.0 .
```

Run Kubernetes container:

```bash
$ kubectl apply -f .devops/deploy.yml
```
