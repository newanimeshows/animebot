from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from db import init_db
from handlers import check_reminders

def setup_scheduler(application):
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_reminders, IntervalTrigger(minutes=1))
    scheduler.start()
    # Ensure scheduler stops gracefully when the application stops
    application.job_queue.run_repeating(lambda _: scheduler.shutdown(wait=False), interval=0, first=0)
