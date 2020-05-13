# AQI Air Quality Index
### About ###
Download and store the Air Quality Index Dataset as csv using Python with the apis used in
[National Air Quality Index](https://app.cpcbccr.com/AQI_India)

### How to use ? ###
* Set Hour, Year, Month, Starting and ending day of the month in `AQI.py` file
```
hour = 15
year = 2020
month = 4
s = 1
e = 0 or monthrange(year, month)[1]
```
* Run the script
```
py AQI.py
```
* After retrieval it will saved as `AQI.csv` for given period of time

(check the above `AQI.csv`)
