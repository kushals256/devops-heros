# Shell Scripting Homework

## Task: System Information Script

`system-info.sh` prints system info, takes user input, creates a directory and a file, and saves running processes with `>` redirection.

### What the script does

- Prints the current date
- Prints the hostname
- Prints the username
- Prints disk usage (`df -h`)
- Prints running processes (`ps`)
- Stores values in variables
- Takes input with `read -p`
- Creates a directory with `mkdir`
- Creates a file with `touch`
- Saves processes to the file with `>`

### Commands used

`mkdir` `touch` `echo` `df` `ps` `read -p` variables `>`

### How to run

```bash
chmod +x system-info.sh
./system-info.sh
```

Then enter name, roll number, and a directory name.

---

## Script run output

Input given:

```text
Enter your name: Kushal Sacharya
Enter your roll number: 01
Enter a directory name to create: sysinfo-output
```

Full output:

```text
===== System Information =====
Date: Fri Sep  4 21:52:45 IST 2026
Hostname: Kushals-MacBook-Air-2.local
Username: kushalsacharya

===== Disk Usage =====
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   228Gi    16Gi    43Gi    28%    459k  451M    0%   /
devfs            204Ki   204Ki     0Bi   100%     706     0  100%   /dev
/dev/disk3s6     228Gi    12Gi    43Gi    22%      12  451M    0%   /System/Volumes/VM
/dev/disk3s2     228Gi    17Gi    43Gi    29%    2.2k  451M    0%   /System/Volumes/Preboot
/dev/disk3s4     228Gi   777Mi    43Gi     2%     533  451M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   482Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   6.0Mi   482Mi     2%      37  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   1.0Mi   482Mi     1%      97  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     228Gi   137Gi    43Gi    77%    2.2M  451M    0%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   2.1Gi   2.8Gi    43%      68   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk4s1     860Mi   575Mi   285Mi    67%     713  4.3G    0%   /Volumes/Slack
/dev/disk3s1     228Gi    16Gi    43Gi    28%    459k  451M    0%   /System/Volumes/Update/mnt1

===== Running Processes =====
  PID TTY           TIME CMD
77756 ttys001    0:00.37 /bin/zsh -il
23193 ttys003    0:00.08 /bin/zsh -i
64673 ttys005    0:00.11 /bin/zsh -il
81295 ttys007    0:00.08 /bin/zsh -il

My name is Kushal Sacharya
My roll number is 01
Created directory: sysinfo-output
Created file: sysinfo-output/process.log
Running processes saved to sysinfo-output/process.log using > redirection
```

### `sysinfo-output/process.log` (created with `>` )

```text
  PID TTY           TIME CMD
77756 ttys001    0:00.37 /bin/zsh -il
23193 ttys003    0:00.08 /bin/zsh -i
64673 ttys005    0:00.11 /bin/zsh -il
81295 ttys007    0:00.08 /bin/zsh -il
```

### Files created by the script

```text
shell scripting/
  system-info.sh
  README.md
  sysinfo-output/
    process.log
```
