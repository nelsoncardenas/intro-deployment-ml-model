create_env:
	python -m venv deploy_env
	python -m pip install --upgrade pip

install_dev_requirements:
	pip install -r requirements/dev.txt