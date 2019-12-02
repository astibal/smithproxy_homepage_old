Title: Howto install legacy 0.8 from .deb
Date: 2019-12-02 22:00
Category: howto
tags: deb, install, howto, 0.8

# Installing Smithproxy from binary .deb packages (stable)

You can simply paste it all into shell, it will do the work.   
As of time of the writing of this howto, script is basically a bit touched Dockerfile for ubuntu docker image. You can see it online here, in my [bitbucket 0.8 repository](https://bitbucket.org/astibal/smithproxy/src/0.8/tools/docker/Dockerfile-ubuntu18.04-run) ... and maybe update it to your liking. 
```
:::text
echo "=== installing bootstrapping tools" && \
apt update && apt install -y \
wget \
python-pip dnsutils wget dnsutils

echo "=== installing dependecies"; \
apt install -y libcli1.9 libconfig++9v5 libssl1.0.0 libunwind8 python-pip && \
apt install -y iptables python-ldap python-pyparsing python-posix-ipc python-soappy python-m2crypto telnet iproute2 && \
apt install -y python3 python3-pip python3-cryptography python3-pyroute2

echo "=== Getting latest stable package names from DNS"; \
SX1=`dig +short latest.ubuntu1804.deb.smithproxy.org TXT | tr -d '"'` ; echo "marked for download: $SX1"; \
SX2=`dig +short latest-pylibconfig2.ubuntu1804.deb.smithproxy.org TXT | tr -d '"'`; echo "marked for download: $SX2"; \
wget $SX2 && dpkg -i `basename $SX2` && \
wget $SX1 && dpkg -i `basename $SX1` && \
echo "=== remove unneeded packages"; \
apt remove -y g++ gcc perl manpages && apt -y autoremove

```
> How does it work? It will install all base tools and dependencies. I am using DNS for newest package versions naming `latest.ubuntu1804.deb.smithproxy.org` will  then always resolve in freshest smithproxy .deb package URL for (in this example) Ubuntu 18.04.

# Further reading

You may want to check [Config quick-start guide](http://smithproxy.org/config-quick-start.html).
