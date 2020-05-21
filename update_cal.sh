rm conferences.yml*
wget https://raw.githubusercontent.com/abhshkdz/ai-deadlines/gh-pages/_data/conferences.yml
source activate main2
python _update_cal.py
