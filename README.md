# Spyne test

## Step 1

```bash
$ poetry install
$ poetry shell
$ spoine
> my program
$ pytest
```

## Step 2

```bash
./cmd/run.sh
# maybe even run
python src/spoine/server/manage.py migrate
```

Then open:

* https://localhost:8000/
* https://localhost:8000/?wsdl
