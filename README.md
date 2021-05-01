# Web Scraping

> **Note:** All the commands should be run from the root of your project, i.e in the same directory as this **README**.

## Step 1: Development

Setup the development environment by running the following commands.

```bash
pip install pipenv

pipenv install --dev
```

Test that packages are correctly installed by running the
following.

```bash
pipenv shell

gunicorn main:app
```

You should see a link in the terminal pressing `CTRL` and clicking on the link should open a web page where you should see output in the format below.

```json
[
  {
    "status": "OPEN",
    "trail_name": "Beaver Dam"
  },
  {
    "status": "OPEN",
    "trail_name": "Briar Chapel"
  },
  ...
]
```

## Step 2: Devops/SRE

### Setup

Setup some required packages by executing the following steps:

- Install [git](https://www.atlassian.com/git/tutorials/install-git)
- Install [docker](https://docs.docker.com/get-docker/)

Start by creating an account on [CircleCI](https://circleci.com/). Make sure you connect your github account and can see the repositories on the [Projects](https://app.circleci.com/projects) page.

Create a new [Github](https://github.com/) repository, pick a name of your own chosing. In the next page, run the following commands in your terminal/cmd.

```bash
git remote add origin <copy_given_url_here>
git branch -M main
git push -u origin main
```

Go back to [CircleCI Projects](https://app.circleci.com/projects) and check whether the repository is now visible. Then click on **Set Up Project**, this will build your project, and any time you push changes to github the project will be built and run.

### Containerize

To containerize your application you will need to to setup [docker](https://docs.docker.com/get-docker/). Now from your terminal run the following.

```bash
docker build -t web-scraping .
```

This will build a docker image.
To run the image run the following.

```bash
docker run web-scraping
```

You should see output like:

```bash
"Beaver Dam" - "OPEN"
"Briar Chapel" - "OPEN"
"└ Skills Area" - "OPEN"
"└ Herndon Loop" - "OPEN"
```

## Cloud Awareness

Create an account on [heroku](https://www.heroku.com/).
Install and configure [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

Navigate to your [heroku dashboard](https://dashboard.heroku.com/apps) and create a new app.

From your command line run the following.

```bash
heroku login
```

This will authenticate you.

The run

```bash
heroku git:remote -a <your-project-name>
```

replacing `your-project-name` with the actual name of the app you created earlier in the [heroku dashboard](https://dashboard.heroku.com/apps).

Then now upload your project by pushing it to heroku.

```bash
git push heroku main
```

You should see a lengthy process, log that should end with something like

```bash
...
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 45.1M
remote: -----> Launching...
remote:        Released v4
remote:        https://<your-project-name>.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/<your-project-name>.git
   ae85864..4e63b46  master -> master
```

Now going back to your [heroku dashboard](https://dashboard.heroku.com/apps), your can click on the project then click open. This should open a link on the browser where your will see something like:

```json
[
  {
    "status": "OPEN",
    "trail_name": "Beaver Dam"
  },
  {
    "status": "OPEN",
    "trail_name": "Briar Chapel"
  },
  ...
]
```
