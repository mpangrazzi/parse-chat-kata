clean:
	pipenv --rm

install:
	pipenv install --dev

test:
	pipenv run pytest test -vv

lock:
	pipenv lock -r --pre

.PHONY: clean install test lock
