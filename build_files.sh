# build_files.sh
echo "BUILD START"

echo "INSTALLING PACKAGES ..."
python3.9 -m pip install -r requirements.txt

echo "COLLECTING STATIC FILES ..."
python3.9 manage.py collectstatic --input==yes

echo "BUILD END"
