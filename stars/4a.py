import itertools
import re
import pprint

shift_change_regex = re.compile(
    r'\[(?P<timestamp>.*)\] Guard #(?P<guard>\d*) begins shift'
    )

nap_regex = re.compile(
    r'\[(?P<timestamp>\d*-\d*-\d* 00:(?P<min>\d\d))\] (?P<status>.*)'
    )

def is_shift_change(log):
    return bool(shift_change_regex.match(log))

def nap_dict(chunk_iter):
    result = {}
    for shift_change, guard_chunk in chunk_iter:
        assert shift_change
        last_change = next(guard_chunk)
        for last_change in guard_chunk:
            pass
        # print(last_change)
        guard = int(shift_change_regex.match(last_change).group('guard'))
        shift_change, nap_chunk = next(chunk_iter)
        assert not shift_change
        for log in nap_chunk:
            mo = nap_regex.match(log)
            assert mo.group('status') == 'falls asleep'
            start = int(mo.group('min'))
            log = next(nap_chunk)
            mo = nap_regex.match(log)
            assert mo.group('status') == 'wakes up'
            end = int(mo.group('min'))
            result[guard] = result.get(guard, []) + [range(start, end)]
    return result

with open('input/day4.txt') as input:
    logs = sorted(log for log in input)
# pprint.pprint(logs)

nap_map = nap_dict(itertools.groupby(logs, is_shift_change))

def nap_total(tup):
    _guard, naps = tup
    return sum( len(nap) for nap in naps)

sleepiest_guard, sg_naps = max(nap_map.items(), key=nap_total)
print(sleepiest_guard)

flat_naps = list(itertools.chain.from_iterable(sg_naps))
sleepiest_minute = max(set(flat_naps), key=flat_naps.count)
print(sleepiest_minute)
print(sleepiest_guard * sleepiest_minute)




