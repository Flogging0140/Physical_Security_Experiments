# Physical Security Experiments
[Google Slides Here](https://docs.google.com/presentation/d/1W2ecQoQON7yraziY6Ja600XYWgqb7X1nyP8KQ3nhXIE/edit?usp=sharing)

## Overview

This was a project during my last semester at MHC for ITEC285, my security class. The goal was to pick a security topic, research its importance, and extra for a demo. 

_Including source code, though omitting the 17pg essay as there is little need for it here_

## Highlights

- Created a Rubber ducky from an Raspberry Pi Pico
- Created a Rubber ducky from an Arduino Leonardo
- Outlined simple security issues and potential solutions
- Brute forced Samsung A70 with Pico
- Persistent Reverse Shell, w/BAD-USB
- .py Script for Windows 10 hash collection

## Video Demo, Gandalf, Pico, Leonardo

Setup both Raspberry Pi Pico and Arduino Pro Micro (Leonardo) as HID devices. Basically they are now user input devices. System does not know difference. Pico also a mass storage device (2mb). Simulate user input to enter commands in RUN box.

[Google Drive Proj Demo](https://drive.google.com/file/d/1JixBeKi5hzql6LhQOCJAU-_r5jU7pBKS/view?usp=sharing)

-   Project Resources, Attributes
	-   Starting point, SEXY-GANDALF - Kylerees64
		-   [Project here](https://github.com/dbragun/payloads/blob/master/SEXY-GANDALF.md)
		-   [GitHub Profile here](https://github.com/Kylerees64)
	-   Pico setup, file resources, guide
		-   [YouTube Video here](https://youtu.be/ksNaAV75k6w)
		-   [YouTube Channel here](https://www.youtube.com/@suvicreations3046)
	-   Arduino Version
		-   [ChatGPT](https://chat.openai.com/) as debugger, transpiler, someone to talk too
		-   Had to make minor changes, issue with type(‘_’, false) vs should have been keyboard.press(‘_’);
	-   DuckyScript Resources, Examples
		-   [Github Hak5 Library here](https://github.com/hak5/usbrubberducky-payloads/tree/master/payloads/library)

## Video Demo, Persistent Reverse Shell, w/BAD-USB

During class created persistent Kali USB for a lab. Listening with NC on port 87, for any IP. Pico injects PowerShell, creates scheduled task on logon, logs out user.

Caveat: Thought PS turns off firewall and Live-Protection, tamper protection has to be disabled (not by default), though this does not get reset when restarted, so only needs to be done once by user or by Ducky Script.

[Google Drive Proj Demo](https://drive.google.com/file/d/1DcURHo1BqtLQ4gLSqlb-22NjOeuWvf5y/view?usp=sharing)

-   Project Resources, Attributes
	-   Starting point, Netcat-Reverseshell-On-Log-In - HokkaidoInu
		-   [Project here](https://github.com/hak5/usbrubberducky-payloads/tree/master/payloads/library/remote_access/Netcat-Reverseshell-On-Log-In)
		-   [GitHub Profile here](https://github.com/HokkaidoInu)
	-   Pair Programmer, help w/Debugging, Emotional Support
		-   [ChatGPT](https://chat.openai.com/)
			-   PowerShell syntax/commands, debugging assistance
-   Issues
	-   Stuck in session 0 😭
	-   Permissions issue, which users to use
	-   Task Scheduler running but not running script 👀
	-   Disabling live-protection
	-   Tamper protection
	-   Potential dependency issue
	-   Currently working with this one

## Video Demo, Brute-Force, Android-10, 4 digit lock

Pico can connect to android phone like a computer, because it is one. Lockout time is limited to 30 seconds, try every 30 seconds, only 10k possibilities, ~4 days, no lockdown/wipe by default.

*Note: I do 4 days because don't have a camera mount. This just was a shortened version, just proof we can enter data and unlock a phone with prompts from DuckyScript.* 

[Google Drive Proj Demo](https://drive.google.com/file/d/1aH5mOCSBW-VEgQzSRfypTavZARONxLFE/view?usp=sharing)

-   Project Resources, Attributes
	-   Starting point, Idea, droidbrute - mandatoryprogrammer
		-   [Project here](https://github.com/mandatoryprogrammer/droidbrute)
		-   [Github Profile here](https://github.com/mandatoryprogrammer/droidbrute/commits?author=mandatoryprogrammer)
	-   Idea, Information
		-   [YouTube Video here](https://youtu.be/x5Rt93jshC8?list=PLgro6dwvA3_0np9qrvPOjZqQdgkSv0SDy)
		-   [YouTube Channel here](https://www.youtube.com/@mobilehacker)
	-   Suggestions, initially learning ducky syntax
		-   [ChatGPT](https://chat.openai.com/)
		-   [YT Proj Demo](https://youtu.be/8jcfhJ3k63w)

## Video Demo, Hash-Collection, Win-10, .py Script

Using lab (from Mike L, ITEC285, MHC) as process. Python Script used as delivery method, already runs fine, installed on Kali. Detects largest drive, guesses is Win-10, mounts, collects hashes, outputs to file, uses pastebin's API to send to internet (anon), unmounts drive. Process finishes in <5 seconds if successful.

[Google Drive Proj Demo](https://drive.google.com/file/d/1exYHbUo6E6JC4rk5qG0IsSIFG8Srrto0/view?usp=sharing)

-   Project Resources, Attributes
	-   Mike Long’s ITEC285, labs.
		-   Practiced python in his labs
		-   Given lab on collecting hashes, following same process in code
	-   Boilerplate, syntax help, debugging help
		-   [ChatGPT](https://chat.openai.com/)
		-   [CoPilot](https://github.com/features/copilot)


# Technologies Used

![icon](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original-wordmark.svg)

![icon](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/raspberrypi/raspberrypi-original-wordmark.svg)

![icon](https://adamtheautomator.com/wp-content/uploads/2019/08/powershell-1.png)

![icon](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg)
