<p align="center"><a href="#readme"><img src="https://gh.kaos.st/logcat.svg"/></a></p>

<p align="center">
  <a href="https://github.com/essentialkaos/logcat/actions"><img src="https://github.com/essentialkaos/logcat/workflows/CI/badge.svg" alt="GitHub Actions Status" /></a>
  <a href="#license"><img src="https://gh.kaos.st/apache2.svg"></a>
</p>

<p align="center"><a href="#installation">Installation</a> • <a href="#usage">Usage</a> • <a href="#build-status">Build Status</a> • <a href="#license">License</a></p>

<br/>

`logcat` is utility for controllable log viewing with sudo.

### Installation

#### From ESSENTIAL KAOS Public repository

```bash
sudo yum install -y https://yum.kaos.st/kaos-repo-latest.el$(grep 'CPE_NAME' /etc/os-release | tr -d '"' | cut -d':' -f5).noarch.rpm
sudo yum install logcat
```

#### Using Makefile and Git

```bash
git clone https://kaos.sh/logcat.git
cd logcat
sudo make install
```

### Usage

```
Usage: logcat {options} file…

Options

  --follow, -f           Output appended data as the file grows
  --head, -h lines       Output the first part of files
  --tail, -t lines       Output the last part of files
  --grep, -g text        Filter output by grep
  --egrep, -G pattern    Filter output by egrep
  --headers, -H          Show headers if more than 1 file are given
  --no-color, -nc        Disable colors in output
  --help, -h             Show this help message
  --version, -v          Show information about version

Examples

  logcat some-file.tar.gz
  Print some-file.tar.gz content

  logcat -f some-file.log
  Output appended to some-file.log data as the file grows

  logcat -g 'SOME_TEXT' -t 10 *.7z
  Read all 7z files, filter data by grep pattern and print only last 10 lines lines
```

### Build Status

| Branch | Status |
|--------|--------|
| `master` | [![CI](https://kaos.sh/w/logcat/ci.svg?branch=master)](https://kaos.sh/w/logcat/ci?query=branch:master) |
| `develop` | [![CI](https://kaos.sh/w/logcat/ci.svg?branch=master)](https://kaos.sh/w/logcat/ci?query=branch:develop) |

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
