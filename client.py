# -*- coding: utf-8 -*-
from progressbar import ProgressBar, Percentage, Bar

__author__ = 'klaswikblad'

from tasks import make_pi
import time
import datetime

from celeryconfig import app as celery_app

import timeit
start_time = timeit.default_timer()
# code you want to evaluate

number_of_digits = 100

print "Client requesting pi digits calculated for significance of 1 to %i digits..." % number_of_digits

results = list(make_pi.delay(x) for x in range(1, number_of_digits))
pbar = ProgressBar(widgets=[Percentage(), Bar()], max_value=number_of_digits).start()
counter = 0

while not all(result.ready() for result in results):
    time.sleep(0.1)
    finishers = filter(lambda x: x.ready(), results)
    for finisher in finishers:
        # finisher.ready == True which means we have result. Get the result by finisher.get()
        # Result will be something json serializable.
        response = finisher.get()
        """print "[%s] [Worker @ %s] pi: %s" % (datetime.datetime.now().strftime('%I:%M:%S%p'),
                                             response['hostname'],
                                             response['result'])
        """
        counter += 1
        pbar.update(counter)
        results.remove(finisher)
pbar.finish()
elapsed = timeit.default_timer() - start_time

print "Time to evaluate {}".format(elapsed)