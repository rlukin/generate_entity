## Simple fake data generator
Python script for generating Gbs of csv based on Faker. Main problem of Faker -
it's slow.


## Dependencies
 - numpy

## How to use
You should pass as argument desired size of a file and redirect script output
```
generate_entity git:(master) $ python generate.py 1000 > out     
generate_entity git:(master) $ python generate.py 10000 | pv > /dev/null
10,2GiB 0:01:42 [ 102MiB/s] [    <=>                                    ]    
generate_entity git:(master) $ python generate.py 1000 | pv > out    
1007MiB 0:00:10 [94,2MiB/s] [                                       <=> ]

```
