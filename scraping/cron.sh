# File to set cron job file to fetch answers after every 3 hours
# Provide executable permission to the file and run it
# To verify whether the job is present in the cron job list or not
# type cronjob -e command and look at the end of the file

#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "*/1 * * * * cd ~/anon/scraping/ && python fetchAnswers.py 172.16.27.23:8361--" >> mycron
#install new cron file
crontab mycron
rm mycron