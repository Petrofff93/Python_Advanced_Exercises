jobs = [int(x) for x in input().split(', ')]
needed_idx = int(input())

target_num = jobs[needed_idx]
jobs_count = 0

while jobs:
    if min(jobs) <= target_num:
        jobs_count += min(jobs)
        jobs.remove(min(jobs))
    else:
        break

print(jobs_count)


