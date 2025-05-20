# fastrtc-whisper-localllm


## Generate cert
```
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```
Place the cert to "./cert"


## Config the `.env`
```
cp .env.example .env
```


## Run!
```
python main.py
```
Goes to port 7861 to check out the demo!
