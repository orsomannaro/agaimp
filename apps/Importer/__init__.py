from apscheduler.scheduler import Scheduler


importer = Scheduler()


#@authenticate
#@server('sigma')
#@importer.cron_schedule(day_of_week='mon-fri', hour=17)
@importer.interval_schedule(seconds=5)
def import_sigma():
    """
    Impostazione dati dal server SIGMA
    """
    print "Impost da SIGMA"
    pass

