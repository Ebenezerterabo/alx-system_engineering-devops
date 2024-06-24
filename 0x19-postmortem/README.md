# Postmortem  
## Incident Report ```Web_stack debugging #3```
The following is the incident from an internal server error that ocurred on 20th June 2024. We realized this issue rendered the web server unavailable and out of reach to users and we apologize to everyone who was affected.  


![Screenshot of the incident](https://www.google.com/url?sa=i&url=https%3A%2F%2Fdatafloq.com%2Fread%2Fsoftware-development-project-postmortem%2F&psig=AOvVaw1uPOtcmcm3CM49b914Xxw8&ust=1719317952243000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCNias9yc9IYDFQAAAAAdAAAAABAE)


### Issue Summary
From 08:00 AM GMT, requests to fetch data from the web server resulted in 500 error response messages which at its highest traffic affected 100% of users. The root cause of this server downtime was an invalid configuration change which exposed a bug in the software configuration settings known as WordPress.

### Timeline
- 08:30 AM GMT: Incident reported/Issue detected.
- 08:40 AM GMT: An engineer noticed something ```system malfunction```
- 08:45 AM GMT: Checked web server ```apache2``` if it's up and runing and finally checked the WordPress software installed on our web server settngs.
- 08:55 AM GMT: The misleading path taken was assuming the problem was from the web server ```apache2```, but it's not true.
- 09:05 AM GMT: The issue was escalated and repored to the software engineering team.
- 09:15 AM GMT: The content of a specific line in the WordPress settings had a typo error with its file extensions listed in the ```wp.settings``` to be precise. We used the ```strace``` command to check the error process and changed the content of that particular settings extension from ```phpp``` to ```php``` and then reconfigured the settings file.
- 09:25 AM GMT: The web server was restarted and the issue was resolved.

### Root cause and resolution
At 08:30 AM GMT, an engineer noticed something ```Internal Server Error```. A configuration change in the WordPress settings file which was done by our software engineerng team rendered a bug that caused an internal server error. This blocked our users from getting access to resources on the web server and the server downtime as well due to this a thorough web stack debugging was conducted to figure out what caused it and at exactly 09:25 AM GMT, the issue was resolved.   

### Resolution and recovery
At 09:25 AM GMT, our software engineering team with vigorous debugging finally caught the bug which was causing the internal server error with the ```strace``` tool used to monitor the process going on in the web server.  
The problem was from a WordPress settings file precisely ```wp.setting``` which has some content of other file extension to keep the WordPress software running but a typo error of one file extension happened that to be ```phpp``` instead of ```php``` and then reconfigured the settings file. The issue was resolved and the web server was restarted.

### Corrective and preventive measures
- Configuration file files should be backed up before any change is made.
- The configuration file should be tested immediately after any change is made to check if its working as expected.
- Ensure staged rollouts of all configuration changes.
- Develop a better mechanism for quickly testing and verifying changes.
- Develop efficient ways of deliverying status notifications during incidents.  

### Reference:
[Google API infrastructure outage incident report](https://sysadmincasts.com/episodes/20-how-to-write-an-incident-report-postmortem)  