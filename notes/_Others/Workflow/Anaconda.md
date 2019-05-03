---
title: Anaconda
---

The following are instruction on how I install the latest version of Anaconda to build my Python 3 Environment.

## Download the Anaconda Installer

We first download the install file (Anaconda uses a shell script installer). You may either:

* Visit the official [Anaconda website](https://www.anaconda.com/download/#linux) and copy the download link for the appropriate version for your system.
* Visit Anaconda's official [installer archives](https://repo.continuum.io/archive/) and copy the link to the version you want corresponding compatible to your computer.

> **Note:** Most commonly your computer is probably an x86 64-bit version. You may always check by running `$ uname -m`. 

> **Note:** You may wish to install the lite version of Anaconda called Miniconda. The following links is the [official website](https://conda.io/miniconda.html) and [installation archives](https://repo.continuum.io/miniconda/). All instructions below are the exact same for Miniconda

Make sure you have the link copied, now we will do some downloading magic (no browsers needed) by,

```sh
$ wget [paste_Anaconda_download_URL_here]
```
>Note: Once again you may need `sudo` permission. From now on all commands may need sudo permission.

You can now check using `ls` to see if you have the shell file on your current directory (file name is similar to `Anacondax-x.x.x-Linux-x86_64.sh`). 

## Install Anaconda

We will now run the shell script installer. You may run either of the following commands (there is no difference),

```sh
$ ./Anacondax-x.x.x-Linux-x86_64.sh
$ sh Anacondax-x.x.x-Linux-x86_64.sh
$ bash Anacondax-x.x.x-Linux-x86_64.sh
```

Please follow the prompt that requires you to:

1. Agree to the agreement
2. Choose an program destination (`~/anaconda` or `~/anaconda3` is sufficient or wherever you wish, some like )
3. Choose whether you would like to update PATH (I recommend yes).

