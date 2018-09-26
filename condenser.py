import sys

# Get the file input, output, and number of candles to condense
try:
    lines = open(sys.argv[1], 'r').readlines()
    outfile = open(sys.argv[2], 'w')
    condensed = int(sys.argv[3])
except:
    print('usage: consenser.py infile outfile N [offset]')

# Offset is 0 by default, and can be set with an optional arg
offset = 0
try:
    offset = int(sys.argv[3])
except:
    pass

# Read all lines into a candles list
candles = []
for line in lines:
    data = line.split(',')
    candle = {}
    candle['time'] = int(data[0])
    candle['open'] = float(data[1])
    candle['high'] = float(data[2])
    candle['low'] = float(data[3])
    candle['close'] = float(data[4])
    candle['volume'] = float(data[5].strip())
    candles.append(candle)    

# Construct new candles
newcandles = []
currentline = offset
counter = 0
while currentline < len(lines) - condensed:
    candle = {}
    candle['time'] = counter
    candle['open'] = candles[currentline]['open']
    candle['close'] = candles[currentline+condensed]['close']
    candle['high'] = max(x['high'] for x in candles[currentline:currentline+condensed])
    candle['low'] = min(x['low'] for x in candles[currentline:currentline+condensed])
    candle['volume'] = sum(x['volume'] for x in candles[currentline:currentline+condensed])
    newcandles.append(candle)
    currentline += condensed
    counter += 1

# Write the new candles to the outfile
for candle in newcandles:
    outfile.write("{},{},{},{},{},{}\n".format(candle['time'], candle['open'], candle['high'], candle['low'], candle['close'], candle['volume']))
