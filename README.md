# intro-deployment-ml-model

## how to connect dvc to google cloud

Let's create a service account doing the following steps:

Enter to Menu -> APIs & Services -> Credentials
![image](https://user-images.githubusercontent.com/18086414/177219392-077c3565-d1cf-49de-8974-6551ed3cab57.png)

Now we create a service account credential.
![image](https://user-images.githubusercontent.com/18086414/177219540-042a2e1f-563c-460f-acdd-1579b5988e67.png)

Then, define the name for the service account credential.

![image](https://user-images.githubusercontent.com/18086414/177219687-f0d391f7-872d-4274-b9c8-aae836fcf683.png)

Grant this service account access to storage in the project.
![image](https://user-images.githubusercontent.com/18086414/177220397-d3d63361-75ad-4381-8c9f-990161768d70.png)

Let's create and download a json key.



Create a bucket called "model-dataset-tracker"

- Create a service account with Roles: Storage Admin, Cloud Run Admin and Service Account User.
- Download service account json
- Transform into b64 code.
- Add this code to ACtions Secrets.

Google technologies
- Google Credentials
- Google Cloud Storage
- Google Cloud Run