## Deploying the app locally

### Creating a virtual environment
It is recommended that you create a Python virtual environment for this app. Just follow the instructions below:
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
* (Windows users):
```
env\Scripts\activate.bat
```

* (Linux/Mac users):
```
source env/bin/activate
```

5. Finally, install the required libraries:
```
pip install -r requirements.txt
```

Once you are done with the app, run `deactivate` in the terminal to deactivate the environment. To delete the environment after deactivation, just delete the `env` folder:
```
rm -r env
```

### Deploying the app
To deploy the app:
```
python main.py
```

Once deployed, go to the http://localhost:8080 in your browser to see the dashboard.