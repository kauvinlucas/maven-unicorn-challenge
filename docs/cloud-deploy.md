## Deploying the app to google cloud

You can deploy this app to the cloud with the App Engine service. It assumes that you have created the project and you have installed Google Cloud CLI.

Deployment steps:

1. Clone and go to this repository
```
git clone https://github.com/kauvinlucas/maven-unicorn-challenge.git
cd maven-unicorn-challenge
```

2. Deploy the app. Follow the prompts as required:
```
gcloud init
gcloud app deploy
```