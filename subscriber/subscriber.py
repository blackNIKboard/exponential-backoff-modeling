import hashlib
import time

from numpy import random

import constant
from request.request import Request


class Subscriber:
    def __init__(self, identifier):
        self.id = identifier

        self.distribution = random.poisson(constant.LAMBDA / constant.SUBSCRIBERS, constant.TIME_LIMIT)
        self.intensity = constant.LAMBDA

        self.probability = constant.P_MAX
        self.is_transmitting = False

        self.runtime = []
        self.discard = []

    def generate_new(self, slot):
        for i in range(0, self.distribution[slot]):
            self.runtime.append(Request(slot))

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
                self.probability = max(self.probability / 2, constant.P_MIN)

    def get_avg_delay(self):
        tmp_sum = 0

        for d in self.discard:
            tmp_sum += d.get_delay()

        return tmp_sum / len(self.discard)
