.PHONY: build

build:
	python setup.py sdist bdist_wheel

upload:
	python setup.py sdist upload -r pypihost