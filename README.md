# UEA_Backend with FastAPI

### Create venv - use the command:
```shell
make
```

### Or digite the command in this directore:
```bash
python3 -m venv venv
```

### For install libs:
```bash
source venv/bin/activate # Activate virtual environments 

pip install --upgrade -r requirements.txt # Install Libs
```

### Save Firebase private key in root as `firebase-key.json`

### For start this application:
```bash
source venv/bin/activate # Activate virtual environments 

python3 main.py # Start Application
```

### Others commands:
```bash
deactivate # Deactivate virtual environments

make clean # Clean Venv and caches
```


## Routes

### Home - GET
`/v1/home`

### Temperature - GET | POST
`/v1/temperatures`

### Docs (Swagger)
`/docs`