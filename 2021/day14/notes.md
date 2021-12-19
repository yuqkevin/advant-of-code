## Performance comparsion

Stuck in wong algrithm (char streaming) with generator, in-memo queue and cascade threading

Time used to get results of part1 (part2 got stuck due to huge calculation or memo usaged):
```
generator ............ 0 seconds  15 ms 213 µs 903 ns
in-memo queue ........ 0 seconds  21 ms 720 µs  66 ns
cascade threathing ... 0 seconds 588 ms 336 µs 246 ns
```

After study colleague's solution (in ruby) and changed to pair counting, it's very fast to get result:
```
python -m 2021.day14.solution part1
part1 result: 2010
part1 time used: 0 seconds 2 ms 373 µs 499 ns.

python -m 2021.day14.solution part2
part2 result: 2437698971143
part2 time used: 0 seconds 7 ms 44 µs 931 ns.
```
