.PHONY: build

build:
	python setup.py sdist bdist_wheel

upload:
	python setup.py sdist bdist_wheel upload -r https://pypi.21nmc.com/simple/