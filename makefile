WORKING_DIR=.
ENV_NAME=playground

all: chdir
	python setup.py sdist bdist_wheel

chdir:
	cd $(WORKING_DIR)

clean:
	rm -rf ./build
	rm -rf ./dist

upload_test: clean all
	twine upload --repository testpypi dist/*

test: chdir
	pwd
	echo $PATH
