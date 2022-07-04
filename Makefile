create_env:
	python -m venv deploy_env
	python -m pip install --upgrade pip

install_dev_requirements:
	pip install -r requirements/dev.txt

install_realpath_in_macos:
	brew install coreutils

create_env_variable:
	export GOOGLE_APPLICATION_CREDENTIALS="/Users/nelsoncardenas/Documents/GitHub/intro-deployment-ml-model/mlops-fundamentals-4224-26a7524e6dd1.json"

connect_dvc_to_datalake:
	dvc remote add dataset-track gs://model-data-tracker-775/dataset
	dvc remote add model-track gs://model-data-tracker-775/model

add_track_for_datasets:
	dvc add dataset/finantials.csv --to-remote -r dataset-track
	dvc add dataset/opening_gross.csv --to-remote -r dataset-track
	dvc add dataset/movies.csv --to-remote -r dataset-track

add_track_for_models:
	dvc add model/model.pkl --to-remote -r model-track