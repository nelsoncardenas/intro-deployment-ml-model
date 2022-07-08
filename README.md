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

- step 1:

  - ![image](https://user-images.githubusercontent.com/18086414/177220527-06e56f78-75b4-47ea-ab76-6e1adedd1960.png)

- step 2:

  - ![image](https://user-images.githubusercontent.com/18086414/177220602-397172ae-5264-4e3d-ad3b-3befd2c6b089.png)

- step 3:
  - ![image](https://user-images.githubusercontent.com/18086414/177220680-bbdd4289-820e-4591-a944-003ad7c7331a.png)

Create a bucket called "model-dataset-tracker"

- Create a service account with Roles: Storage Admin, Cloud Run Admin and Service Account User.
- Download service account json
- Transform into b64 code.
- Add this code to ACtions Secrets.