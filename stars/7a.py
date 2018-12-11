import functools

def build_prereqs(prereqs, input):
    spl = input.split()
    prereqs[spl[1]] = prereqs.get(spl[1], set()) | {spl[0]}
    if spl[0] not in prereqs:
        prereqs[spl[0]] = set()
    return prereqs
completed_steps = []

with open('input/day7.txt') as input:
    prereqs = functools.reduce(build_prereqs, input, {})

step_list = sorted((k,v) for k, v in prereqs.items())

while len(completed_steps) < len(step_list):
    completed_steps.append(
        next(k for k,v in step_list 
            if k not in completed_steps and set(completed_steps) >= v
        )
    )

print(''.join(completed_steps))

