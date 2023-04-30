# build_files.sh
echo "BUILD START"

echo "Installing modules ..."
python3.9 -m pip install -r requirements.txt

echo "collecting static files ..."
python3.9 manage.py collectstatic --noinput

echo "BUILD END"
