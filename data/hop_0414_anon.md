CONTEXT:
- David Sodaman: Agency owner/founder
- Clay Bell: Agency accounts/project manager
- Roman Prasad: Agency developer(s)
- Adam Chang & Candice: Clients of the agency

--- --- ---

**Adam Chang - 2024-11-26 07:00:50**

Hey @RomanPrasad. We'll do another test on Tuesday @ 9pm PST. Need help in two things before then:

• Push the requested changes (e.g. clarify between parent/child name; remove the "Good Night Abe", and remove "therapy")
• Can you please make <REDACTED_EMAIL>
2=&gt;Received Conversation ID: REDACTED
3=&gt;Session resumed: <tel:REDACTED|REDACTED>
4=&gt;Resuming previous session...
5=&gt;getAnthropicCompletion Attempt 1: Sending request to anthropicClient.messages.create
6=&gt;getAnthropicCompletion response received in 2.0950 seconds: Hard-working?
7=&gt;Time taken to execute sendTTS function in seconds: 0.526
8=&gt;getAnthropicJsonCompletionAttempt 1: Sending request to anthropicClient.messages.create
9=&gt;getAnthropicJsonCompletion Success after 1 attempt(s): Time taken: 1.2040 seconds
10=&gt;getAnthropicCompletion Attempt 1: Sending request to anthropicClient.messages.create
11=&gt;getAnthropicCompletion response received in 3.2490 seconds: Self-controlled?
12=&gt;Time taken to execute sendTTS function in seconds: 0.311
13=&gt;getAnthropicJsonCompletionAttempt 1: Sending request to anthropicClient.messages.create
14=&gt;getAnthropicJsonCompletion Success after 1 attempt(s): Time taken: 3.6160 seconds
15=&gt;getAnthropicCompletion Attempt 1: Sending request to anthropicClient.messages.create
16=&gt;getAnthropicCompletion response received in 2.5250 seconds: Cheerful?
17=&gt;Time taken to execute sendTTS function in seconds: 0.331
18=&gt;getAnthropicJsonCompletionAttempt 1: Sending request to anthropicClient.messages.create
19=&gt;getAnthropicJsonCompletion Success after 1 attempt(s): Time taken: 5.0480 seconds
20=&gt;getAnthropicCompletion Attempt 1: Sending request to anthropicClient.messages.create
21=&gt;getAnthropicCompletion response received in 1.4690 seconds: Kind?
22=&gt;Time taken to execute sendTTS function in seconds: 0.57
23=&gt;getAnthropicJsonCompletionAttempt 1: Sending request to anthropicClient.messages.create
24=&gt;getAnthropicJsonCompletion Success after 1 attempt(s): Time taken: 8.9750 seconds
25=&gt;getAnthropicCompletion Attempt 1: Sending request to anthropicClient.messages.create
26=&gt;getAnthropicCompletion response received in 2.2010 seconds: I see you identified being honest as a strength. Now, let's practice saying it proudly. When I say "Honest?" you say "I'm honest." Ready? Honest?
27=&gt;Time taken to execute sendTTS function in seconds: 0.697
28=&gt;getAnthropicJsonCompletionAttempt 1: Sending request to anthropicClient.messages.create
29=&gt;getAnthropicJsonCompletion Success after 1 attempt(s): Time taken: 4.5110 seconds
30=&gt;getAnthropicCompletion Attempt 1: Sending request to anthropicClient.messages.create
31=&gt;getAnthropicCompletion response received in 3.6450 seconds: Great! Now let's count up your strengths. You identified that you are honest. That's 1 wonderful strength! Even having one strength is something to be proud of. Would you like to reflect on what it means to you to be honest?
32=&gt;Time taken to execute sendTTS function in seconds: 0.748
33=&gt;getAnthropicJsonCompletionAttempt 1: Sending request to anthropicClient.messages.create
34=&gt;getAnthropicJsonCompletion Success after 1 attempt(s): Time taken: 3.4760 seconds

---

**Roman Prasad - 2024-12-25 00:05:32**

This scenario where we allow resuming a session after screen is turned off would be tricky to implement

---

**Roman Prasad - 2024-12-25 00:11:26**

For this we will need to save conversation history after each message which might increase latency.

---

**Adam Chang - 2024-12-25 01:35:52**

I wouldn’t worry about that for the proof of concept.

---

**Roman Prasad - 2024-12-25 02:42:30**

Ok

---

**Roman Prasad - 2024-12-27 13:34:17**

@AdamChang I have updated the app on testflight with the ability to resume when you screen turns off and is turned on again. pls update your app to the latest version from testflight

#### Thread replies:

**Adam Chang** - 2024-12-27 16:02:55

Thanks, @RomanPrasad. I am on vacation now and my phone doesn't work. I'll give it a try when I get back in a few days.

**Roman Prasad** - 2024-12-27 16:03:45

Ok np

**Roman Prasad** - 2024-12-27 16:04:02

Enjoy your vacation!! :ok_hand:

**Adam Chang** - 2024-12-27 21:02:41

@RomanPrasad Just got to try the resumption and it works fine. Thank you.

---

**Clay Bell - 2025-01-13 19:04:47**

Hi @AdamChang &amp; @Candice - After the Christmas break and a chance to use the app - are you considering a further build out to an MVP that we could help you design and scope out for budget/planning and technical design?

---

**Adam Chang - 2025-01-13 19:10:56**

Thank you for getting in touch. We do plan to build a MVP but the product will actually be quite different after collecting feedback from users. We are planning it out now and hopefully will have something to share with you soon. Thank you :pray:

---

**Clay Bell - 2025-01-13 19:13:41**

Oh excellent - that real-world data is extremely valuable so let us know if you have questions in the meantime!

---

**Adam Chang - 2025-01-16 23:08:45**

@DavidSodaman @RomanPrasad Hi. Just want to check with you whether we have records of all the sessions (e.g. conversation logs or a summary of the challenges/goals). We want to do some more detail analysis. Thank you.

---

**David Sodaman - 2025-01-17 17:16:20**

@AdamChang Not exactly, but it shouldn't be too hard to add as we already have some form of session persistence. @RomanPrasad Can you confirm?

---

**Adam Chang - 2025-01-17 17:28:58**

We don’t need to add that as a feature. We just want to see if there’s any data we have already collected for analysis. Thank you :pray:

---

**Roman Prasad - 2025-01-17 17:45:36**

@AdamChang we do have the conversation log for about 62 sessions

---

**Roman Prasad - 2025-01-17 17:46:07**

this might contain some stale data when resuming conversation feature was not implemented, so possibly some of them might not have been completed

---

**Adam Chang - 2025-01-17 17:46:38**

@RomanPrasad that’s great. Can you please send them to us or let us know how to retrieve them? Thank you :pray:

---

**Roman Prasad - 2025-01-17 17:47:51**

i can send you a dump which will contain all the conversations. the conversations for a session would be in the allConversationHistory attribute of the json

---

**Roman Prasad - 2025-01-17 17:50:17**

one conversation interchange consists of 3 steps:
1. assistant message
2. vis prompt
3. user response
so you can use this info while analysing the json. or if you want a certain kind of analysis, i can assist with that. just let me know

---

**Roman Prasad - 2025-01-17 17:50:23**

@AdamChang

---

**Adam Chang - 2025-01-17 18:03:34**

Thank you. I’ll take a look and let you know if we have any questions

---

**Adam Chang - 2025-02-16 03:06:18**

Hi @DavidSodaman @ClayBell @RomanPrasad

Just want to give you guys an update on what we are working on.

For the actual MVP, we have decided to work on this idea instead - <REDACTED_URL>, which will still involve significant AI work.

We are currently working with a designer on the UI/UX.

---

**David Sodaman - 2025-02-17 16:01:06**

Hey @AdamChang /@Candice , thanks for sharing the new concept! It looks really exciting. Id love to figure out how we can best support this pivot. By the way, one of our AI-focused front-end engineers is becoming available in about 1-2 weeks, so that could be good timing if you need extra hands.
A few quick questions:
• Are there parts of the original POC we should carry over, or is this a fresh build?
• Do you have any timeline, especially with the new UI/UX work?
• How do you see us fitting in on the AI and back-end side?

#### Thread replies:

**Adam Chang** - 2025-02-19 09:59:01

There will be some AI conversation elements as well (e.g. practicing scenarios), although we probably won't be using it to set SMART goals for the child.

The UI/UX will probably take 4 weeks or so, although I think we can start discussing how to do the AI part earlier.

I think we can start with consultation on the architecture/design, and then we can decide on which part can be completed by our app development team and which part we would need your help.

Thank you.

---

**Adam Chang - 2025-02-22 12:29:06**

@DavidSodaman One thing I have forgotten to ask is about the source code. Can you please give us access to the code repository? It would be great to get access any available documentation as well. Thank you :pray:

#### Thread replies:

**Roman Prasad** - 2025-02-22 12:35:36

pls provide the github account email id, i will give access

**Adam Chang** - 2025-02-22 12:39:19

<mailto:<REDACTED_EMAIL><REDACTED_EMAIL>> :pray:

**Roman Prasad** - 2025-02-22 17:06:14

@AdamChang we are on github free plan. so  adding more collaborators will cost money. thats why sending you this source code as a zip file

**Roman Prasad** - 2025-02-22 17:08:34

this is the mobile app

**Adam Chang** - 2025-02-23 05:53:53

Okay, thank you :pray:

---

**Roman Prasad - 2025-03-29 11:25:12**

@AdamChang I tried to publish the app to testflight again. but this time i have changed my laptop. so from a new laptop I dont see your company despite having been logged in as a team member with admin access to your account. please connect with me once you are around. I might need to sign in with your credentials to be able to publish this as a workaround

---

**Adam Chang - 2025-03-29 12:04:30**

I see. Let me try to log in but it may take a bit of time since I am in Asia again. Thank you

---

**Roman Prasad - 2025-03-29 12:16:34**

ok. also check if anything changed from your end. maybe some payment issue or some sort of agreements to be completed

---

**Adam Chang - 2025-03-29 15:19:27**

Hi Roman Prasad. Did you log in using <mailto:<REDACTED_EMAIL>@gmail.com>?

---

**Adam Chang - 2025-03-29 15:19:43**

That seems to be the one you should use

---

**Adam Chang - 2025-03-29 15:21:03**

I also resent invite to <mailto:Roman <REDACTED_EMAIL> <REDACTED_EMAIL>>

---

**Roman Prasad - 2025-03-29 15:23:00**

actually i would require access using <mailto:<REDACTED_EMAIL>@gmail.com> because my apple dev account (and my mac) uses ths email id

---

**Roman Prasad - 2025-03-29 15:41:12**

i think just try deleting my name from list of authorised users and then resend me invite to <mailto:<REDACTED_EMAIL>@gmail.com>

---

**Adam Chang - 2025-04-02 09:14:13**

Just resent invitation to the Gmail address

---

**Roman Prasad - 2025-04-02 13:30:52**

@AdamChang requesting you to grant me time till tomorrow. Super busy and working on multiple things at once

---

**Roman Prasad - 2025-04-02 13:31:12**

i’ll surely give this a try tomorrow

---

**Adam Chang - 2025-04-02 13:31:57**

No problem. Thank you for your help

---

**Roman Prasad - 2025-04-02 13:32:08**

really sorry for the delay

---

**Roman Prasad - 2025-04-02 18:01:58**

@AdamChang did not work. but i have your account’s credentials. can you provide me the otp you got?
iguess if you are in asia timezone, then just ping me once you are online tomorrow

---

**Roman Prasad - 2025-04-02 18:02:13**

i jsut need to login to xcode with your account’s credentials

---

**Roman Prasad - 2025-04-03 01:36:28**

also @AdamChang please check this issue:

---

**Roman Prasad - 2025-04-03 01:37:02**

perhaps this could be the one causing problems at my end

---

**Roman Prasad - 2025-04-03 01:39:33**

if this does not work, then perhaps this AI chat thread might help:

That’s the key issue! There’s a difference between App Store Connect access and Apple Developer Portal access.
You’ve been added to App Store Connect (which handles app submissions, TestFlight, etc.), but it seems you haven’t been properly added to the Developer Portal (which handles certificates, provisioning profiles, and signing capabilities).
Here’s what needs to happen:
1. Your client needs to add you to the Developer Portal specifically:
    ◦ They need to log in to <REDACTED_URL> (not App Store Connect)
    ◦ Go to “People” or “Users and Access”
    ◦ Add you as a user with the appropriate role (Admin or Developer)
    ◦ Make sure to check permissions for managing certificates and provisioning profiles
2. You’ll receive an email invitation:
    ◦ Once your client adds you to the Developer Portal, you’ll get an email
    ◦ You must accept this invitation to gain access
    ◦ This is separate from the App Store Connect invitation you already accepted
3. After accepting the invitation:
    ◦ Log out of <REDACTED_URL> and log back in
    ◦ You should now see both your account and your client’s account
    ◦ In Xcode, refresh your accounts (Xcode → Settings → Accounts)
    ◦ The client’s team should now appear in the signing dropdown
This is a common confusion - many people think App Store Connect access automatically grants Developer Portal access, but they’re actually separate systems with separate user management, even though they use the same Apple ID.
Ask your client to specifically add you to the Developer Portal (not just App Store Connect), and that should resolve the issue.

#### Thread replies:

**Roman Prasad** - 2025-04-14 16:30:53

use the steps here

**Roman Prasad** - 2025-04-14 16:31:08

(point 1 specifically)

**Roman Prasad** - 2025-04-14 16:31:18

@AdamChang

**Adam Chang** - 2025-04-14 16:34:25

Yah, those are the steps I used

**Adam Chang** - 2025-04-14 16:35:23

I think the instructions there may not be accurate?

**Adam Chang** - 2025-04-14 16:35:39

I start at <REDACTED_URL>

**Adam Chang** - 2025-04-14 16:35:56

But it always jumps back to appstoreconnect when I click on users and access

**Adam Chang** - 2025-04-14 16:36:14

But then I am adding you to the same list of people as before

**Roman Prasad** - 2025-04-14 16:42:55

hmm thats strange

**Roman Prasad** - 2025-04-14 16:43:10

then only option left for me would be to login with your credentias

**Adam Chang** - 2025-04-14 17:01:50

Sure

**Adam Chang** - 2025-04-14 17:02:25

My credentials is <mailto:<REDACTED_EMAIL><REDACTED_EMAIL>> and password is <REDACTED>

**Adam Chang** - 2025-04-14 17:07:49

Please try to login. You can choose text for 2nd factor and I can give you the code. Thanks :pray:

**Roman Prasad** - 2025-04-14 17:12:24

ok doing now

**Roman Prasad** - 2025-04-14 17:13:14

code pls

**Adam Chang** - 2025-04-14 17:14:38

Haven’t received it yet

**Adam Chang** - 2025-04-14 17:14:51

Did you ask it to send by text?

**Adam Chang** - 2025-04-14 17:15:11

I can’t get the device one, so it needs to send me a text code

**Roman Prasad** - 2025-04-14 17:15:45

there is no option to send by text in xcode

**Roman Prasad** - 2025-04-14 17:15:59



**Adam Chang** - 2025-04-14 17:16:43

Can you please try the did not receive a code?

**Adam Chang** - 2025-04-14 17:24:21

@RomanPrasad

**Roman Prasad** - 2025-04-14 17:26:33

hi yes

**Roman Prasad** - 2025-04-14 17:26:35

just tried

**Adam Chang** - 2025-04-14 17:32:10

Hmm, perhaps I need to log into that account from one of my devices

**Roman Prasad** - 2025-04-14 17:33:33

ok

**Adam Chang** - 2025-04-14 17:34:46

Let me find a way to do that.

---

**Adam Chang - 2025-04-03 04:55:23**

Perhaps let’s wait until I get back to the States in around a week since I don’t have access to my text messages as well so that makes sign-in a bit difficult. Thank you :pray:

---

**Roman Prasad - 2025-04-03 05:03:59**

ok

---

**Adam Chang - 2025-04-14 16:25:24**

Hi @RomanPrasad I am back to the States. Let me try to add you again. Which email do you want me to use? Thank you :pray:

---

**Roman Prasad - 2025-04-14 16:25:45**

pls use <mailto:<REDACTED_EMAIL>@gmail.com> as thats the email my apple account uses

---

**Roman Prasad - 2025-04-14 16:26:24**

make sure to add me to developer portal and not only app store connect

---

**Adam Chang - 2025-04-14 16:28:15**

Just sent you a new invite

---

**Roman Prasad - 2025-04-14 16:30:43**

that does’t fix the issue. i got invite for apple appstore connect. not developer portal

---

**Adam Chang - 2025-04-14 16:32:05**

I already follow the process