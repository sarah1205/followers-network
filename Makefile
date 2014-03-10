init:
	pip install -r requirements.txt --use-mirrors

install:
	pip install .

test:
	nosetests tests

uninstall:
	pip uninstall followers
