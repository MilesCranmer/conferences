# Generate a Google calendar of top AI/ML conferences


To use: edit the selection in `top_conferences.csv`, and change the line in `update_cal.sh`:
```
source activate main2
```
to whatever python environment you use (or delete this line), then run `./update_cal.sh`. Import the generated `calendar.csv` into your Google Calendar.
