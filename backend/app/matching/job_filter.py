def remove_duplicate_jobs(jobs):

    seen=set()

    result=[]


    for job in jobs:


        key=(
            job.title.lower(),
            job.company.lower()
        )


        if key not in seen:

            seen.add(key)

            result.append(job)



    return result