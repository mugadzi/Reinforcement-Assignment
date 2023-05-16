install: venv
	. venv/bin/activate; pip3 install -r requirements.txt
venv :
	test -d venv || python3 -m venv venv
run:
	python Scenario1.py
	python Scenario2.py
	python Scenario3.py
clean:
	rm -rf venv
	find -iname "*.pyc" -delete