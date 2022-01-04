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
* Whenever a user checksout (Email will be sent to admin) <br>
![image](https://user-images.githubusercontent.com/74812824/147832450-9ca2adba-955b-4efc-9f37-deca527868d3.png)

* Whenever admin adds a new product, all users will be informed <br>
![image](https://user-images.githubusercontent.com/74812824/147832459-64d8d6d4-f5a7-475e-a906-fdcd3da9935f.png)

Example of an email sent by flask <br>
![image](https://user-images.githubusercontent.com/74812824/147832491-a78b01b2-3a9c-44ac-a9c4-0451808e3d50.png)

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
