## Deploying the app locally

### Creating a virtual environment
First of all, it's recommended that you create a Python virtual environment for this app. Just follow the instructions below:
1. Clone and go to this repository
```
git clone https://github.com/kauvinlucas/maven-unicorn-challenge.git
cd maven-unicorn-challenge
```

2. Create a new folder named `env`:
```
mkdir env
```

3. Create the virtual environment using the virtualenv library
```
python -m venv env
```

4. Activate the environment:
* (Windows users) Run the following command:
```
env\Scripts\activate.bat
```

* (Linux/Mac user) Run the following command:
```
source env/bin/activate
```

5. Finally, install the required libraries:
```
pip install -r requirements.txt
```

Once you are done with the app, run `deactivate` in the terminal to deactivate the environment. To delete the environment, just delete the `env` folder:
```
rm -r env
```

### Deploying the app
To deploy the app:
```
python app.py
```

Once deployed, to the http://localhost:8050 to see the dashboard.