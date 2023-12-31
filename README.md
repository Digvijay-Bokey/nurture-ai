# **Nurture**: An AI tool to help bridge the gap between children with special needs and their caretakers.

## Inspiration
The inspiration behind "Nurture AI" stemmed from understanding the unique challenges faced by parents, especially those of special needs children. Recognizing that constant supervision can be both exhausting and impractical, we sought to create a tool that would assist in monitoring their child’s emotional and mental state, especially during times when direct supervision isn't possible. This tool is not only meant to offer peace of mind but also aims to foster independence in children, giving them the confidence to engage in activities like homework or play, knowing they're still under a watchful, caring eye.


## What it does
Nurture AI uses AI-driven facial recognition and emotion detection technology through a simple webcam to analyze a child's emotional state in real time. The app recognizes a range of emotions – from distress and frustration to joy and contentment. When it detects negative emotional shifts or signs of distress, it promptly notifies the parent or caregiver via text. This feature ensures that the caregiver can intervene quickly when necessary, yet also allows them to manage other tasks without constant physical supervision.


## Tools Used
We used both Hume, Reflex, Twillo, and Redis to make this project possible. 


## Prizes
**CalHacks 2023 category winner for:**

Major League Hacking / Most Creative Use of Redis Cloud


## Usage and Requirments

You will need your own Twilio SMS account, Hume API, and Redis setup.

**To use you will need to create a creds.py file with the following format:**

### Format for creds.py
``` python
#twilio
twilio_sid = '[Your Credentials]'
twilio_token = '[Your Credentials]'
twilio_phone = '[Sending Twilio Number]'

#hume
hume_key = '[Your Credentials]'


#redis
redis_host = '[Your Credentials]'
redis_port = '[Your Port Prefrence]'
redis_password = '[Your Credentials]'
```
## Sidenote

This is a cloned version of the private repo used during the actual project in order to hide api keys from repo history. 

## Devpost

[Devpost Link](https://devpost.com/software/nurture-m7p5wg)
