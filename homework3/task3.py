#!/usr/bin/env python
import smtplib
import psutil
import config
from datetime import datetime
from time import sleep
counter = 0 # Variable for tracking high load
# server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login("service_acc@gmail.com",'123456')
# msg = "You have high load during last 5 checks."

while(True):
    cur_date = datetime.now()
    cur_date = cur_date.strftime("%H:%M:%S\t\t\t%d-%m-%Y ") # Get current date and time
    core_stat = psutil.cpu_percent(percpu=True) # Core statistic
    avg_cpu = sum(core_stat[:])/psutil.cpu_count() # Average core value
    #     if(avg_cpu>90): # Notification about high load
    #     counter += 1
    #     if(counter == 4):
    #         server.sendmail("service_acc@gmail.com","sysadmin_acc@gmail.com",msg)
    # else:
    #    counter = 0

    vm = (psutil.virtual_memory().used)/1000000  # Get used RAM in megabytes
    mem = ((psutil.virtual_memory().used) + (psutil.swap_memory().used))/1000000 # Get used VM in megabytes
    disk_wr = psutil.disk_io_counters(perdisk=False).write_time/1000000 # Get write time in seconds
    disk_read = psutil.disk_io_counters(perdisk=False).read_time/1000000 # Get read VM in seconds
    bytes_sent = psutil.net_io_counters().bytes_sent/1000000 # Get amount of sent traffic in megabytes
    bytes_recieved = psutil.net_io_counters().bytes_recv/1000000 # Get amount of recieved traffic in megabytes


    if(config.output == 'text'):# Output all statistic in the report.txt
        file = open('report.txt', 'a')
        file.write("\n\n" + str(cur_date))
        file.write("\n--------------------------------------------------------------------------------------------------------")
        file.write("\nMemory\n--------\nVirtual Memory usage\t\t " + str(vm) + "M\nRAM usage\t\t\t\t\t "+str(mem)+"M\n--------")
        file.write("\nCPU\n--------\nAverage load\t\t\t\t "+str(avg_cpu)+"\nAverage per cores\t\t\t "+str(core_stat[:])+"\n--------")
        file.write("\nDisk\n--------\nDisk time write\t\t\t\t " + str(disk_wr) + "s\nDisk time read\t\t\t\t  " + str(disk_read) + "s\n--------")
        file.write("\nNetwork\n--------\nBytes send\t\t\t\t\t " + str(bytes_sent) + "M\nBytes recieved\t\t\t\t" + str(bytes_recieved)+"M")
        file.write("\n----------------------------------------------------------------------------------------------------------\n\n\n\n\n")
        file.close()
    else:
        exit("Please,use output='text' format in config the file")
    sleep(config.interval*60)

