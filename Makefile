setup:
	( \
		python3 -m venv ./venv; \
		. venv/bin/activate; \
		pip install --upgrade pip setuptools wheel; \
		pip install -r requirements.txt; \
	)

update:
	( \
		. venv/bin/activate; \
		pip install --upgrade pip setuptools wheel; \
		pip install -r requirements.txt; \
	)

clean:
	isort .
	black .
