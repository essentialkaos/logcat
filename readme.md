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
Usage: logcat <options> <file>...

Options:

  --follow, -f           Output appended data as the file grows
  --head, -h num         Output the first part of files
  --tail, -t num         Output the last part of files
  --grep, -g text        Filter output by grep
  --egrep, -G pattern    Filter output by egrep
  --headers, -H          Show headers if files more than 1
  --ignore-errors, -I    Don't show error messages if file not readable or not exist
  --help, --usage, -h    Show this help message
  --version, --ver, -v   Show information about version
```

#### Build Status

| Repository | Status |
|------------|--------|
| Stable | [![Build Status](https://travis-ci.org/essentialkaos/logcat.svg?branch=master)](https://travis-ci.org/essentialkaos/logcat) |
| Unstable | [![Build Status](https://travis-ci.org/essentialkaos/logcat.svg?branch=develop)](https://travis-ci.org/essentialkaos/logcat) |

#### License

[EKOL](https://essentialkaos.com/ekol)
