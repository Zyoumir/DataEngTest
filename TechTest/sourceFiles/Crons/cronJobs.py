from crontab import CronTab

cron = CronTab(tabfile='cronLogs.tab',user = True)
job = cron.new(command='0 0 * * * py sourceFiles.App.main')

#remove the comment from the ligne under me to execute the script every monday
job.enable()