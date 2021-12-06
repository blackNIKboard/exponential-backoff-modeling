from numpy import random

import constant
from request.request import Request


class Subscriber:
    def __init__(self, identifier):
        self.id = identifier

        self.intensity = constant.LAMBDA / constant.SUBSCRIBERS
        self.distribution = random.poisson(self.intensity, constant.TIME_LIMIT)
        # self.distribution = old.poisson.poisson(self.intensity, constant.TIME_LIMIT)
        # self.distribution = old.poisson.generate(self.intensity, constant.TIME_LIMIT)

        self.probability = constant.P_MAX
        self.is_transmitting = False

        self.runtime = []
        self.discard = []

    def generate_new(self, slot):
        for i in range(0, self.distribution[slot]):
            self.runtime.append(Request(slot))

        return self.distribution[slot]

    def try_transmit(self):
        if len(self.runtime) >= 1:
            self.is_transmitting = random.random() < self.probability
        else:
            self.is_transmitting = False

        return self.is_transmitting

    def update(self, channel_response, slot):
        if self.is_transmitting:
            if channel_response == constant.RESPONSE_OK:
                self.probability = constant.P_MAX
                self.discard.append(self.runtime.pop(0).exit(slot))

            elif channel_response == constant.RESPONSE_COLL:
                generated_probability = self.probability / constant.EXPONENT

                if generated_probability > constant.P_MAX:
                    generated_probability = constant.P_MAX

                self.probability = max(generated_probability, constant.P_MIN)

    def get_avg_delay(self):
        tmp_sum = 0

        if len(self.discard) > 0:
            for d in self.discard:
                tmp_sum += d.get_delay()

            return tmp_sum / len(self.discard)

        return -1

    def get_processed_requests(self):
        return len(self.discard)
