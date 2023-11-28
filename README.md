Test Clickhouse Backend
===

Project to display issue [#62](https://github.com/jayvynl/django-clickhouse-backend/issues/62) 


Steps
---

Prerequisites: docker and docker compose are installed.

```shell
git clone https://github.com/ernestasga/error-clickhouse-backend-jsonfield.git
cd test-clickhouse-backend
docker-compose up -d
docker-compose run --rm backend ./prepare.sh
```

Then open http://localhost:8000/ in your browser. See the error in the console.