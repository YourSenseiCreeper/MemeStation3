coverage run --rcfile=coverageHello.coveragerc ../manage.py test tests
coverage report -m
coverage html -d coverage_html
start opera.exe %CD%/coverage_html/index.html
pause