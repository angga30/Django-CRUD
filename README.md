# bsm_web: <img src="https://travis-ci.org/scottx611x/bsm_web.svg?branch=master"/> [![Sauce Test Status](https://saucelabs.com/buildstatus/scottx611x)](https://saucelabs.com/u/scottx611x)

<div align="center">
  <a href="https://saucelabs.com/u/scottx611x">
    <img src="https://saucelabs.com/browser-matrix/scottx611x.svg" alt="Sauce Test Status"/>
  </a> 
</div>

### A basic Django CRUD app to keep track of BSM Project Sample data.

## Prereqs:
- `git`
- `pip`
- `python 2.7.X or 3.4.X`
- `virtualenv` (optional)
- `virtualenvwrapper`

## Installation:
- `mkvirtualenv bsm && workon bsm` 
- `git clone https://github.com/scottx611x/bsm_web.git && cd bsm_web`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`
- Check out the app @ http://localhost:8000
