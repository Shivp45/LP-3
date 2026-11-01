# Job Sequencing with Deadlines using Greedy Method

def job_sequencing(jobs):

    # Sort jobs according to profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)

    # Create empty time slots
    slots = [None] * max_deadline

    total_profit = 0

    # Schedule jobs
    for job in jobs:

        job_id, deadline, profit = job

        # Find latest available slot before deadline
        for j in range(min(deadline, max_deadline) - 1, -1, -1):

            if slots[j] is None:
                slots[j] = job_id
                total_profit += profit
                break

    print("\nScheduled Jobs:")
    for i in range(max_deadline):
        if slots[i] is not None:
            print("Time Slot", i + 1, ":", slots[i])

    print("\nMaximum Profit:", total_profit)


# Main Program
print("JOB SEQUENCING WITH DEADLINES")
print("--------------------------------")

n = int(input("Enter the number of jobs: "))

jobs = []

print("\nEnter job details:")

for i in range(n):

    print("\nJob", i + 1)

    job_id = input("Enter Job ID: ")
    deadline = int(input("Enter Deadline: "))
    profit = int(input("Enter Profit: "))

    jobs.append((job_id, deadline, profit))

# Call function
job_sequencing(jobs)