import numpy

import constant
from main import simulate


def analyse_exponential_backoff():
    lambdas = numpy.linspace(0.1, 0.9, 100)
    avg_delay = []
    in_intensity = []
    out_intensity = []

    original_intensity = constant.LAMBDA

    for lamb in lambdas:
        constant.LAMBDA = lamb

        tmp_avg_delay, tmp_in_intensity, tmp_out_intensity = simulate()

        avg_delay.append(tmp_avg_delay)
        in_intensity.append(tmp_in_intensity)
        out_intensity.append(tmp_out_intensity)

    constant.LAMBDA = original_intensity

    numpy.savetxt('data/average_delay_on_lambda.csv', numpy.vstack((lambdas, avg_delay)).T, delimiter=', ')
    numpy.savetxt('data/output_intensity_on_input_intensity.csv', numpy.vstack((in_intensity, out_intensity)).T,
                  delimiter=', ')


def analyse_different_exponents():
    exponents = numpy.linspace(0.1, 7, 100)
    avg_delay = []
    in_intensity = []
    out_intensity = []

    for exp in exponents:
        constant.EXPONENT = exp

        tmp_avg_delay, tmp_in_intensity, tmp_out_intensity = simulate()

        avg_delay.append(tmp_avg_delay)
        in_intensity.append(tmp_in_intensity)
        out_intensity.append(tmp_out_intensity)

    numpy.savetxt('data/average_delay_on_exponent.csv', numpy.vstack((exponents, avg_delay)).T, delimiter=', ')
    numpy.savetxt('data/intensity_on_exponent.csv', numpy.vstack((exponents, in_intensity, out_intensity)).T,
                  delimiter=', ')
