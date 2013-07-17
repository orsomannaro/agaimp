import datetime

from apscheduler.scheduler import Scheduler

from apps.userauth import authenticate


scheduler = Scheduler()


#@authenticate(server = 'sigma')
def import_sigma():
    """
    Impostazione dati dal server SIGMA
    """
    print datetime.datetime.now().strftime("%H:%M:%S.%f")
    print "Import da SIGMA"


def execute():
    import_sigma()


def shutdown():
    scheduler.shutdown()


def schedule():
    scheduler.add_interval_job(import_sigma, seconds=3)


def stop():
    jobs = scheduler.get_jobs()
    for job in jobs:
        scheduler.unschedule_job(job)


scheduler.start()
