# DevChamp

The DEVCHAMPION 2020 competition was on 02 December 2020, Those who still want to test the cybersecurity challenges: Capture the Flag (CTF) can register on CTFd platform https://isograd.ctfd.io.

## Network Challenges

####  First Challenge 75pts ###

![Suricata Screenshot](https://i.imgur.com/oR8i5fF.png)

the challenge (alert-debug.log) is a raw log file, let first extract all the strings inside

`strings alert-debug.log | less `

cool, then let try to get the flag since we knew its format DEVCHAMP[...]

`strings alert-debug.log | grep -A 1 DEV

![grep the flag](https://i.imgur.com/E18oAGY.png)

#### Second Challenge 125pts

