export PYTHONPATH=${PYTHONPATH}:$PWD/../testsuite-site/:$PWD/../
export DJANGO_SETTINGS_MODULE=testsuite.settings

python manage.py test --verbosity=3