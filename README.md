# Candlestick Chart Condenser
This is a quick and easy python3 script allowing a user to condense candlestick chart data from a CSV file.

## Example
If you have a CSV file called data.txt with minute candle data for a certain traded good, and you want to condense it into an hourly CSV, simply run the command:
`python condenser.py data.txt output.csv 60`

In addition, you can supply an optional offset. If, for example, you wanted to start on the fifth candle:
`python condenser.py data.txt output.csv 60 5`

Very simple!
