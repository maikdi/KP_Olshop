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
