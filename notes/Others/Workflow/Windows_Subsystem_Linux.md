---
title: Windows Subsystem for Linux
---
The sections on these instructions are ordered by importance.


<!-- TOC -->

- [Prerequisite](#prerequisite)
- [Installation](#installation)
    - [Enable Windows Subsystem for Linux (WSL)](#enable-windows-subsystem-for-linux-wsl)
    - [Install Ubuntu](#install-ubuntu)
    - [Setup Ubuntu Account](#setup-ubuntu-account)
- [Update Ubuntu's Software](#update-ubuntus-software)
- [Optional](#optional)
    - [Upgrade Ubuntu OS](#upgrade-ubuntu-os)
    - [Build Essential (Recommended)](#build-essential-recommended)
    - [Reinstall SSH (Recommended)](#reinstall-ssh-recommended)
    - [Fix Console Color Scheme (Recommended)](#fix-console-color-scheme-recommended)
    - [Turn off Bell](#turn-off-bell)
    - [Python Environment - Anaconda](#python-environment---anaconda)

<!-- /TOC -->


The following instructions are how I setup my Windows Subsystem Linux. It is an exhaustive list of all essential tweaks and environments I need. Coincidentally, this may be very useful to you to set up your own Linux environment as instructions are not always all in one place or even trivial to Google.

## Prerequisite

- Windows 10 v1709 Fall Creator's Update or higher.

> **Note:** It is possible to use WSL if you have Windows 10 v1607 Creator's Update or higher. I do not recommend this as the original WSL will be deprecated.

## Installation

The official installation instructions by Microsoft are listed [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10). Sometimes the official instructions are not updated or difficult to find so I hope these instructions are more hands on and useful to you.

### Enable Windows Subsystem for Linux (WSL)

1. Windows search "Windows Features"
2. Enable "Windows Subsystem for Linux" (located all the way down)
> _A restart may be necessary_

### Install Ubuntu

1. Go to the "Windows Store"
2. Find and install "Ubuntu" by "Canonical Group Limited"

> **Note:** You may wish to install the other Linux distro if you like. I will not cover them so I recommend Ubuntu for beginners.
> **Note:** The term WSL often refers to Ubuntu distro of WSL.

### Setup Ubuntu Account

1. Open Ubuntu shell terminal either by:
    * Windows search "Ubuntu"
    * Win+R either `ubuntu`, `wsl`, or `bash`
2. Follow the prompt to enter your desired username and password.

Congratulations, you now have a working Ubuntu/Linux shell terminal! You are now all powerful to install/run any Linux program (almost). From now on, I will refer to the shell terminal as WSL. We will now always be working in a terminal instance. When I say "run this", I will always mean open up a WSL terminal and run the following code.

## Update Ubuntu's Software
Initially Ubuntu requires a manual update of the list of available updates. To do so run,

```sh
$ sudo apt-get update
```

> **Note:** `sudo` is not necesarrily needed but since it's a good practice to us when installing I provided it as a code example. If you run into an error, often a permission error, it is very likely you're required to use `sudo` before all `apt-get` command like `$ sudo apt-get update`. `sudo` is a superuser command that only the root account and sudoers are allowed to use. You are very likely a sudoer since you're the only account activate user account (except root).

Using the new update list, we will now upgrade any outdated software installed,

```sh
$ sudo apt-get upgrade
```

## Optional
The following sections are optional. Those marked recommended in section title are those you're most likely going to install and need in the future.

### Upgrade Ubuntu OS
Initially you're likely to have an older release of Ubuntu; you can check your version by,

```sh
$ lsb_release -a
```

The latest releases of Ubuntu are listed [here](https://www.ubuntu.com/download/desktop). You may prefer to use the most recent release rather than the LTS (long-term support) version. If so run,

```sh
$ sudo apt-get dist-upgrade
```

### Build Essential (Recommended)
Ubuntu does not come with very important compilers like GNU C/C++ compiler which is often required for many programs (e.g., gcc, makefile, particular Python libraries). Either way many programmers recommend build-essentials because it is essential to build a program (hence the name). To do so run,

```sh
$ sudo apt-get install build-essential
```

### Reinstall SSH (Recommended)

This step is crucial if you want to use SSH. There are many issues with using the SSH that WSL came with. Many of these issues are found to be fixed if you just reinstall SSH. To do so:

1. Uninstall SSH

    ```sh
    $ sudo apt-get purge openssh-server
    ```

2. Install SSH

    ```sh
    $ sudo apt-get install openssh-server
    ```

> It may be necessary to restart your SSH process especially if you change `/etc/ssh/sshd_config`. You can do so by:
>   ```
>   $ sudo service ssh --full-restart
>   ```

### Fix Console Color Scheme (Recommended)
Surprisingly and unprofessionally, the color scheme Windows defaulted for Ubuntu is not only ugly but sometimes unreadable especially when using `ls`. This time we will not be using WSL but Windows PowerShell itself to install this. Note that this is not needed if you plan on using zsh (aka Z shell or bash on steroids) anytime soon.

1. Download the latest colortool officially from [Microsoft GitHub repository](https://github.com/Microsoft/console/releases).

2. Unzip the file and open powershell at the directory where `colortool.exe` is located.

3. Run `colortool.exe` in powershell like so,

    ```powershell
    .\colortool.exe -d [color-scheme]
    ```
    You may choose from the following color schemes to replace `[color-scheme]`:

    * `cmd-legacy`: The current default which is highly not recommended.
    * `campbell`: The Windows official console color-scheme which is my choice.
    * `campbell-legacy`
    * `deuteranopia`: For those who are color blind.
    * `OneHalfDark`
    * `OneHalfLight`
    * `solarized_light`
    * `solarized_dark`

 After the command, opening a new WSL terminal should have its color scheme updated. Try to see if `ls` is readable.

### Turn off Bell
You've probably alread heard a bell sound everytime you make press a key that's not allowed in the terminal. If you're like me and hate the bell sound the good news is you can turn it off (of course, almost everything is customizeable). To do so,

1. Using your favorite text editor open `/etc/inputrc`

```shell
$ sudo nano /etc/inputrc
```

2. Uncomment or add `set bell-style none` to your settings.

That's it! Now the only other place you may hear this is if you use vim. If you do see where I got this solution [here](https://stackoverflow.com/questions/36724209/disable-beep-of-linux-bash-on-windows-10).

### Python Environment - Anaconda
I've written the instructions in a separate page [here](/Anaconda.md)

<!-- ### Install a Browser - Google Chrome
Sometimes you may want to install a browser. It's usually not to be used for browsing (since you have a browser already installed on Windows) but for some programs that outputs onto one of your local ports (e.g., Jupyter outputs a display to port `localhost:8888`).

I've chosen Chrome due to popularity:

1. Download Google Chrome debian package (similar to an install like `.exe`) to a temporary folder (either `~`, `/tmp`, or anywhere).

```sh
cd /tmp
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

2. Run the installer

```sh
sudo dpkg -i google-chrome-stable_current_amd64.deb
``` -->