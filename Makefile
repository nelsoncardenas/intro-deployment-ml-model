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
	dvc add dataset/finantials.csv
	dvc add dataset/opening_gross.csv
	dvc add dataset/movies.csv

add_track_for_models:
	dvc add model/model.pkl

push_track_for_datasets:
	dvc push dataset/finantials.csv -r dataset-track
	dvc push dataset/opening_gross.csv -r dataset-track
	dvc push dataset/movies.csv -r dataset-track

push_track_for_models:
	dvc push model/model.pkl -r model-track

bad_add_track_for_datasets:
	dvc add dataset/finantials.csv --to-remote -r dataset-track
	dvc add dataset/opening_gross.csv --to-remote -r dataset-track
	dvc add dataset/movies.csv --to-remote -r dataset-track

create_dvc_dag:
	dvc run -n prepare -o dataset/full_data.csv python src/prepare.py
	dvc run -n training -d dataset/full_data.csv python src/train.py