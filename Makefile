run:  # Run server
	uvicorn main:app --reload

lint:
	flake8 && find . -type f -name "*.py" | xargs pylint
