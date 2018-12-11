import functools
import string

lengths = {step: i+61 for i, step in enumerate(string.ascii_uppercase)}

def build_prereqs(prereqs, input):
    spl = input.split()
    prereqs[spl[1]] = prereqs.get(spl[1], set()) | {spl[0]}
    if spl[0] not in prereqs:
        prereqs[spl[0]] = set()
    return prereqs

completed_steps = []
steps_in_progress = {}
time = -1
workers = 5

def assign_worker(step):
    global workers
    workers = workers - 1
    steps_in_progress[step] = 0

def finish_step(step):
    global workers
    print(workers)
    if steps_in_progress[step] == lengths[step]:
        completed_steps.append(step)
        del steps_in_progress[step]
        workers = workers + 1

def work_on_steps():
    for step in steps_in_progress:
        steps_in_progress[step] = steps_in_progress[step] + 1 

with open('input/day7.txt') as input:
    prereqs = functools.reduce(build_prereqs, input, {})

step_list = sorted((k,v) for k, v in prereqs.items())

while len(completed_steps) < len(step_list):
    for step in list(steps_in_progress):
        finish_step(step)

    for step, prereqs in step_list:
        if (
            step not in completed_steps and 
            step not in steps_in_progress and 
            set(completed_steps) >= prereqs and 
            workers > 0
        ):
            assign_worker(step)

    work_on_steps()
    time = time + 1

print(time)
