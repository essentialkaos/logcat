<p align="center"><a href="#readme"><img src=".github/images/card.svg"/></a></p>

<p align="center">
  <a href="https://github.com/essentialkaos/logcat/actions"><img src="https://github.com/essentialkaos/logcat/workflows/CI/badge.svg" alt="GitHub Actions Status" /></a>
  <a href="#license"><img src=".github/images/license.svg"/></a>
</p>

<p align="center"><a href="#installation">Installation</a> • <a href="#usage">Usage</a> • <a href="#build-status">Build Status</a> • <a href="#license">License</a></p>

<br/>

`logcat` is utility for controllable log viewing with sudo.

### Installation

#### From ESSENTIAL KAOS Public repository

```bash
sudo yum install -y https://pkgs.kaos.st/kaos-repo-latest.el$(grep 'CPE_NAME' /etc/os-release | tr -d '"' | cut -d':' -f5).noarch.rpm
sudo yum install logcat
```

#### Using Makefile and Git

```bash
git clone https://kaos.sh/logcat.git
cd logcat
sudo make install
```

### Usage

<img src=".github/images/usage.svg" />

### Build Status

| Branch | Status |
|--------|--------|
| `master` | [![CI](https://kaos.sh/w/logcat/ci.svg?branch=master)](https://kaos.sh/w/logcat/ci?query=branch:master) |
| `develop` | [![CI](https://kaos.sh/w/logcat/ci.svg?branch=master)](https://kaos.sh/w/logcat/ci?query=branch:develop) |

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
