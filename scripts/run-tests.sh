#!/bin/bash
result=0
trap 'result=1' ERR

flake8 parserator_web tests && echo 'Python linting passed! 👍'
npx eslint parserator_web/static/js/*.js && echo 'JavaScript linting passed! 👍'
pytest -sxv

exit "$result"
