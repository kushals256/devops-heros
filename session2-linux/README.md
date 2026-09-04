# Linux Fundamentals

Homework notes from Linux session: soft vs hard links, `adduser` vs `useradd`, `journalctl`, and a command cheat sheet.

---

## Task 1: Soft link and hard link

### What I learned

A **hard link** is another name for the **same file** (same inode). Both names point at the same data on disk.

A **soft link** (symlink) is a **separate small file** that stores a path to a target. It is a pointer, not a second name for the same inode.

### Commands

```bash
# hard link
ln original.txt hardlink.txt

# soft link
ln -s original.txt softlink.txt

# inspect inode (column 1) and link count (column 3)
ls -li original.txt hardlink.txt softlink.txt

# delete a link (removes that name)
rm hardlink.txt
rm softlink.txt
```

### Practice

Created `original.txt`, then a hard link and a soft link.

- `original.txt` and `hardlink.txt` had the **same inode**. Link count was `2`.
- `softlink.txt` had a **different inode** and showed as `softlink.txt -> original.txt`.
- Editing `original.txt` changed what both the hard link and the soft link showed.
- After `rm original.txt`:
  - hard link still had the data
  - soft link broke (`No such file or directory`) — it became a **dangling symlink**
- `rm` on the links does not delete the original while other hard links still exist.
- Hard link to a directory failed (`Is a directory`). Soft link to a directory worked.

### Interview answer

A hard link is a second directory entry for the same inode. Same data, same permissions. The file exists until the last hard link is removed. Hard links cannot point at directories (as a normal user) and cannot cross filesystems.

A soft link is a separate file that stores a path. It can point at directories and across filesystems. If the target is renamed or deleted, the symlink is dangling. `ln` creates a hard link; `ln -s` creates a soft link.

| | Hard link | Soft link |
|---|---|---|
| Command | `ln file link` | `ln -s target link` |
| Inode | Same as original | Own inode |
| After deleting original | Data still there | Broken (dangling) |
| Directories | No | Yes |
| Across filesystems | No | Yes |
| `ls -l` | Looks like a normal file | `link -> target` |

---

## Task 2: `adduser` vs `useradd`

### Difference

| | `useradd` | `adduser` |
|---|---|---|
| What it is | Low-level binary (`shadow-utils`) | Debian/Ubuntu helper script (wraps `useradd`) |
| How you use it | Flags only, non-interactive | Interactive by default |
| Home directory | Only if you pass `-m` | Created automatically |
| Password | Set later with `passwd` | Asks during create |
| Extra info (GECOS) | You pass flags | Asks (name, room, phone) |
| Distros | All Linux | Debian/Ubuntu (on RHEL, `adduser` is often a symlink to `useradd`) |

### Which is preferred on Ubuntu, and why

**`adduser` is preferred on Ubuntu.**

It is the Debian-recommended command for humans. It creates `/home/<user>`, copies `/etc/skel`, sets a password, and adds a default group. `useradd` is easy to misuse: `useradd bob` with no `-m` often creates an account **with no home directory**.

Use `useradd` in scripts when you need exact flags (`-u`, `-g`, `-s`) or the same command on mixed distros.

### Create a test user (recommended command)

```bash
sudo adduser hwtest
id hwtest
getent passwd hwtest
ls -ld /home/hwtest
```

Non-interactive:

```bash
sudo adduser --disabled-password --gecos "Linux Homework Test User" hwtest
```

Low-level equivalent (not preferred on Ubuntu):

```bash
sudo useradd -m -s /bin/bash hwlow
sudo passwd hwlow
```

Remove the test user:

```bash
sudo deluser --remove-home hwtest
```

---

## Task 3: `journalctl`

### What it is used for

`journalctl` reads the **systemd journal** — logs from the kernel, systemd, and services. On Ubuntu this is the main way to debug a service instead of only grepping `/var/log/syslog`.

### View system logs

```bash
journalctl                  # all journals
journalctl -b               # this boot only
journalctl -f               # follow live (like tail -f)
journalctl -p err -b        # errors and worse, this boot
journalctl --since "1 hour ago"
journalctl -k               # kernel only
```

### Check logs for a specific service

```bash
# -u = systemd unit name (this is the important one)
journalctl -u ssh
journalctl -u ssh -n 50 --no-pager
journalctl -u nginx -f
journalctl -u docker.service --since today

# find the unit name if you are not sure
systemctl list-units --type=service --state=running
```

- `-u` — one service
- `-n 50` — last 50 lines
- `--no-pager` — print to the terminal instead of `less`
- `-f` — follow new lines

---

## Task 4: Linux command cheat sheet

### Files and navigation

| Command | Purpose | Example |
|---|---|---|
| `pwd` | Print working directory | `pwd` |
| `ls` | List files | `ls -la` |
| `cd` | Change directory | `cd /var/log` |
| `cat` | Print whole file | `cat /etc/os-release` |
| `less` | Page through a file | `less /var/log/syslog` |
| `head` / `tail` | First / last lines | `tail -n 100 app.log` |
| `cp` / `mv` / `rm` | Copy / rename / delete | `cp a.txt b.txt` |
| `mkdir` | Create directory | `mkdir -p demo/logs` |
| `touch` | Create empty file | `touch notes.md` |
| `ln` / `ln -s` | Hard / soft link | `ln -s /etc/hosts hosts.link` |
| `find` | Search files | `find /var/log -name "*.log"` |
| `grep` | Search text | `grep -R "error" /var/log` |

### Users and permissions

| Command | Purpose | Example |
|---|---|---|
| `whoami` / `id` | Current user and groups | `id` |
| `chmod` | Change permissions | `chmod 755 script.sh` |
| `chown` | Change owner | `sudo chown bob:bob file` |
| `sudo` | Run as root | `sudo apt update` |
| `adduser` | Create a user (Ubuntu) | `sudo adduser hwtest` |
| `passwd` | Set password | `sudo passwd hwtest` |

### Process, disk, network

| Command | Purpose | Example |
|---|---|---|
| `ps` | Process list | `ps aux \| grep ssh` |
| `top` | Live processes | `top` |
| `kill` | Stop a process | `kill -9 PID` |
| `df -h` | Disk free | `df -h` |
| `du -sh` | Size of a path | `du -sh /var/log` |
| `free -h` | Memory | `free -h` |
| `uname -a` | Kernel and arch | `uname -a` |
| `ip a` | IP addresses | `ip a` |
| `ss -tulpn` | Listening ports | `ss -tulpn` |
| `ping` / `curl` | Network / HTTP | `curl -I https://example.com` |

### Services and logs

| Command | Purpose | Example |
|---|---|---|
| `systemctl status` | Is a service running? | `systemctl status ssh` |
| `systemctl restart` | Restart a service | `sudo systemctl restart nginx` |
| `systemctl enable` | Start on boot | `sudo systemctl enable docker` |
| `journalctl -u` | Logs for one service | `journalctl -u ssh -n 50` |
