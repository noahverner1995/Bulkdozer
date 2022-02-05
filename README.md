<h1 align ="center"> Bulkdozer</h1>
<p align="center">
    <img src="logo/bulkdozer_logo_1000x1000.png"/>
</p>
<br>
<p align="center"><em>Prepare your servers OpenSea! <b>#EverybodyStandBack</b></em></p>
<br>

## Overview

Imagine that you were able to replicate the efficiency of uploading a big collection of NFTs with its corresponding metadata to a marketplace like <a href="https://opensea.io/">OpenSea</a>, just like <a href ="https://opensea.io/collection/boredapeyachtclub">The Bored Ape Yacht Club</a> and <a href ="https://opensea.io/collection/cryptopunks">Cryptopunks</a> have done in the past.

**You would be saving a lot of time and avoiding headaches if that were possible!** 😎
  
  ><em><h4>Interesting, but I've heard that it requires to know a lot about Smart Contracts, Solidity and other geek stuff to do so...🤔</h4></em> 
  
Fortunately that's not exactly the case ***IF you have created a collection of NFTs using*** <a href ="https://github.com/noahverner1995/SAND-wich">***SAND-wich***</a> 🥪😉.

<a href ="https://github.com/noahverner1995/SAND-wich">**SAND-wich**</a> is another open-source project that is useful for making simple NFT collections that require merging any number of 2d layers following an specific order (provided by you), as well as the corresponding metadata used in the process. 

Once you have created your NFT collection with **SAND-wich**, and also read this guide, you will be ready for starting <a href ="https://github.com/noahverner1995/Bulkdozer/blob/main/exe/bulkdozer.exe">**The Bulkdozer**</a> 🚛.
  
  ><em><h3>That's cool, what do I need to know? 🤷‍♂️</h3></em> 

I'm glad you ask!
  
Essentially you must know that after having logged in to your OpenSea account, and created the corresponding NFT collection in which you desire to upload your NFTs, you will start **The Bulkdozer**, which will ask you for some inputs, for then taking limited control of your Chrome Browser for doing an automated process, until it completely finishes uploading your NFTs (including the metadata).

**There are several conditions you need to meet and maintain if you want this program to run as good as expected**, these ones will be shown further below in this guide.
  
By now, let's start mentioning a summary of the technology this program uses 🤖:

  - **Technology stack**: Python 3.9.6 [MSC v.1929 64 bit (AMD64)], Pandas 1.3.1, Selenium 4.1.0, NumPy 1.21.1, PyAutoGUI 0.9.53.
  - **Status**:  0.1.0
  - **Executable**: https://github.com/noahverner1995/Bulkdozer/blob/main/exe/bulkdozer.exe
  - **What makes this software different from others?** The ease of use, the brand concept behind it, and the added value it provides to the collections created with **SAND-wich**.

## Installation

**If you are a developer**, you will first have to have installed `Python 3.9.6` or later with the following dependencies: `Pandas 1.3.1` or later, `Selenium 4.1.0` or later, `NumPy 1.21.1` or later, `PyAutoGUI 0.9.53` or later. Then you can copy the code from the `bulkdozer.py` file and run it in your preferred environment.
    
**If you ARE NOT a developer**, you will first have to deactivate your Antivirus for then <a href ="https://github.com/noahverner1995/Bulkdozer/blob/main/exe/bulkdozer.exe">downloading the exe file</a>. Then you can execute the program by clicking on it and pressing ↵Enter.

## Usage

First of all, you will open `Chrome Browser` using <a href="https://chromedevtools.github.io/devtools-protocol/">**DevTools as protocol client**</a>. This is a mandatory condition since it's the only way (at least known by me so far) to properly let a program take control of a `Chrome Browser` instance with `Selenium` while also **AVOIDING triggering Cloudflare DDoS protection** as shown below:

(Btw, ***keep in mind that you can only have 1 Chrome Instance (window) open when doing this process***, so if you want to keep reading this guide while also running the **The Bulkdozer**, read this guide in a different device (i.e. Your phone or another PC) and start **The Bulkdozer** in your regular PC)


<br>
<p align="center">
   <img src="screenshots/cloudflare-checks-your-browser-5-seconds-delay.png"/>
</p>
<p align="center"><em>If you see this when trying to automate a process in a webpage,</em></p>
<p align="center"><em>it means you DID NOT run Chrome Browser with DevTools protocol enabled</em></p>
<br>

Don't worry, it's not difficult, just go the **Windows Search Bar**, type "chrome", find the Application option, right-click it, and select `Open file location` as shown below:

<p align="center">
    <img src="screenshots/get-chrome-executable-path.png"/>
</p>

It will open a folder containing all of the corresponding executable files your `Start Menu` has, now you will right-click again the `Google Chrome` executable file and select `Open file location` as shown below:

<br>
<p align="center">
   <img src="screenshots/get-THE-REAL-chrome-executable-path.png"/>
</p>
<br>

Okay, now you will copy the path of the current folder (and paste it in a temporary `.txt` or `.docx` file) as shown below:

<br>
<p align="center">
   <img src="screenshots/copy-the-current-path.png"/>
</p>
<br>

Now, you will run the regular `Chrome Browser` but just to get the `user-data-dir`, type `chrome://version/` in the URL bar within a tab, as shown below:

<br>
<p align="center">
   <img src="screenshots/get-user-data-dir.png"/>
</p>
<br>

Copy that path (and paste it in the same temporary `.txt` or `.docx` file previously created), then close the regular `Chrome Browser` you have open.


All right now, you are going to run `Chrome Browser` with DevTools protocol enabled, go to the **Windows Search Bar**, type "cmd" and open the first option that appears, then type `cd` followed by the first path you copied previously, then press ↵Enter as shown below:

<br>
<p align="center">
   <img src="screenshots/cmd-first-path.png"/>
</p>
<br>

Okay, now type `chrome.exe --remote-debugging-port=9222 --user-data-dir:` followed by the second path you copied previously inside quotation marks (`""`), then press ↵Enter as shown below: 

<br>
<p align="center">
   <img src="screenshots/run-chrome-with-devtools-enabled-and-user-data-dir.png"/>
</p>
<br>

All right, it will open a **Chrome instance** (window) like this one down below:

<br>
<p align="center">
   <img src="screenshots/chrome-instance-running.png"/>
</p>
<p align="center"><em>Make sure to check if this Chrome instance has the Metamask extension installed.</em></p>
<p align="center"><em>Else, you will have to install it manually, like the first time 🤷‍♂️</em></p>
<br>

