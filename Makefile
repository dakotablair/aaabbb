.DEFAULT_GOAL := help
.PHONY: coverage deps help lint publish test

coverage:  ## Run tests with coverage
	coverage erase
	coverage run --include=aaabbb/* -m pytest -ra
	coverage report -m

deps:  ## Install dependencies
	pip install black coverage flake8 flit mccabe mypy pylint pytest tox

lint:  ## Lint and static-check
	flake8 aaabbb
	pylint aaabbb
	mypy aaabbb

publish:  ## Publish to pypi
	flit publish

publish-test:  ## Publish to pypi test repository
	flit publish --repository pypitest

test:  ## Run tests
	pytest -ra