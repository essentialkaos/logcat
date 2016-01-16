### LogCat

`logcat` is utility for controllable log viewing with sudo.

#### Installation

###### From ESSENTIAL KAOS Public repo for RHEL6/CentOS6

```
yum install -y http://release.yum.kaos.io/i386/kaos-repo-6.8-0.el6.noarch.rpm
yum install logcat
```

###### Using install.sh

We provide simple bash script `script.sh` for installing app from the sources.

```
... install cracklib-check

git clone https://github.com/essentialkaos/logcat.git
cd logcat

sudo ./install.sh
```

If you have some issues with installing, try to use script in debug mode:

```
sudo ./install.sh --debug
```

#### Usage

```
```

#### Build Status

| Repository | Status |
|------------|--------|
| Stable | [![Build Status](https://travis-ci.org/essentialkaos/logcat.svg?branch=master)](https://travis-ci.org/essentialkaos/logcat) |
| Unstable | [![Build Status](https://travis-ci.org/essentialkaos/logcat.svg?branch=develop)](https://travis-ci.org/essentialkaos/logcat) |

#### License

[EKOL](https://essentialkaos.com/ekol)
