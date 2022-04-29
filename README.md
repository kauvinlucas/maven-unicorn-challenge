# Maven Unicorn Challenge

## What's this?
This a dashboard web app that was used as submission for a visualization challenge called ["Maven Unicorn Challenge"](https://www.mavenanalytics.io/blog/maven-unicorn-challenge?utm_source=linkedin&utm_campaign=unicornchallengelaunch_jp20220415) by Maven Analytics.

The dashboard is meant to show an overview of fundings and valuations of the companies that entered the unicorn club in the first quarter of 2022. The data was represented with bar charts, heatmaps, treemaps and scatter maps.

## About the Maven Unicorn Challenge
Maven Analytics has added a new dataset to the [Data Playground](https://www.mavenanalytics.io/data-playground), containing a complete list of the world's unicorn companies. The task was to illustrate the current landscape of unicorn companies around the world, presented in the form of a single-page dashboard.

## About the app
The dashboard app was made entirely with Python, although I tweaked some of the visuals with CSS. Plotly and Pandas were the only main libraries used to make this app.

## Requirements
It's recommended to have Python +3.4. This app was built using Python 3.10.4.

## Deployment instructions
You can deploy this app with **Google Cloud App Engine** by following the instructions [here](docs/cloud-deploy.md). To deploy this app **locally**, you can follow the instructions [here](docs/local-deploy.md).

## Screenshot
![Dashboard](assets/screenshot.png)