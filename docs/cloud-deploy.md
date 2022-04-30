## Deploying the app to Google Cloud

You can easily deploy this app to the cloud with the [App Engine](https://cloud.google.com/appengine/) service from Google Cloud. It assumes that you already have a project, a billing account and Google Cloud CLI installed in your machine.

Deployment steps:

1. Clone this repository and go to the root folder:
```
git clone https://github.com/kauvinlucas/maven-unicorn-challenge.git
cd maven-unicorn-challenge
```

2. Deploy the app. Follow the prompts as required:
```
gcloud init
gcloud app deploy
```

Once successfully deployed, use the command `gcloud app browse` to open the app in your browser.