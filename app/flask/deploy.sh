#!bin/bash

pip3 freeze > requirements.txt

export PROJECT_ID=sandbox-kurihara-h
export IMAGE=cloud-run-sample

docker build -t gcr.io/${PROJECT_ID}/${IMAGE} .

docker push gcr.io/${PROJECT_ID}/${IMAGE}

gcloud run deploy ${IMAGE} --image gcr.io/${PROJECT_ID}/${IMAGE} --region=asia-northeast1 --allow-unauthenticated