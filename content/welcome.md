Title: Welcome to smithproxy homepage!
Date: 2019-11-30 12:12
Category: intro
save_as: index.html

** THIS SITE IS IN PROGRESS OF MIGRATION FROM OLD SITE SYSTEM **  
** THANKS FOR PATIENCE **  

<a href="https://scan.coverity.com/projects/smithproxy">
  <img alt="Coverity Scan Build Status"
       src="https://scan.coverity.com/projects/19942/badge.svg"/>
</a>
<a href="https://travis-ci.org/github/astibal/smithproxy">
  <img alt="Travis-CI Build status"
       src=https://travis-ci.org/astibal/smithproxy.svg?branch=master>
</a>
  
Welcome on project homepage. **Smithproxy** is a free, open-source, fast and featured transparent proxy written in C++.

Its goal is to provide:

> * fast and easy TLS mitm capabilities including STARTTLS
* unified and strong protection for outbound TLS connections, including OCSP checks
* flexible setting management using granular policy and profile controls
* rich features, including authentication, packet inspections
* provide tools for further packet dump processing, like [pplay](https://bitbucket.org/astibal/pplay)

**Smithproxy** applications:

> * Linux router, traffic is redirected to smithproxy using TPROXY rules
* Linux server, users access smithproxy with SOCKS5
* Linux docker image, users access smithproxy with SOCKS5
