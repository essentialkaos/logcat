<p align="center"><a href="#readme"><img src="https://gh.kaos.st/logcat.svg"/></a></p>

<p align="center">
  <a href="https://travis-ci.com/essentialkaos/logcat"><img src="https://travis-ci.com/essentialkaos/logcat.svg"></a>
  <a href="https://essentialkaos.com/ekol"><img src="https://gh.kaos.st/ekol.svg"></a>
</p>

<p align="center"><a href="#installation">Installation</a> • <a href="#usage">Usage</a> • <a href="#build-status">Build Status</a> • <a href="#license">License</a></p>

<br/>

`logcat` is utility for controllable log viewing with sudo.

### Installation

#### From ESSENTIAL KAOS Public repository

```
sudo yum install -y yum install -y https://yum.kaos.st/get/$(uname -r).rpm
sudo yum install logcat
```

#### Using `install.sh`
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

### Usage

```
Usage: logcat {options} file...

Options

  --follow, -f           Output appended data as the file grows
  --head, -h num         Output the first part of files
  --tail, -t num         Output the last part of files
  --grep, -g text        Filter output by grep
  --egrep, -G pattern    Filter output by egrep
  --headers, -H          Show headers if more than 1 file
  --ignore-errors, -I    Don't show error messages if file isn't readable or doesn't exist
  --help, -h             Show this help message
  --version, -v          Show information about version

Examples

  logcat some-file.tar.gz
  Print some-file.tar.gz content

  logcat -f some-file.log
  Output appended to some-file.log data as the file grows

  logcat -g 'SOME_TEXT' -t 10 *.7z
  Read all 7z files, filter data by grep pattern and print only last 10 lines

```

### Build Status

| Branch | Status |
|--------|--------|
| `master` | [![Build Status](https://travis-ci.com/essentialkaos/logcat.svg?branch=master)](https://travis-ci.com/essentialkaos/logcat) |
| `develop` | [![Build Status](https://travis-ci.com/essentialkaos/logcat.svg?branch=develop)](https://travis-ci.com/essentialkaos/logcat) |

### License

[EKOL](https://essentialkaos.com/ekol)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
