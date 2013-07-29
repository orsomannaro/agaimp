import datetime

from apscheduler.scheduler import Scheduler

from apps.userauth import server, SIGMA_AUTH


scheduler = Scheduler()


@server(SIGMA_AUTH)
def import_sigma():
    """
    Impostazione dati dal server SIGMA
    """
    print datetime.datetime.now().strftime("%H:%M:%S.%f")
    print "Import da SIGMA"


def execute():
    try:
        import_sigma()
    except:
        print 'errore su execute'


def shutdown():
    scheduler.shutdown()


def schedule():
    scheduler.add_interval_job(import_sigma, seconds=3)


def stop():
    jobs = scheduler.get_jobs()
    for job in jobs:
        scheduler.unschedule_job(job)


scheduler.start()
