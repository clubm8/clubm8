# clubm8

[![Build Status](https://travis-ci.org/clubm8/clubm8.svg?branch=master)](https://travis-ci.org/clubm8/clubm8)

This is an example project for clubm8. DO NOT USE THIS REPOSITORY FOR
PRODUCTION unless you generate a new SECRET_KEY in `clubm8/settings.py`!

## Requirements

* python3
* virtualenv

## Setup

```
$ virtualenv env -p python3
$ source env/bin/activate
$ git clone --recursive https://github.com/clubm8/clubm8.git
$ cd clubm8
$ pip install -r requirements.txt
```

## Running

```
$ cd <wherever_clubm8_was_cloned>
```

### Tests

```
$ ./manage.py test
```

### Import demo data

```
$ ./manage.py loaddata clubm8core/{tags,events,occurrences,plans,slots,news,special}
```

### Development server

```
$ ./manage.py runserver
```
