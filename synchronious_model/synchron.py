import queue
from numpy import mean

import constant
from synchronious_model.common import *

TIME_LIMIT = constant.TIME_LIMIT

LAMBDA = constant.LAMBDA  # float(input("Enter lambda: "))
POISSON_DIST = random.poisson(LAMBDA, TIME_LIMIT)

THEORY_MN = (LAMBDA * (2 - LAMBDA)) / (2 * (1 - LAMBDA))
THEORY_MD = (THEORY_MN / LAMBDA) + 0.5

if __name__ == "__main__":
    reqs_queue = queue.Queue()
    processed_reqs = []

    cur_slot = 0
    N = 0

    reqs_overall = 0

    while cur_slot < TIME_LIMIT:
        if not reqs_queue.empty():
            request = reqs_queue.get()
            request[FINISH_TIME] = cur_slot + 1
            processed_reqs.append(request)

        incoming_reqs_count = get_requests_count(POISSON_DIST, cur_slot)
        reqs_overall += incoming_reqs_count
        update_queue(incoming_reqs_count, reqs_queue, cur_slot)

        cur_slot += 1
        N += reqs_queue.qsize()

    delays = [value[FINISH_TIME] - value[INCOME_TIME] for value in processed_reqs]
    avg_subscribers = N / TIME_LIMIT

    print(f"\nTh. MN: {THEORY_MN}")
    print(f"Real N: {avg_subscribers}\n")

    print(f"Th MD; {THEORY_MD}")
    print(f"Real d: {mean(delays)}\n")

    print(f'λ out: {len(processed_reqs) / TIME_LIMIT}')
    print(f'λ in: {reqs_overall / TIME_LIMIT}')
