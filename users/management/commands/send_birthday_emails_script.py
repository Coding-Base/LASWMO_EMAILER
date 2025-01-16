from apscheduler.schedulers.blocking import BlockingScheduler
import os

# Define the function that will run your Django command
def send_birthday_emails():
    os.system('python manage.py mongo_send_birthday_email')

# Create the scheduler
scheduler = BlockingScheduler()

# Add the job to the scheduler (set to run every day at 9:00 AM)
scheduler.add_job(send_birthday_emails, 'cron', hour=13, minute=55)

# Start the scheduler
print("Scheduler started. Waiting to send birthday emails daily at 22:15 PM...")
scheduler.start()






