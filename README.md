## New York State Electricity Prediction with Neural Network
Electricity load data available from [NYISO](http://mis.nyiso.com/public/P-58Clist.htm).
Hourly weather data available from [Mesowest](https://developers.synopticdata.com/mesonet/v2/stations/timeseries/).

Implementation of linear regression referencing Stanford's [CS229 Lecture Notes](http://cs229.stanford.edu/notes2020fall/notes2020fall/cs229-notes1.pdf).

## Python
### Prerequisites
- Python 3.9+
- `numpy`
-`matplotlib`

### Prepare Data
```bash
./get_data.sh
```

### `TODO`
- [ ] Turn `datetime` and `str` object type into numeric types
- [ ] Generate the linear regression method for the first 5 years (2001 - 2006) load data
- [ ] Compute the predicted results for the 6th year (2007) and compare it with the actual load data in 2007
- [ ] Implement backpropagation neural network for prediction, with validation, following the above steps