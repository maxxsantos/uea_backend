VENV = venv

${VENV}:
	python3 -m venv $@

clean:
	rm -rf venv
	rm -rf `find -iname __pycache__`