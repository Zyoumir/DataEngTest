# Data Engineering Test

## Steps to start the project

- [Clone the project](#step1)
- [Make sure you have packages installed](#step2)
- [Use the right python version](#step3)
- [Install the project dependencies](#step4)
- [The commands](#step5)

### <a name="step1"></a> Step 1: Clone the project
```bash
git clone git@github.com:Zyoumir/DataEngTest.git
cd DataEngTest
```
Make sure you put log files in the Dataset

### <a name="step2"></a> Step 2: Make sure you have python3 installed
```bash
python3 -v # Should return the version 
```
If it's not installed check https://www.python.org/downloads/ for installation steps

### <a name="step3"></a> Step 3: Install the project dependencies
```bash
pip install -r package.md
```
### <a name="step4"></a> Step 4: The commands
```bash
py -m  sourceFiles.App.main                   # Start the application
```
### <a name="step5"></a> Step 4: Cron Jobs to run every day
```bash
Put simple, here is what you do:
```

- Create your Python Script;
- Open Terminal;
- Write crontab -e to create crontab;
- Press i to launch edit mode;
- Write the schedule command * * * * * /usr/bin/python /path/to/file/<FILENAME>.py;
- Press esc to exit edit mode;
- Write :wq to write your crontab
    - - To delete the running job:
    - - To delete the entire crontab: Run crontab -r
    - - To delete a single cron job: Go to crontab -e, press i, press dd and press :wq to write the file.



With respect :handshake:
