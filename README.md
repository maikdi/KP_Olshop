# kp_olshop

## Project setup
### Requirements 
* Node.js (preferably v16.13.0)
* Python 3.10.0 (or other Python 3 builds)
Install Node dependencies
```
npm install
```

Setting up python environment
change directory to the 'rest_api' directory and then run
```
python3 -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
<hr>

### Additional Features!
This project is also a joint project with Distributed System lecture <br>
So, as a result this app is able to send emails based on these events:
* Whenever a user checksout (Email will be sent to admin)
* Whenever admin adds a new product, all users will be informed

#### Setting up additional feature.
* Celery. 
Celery should be installed when installing from requirements.txt
* * It is recommended to use Linux environment when using Celery
* redis-server
You will need a redis-server to work with the celery. If you do not have one yet. Download it here https://redis.io/download

#### Run with additional features
* In the app directory compile vue with 
```
npm run serve
```
* Open another terminal in the same directory and run
```
cd rest_api
python3 -m venv venv
.\venv\Scripts\activate
py app.py
```
* In antoher terminal run the redis-server
* In another terminal (yes, this is the fourth terminal you must open) run
```
celery -A tasks worker -E --loglevel=INFO
```
<hr>

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
