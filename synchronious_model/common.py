from numpy import random

INCOME_TIME = 'INCOME_TIME'
FINISH_TIME = 'FINISH_TIME'


def get_requests_count(sample, slot) -> int:
    return sample[slot % len(sample)]


def update_queue(new_requests, reqs_queue, slot_number) -> None:
    if new_requests:
        time_diffs = random.rand(new_requests)

        for req_number in range(new_requests):
            reqs_queue.put(
                {INCOME_TIME: slot_number + time_diffs[req_number],
                 FINISH_TIME: None}
            )
    else:
        pass
