echo " BUILD START"
python 3.9 -m pip install -r requirments.txt
python manage.py collectstatic --noinput --clear
echo " BUILD END"