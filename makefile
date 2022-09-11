.PHONY: check

check:
	pylint *.py
	mypy *.py
