## LogCat [![Code Climate](https://codeclimate.com/github/essentialkaos/logcat/badges/gpa.svg)](https://codeclimate.com/github/essentialkaos/logcat) [![License](https://gh.kaos.io/ekol.svg)](https://essentialkaos.com/ekol)

`logcat` is utility for controllable log viewing with sudo.

### Installation

<details>
<summary><strong>From ESSENTIAL KAOS Public repo for RHEL6/CentOS6</strong></summary>
```
[sudo] yum install -y https://yum.kaos.io/6/release/i386/kaos-repo-7.2-0.el6.noarch.rpm
[sudo] yum install logcat
```
</details>

<details>
<summary><strong>From ESSENTIAL KAOS Public repo for RHEL7/CentOS7</strong></summary>
```
[sudo] yum install -y https://yum.kaos.io/7/release/x86_64/kaos-repo-7.2-0.el7.noarch.rpm
[sudo] yum install logcat
```
</details>

<details>
<summary><strong>Using install.sh</strong></summary>
We provide simple bash script `script.sh` for installing app from the sources.

```
git clone https://github.com/essentialkaos/logcat.git
cd logcat

[sudo] ./install.sh
```

If you have some issues with installing, try to use script in debug mode:

```
[sudo] ./install.sh --debug
```
</details>

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

| Repository | Status |
|------------|--------|
| Stable | [![Build Status](https://travis-ci.org/essentialkaos/logcat.svg?branch=master)](https://travis-ci.org/essentialkaos/logcat) |
| Unstable | [![Build Status](https://travis-ci.org/essentialkaos/logcat.svg?branch=develop)](https://travis-ci.org/essentialkaos/logcat) |

### License

[EKOL](https://essentialkaos.com/ekol)
