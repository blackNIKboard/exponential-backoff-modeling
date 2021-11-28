import constant
from subscriber.subscriber import Subscriber


def get_overall_request_count(subs):
    count = 0

    for subscr in subs:
        count += len(subscr.runtime)

    return count


if __name__ == "__main__":
    subscribers = []

    previous_finished = 0
    current_slot = 0

    for i in range(0, constant.SUBSCRIBERS):
        subscribers.append(Subscriber(i + 1))

    while current_slot < constant.TIME_LIMIT:
        transmitting_count = 0

        for s in subscribers:
            s.generate_new(current_slot)

        print(f"SLOT {'{:05d}'.format(current_slot)} request count on START: {get_overall_request_count(subscribers)}")

        for s in subscribers:
            if s.try_transmit():
                transmitting_count += 1

        for s in subscribers:
            if len(s.runtime) >= 1:
                print(f"    Subscriber {s.id} ({s.is_transmitting} with prob {s.probability}) requests:")
                for r in s.runtime:
                    print(f"        {r.id}")

        if transmitting_count == 1:
            for i in subscribers:
                i.update(constant.RESPONSE_OK, current_slot)
                if i.is_transmitting:
                    print(f"    Subscriber {i.id} transmitted")
        elif transmitting_count > 1:
            for s in subscribers:
                s.update(constant.RESPONSE_COLL, current_slot)

        print(
            f"SLOT {'{:05d}'.format(current_slot)} "
            f"request count on FINISH: {get_overall_request_count(subscribers)} \n")
        # print(
        #     f"WINDOW {'{:05d}'.format(current_slot)} "
        #     f"Currently transmitting {transmitting_count} (new {POISSON_DIST[current_slot]}) -
        #     > {len(finished) - previous_finished} finished \n")

        current_slot += 1

    print(subscribers[0].get_avg_delay())
    pass
