from apscheduler.scheduler import Scheduler

from apps.userauth import authenticate


scheduler = Scheduler()


#@server('sigma')
#@scheduler.cron_schedule(day_of_week='mon-fri', hour=17)
#@authenticate
def import_sigma():
    """
    Impostazione dati dal server SIGMA
    """
    print "Import da SIGMA"
    pass


def start():
    scheduler.add_interval_job(import_sigma, seconds=2)


def stop():
    jobs = scheduler.get_jobs()
    for job in jobs:
        scheduler.unschedule_job(job)


scheduler.start()


