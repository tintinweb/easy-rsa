EasyRSA 3rd-party package for Synology
======================================



Note - this is just a proof of concept.

+ removed --interactive from easy-rsa build scripts (easier for scripting)


Installation
============

1. upload and install EasyRSA.spk in package manager 
2. check /usr/syno/synoman/webman/3rdparty/EASYRSA 



Packaging
============

1. tgz src/EasyRSA/package/* => package.tgz 
2. tar src/EasyRSA/INFO,package.tgz,scripts  => EasyRSA.spk


TODO
====

* create simple GUI for a single root-ca based on build-ca,build-dh, build-key-server, build-key
