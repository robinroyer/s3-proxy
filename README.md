
## Proxy


To mock a proxy we will build and user a container:

```
docker build -t mitmproxy-mock .
docker run -p 8080:8080 -p 8081:8081 mitmproxy-mock
```

you will see some logs on usage.


## Test proxy config


#### Boto3

- Add your account email to the script as an access key.
- Add your token to the script (from https://tasq.qarnot.com/settings/access-token)

```
pip install boto3
python boto3-proxy.py
```

#### Qarnot SDK

Add your token to the script (from https://tasq.qarnot.com/settings/access-token)
```
pip install qarnot
python qarnot-proxy.py
```

#### Qarnot SDK From env


- Add your token to the script (from https://tasq.qarnot.com/settings/access-token)

Add the correct proxuy configuration to your env vars
```
# export http_proxy="http://<user>:<pass>@<proxy>:<port>"

export http_proxy="http://localhost:8080"
export HTTP_PROXY="http://localhost:8080"
export https_proxy="http://localhost:8080"
export HTTPS_PROXY="http://localhost:8080"
```

then run your classic script

```
pip install qarnot
python qarnot-proxy-from-env.py
```