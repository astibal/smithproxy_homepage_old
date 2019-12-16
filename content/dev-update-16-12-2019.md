Title: Smithproxy weekly update 2019 Dec/2,3c
Date: 2019-12-16
Category: news
tags: news, patreon, devel

 
First of all, apologies for my delay in publishing this update. Too much on the plate last weeks. But there is at least more to tell, right? :) So let's get it started.

## [SOLVED] smithproxy 2k20 problem
The end of life of most important components in many (not only open-source) projects is at the door. There is still whole lot of maintainers scratching their heads in a painful process of moving on. We all love our already existing code which *works*, is *well tested* and in fact there should be no real reason to change it. Unless somebody makes you.  

**Smithproxy is ready**

* **python3 only** scripting  
  Deprecated libraries were *removed* and replaced with recent ones (thanks *SOAPpy* for a good service, welcome *Spyne* aboard!)

* linked to **OpenSSL 1.1.1**   
  Welcome *TLS1.3*, and much better API. This was a major task to do, migrating was **not easy, but worth it**   

* big code cleanup - using C++17 features  
  Reviewed code, C parts were reworked, old C++ code improved. Honestly, I am looking forward for C++20 and co-routines!


## [IN PROGRESS] what am I up to

* CLI saving/modifying features
  Smithproxy should be able to deliver firewall-like CLI experience. Viewing, inspecting live elements and aspect of the system. This is mostly there. 
  You are maybe aware of previously announced wide improvements of logging, which is vital part of CLI interface of decent firewalling system.  
  But we need to modify **on the fly** internal variables, and automatically reflect these by refreshing others. For example, modifying port-object, all policies 
  using it should reload it. Deleting such an object should not be allowed, because it's used. And so on.  
  Saving running configuration into file seems compared to above as a relatively simple task then. 
  
* Signature reload
  Smithproxy has to support changes in signature base, without restarting its process. Pointers will be reworked to use shared_ptr and weak_ptr. Or maybe something else, to drop signatures only when it's possible. Some versioning should be there, too.

* OCSP/CRL async IO
  There is a new piece of code (see below) which will help with this one.
  

## [NEWS] Git highlights, development update

### Cpp17 merged to Master
This is big one. It took some months to clean-up code and move it to decent C++11 - C++17 standard. Master is currently main development codebase. 

### LTO - link-time optimization 
... enabled by default for *Release* builds.

### Coverity - Static Code Analysis
Apart from that, I took an opportunity to use [Coverity scan](https://scan.coverity.com/). It's a great tool, and helped me to dissect code mistakes and helped to fix them. I really thank you, [Synopsis](https://www.synopsys.com) to offer this service for free. That's something.  

If you have not noticed, here is small icon indicator:  
<a href="https://scan.coverity.com/projects/smithproxy">
  <img alt="Coverity Scan Build Status"
       src="https://scan.coverity.com/projects/19942/badge.svg"/>
</a>  
Current defect density of 0.21 is good. I am not satisfied yet, but we are getting closer. 

**EDIT:** Coverity Scan site is currently *broken*. It does analyze projects and it's already 2 weeks.

### New Async IO
This is quite important addition to the code. socksServerCX class was already using precursor of this addition for asynchronous DNS queries, but it wasn't really nice code and it was too specific. I rewrote it, made it *very* generic, and replaced DNS query code with it. It worked at first attempt! Development is sometimes sooo rewarding :-).

This is only thing necessary to implement asynchronous DNS query.  

Implentation: constructor takes owner hostCX to *"**tap** -- freeze IO"*, and optional callback (std::function type). If callback is not set, owner must be checking status himself.
```
:::c++
class AsyncDnsQuery : public AsyncSocket<std::pair<DNS_Response *, int>> {
public:
    explicit AsyncDnsQuery(baseHostCX* owner, callback_t callback = nullptr):
            AsyncSocket(owner, callback) {}
    using dns_response_t = std::pair<DNS_Response *, int>;

    task_state_t update() override {
        response = DNSFactory::get().recv_dns_response(socket(),0);
        return task_state_t::FINISHED;
    }

    dns_response_t& yield () override {
        return response;
    }

private:
    dns_response_t response {nullptr, -1};
    logan_lite log = logan_lite("com.dns.async");
};
```
And amusingly tiny use from actual code needing it:

```
:::c++
// ...
int dns_sock = DNSFactory::get().send_dns_request(fqdn, A, nameserver);
if(dns_sock) {
    _dia("dns request sent: %s", fqdn.c_str());

    using std::placeholders::_1;
    async_dns_query = new AsyncDnsQuery(this, std::bind(&socksServerCX::dns_response_callback, this, _1));  
                                        // ^- call this->dns_response_callback
    async_dns_query->tap(dns_sock);     // actually freezing associated hostCX IO (which is _this_)
                                        // freezing is optional, in this DNS case it's mandatory, though
// ...
```

Sorry for a small excursion into smithproxy C++ code. Maybe someone finds it interesting.

### New Sites

Smithproxy and PPlay have got a new sites. Joomla is gone, replaced by static pages only.  
Why? **Because I am not joomla guy**. I wanted to like it, but it's too... everything. Currently I am using pelican, python static site generator. It's good for the purpose it seems.   

  

# Next steps, goals

## 0.9 - upcoming release

We are close to **0.9 release**. There 3 things blocking this release:  

* CLI save/modify project (in progress)
    * partly blocked by signature versioning mechanism (tbd)
* Asynchronous OCSP/CRL download (in progress)
* iptables -j REDIRECT support for OUTPUT chain, to support locally originated traffic (tbd)
* new argument option --one-arm, which would just run SOCKS and REDIRECT threads (tbd)

Now the question: can I make it till the end of year? Maybe. But more likely, 0.9 will be released in January/February 2020. Once finished with projects above, there will be testing phase ongoing, trying to catch and iron out as many issues as possible before release.

## 1.0 scheduling

**Version 1.0** will come later, in Q2 2020. This seems quite early after 0.9. Well, there is couple of features which are already partly implemented, but not finished, but they are not really intended to take place in 0.9.

Assorted (and possibly incomplete) list of features blocking 1.0 release

* All 0.9 features, obviously
* Python in-band scripting (intro code)
* binary capture files - current text ones are performance killer (good code foundation with ltventry header, having compatible python module ready, too)
* better authentication portal + new authentication options (ie SAML). (intro code in different project)
  
  
# Conclusion & thank you
Thank you for reading this rather longer update. As you noticed, it's placed already outside patreon site. I am testing which medium is better fits the community.  

Anyway, speaking of community: it's always good to hear from you. Come over to smithproxy [discord channel](https://discord.gg/vf4Qwwt), or [drop us a line](mailto:support@smithproxy.org)! 

So, till next time!
- Ales
