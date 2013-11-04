EasyRSA 3rd-party package for Synology
======================================



Note - this is just a proof of concept.

+ removed --interactive from easy-rsa build scripts


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
* imporove GUI
* basedir restriction / cmd restriction for php-cli



Notes
=====

* certificate icon taken from: http://www.softicons.com/free-icons/toolbar-icons/diagram-icons-by-double-j-design/certificate-icon  // License:CC as of 04.Nov.2013
