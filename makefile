include .env
export $(shell sed 's/=.*//' .env)

.venv: requirements.txt
	python -m venv $@
	$@/bin/pip install -r $<

tweet: .venv
	.venv/bin/python src/twitter_db.py

clean:
	rm -rf .venv
