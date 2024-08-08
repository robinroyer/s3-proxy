
### Proxy


to mock a proxy we will build and user a container:

```
docker build -t mitmproxy-mock .
docker run -p 8080:8080 -p 8081:8081 mitmproxy-mock

```


### test proxy


Add your token to the script (from https://tasq.qarnot.com/settings/access-token)
```
pip install qarnot
python qarnot-proxy.py
```