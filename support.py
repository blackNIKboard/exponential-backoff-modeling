# Print iterations progress
def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', print_end="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    # Print New Line on Complete
    if iteration == total:
        print()


def get_overall_request_count(subs):
    count = 0

    for subscriber in subs:
        count += len(subscriber.runtime)

    return count


def get_overall_processed_count(subs):
    tmp_sum = 0

    for subscriber in subs:
        tmp_sum += subscriber.get_processed_requests()

    return tmp_sum


def get_overall_average_delay(subs):
    tmp_sum = 0
    length = 0

    for subscriber in subs:
        tmp = subscriber.get_avg_delay()

        if tmp != -1:
            tmp_sum += tmp
            length += 1

    if length > 0:
        return tmp_sum / length
    else:
        return 0
