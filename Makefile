.PHONY: all clean

all: dist

clean:
	rm -rf build dist url2env.egg-info

dist: env/bin/python
	env/bin/python setup.py bdist_wheel --universal

upload: dist env/bin/twine
	env/bin/twine upload dist/*

env:
	virtualenv env

env/bin/python: env

env/bin/twine: env
	env/bin/pip install twine
