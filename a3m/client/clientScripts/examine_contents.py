import os

from a3m.executeOrRunSubProcess import executeOrRun


def main(job, target, output):
    args = ["bulk_extractor", target, "-o", output, "-M", "250", "-q", "-1"]
    try:
        os.makedirs(output)

        _, stdout, stderr = executeOrRun("command", args, capture_output=True)

        job.write_output(stdout)
        job.write_error(stderr)

        # remove empty BulkExtractor logs
        for filename in os.listdir(output):
            filepath = os.path.join(output, filename)
            if os.path.getsize(filepath) == 0:
                os.remove(filepath)
        return 0
    except Exception as e:
        return e


def call(jobs):
    for job in jobs:
        with job.JobContext():
            target = job.args[1]
            sipdir = job.args[2]
            file_uuid = job.args[3]
            output = os.path.join(sipdir, "logs", "bulk-" + file_uuid)
            result = main(job, target, output)

            if isinstance(result, Exception):
                job.print_error(str(result))
                job.set_status(1)
            else:
                job.set_status(0)
