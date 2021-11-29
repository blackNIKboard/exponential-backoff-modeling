import analyse
import constant
import support
from subscriber.subscriber import Subscriber


def simulate():
    subscribers = []

    overall_requests = 0
    current_slot = 0

    for i in range(0, constant.SUBSCRIBERS):
        subscribers.append(Subscriber(i + 1))

    if not constant.DEBUG:
        support.print_progress_bar(0, constant.TIME_LIMIT, prefix='Progress:', suffix='Complete', length=50)
    while current_slot < constant.TIME_LIMIT:
        if current_slot % (constant.TIME_LIMIT / 100) == 0 and not constant.DEBUG:
            support.print_progress_bar(current_slot, constant.TIME_LIMIT,
                                       prefix='Progress:', suffix='Complete', length=50)

        if current_slot == constant.TIME_LIMIT - 1 and not constant.DEBUG:
            support.print_progress_bar(constant.TIME_LIMIT, constant.TIME_LIMIT,
                                       prefix='Progress:', suffix='Complete', length=50)

        transmitting_count = 0

        for s in subscribers:
            overall_requests += s.generate_new(current_slot)

        if constant.DEBUG:
            print(
                f"SLOT {'{:05d}'.format(current_slot)} request count on START: "
                f"{support.get_overall_request_count(subscribers)}")

        for s in subscribers:
            if s.try_transmit():
                transmitting_count += 1

        for s in subscribers:
            if len(s.runtime) >= 1 and constant.DEBUG:
                print(f"    Subscriber {s.id} ({s.is_transmitting} with prob {s.probability}) requests:")
                for r in s.runtime:
                    print(f"        {r.id}")

        if transmitting_count == 1:
            for i in subscribers:
                i.update(constant.RESPONSE_OK, current_slot)
                if i.is_transmitting and constant.DEBUG:
                    print(f"    Subscriber {i.id} transmitted")
        elif transmitting_count > 1:
            for s in subscribers:
                s.update(constant.RESPONSE_COLL, current_slot)

        if constant.DEBUG:
            print(
                f"SLOT {'{:05d}'.format(current_slot)} "
                f"request count on FINISH: {support.get_overall_request_count(subscribers)} \n")

        current_slot += 1

    lamb_in = overall_requests / constant.TIME_LIMIT
    lamb_out = support.get_overall_processed_count(subscribers) / constant.TIME_LIMIT
    avg_delay = support.get_overall_average_delay(subscribers)

    print(f"\n---Analysis:")
    print(f"Avg. delay: {avg_delay}")
    print(f"Lambda  in: {lamb_in}")
    print(f"Lambda out: {lamb_out}")

    return avg_delay, lamb_in, lamb_out


if __name__ == "__main__":
    analyse.analyse_exponential_backoff()
    analyse.analyse_different_exponents()
