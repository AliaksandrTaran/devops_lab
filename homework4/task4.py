#!/usr/bin/env python
import os
from glob import glob
import socket
import platform
import zipfile
import gzip
import psutil
import config
from datetime import datetime
from time import sleep
counter = 0  # Counter for log rotation
if not os.path.exists('json_logs'):  # Directory for json logs
    os.makedirs('json_logs')
if not os.path.exists('txt_logs'):  # Directory for txt logs
    os.makedirs('txt_logs')

class Comp_Res:
    def __init__(self):
        self.cur_date_time = datetime.now()
        self.cur_date = self.cur_date_time.strftime("%H:%M:%S\t\t\t%d-%m-%Y ")  # Current date
        self.core_stat = psutil.cpu_percent(percpu=True)  # Core statistic
        self.avg_cpu = sum(self.core_stat[:])/psutil.cpu_count() # Average core value
        self.vm = (psutil.virtual_memory().used)/1000000  # Get used RAM in megabytes
        self.mem = ((psutil.virtual_memory().used) + (psutil.swap_memory().used))/1000000  # Get used VM in megabytes
        self.disk_wr=disk_wr = psutil.disk_io_counters(perdisk=False).write_time/1000000  # Get write time in seconds
        self.disk_read = psutil.disk_io_counters(perdisk=False).read_time/1000000  # Get read VM in seconds
        self.bytes_sent = psutil.net_io_counters().bytes_sent/1000000  # Get amount of sent traffic in megabytes
        self.bytes_recieved = psutil.net_io_counters().bytes_recv/1000000  # Get amount of recieved traffic in megabytes


class Comp_Res_Add(Comp_Res):  # Inherited class with additional information
        bit_proc=platform.machine()  # Width of bus of thr CPU
        fqdn_name=socket.getfqdn()  # FQDN of the PC


while(True):
    comp_res = Comp_Res_Add()  # Create object of the class
    if config.output == 'text':  # Output all statistic in the report.txt
        file = open(os.getcwd() + "/txt_logs/" + comp_res.cur_date_time.strftime("%d-%m-%Y__%H_%M_%S") + ".txt", 'a')
        file.write("\n\n" + str(comp_res.cur_date))
        file.write("\n--------------------------------------------------------------------------------------------------------")
        file.write("\nMemory\n--------\nVirtual Memory usage\t\t " + str(comp_res.vm) + "M\nRAM usage\t\t\t\t\t "+str(comp_res.mem)+"M\n--------")
        file.write("\nCPU\n--------\nAverage load\t\t\t\t "+str(comp_res.avg_cpu)+"\nAverage per cores\t\t\t "+str(comp_res.core_stat[:])+"\n--------")
        file.write("\nDisk\n--------\nDisk write time\t\t\t\t " + str(comp_res.disk_wr) + "s\nDisk read time\t\t\t\t " + str(comp_res.disk_read) + "s\n--------")
        file.write("\nNetwork\n--------\nBytes send\t\t\t\t\t " + str(comp_res.bytes_sent) + "M\nBytes recieved\t\t\t\t" + str(comp_res.bytes_recieved)+"M\n--------")
        file.write("\nSystem information\n--------\nWidth of bus\t\t\t\t" + str(comp_res.bit_proc) + "\nComputer name\t\t\t\t" + str(comp_res.fqdn_name))
        file.write("\n----------------------------------------------------------------------------------------------------------\n\n\n\n\n")
        file.close()  # Log rotation
	counter += 1
        if counter > 100:
            for file_txt in glob('./txt_logs/*.json'):  # Compress each txt file
                with zipfile.ZipFile('./txt_logs/' + comp_res.cur_date_time.strftime("%d-%m-%Y__%H_%M_%S") + '.zip', 'a') as zip_arch_for_txt:
                    zip_arch_for_txt.write('./txt_logs/' + file_txt)
                    os.remove('./txt_logs/' + file_txt)  # Remove compressed txt file
            counter = 0
    elif config.output == 'json':
        file = open(os.getcwd() + "/json_logs/" + comp_res.cur_date_time.strftime("%d-%m-%Y__%H_%M_%S") + ".json", 'a')
        file.write("""{\n\t"Memory": {\n\t\t\t"Virtual memory usage(in Megabytes)":""" + str(comp_res.vm) + """,\n\t\t\t"RAM usage(in Megabytes)":""" + str(comp_res.mem) + """\n\t\t},""")
        file.write("""\n\t"CPU": {\n\t\t\t"Average load":""" + str(comp_res.avg_cpu) + """,\n\t\t\t"Average per cores":""" + str(comp_res.core_stat[:]) + """\n\t\t},""")
        file.write("""\n\t"Disk": {\n\t\t\t"Disk write time(in seconds)":""" + str(comp_res.disk_wr) + """,\n\t\t\t"Disk read time(in seconds)":""" + str(comp_res.disk_read) + """\n\t\t},""")
        file.write("""\n\t"Network": {\n\t\t\t"Bytes send(in Megabytes)":""" + str(comp_res.bytes_sent) + """,\n\t\t\t"Bytes recieved(in Megabytes)":""" + str(comp_res.bytes_recieved) + """\n\t\t}\n}\n\n\n\n""")
        file.close()
        counter += 1
        if counter > 100:  # Log rotation
            for file_json in glob('./json_logs/*.json'):  # Compress each json file
                with zipfile.ZipFile('./json_logs/' + comp_res.cur_date_time.strftime("%d-%m-%Y__%H_%M_%S") + '.zip', 'a') as zip_arch_for_json:
                    zip_arch_for_json.write('./json_logs/' + file_json)
                    os.remove('./json_logs/' + file_json)  # Remove compressed json file
            counter = 0
    else:
        exit("Please,use output='text' format in config the file")
    sleep(config.interval * 60)

 #  After  this,I've learned about built-in json functions:)


