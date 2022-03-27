from crontab import CronTab

cron = CronTab()
job = cron.new(command='py main.py')
job.dow.every('MON')

cron.write()

#remove the comment from the ligne under me to execute the script every monday
#job.enable()