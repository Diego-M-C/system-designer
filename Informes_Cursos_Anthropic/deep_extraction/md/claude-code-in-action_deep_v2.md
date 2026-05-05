# Claude Code in Action

> **Source:** [https://anthropic.skilljar.com/claude-code-in-action](https://anthropic.skilljar.com/claude-code-in-action)
> **Category:** developer-tools | **Difficulty:** intermediate | **Domain:** Developer Tools
> **Tags:** claude-code, cli, git, github, mcp, automation
> **Extracted:** 2026-04-11 | **Version:** v3 (with YouTube transcripts + quiz content)

---

## Extraction Statistics

| Metric | Value |
|--------|------:|
| Total Lessons | 21 |
| Sections | 4 |
| JW Player Transcripts | 15 |
| YouTube Transcripts | 0 |
| Modular Text Lessons | 4 |
| Quiz Assessments | 1 |
| JW Transcript Chars | 72,552 |
| YouTube Transcript Chars | 0 |
| Modular Text Chars | 5,795 |
| **Total Content** | **78,347** |

## Curriculum Structure

- **What is Claude Code?** (3 lessons)
- **Getting hands on** (9 lessons)
- **Hooks and the SDK** (7 lessons)
- **Wrapping up** (2 lessons)

---

## Complete Lesson Content

### What is Claude Code?

#### Lesson 1: Introduction

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/303233](https://anthropic.skilljar.com/claude-code-in-action/303233)

**Video:** 001 - Introduction.mp4 | **Duration:** 0m 38s | **Platform:** jwplayer | **Captions:** English, English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Hello and welcome. My name is Stephen Grider

and I'm a member of Technical Staff at Anthropic. In

this course, we're going to get to you up to speed with Claude Code. And

before we get into anything too technical, I want to give you a

quick overview on what will be learning. This

course is organized into four sections. We're

going to first spend some time to understand exactly what

a coding assistant is. We'll then take a look at Claude

Code itself and understand what makes it stand out among

all the different coding assistants on the market.

Once we've established that, we'll walk through the use of Claude Code

on a typical project and get some hands-on experience.

Finally, we'll wrap things up by seeing how you can get the most

out of Claude Code on your own projects.

---

#### Lesson 2: What is a coding assistant?

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/303235](https://anthropic.skilljar.com/claude-code-in-action/303235)

**Video:** 002 - What is a Coding Assistant?.mp4 | **Duration:** 5m 53s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, we're going to get a better understanding

of what a coding assistant is. Yes,

a coding assistant is a tool that writes code, but I want

to give you a deeper understanding of what's going on behind the scenes.

You see, by understanding what a coding assistant really

does and how it works, you'll have a greater appreciation

of what makes a truly amazing assistant to

complement your team. Here's one way that you

can picture what a coding assistant is doing. An assistant

is first given a task. In this case, maybe the assistant

needs to fix a bug based upon some kind of error message.

This task is passed off internally to a language model, which

needs to figure out how to solve the issue. Now, different

language models solve problems in very different styles depending

upon the complexity of the task. But in many cases, they

work very much like how a human would work. It

first might need to gather context by understanding what the error

is referring to, what area in the code base is throwing the error,

and what files seem to be relevant. Once

it has gathered that information, it then needs to formulate a

plan on how it will actually accomplish the task.

In this case, it might decide to change some code and then run

or write a test to verify that the issue is actually

fixed. Finally, it will take an action. In

this case, that might be updating a file and running

the test. Now, I want to give you some more information

on this entire process. In particular, I'd

like you to notice that the first and last steps here

require the coding assistant to actually do something.

In other words, to actually gather information from the outside world

or affect the outside world in some way. For

example, to gather context, the assistant needs to maybe

read a file or fetch some documentation online.

And for taking an action, the assistant might need to actually

run a command or edit a file. Now

having a language model actually do these things

is a little bit trickier than it actually sounds.

Let me help you understand why that is. Let's

imagine that we are interacting with a language model directly,

so it's not running inside of any coding assistant or anything

like that. Let's then imagine that we asked this

language model directly what code is written inside

the main.go file. Language

models running outside the context of any coding

assistant or similar tool do not inherently

have the ability to say read a file or write

a command or anything like that. Language

models take in content like text and they return

text. That's it. That's the entire extent

of their capabilities. And this is true of all language

models. So if you were to send some text

into a plain language model asking to read a file,

it would most likely respond by saying that it doesn't have

the ability to read any files. So let me show

you what coding assistance and many, many other tools

out there do to actually allow a language model to,

quote unquote, read a file. So here's what happens. Whenever

you send a request off to your coding assistant, the coding

assistant behind the scenes is going to automatically append

a lot of text into your request.

In this particular case, we can imagine that the coding assistant

is going to add on some text that says something like, if you,

language model, want to read a file, respond with

this very carefully formatted message. For

example, maybe something like, read file, colon,

and then the name of a file to read. So in this

case, the language model would hopefully realize that in order

to answer our question, it needs to respond

by reading that file. So it might respond with, read

file colon main.go. Now the coding

assistant would be in charge of receiving this very carefully

formatted message and realizing that the language model wants

to take some kind of action by reading a file. So

the coding assistant would then be responsible for actually a read

in the file and sending the contents of that file

back into the language model. Now that the language

model has received the actual contents of that file, it

can write a final response that gets sent back to us.

in which it might say, well, I read this file and it

contains some amount of code, whatever else, whatever's inside

that file. This entire system of giving

a language model these extra little instructions

asking it to respond in a very well formatted or carefully

formatted way is referred to as tool use.

So tools are used to give models extra capabilities.

The model is responsible for responding in a very particular

way. And then something like our coding assistant would be responsible

for actually doing whatever was promised. So

actually reading a file, writing a file, or whatever else.

Again, this is how every single language model out

there works. They all work with this idea of tool use.

Now, here's the critical part to understand. The Claude series

of models, so Opus, Sonnet, and Haiku,

are particularly strong at understanding what

tools do, when they're called, and actually using

them to effectively complete tasks and using them

in really interesting combinations to complete

more advanced or complex tasks.

Claude's strong tool use is the absolute core strength

of Claude code as a coding assistant. Here's why.

First, as I just mentioned, with better tool use,

Claude can handle more complex tasks.

Second, Claude code itself is extensible, so

it's really easy to add in new tools to Claude. And

Claude will happily make use of those tools.

This is especially important for continued relevance,

given the fast changes that we're seeing in the world of development.

In other words, Claude Code is an assistant that

will change with you in the years to come. And

finally, with improved tool use, you often get better

security because Claude can effectively search

your code base to find relevant code without relying

upon indexing, which often relies upon sending

your entire code base to outside servers.

Let's do a quick review on what we learned inside this video

around what a coding assistant really is. So remember,

coding assistants use language models internally to complete

different tasks. These language models, they need

to know how to use tools to work on the

vast majority of tasks that they are given. Tools are used to read

files, write files, run commands, and essentially everything

else that doesn't just involve generating some text.

Not all language models make use of tools at the

same level, and this has a big impact on the

overall efficiency of a coding assistant.

---

#### Lesson 3: Claude Code in action

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/303242](https://anthropic.skilljar.com/claude-code-in-action/303242)

**Video:** 003 - Claude Code in Action.mp4 | **Duration:** 8m 25s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Just a moment ago, I made some pretty big claims by saying that

Claude was an expert at making use of tools. And

that Claude code was easily extensible. Naturally,

you might be a little skeptical, so I'd like to give you a few

quick demonstrations. On this table are the

default tools that are available in Claude code. It

has all the abilities you would expect, like reading files,

writing files, running commands, and so on. I'm

going to show you a couple of tasks completed using

Claude Code. And in each case, it will use

this set of tools in rather intelligent ways. And

in at least one task, I'll even give Claude an

additional new set of tools to make use of.

Not only will this process give you a good idea of what Claude

code can do right out of the box, but hopefully

you will also see how easily you can extend Claude

code with more functionality. Here's my

first task for Claude code. I'm going to ask it to find

and optimize performance issues in the chalk library.

In case you're not familiar with it, chalk is a JavaScript package.

Here's the documentation for it. Now this is a very

small library that has one very simple purpose.

All it does is print out text in nicely formatted

colors, so like exactly as you see in this example screenshot

right here. So you can give the text colors or backgrounds

and formatting, all that kind of stuff. Now, this

might sound like a really simple and silly package,

but here's the thing. It turns out this is actually the fifth

most downloaded package in the entire JavaScript ecosystem.

Last week in particular, it had 429

million downloads. So this package is used

far and wide to put it simply. If

I could find any way to optimize anything inside

this package, well, it would probably be worth the effort.

So I'm going to ask Claude to run the benchmarks, identify

the worst performing cases, use some profiling tools

to figure out why those cases are running so slowly, and then

fix them. We'll then see that Claude is going to use a wide

variety of different tools to intelligently tackle this problem.

It'll form up a 2DList to track its progress,

execute commands to run the benchmarks, write a file to better

zoom in on one particular case, use a CPU

profiler to understand why that case is running so slowly,

and then implement some improvements. By the end,

we'll get a 3.9 times improvement in throughput

in one particular operation around this library. Here's

another example of how well Claude can string together different

tool calls to complete a rather complex task. I'm

going to give it a data set inside the CSV file. All

the data inside of here contains information about different users

of a video streaming platform. And I'm going to ask it to

just do a general analysis, maybe identify some causes

of churn on the platform. And I want all this analysis

to be done inside of a Jupyter notebook. Here's

my data set. I'm then going to ask Claude to run

the analysis and let's see how it does. This is

a great example of where effective tool use is really

important. You see, it's not really enough that

Claude just writes code into a notebook. Claude can

also execute code in different cells and view the results

of those executions. That means that Claude

can take some initial look at the data in the notebook and

then customize each successive cell to hone

in on some particular details. Next

up, I'd like to show you an example of a task where I extend Claude

Code's capabilities by giving it access to a new set

of tools. I built a small app that will

generate UI components based upon some description entered

on the left side of the screen. The generated component

is then displayed on the right side. Now, the app can

generate good looking components quite easily, but

the chat interface on the left and the header at the top

are not looking so nice. So

I'm going to use Claude Code to improve the styling. If

I just asked it to fix the styling and the chat interface in the

header, it would likely do a fine job. But remember,

my goal here is to show you how easy it is to

add additional functionality to Claude Code. So along

with this styling task, I'm going to also give Claude Code

access to a new set of tools provided by

something called the Playwright MCP server, which

I'll tell you more about later on. These tools allow

Claude to directly open and control a browser.

So here's what that process looks like in action. I'm

going to ask Claude to improve the styling of my app and make

use of a browser to do so. It'll then open

a browser on the right-hand side of the screen. Navigate to my

app, it'll take a screenshot to view the current styling,

and then update the styling. We could even ask

Claude to take another screenshot of the page when

it was complete and iterate on the design a couple of times

to really get a nice design that really pops. And

before long, we've got something that actually looks pretty reasonable.

There's one last set of demonstrations that I like to give you. Remember

what I mentioned a moment ago. Claude's ability to

utilize tools so well is what will allow Claude code

to grow with you and your team in the future. Let

me show you an example of that right away. Claude has

a very close integration with GitHub. You can set up Claude

code to run inside of a GitHub action,

where it will be executed automatically based upon certain

events, like creating a pull request or

when directly mentioned inside an issue. When

Claude Code runs on GitHub, it not only gets

to view and run your code, but it also

gets to access a new set of tools for interacting

with GitHub, like the ability to create comments

or create commits or pull requests and so on. You

can use this integration to automatically review pull

requests. Let me show you an example. Let me first

set up a little scenario for you. Let's imagine that we are

building out some infrastructure on AWS, and all

of our infrastructure is to find inside of a set of terraform

files, which are committed and stored on GitHub.

Because all of our infrastructure is to find inside of terraform

files, Claude Code has a really good idea of how

information is flowing through our infrastructure.

And let's imagine that in the SAP, I have a DynamoDB

table. If you're not familiar with those, it's kind of like a normal database

table. Inside there, I'm storing some different information

about users, including maybe plans viewed and

a registration date. And for maybe some

reason, we want to share just that plans viewed and

registration date information with some internal

marketing team, but also some external

marketing team as well. So some other company has

access to the data that we are writing in this bucket.

So it's really important for us to always be aware of what information

is being written into that bucket over time. Nightly,

we might have a Lambda function, pull out all the different users

that have been added into that table, and then extract just

plans for you and the registration date, and store

that in the S3 bucket so these two marketing teams

can access that information. Now let's

imagine that months later on, the internal

marketing team asks us to also store the email

inside of this S3 bucket as well. So we might

go into the Lambda function and add in just one single line

of code that takes the user's email and stores it inside

the bucket. And because this is months later on,

we might have completely forgotten that this S3 bucket

is shared with a external marketing partner. So

now at this point in time, we are putting personally identifiable

information into this bucket, which is accessible

by a separate company. This is a big no-no. Definitely

something we would not want to do. But at the same time, this

is an error that does occur, and it's kind

of hard to catch if we don't have a good idea of exactly

what's going on with this S3 bucket. Well,

it turns out that Claude Code can catch this kind

of scenario inside of a pull request quite easily,

specifically because all of our infrastructure is defined inside

of those terraform files. So here's a quick example.

I built that project that I just showed you in that diagram. I

created a pull request to add in the

user's email inside of the Lambda function. So the only

line of code that I changed was that right there. I'm saying that

for every user, I want to get their email and add that into

the bucket as well. Now, Claude

has an excellent idea of my infrastructure. So

it was able, inside of a automated review, this

we're seeing right here, to take a look at all the changes I made

inside this pull request. It was able to figure out exactly

how my infrastructure works, and it was able to identify

that I am exposing some PII to

a partner. So it has listed out the data flow

right here, the exact steps that occur. and goes

into great detail on how this bucket is shared with a

external partner. Catching issues like this

during development instead of after we deploy this

change is an amazing benefit to using Claude

Code's integration on GitHub. I'm going to go into

a lot of detail later on and show you exactly how to set

up a flow exactly like this. I think

that we've now got a good idea of what Claude Code can do thanks

to its excellent ability to make use of tools. Remember,

you really want to think of Claude Code as a flexible assistant

that can be customized, grow, and change over time to

meet the needs of your team.

---

### Getting hands on

#### Lesson 4: Claude Code setup

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/301614](https://anthropic.skilljar.com/claude-code-in-action/301614)

Time to get Claude Code set up locally!
Full setup directions can be found here: https://code.claude.com/docs/en/quickstart
In short, you'll need to do the following:

Install Claude Code

MacOS (Homebrew): brew install --cask claude-code
MacOS, Linux, WSL: curl -fsSL https://claude.ai/install.sh | bash
Windows CMD: curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd

After installation, run claude at your terminal. The first time you run this command you will be prompted to authenticate

If you're making use of AWS Bedrock or Google Cloud Vertex, there is some additional setup:

Special directions for AWS Bedrock: https://code.claude.com/docs/en/amazon-bedrock
Special directions for Google Cloud Vertex: https://code.claude.com/docs/en/google-vertex-ai

**Code Examples:**

```
Install Claude Code
```

```
MacOS (Homebrew): brew install --cask claude-code
```

```
brew install --cask claude-code
```

```
curl -fsSL https://claude.ai/install.sh | bash
```

```
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

```
claude
```

**Resources & Links:**


---

#### Lesson 5: Project setup

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/301615](https://anthropic.skilljar.com/claude-code-in-action/301615)

Working with Claude Code is more interesting if you have a project to work with.
I've put together a small project to explore with Claude Code. It is the same UI generation app shown in a previous video. Note: you don't have to run this project. You can always follow along with the remainder of the course with your own code base if you wish!
Setup
This project requires a small amount of setup:

Ensure you have Node JS installed locally. Link to installation directions.
Download the zip file called uigen.zip attached to this lecture and extract it
In the project directory, run npm run setup to install dependencies and set up a local SQLite database
Optional: this project uses Claude through the Anthropic API to generate UI components. If you want to fully test out the app, you will need to provide an API key to access the Anthropic API. This is optional. If no API key is provided, the app will still generate some static fake code. Here's how you can set the api key:

Get an Anthropic API key at https://console.anthropic.com/
Place your API key in the .env file.

Start the project by running npm run dev

**Code Examples:**

```
uigen.zip
```

```
npm run setup
```

```
.env
```

```
npm run dev
```

**Resources & Links:**


---

#### Lesson 6: Adding context

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/303241](https://anthropic.skilljar.com/claude-code-in-action/303241)

**Video:** 004 - Adding Context.mp4 | **Duration:** 5m 14s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

I've got my code editor open inside that small project,

and I'm going to start up the development server with a NPM run

dev. And when I run that, I'm going to be able to

navigate to a local host 3000 inside my browser

and see the application running. So here it is right here. We

are going to use Claude to do a little bit of work on this project.

But first, there's something really critical I want you to understand around

using Claude. Specifically, I want you to walk away

from this course with a strong understanding of context management.

You see, inside of your typical project, there might be dozens or

hundreds of files, each with a tremendous amount

of information. Whenever we ask Claude a question

or give it a task, there is some ideal amount of

information that Claude needs. Just enough

to help to understand how to answer your question or complete your task.

As soon as we start adding in additional information that's

not relevant, Claude's effectiveness will start

to decrease. So it is really important for us to

help guide Claude towards relevant files or

documentation inside of our project. Claude code can

certainly work without any handholding, but you'll get the best

results if you provide just a little bit of guidance.

So for the remainder of this video, I'm going to give you a bunch of different tips

on how to give Claude the best context possible. To

get started, inside my editor, I've opened up my terminal, and

I'm going to start Claude Code up by running the Claude

command. Whenever you run Claude Code

in a project for the first time, I highly recommend running

the slash init command. This gets

Claude to take a deep look at your entire code base. It'll

figure out the purpose of the project, the general architecture,

relevant commands, critical files, and so on. After

this search, it'll summarize its findings and place them

into a file called Claude.md.

When Claude tries to create this file, it will ask for permission.

You can either hit Enter to accept, or if you don't

want to have to grant permission to every file write request,

you can also press Shift Tab, which will allow

Claude Code to freely write files in your project.

I would encourage you to open up the Claude MD file that was generated

and take a look at its contents. As I mentioned, the

contents of this file are included in every request we make off

the Claude. This file really has two different purposes.

First, it helps Claude better understand your codebase so

it can find relevant code more quickly. And second, it

serves as a location where you can give Claude some general

guidance. Just so you know, there are multiple

Claude MD files that Claude Code will make use of. There

is a project level, a local level, and a machine

level. The project level is what we just generated

by running the slash init command. We are generally

going to commit this file to source control, like Git. We're

going to share this file with other engineers and just have some project

specific directions that we want to hand off to Claude. Optionally,

we can also create a Claude local MD file.

This file is not going to be committed and you're generally not going

to share with any other engineers. Inside this file,

you might put in some personal instructions that you want

Claude to follow just for you. Finally,

you can have a global Claude MD file on your machine.

This file will contain instructions or be applied to all

projects that you run locally. Now, I

keep on mentioning giving Claude special or custom instructions.

So let me show you an example of that. Let's imagine that

Claude is using comments way too often in the code that it writes.

We can address this by updating our Claude MD file.

We can either manually modify the file or a little

bit of a shortcut is inside of Claude Code we

could put in a pound sign. This puts us in

memory mode. This allows us to edit one of our

Claude MD files intelligently. So we can put

in a request like, don't write comments so often. I'll

then specify that I want to add this instruction to the project

Claude MD file, and Claude is then going to merge

this instruction into that file intelligently. If

I then open the file up and do a search, I'll see that in

fact, yes, it did add in that new instruction.

Now that we've created our Claude MD file, I want to give you a

better understanding of how to pull in specific context

into a conversation. Let's imagine that we want to better

understand how the authentication system in this project works.

We could just ask Claude to tell us about it, in which case, we would

search over our codebase and find files relevant

to the authentication system. That would definitely work, but

it would just take some amount of time. Alternatively,

if we already know some files that are relevant for

the authentication system, we could mention them using

the ATT character. When we mention a file,

it will be automatically included inside of our request off to

Claude. This is an excellent technique for

pointing Claude in a specific direction. You

can use the same syntax to also mention files

inside of Claude MD. Let me show you an example of

why that is really useful. inside of the Prisma

folder of this project, there's a file called schema.prisma.

This file contains a complete definition of all the different

tables and types of records that exist inside the SQLite

database that is used to store information inside this project.

Because this information is so important and relevant

to so many aspects of this project, I might decide

to mention this file inside of my Claude MD

file. Let me show you how I do that. First,

I'll enter a pound to enter memory mode. I'll then

mention that schema file, and specifically, tell Claude

to reference that file any time it needs to better understand

the structure of data inside the database. Once

the update is complete, I'm going to take a look at the Claude MD file

and just verify that the note was added. When you mention

a file like this, its contents are automatically included

inside of your request. So if I ask what attributes

the user has, Claude can immediately answer without

reading the schema file.

---

#### Lesson 7: Making changes

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/303236](https://anthropic.skilljar.com/claude-code-in-action/303236)

**Video:** 005 - Making Changes.mp4 | **Duration:** 4m 4s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's try making a couple of changes to this project.

Along the way, I'll show you some useful features around Claude Code.

The first thing I'd like to do is move this placeholder text over

here on the left-hand side down to the center of this panel.

To help Claude understand exactly what content I want

moved, I'm going to take a screenshot of

that area right there, and then I'm going to paste

it into Claude Code using Ctrl V.

Note that it's Control-V and not Command-V

that you might be used to on Mac OS. Control-V is

used specifically to paste in a screenshot. I

can then ask Claude to center that placeholder. After

a little bit of searching, Claude is able to make the styling update.

And then back inside the browser, yeah, looks great. Let

me show you the next thing I would like to change in this app. I'm going to ask

for a card component that displays a title and some description.

The card is generated without any issue, but there is one

awkward thing. On left hand side in the chat interface,

there's String Replace Editor. That little panel

right there is meant to indicate to the user that a file is being

created. But right now it's using a very technical term

String Replace Editor for the tool that is being used behind the scenes.

I would like to show a user a little more friendly text here and

just tell the user that a file is being created and the name of

the file. And of course, we should also handle cases where

maybe this chatbot is editing a file or deleting

a file and other stuff like that. To help guide Claude's

attention, I'm going to once again take a screenshot of this so

it understands exactly what I'm talking about. Then, back

over here, I'm going to paste that image in and ask Claude

to replace that particular text with some more

user-friendly message. Now, this is a little

bit of a tricky task that will require Claude to do

a decent amount of research in this project to complete.

Whenever you give Claude a harder task, there are two

ways that you can easily boost Claude's intelligence. The

first way is to enable Plan mode. Plan mode

is enabled by pressing Shift-Tab twice, or

just once if you are already auto-accepting file edits.

In Plan mode, Claude will do much more research

over the contents of your project, reading more files

and coming up with a detailed plan on how to complete your

task. After completing the plan, Claude will

tell you exactly what it wants to do to complete your task.

At that point, you can either accept this plan, and Claude will

implement it, or you can redirect Claude in some

way, maybe it missed some file, or didn't consider

some scenario. The second way in which we can boost

Claude's intelligence is by enabling thinking. This

turns on Claude's extended thinking feature, allowing

it to reason more about a particular task. To

enable thinking, there are a handful of different trigger phrases.

Each one gives Claude a progressively larger token

budget to think with. Given that this is a trickier task,

I might ask Claude to ultra-think about the best way to implement

it. The last thing to understand is that planning

and thinking can be used together. So in addition to

this ultra-think, I'm going to also turn on Plan mode

as well. And now I'm going to run this and we'll see how well

Claude can implement this feature. Now, you might

be wondering when you should use planning and when you should use

thinking. Think of these two as handling

breadth-first depth. Planning mode is useful

when you have a task that requires a wide understanding

of your codebase and requires looking at different areas.

It's also useful when working on a task that requires several

steps to complete. Thinking, on either hand, is

useful when you are focusing on a particular tricky

bit of logic or troubleshooting a difficult

bug. The second question you might have is whether

you should just enable thinking and planning all the time.

Well, you certainly can, just keep in mind that planning

and thinking consume additional tokens, so there

is a cost associated with using them. After

a couple of minutes of work, it looks like the feature is complete. So

I'm going to go back over to my editor and test this out. So

right away, we can see that we get some better status information here

than what we have before. Users are now being told that a file

is being created. And if I send in a followed request,

maybe to change the title. Hopefully

now on the follow-up, we'll see something about editing that file.

So there we go. So now we're editing the app.jsx file.

Well, I would say Claude definitely succeeded in implementing

this feature. Now that we have made some changes to this

project, we should probably commit our changes. Claude

Code is a solid Git Assistant. We can ask it to

stage and commit our changes and it will write a

descriptive commit message for us.

---

#### Lesson 8: Course satisfaction survey

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/303701](https://anthropic.skilljar.com/claude-code-in-action/303701)

---

#### Lesson 9: Controlling context

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/303237](https://anthropic.skilljar.com/claude-code-in-action/303237)

**Video:** 006 - Controlling Context.mp4 | **Duration:** 3m 37s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, I'd like to show you a couple of different techniques

for controlling and directing the flow of conversation. Here's

a basic example right away. I'm going to ask Claude

to write tests for some functions written into a authentication

file. Claude quickly comes up with a plan for authoring

several different tests. However, I know that testing

this file is a little tough, and I'd like Claude

to only test one thing at a time. To interrupt

Claude, I can press escape. This will stop Claude

in its tracks, allowing me to suggest a different path.

Combining Escape, along with memories, is a really

powerful way to fix errors that Claude makes repeatedly. Here's

an example. I'm going to ask Claude to write tests for the

same file again. This time around, it will attempt to

read a test configuration file that doesn't actually

exist. Now, this is an error that I've seen

Claude make before on this project. So to

stop this mistake from being repeated, I'll very quickly hit

Escape. I'll then use the pound shortcut to add

in a memory about the correct name of this test config

file. And now, I probably won't have to see this error

again. Some of these conversation

control shortcuts seem like they're just for convenience.

But use correctly, they can really improve Claude's

ability to work effectively and stay on task. So

let me show you a more practical example. Inside

the auth.ts file, there are four different functions.

And I would like to get Claude to write tests for each of them one

at a time, first starting on a function called create

session. Claude will definitely attempt to write the tests,

but as it is running them, it runs into an error and

spends a little bit of time debugging it. It turns out

there was a package that I forgot to install. Eventually

the tests are completed and working, and it's time

to start working on the next set of tests. But

here's the thing. In my conversation history, there

is now a lot of back and forth around that broken package.

Now this is a bunch of context that is not at

all relevant to writing the next set of tests.

Ideally, we would be able to jump back in time and

go back to the previous message we sent and just update

it to say, write test for a git session. Now,

the benefit here is that we maintain the context where Claude

already took a look at the contents of the auth.ts file.

And it already knows what we're talking about when we refer to git session.

And because we dumped all those extra messages that were just about debugging,

we're not going to have as much distraction going on here. So

again, Claude can really just stay focused in on task.

To go back in the conversation history, hit Escape twice.

This will show you all the different messages that you have set, so you

can rewind back to a previous point in time and skip

over some intermediate conversation. Claude

is now going to start working on the next set of tests. This

time around, Claude stays super focused, but unfortunately,

it runs into a number of issues. It eventually resolves

them and gets the test to pass. Now at this

point, Claude has been working by itself for several minutes and

has a really good idea of how to write tests for this file.

At the same time, once again, we have a bunch of context

in this conversation history. When it is time

to write tests for the next function, I want to use

a command called compact. The compact

command will take all the messages in the current conversation

and summarize them. Compact is really useful

when Claude has learned a lot about the current task

and you want to maintain that knowledge as it goes into the next

task. The last context-related

command to be aware of is the Clear command. Clear

will dump the entire conversation history, allowing you to start

off from scratch. Clear is most useful anytime

you're about to start on a completely different task unrelated

to the current one. I recommend using these shortcuts

quite a bit, particularly when you are changing between tasks

or anytime you are having a long-running conversation with Claude.

In the remainder of this course, we'll use them several times to

make sure that Claude stays on task and focused.

---

#### Lesson 10: Custom commands

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/303234](https://anthropic.skilljar.com/claude-code-in-action/303234)

**Video:** 007 - Custom Commands.mp4 | **Duration:** 1m 44s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

When you run Claude Code, you can enter in a forward

slash and see a bunch of commands that are built into Claude Code

by default. In addition to these default commands,

you can easily add your own custom commands as well. Custom

commands are useful for automating repetitive tasks that

you find yourself running frequently. Let me show you an example of how

to make one. Inside of my project directory,

I'm going to find the .Claude folder. Inside there, I'll

make a new directory called commands. And then inside

that, I'll make a new file called audit.md.

The name of the file that we create, in this case audit,

is going to be the name of the command we eventually run. The

goal of this command is going to be to audit all the different dependencies

that have been installed into this project, update them

if there are any vulnerabilities, and then run

tests to make sure that nothing actually broke. Once

you have created the command file, you'll then restart Claude

Code. Don't forget to restart it. When you reopen

Claude Code, put in slash audit. This

will then display the command that you just created. You can then

run this, and in this case, it will do exactly what we ask Claude

to do. It'll run a command, see if there are any vulnerable

packages, fix them if necessary, and then run

tests. Commands can also receive arguments. Let

me show you an example. I'm going to make another command called write

test. Whenever I run this command, I want to have

some tests created for a very particular file inside

my project. Inside of the command text, I'm going

to put in a placeholder of dollar sign arguments. Whenever

I run the command, if I pass in a path to a file, that

path will be inserted at dollar sign arguments.

So now I can restart Claude Code again and then execute

the write test command. Now, to be clear,

the arguments we pass in don't have to be a file

path. It can be any string we want to pass in. So

I might casually ask for tests for a file in some particular

folder, giving Claude just a little bit of direction on

where to look.

---

#### Lesson 11: MCP servers with Claude Code

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/303239](https://anthropic.skilljar.com/claude-code-in-action/303239)

**Video:** 008 - Extending Claude Code with MCP Servers.mp4 | **Duration:** 2m 53s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

You can add new tools and capabilities to Claude Code

through the use of MCP servers. These

MCP servers either run remotely or locally

on your machine. A very popular MCP

server named Playwright gives Claude Code the

ability to control a browser. Let me show you how to

add it to Claude Code, and then we'll use it to develop

our app a little bit more. To install the server at

your terminal, not inside of Claude Code, we'll execute

Claude MCP Add. And then a name

for this MCP server, I'm going to name it playwright. And

then after the name, we'll add in a command that will start up

the server locally on your machine. We can then start

Claude Code and ask it to open a browser and navigate

to our application at localhost 3000.

Before the browser opens, you might notice that you are required to give

permission for that tool to run. If you get tired

of all those permission pop-ups, you can open up the Claude

directory inside their settings.local.json.

And then inside of the allow array, you can add in a

string of MCP underscore underscore,

notice there are two underscores there, playwright. This

allows Claude Code to make use of this MCP server and

the tools inside of it in any way it wants without requiring

you to provide permission every time. If I restart

Claude Code and then ask it to open a browser again,

it will do so without requiring me to give permission. There

are incredible number of ways that you can use the Playwright MCP

server. Let me show you one that would be really applicable to the

project we are working on right now. Back inside

my editor, I'm going to find the SRC, Lib, prompts,

generation.tsx file. This is the prompt

that is used to actually generate the components that you ask

for inside of our app. So I want to allow

Claude Code to make use of the browser, generate

a component on its own, and then tweak this prompt

on its own based upon the generated component. And

hopefully, we'll end up with some better looking components

being generated out of our app. So let me show you how

we would do that. Back inside of Claude Code, I'm going to ask

it to navigate to localos3000.

attempt to generate a component, take a look at the

generated source code and evaluate the styling, and

then update our prompt inside that generation.tsx

file, and hopefully we'll end up with some at

the end of the day better styling on our generated components.

So let's see how it does. Claude is going to first open

up the browser. It's going to attempt to generate a component.

And looking at some of the commentary from Claude here, it looks like

it's not quite so happy. You might actually notice

that it complains about a very common style that's used in

applications like this, a purple to blue kind

of gradient. Claude is then going to update

our prompt and then try to generate a new component.

And I'll be honest with you, this actually gave

a much better result than I ever expected. This

testimonial card actually looks really, really great. Based

on these results alone, you can immediately get a sense that

MCP servers really open the door to a lot of interesting

use cases. And I highly recommend you look into some

MCP servers that might aid Claude in developing

whatever kind of project you personally are working on.

---

#### Lesson 12: Github integration

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/303240](https://anthropic.skilljar.com/claude-code-in-action/303240)

**Video:** 009 - Github Integration.mp4 | **Duration:** 3m 40s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Claude code has an official GitHub integration that

allows Claude code to run inside of a GitHub action.

You can set up this integration by running slash install

GitHub app. This will walk you through a couple of steps.

First, you'll need to install the Claude code app on GitHub.

Next, you'll need to add in an API key. And then

after this, a pull request will be automatically generated.

This pull request adds in two different GitHub actions.

The first action adds in mentioning support. So

from an issue or a pull request, you can mention Claude

with @Claude and give Claude some kind of task

to run. The second action adds in support

for reviewing pull requests. So whenever you create a pull request,

Claude code will automatically run and review the proposed

changes. Both of these actions can be customized,

and you can also add in additional actions to trigger based

on other types of events. Let me show you how you

can customize the mentioning feature. First, we

just merged in those two action config files to

our repository on GitHub. So I need to pull

those changes down to my local machine. Then inside

of the newly created GitHub workflows directory, I'll

see these two action config files. One adds

in support for the pull request review, and the other adds

in support for handling mentions. Now, here's how

I want to customize the mention functionality. Whenever

I mention Claude inside of an issue or a pull request,

I wanted to be able to run the project and use the Playwright

MCP server to access the app inside

of a web browser, all inside of a GitHub action.

To make this work, I'll first add in a step before

Claude code runs in this workflow. I'll run

the setup command and then start the development server up.

Then I'm going to update the Claude code configuration. I'll

add in some custom instructions. These are passed directly

to Claude and they allow us to provide some additional

directions or context. In this case, I'll

tell Claude that the development server is already running and

that I can use the Playwright MCP server to access

the app in the browser if needed. Then I

will add in some configuration to set up the Playwright MCP

server itself. There is one other thing to be aware

of here. When you're running Claude Code inside of an action,

we have to specifically list out all the permissions that

we want to grant Claude Code. And there's one tricky

aspect to this. If you're using an MCP

server, you have to individually list out each

tool from each MCP server that you want

to allow. There is no shortcut for permissions

like we saw previously. Unfortunately, the Playwright

MCP server has many different tools, so they each

need to be listed out. Once I've finished with

this configuration update, I'll be sure to commit these changes and

push them. Now it's time to test out this updated

workflow. I'm going to give Claude a little task.

In our actual app, see these two buttons up here. Right

now they work fine. I can toggle between the preview and the code

panels without issue. But I'm going to pretend as though

they weren't working as intended. I'm going to take a

screenshot with that button right there. I'm going to make an

issue. I'm going to paste in the screenshots. And I'm

going to mention Claude with @Claude and ask it

to verify that the two buttons are working as intended.

I'll then create the issue and wait. Now, it is

going to take a minute or two for the action to actually start up

and for Claude's response. Remember, as we just saw in

the action, we are now setting up the entire app and

starting it running before Claude Code even starts to

run at all. But eventually, Claude

will respond. It will very often create a checklist

of steps to accomplish the given task. In this case,

it is going to attempt to visit the app, manually test out

the button, and fix any issues that it finds. Claude

will notice that the buttons actually are working just fine, and

so it's going to terminate early with the message documenting

its findings. Now, this is just a small

example of how you can use Claude Code's GitHub integration.

I recommend you spend some time to think about how you can custom

tailor it for your own particular project.

---

### Hooks and the SDK

#### Lesson 13: Introducing hooks

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/312000](https://anthropic.skilljar.com/claude-code-in-action/312000)

**Video:** 010 - Introducing Hooks.mp4 | **Duration:** 3m 37s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, we're going to take a look at hooks.

These allow you to run commands before or after Claude

attempts to run a tool. Hooks can be used to implement

really interesting and very useful functionality.

For example, after Claude decides to write a file,

you can automatically run a code formatter on

the created file, or you can run tests after

a file is edited, or you can block Claude

from reading particular files. The possibilities

are really endless, and I've got a couple of good

examples lined up to show you some ideas of

how you might use hooks on your particular project.

First, however, let me help you understand exactly how

hooks work. As a reminder, when you ask Claude

code something, your query is sent off to the Claude model

along with some tool definitions. The Claude model

might then decide to run a tool by providing a carefully

formatted response. And at that point,

it is up to Claude code to run the requested tool, maybe

in this case to read a file, and then respond with the result

of that tool call. Now hooks give

us the ability to execute code just before

or just after the tool execution.

Hooks that run before a tool are referred to as

pre-tool use hooks because they run before

the tool. And hooks that run after the tool are

referred to as post-tool use for the same reason.

To define hooks, we add configuration to the Claude

Settings file. Remember that there are several different

settings files, one for global use across all

projects on your machine, one for your particular project

that gets shared with other engineers, and one for just you

on a particular project. You can add hooks,

either by writing them out by hand, inside

this file, or by using the built-in slash hooks

command inside of Claude Code itself. The

configuration itself looks like what you see on

the right-hand side of the screen. Let me walk you through this example

file just to give you a better idea of what's going

on. So first, notice that there are two

distinct sections inside of this file. One

section lists out all the commands that should be executed before

a tool use. Remember, those are referred to as pre-tool

use hooks. The other section lists out all the different

commands that should be executed after a tool

use. And again, those are post-tool use hooks.

In each of these sections, we provide a matcher. This

indicates which tool use types we are looking for.

So in this case, I want to find uses of the read

tool. Whenever Claude Code attempts to read

a file, I want to run the command you see listed

there. Likewise, inside the post tool

use section, after a use of the write, edit,

or multi-edit tools, there's a different command

that I want to run. Now, here's the important part.

Here's what hooks are really intended to do. Those

commands you saw will be given details about the tool call

that Claude wants to run. In the case of a

pre-tool use hook, you can inspect what

Claude wants to do. And if for any reason

you don't want to allow it, you can block the tool use operation

and send an error message back to Claude. In

the case of a post tool use hook, the tool call

has already occurred, so it's too late to block it. But

you can do some follow-up operation based upon the tool

call, like maybe format a file that was just edited.

You can also provide some message back to Claude about

that tool use. For example, you might decide to

run a separate program to check the code quality

of the edit, or maybe do a type check,

and then provide that feedback back to Claude. Claude

might then take that feedback and make an update

to the file that it just wrote to. If you're still

confused about hooks or what they are intended to do, that

is absolutely okay. Wrapping your head around hooks

can be really challenging. So let's come back in a moment

and work on a sample project with hooks.

---

#### Lesson 14: Defining hooks

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/312002](https://anthropic.skilljar.com/claude-code-in-action/312002)

**Video:** 011 - Defining Hooks.mp4 | **Duration:** 3m 44s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

To get a better idea of how hooks work, we're

going to take a look at a new sample project. Attach this

lecture as a file called Query.zip. I'd

encourage you to download this project and open your code editor

inside of it. Once you've got your editor open, at

your terminal, Run, NPM, Run, Setup.

This is going to install a couple of dependencies and get a

couple of hooks ready for use. To better understand

hooks, we're going to make our own inside of this project. So

here's what I want our hook to do. Inside the

root directory of our project is a file called .env.

This file contains some sensitive information. And

out of an abundance of caution, I want to completely

prevent Claude from ever reading this file directly.

Let me show you a couple of diagrams to help you understand how

we're going to put this hook together. Step one is to

decide on whether we need a pre-tool use or a

post-tool use hook. In this scenario, we

want to prevent Claude from ever reading a particular file.

If we make a post-tool use block, then we will

have executed our hook or ran our command after

Claude already read the file. So in this case, we

definitely need a pre-tool use hook to make

sure that we can prevent the read operation from occurring.

The next thing we need to do is decide exactly which

kind of tool calls we want to watch for. I've

got a list of all the different current tool names on the right

hand side of this diagram. Now, memorizing all

the different tool names that are included inside of Claude

Code can be really challenging, especially since you can

add your own custom tools through the use of MCP

servers. So let me show you a little trick you can use

here. If I go back over and open up Claude

Code, I can directly ask Claude for a bullet

point list of all the different tool names that it has access

to right now. Out of all these different tools, there

are two that can be used to very easily read the contents of a

file. First, there's the retool, and then it's

easy to miss, but this one can actually read the contents of a file

as well, the GREP tool. GREP can search the

contents of a file. So we really want to watch

for tool calls for the retool and the GREP

tool. Next up, we need to write out a command

that is going to receive some information about the tool called

that Claude wants to make. Here's how that part works. We're

going to write out a command, Claude is going to automatically execute

it. And then on standard in to that process,

Claude is going to feed in some tool called data as

JSON. I've got an example of some tool called data

on the top right hand side. So it's going to be a big JSON

object that has some information about the tool name and

the input to that tool. In this case, the tool name

is read, so Claude is trying to call the read tool, and

it might be trying to read specifically a file path pointing

to that .e and v file. And again, that's the

file that we want to prevent a read operation for. So

then inside of our program or our command, we need

to receive this information through standard in, parse

that JSON, and then read the tool name, the

tool input arguments, and so on, and decide what

we want to do with this tool call. Then

onto step four. In step four, after our

command receives that proposed tool called data, we're

then going to exit. And our exit code is

going to provide a signal back to Claude Code. An

exit code of zero means everything is OK, and

we want to allow this tool call to occur. An

exit code of two, however, is a sign-to-Claude

Code that we want to block this tool call. And

that specifically only applies for the pre-tool use

hooks. Because remember, only in a pre-tool use hook

can we actually block a tool call. If we exit

with a code of two, then any standard air

logs that we generated inside of our command during that time will

also be sent as feedback to Claude. So we

can both deny the tool call and give Claude a reason

at the same time as well. So that's the entire

process. And I know once again, there's a lot of stuff

going on here. So let's go through this entire process

of wiring everything up needed for this hook inside of

our project to understand how all these steps come together.

---

#### Lesson 15: Implementing a hook

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/312003](https://anthropic.skilljar.com/claude-code-in-action/312003)

**Video:** 012 - Implementing a Hook.mp4 | **Duration:** 4m 14s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's put together our custom hook. Remember, the entire

goal here is to prevent Claude from ever reading the contents

of the .env file. In the last video, we

discussed many of the different configuration options we'll need to

set, so in this video, we'll be mostly focused on the implementation.

To get started, inside the . Claude directory, I'm

going to open up the settings.local.json file.

Remember, inside of here, we have a list of pre-tool

use hooks and post-tool use hooks.

As we discussed a moment ago, we want to make a pre-tool

use hook so that we can prevent Claude from ever reading the contents

of that particular file. I already added in

a little configuration section right here for us, just to

save us a little bit of typing. All we need to do is

fill in the matcher and the command. First

is the matcher. So the matcher is going to be the tools

that we want to watch for. In our case, as

we discussed, we want to watch for calls to the read

and the grep tools. I'm

going to separate those two tool names with a pipe symbol.

So that's not an L or a capital I. It is

a symbol right above the return key on your keyboard. Then,

next up, we need to provide a command to run whenever

Claude attempts to call those two tools. We

could put in here any command you want, so it can be a CLI,

it can be a call to a shell script, absolutely anything.

To follow the pattern that I've already established inside the rest

of this file, I'm going to call a node.js

script that I placed ahead of time inside the hooks directory

of this project. So inside the hooks directory, I

put together for us a read_hook.js

file. This is the file that I want to run whenever

Claude attempts to call one of those two tools.

So to call that, I'm going to replace the true right here, which

is just a placeholder for right now, with node

./hooks/

read_hook.js. I'm

going to save this file and that's all we have to do inside

of here. Next up, we need to actually implement

the command that's going to run anytime Claude tries to call the

read or the grep tools. So that's going to be the read_hook.js

file. At the top of this file, I've got some code

that's going to read from standard in and parse that data

as JSON. So this tool args

object right here, that's going to be the big JSON object I showed

you in this diagram back over here. So it's going to have properties

like session ID, the tool name, the tool input,

and so on. So all we really need to do is

take a look at that file path right there and decide whether

or not it is trying to read the .env file. If

it is, then we want to make sure that we exit from

our program or our command here with an exit code

of two. And hopefully also log some information

out to Claude that says, sorry, but you can't read that file.

So you'll notice that back over here, I've already got some code that's going to read that

file path. You'll also notice that there is a

fallback of looking at toolInput.path

right here. I'll tell you why that's added in in just

a moment. So now let's implement the to-do

statement. We'll say if readPath includes '.env',

that means that Claude must be trying to read the .env

file. And if that's the case, then I want to make

sure that we block that operation and provide some logging

feedback to Claude. So I'm going to first add in a

console.error, specifically a console.error,

because we want to log to standard error. Remember, that's

how we provide some feedback to Claude. And I'll say something

like, "You cannot read the .env

file." And then I'll do a process.exit(2).

So now to test this out, I'm going to save the file. I'm

going to open up Claude Code. If you already have it

open, make sure you restart Claude Code. You

have to restart it to have any changes to your hooks take effect.

I'm going to ask Claude to read the .env

file. And it's probably going to attempt

to, but as it attempts to read it, we're going to

send back an error that says "You cannot read the .env file."

And Claude is hopefully going to realize that, sorry, you can't

actually read this. As a matter of fact, it's even able to recognize

that it was prevented by a read hook. Now,

our hook should also be working on grep operations as

well. So if I ask Claude to try the

grep tool, This should also

hopefully be forbidden as well. So let's see how it

does. And yep, same thing, it is now forbidden.

So that is a working hook that we have put together. Now

this hook is not terribly useful, and I'm going to show you

a much more useful hook in just a moment.

---

#### Lesson 16: Gotchas around hooks

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/312423](https://anthropic.skilljar.com/claude-code-in-action/312423)

You may notice that after running the npm run dev command there are two settings.json files in the .claude directory. Let me explain what's going on there.
The Claude Code documentation lists some recommendations around hooks security:

One of the recommendations is to use absolute paths (rather than relative paths) for scripts. This helps mitigate path interception and binary planting attacks.
This recommendation also makes it much more challenging to share settings.json files. The reason is simple: the absolute path to any of the hook scripts on your machine will likely be different from the absolute path on my machine, simply because we will probably place the project in separate directories. 
To solve this problem, our project has a settings.example.json file. Inside of it, the script references contain a $PWD placeholder. When we run npm run setup, some dependencies are installed, but it also runs an init-claude.js script placed inside the scripts directory. This script will replace those $PWD placeholder with the absolute path to the project on your machine, copy the settings.example.json file, and rename it to settings.local.json.
This script allows us to share settings.json files but still use the recommended absolute paths!

**Code Examples:**

```
npm run dev
```

```
settings.json
```

```
.claude
```

```
settings.json
```

```
settings.example.json
```

```
$PWD
```

```
npm run setup
```

```
init-claude.js
```

```
$PWD
```

```
settings.example.json
```

```
settings.local.json
```

**Resources & Links:**


---

#### Lesson 17: Useful hooks!

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/312004](https://anthropic.skilljar.com/claude-code-in-action/312004)

**Video:** 013 - Useful Hooks!.mp4 | **Duration:** 11m 33s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, I'd like to show you some really useful

hooks that you might want to use on your own projects. These

hooks are intended to address some common weak points

in Claude Code. To help you understand how the first one

works, let me give you a quick demonstration of a problem

that Claude Code sometimes runs into, especially

on larger projects. So inside the SRC

directory, I'm going to find schema.ts.

Inside of here, there's just one single function called create

schema. This function is called from the main.ts

file, specifically right here. Now,

I'm going to go back to the schema.ts file and I'm going to update

the function definition. I'm going to say that if you

ever want to call this function, you must also pass

in a verbose argument that must be of

type Boolean. Now, as soon as I add in this change,

if I go back to the main.ts file, I'm going to get a

type of error because I just updated the definition of

this function, but I have not actually added in

a value for verbose. So the error

right here says specifically argument for verbose

was not provided. Now, I'm

going to undo that change very quickly. I'm going to

close the main.ts file. I'm then going to open

up Claude Code and ask it to make the exact same

change. Now if I run this, Claude Code is

going to have absolutely no issue making this edit whatsoever. But

it's going to update this file and then unfortunately after

making that change, so there's the new verbose true right

there. Unfortunately, Claude won't go around the project

and try to find where that function is actually called and try to

update any of the different call sites. So if I now open

up main.ts, we'll see that we do, in fact, have

an error over here. And Claude didn't really catch this,

unfortunately. So the first hook that I want to show you

will fix this solution super easily.

In case you're not familiar with TypeScript, and if you're not, that's totally

fine. If I close out of Claude Code and run the

command, TSC-dash-noemit,

that's going to run a type check on my entire project. And

in this type check, we can see that the error is very

evident right here. So it's complaining about our call

to create schema from that main.ts file.

So my idea for a hook is really simple. I

think that any time that we edit a TypeScript file,

we should run the TypeScript type checker and see

if there are any distinct errors. If there are,

we should attempt to feed these errors back into Claude

immediately inside of a post-tool use hook.

And hopefully, this will give Claude a signal and tell it that there

is a type error that it just introduced, that

it probably needs to go and fix somewhere else inside of our project.

Now, I already put this hook together for us, fortunately, just

to save us a little bit of time inside the hooks,

TSC.js file. So inside this file,

I've got a bunch of logic put together to run the TypeScript type checker,

take any errors that found, and pass them back into

Claude. At present, I disabled

this hook just so I can give you that demonstration you just saw. So

I disabled it by adding the process exit 0 right there.

I'm going to delete that. And now this hook should be working AOK.

So if I now go back to the schema.ts

file, Remove that verbose flag, restart

Claude Code, and ask it to make

the same change once again. It

will make the change. And then hopefully this time, it will immediately

get that feedback from the TypeScript type checker saying,

hey, you've got an error somewhere else in the project that you've just introduced.

And hopefully, Claude will go and fix it. So we can

see right here, there's the edit that was made. We got

some edit operation feedback from the hook that we put together.

So it found an issue inside of one of our different files.

And Claude is now saying, OK, I understand. I introduced

an error. I need to fix the call to create

schema inside of main.ts.

And then the next update it makes is going to attempt to go into

that file and update that function call to

add in that missing argument. So this is

a hook that you might want to try implementing on your own personal

projects. Now, even though this hook was implemented

specifically for TypeScript, it still works for any

other kind of typed language where you can run a type

checker very easily. Even if you're using an untyped

language, you might even implement the same idea of functionality

using tests instead of running a type checker. So

every time an edit is made, you could run your test to make

sure that the edit is OK. Now, the next

hook that I would like to show you is a little bit more challenging

to explain, but once you get the idea behind it, I think

that you will definitely find this next one really

helpful, particularly in larger projects. To

help you understand this other hook, I want to give you a little bit of background

on this project. Inside of the SRC query

directory, there are many different files. Each

of these different files contains many different SQL queries

written inside of different functions. Inside

of the orderqueries.ts file in particular,

I want to point out that there is a function inside of here called

git pending orders. This query goes through

a database that contains some e-commerce related

data. And in theory, it's going to find all the different

orders that have been created that are in a pending state.

So just keep that function in mind for a moment. Okay,

so I'm going to show you a couple of good diagrams really quickly to help you understand

a common problem that starts to arise inside of larger

projects. So in this diagram, I've got my

list of different query files on the left-hand side, and as we saw,

each of those different query files contains many different queries.

Inside of that order queries file in particular is the

git pending orders function. So we've already got

a query put together that will attempt to find some

different pending orders. Now, if I go

to Claude and ask it to update the main.ts

file to print out all the different orders that have been

in a pending state for longer than three days, in

a perfect world, Claude would find the order

queries.ts file. It would find that existing query

and it would make use of it as opposed to writing

out a brand new query. So that's what we want.

And we'll see that if we make use of Claude right now and ask

it to do exactly that, We're going to get

exactly the result we want. So I'm going to ask Claude in the main.ts

file, print out orders that have been pending. Now,

to Claude's credit, it is going to take a look at the

different query files that exist. It's going to find the order queries

file. And then inside there, it's going to recognize that there

is already a query called get pending orders. And

it's going to attempt to use that function as opposed

to creating a new query. We didn't want a new

query. We wanted Claude to use the existing

function. So when we gave Claude a very focused

and directed task, it was able to understand that,

yeah, I probably shouldn't write a new query. It should at least

take a look at some of the ones that already exist. And that was definitely

good. Now I'm going to give Claude a little bit

of a curve ball. I'm going to purposefully make this task

a little bit more difficult. First, I'm going to run slash

clear to clear out all the context that we've gained. Then,

I'd like you to take a look at the task.md file.

Inside this file, I put together a prompt that is still going to

ask Claude to find orders that have been pending for a while,

but I've also wrapped it up in some larger project.

I'm asking Claude to write out a Slack integration

that's going to message a specific channel once

a day with all the different orders that have been pending for too

long. So in this scenario, we still want to find orders

of been pending for too long, but now I've wrapped it inside

this larger task. And if I take this

task and then feed it into Claude,

again, after doing that slash clear operation, we're

going to see that this time around, unfortunately, it's

not going to stay quite as focused, and it's going to end up

trying to write out a brand new Git pending

orders query, which is, again, not what we want,

because that would be a duplicating code throughout our project.

If I let this run for a bit, I will eventually see that, yes,

it does, in fact, make a brand new query called Git

orders pending too long. So this is

an example of where a Claude kind of lost focus and

decided to write a brand new query as opposed to reusing

an existing one. Again, we've got some duplicate code

here, which is probably not what we want. In

addition, it didn't only create the new query, it also

created a brand new file, which is also probably something we don't

want. We'd probably want this order-related query to

be added to the order queries file. So

now that we understand the issue here, let me show you how we could fix this potentially

by making use of a hook. All right, so

whenever Claude attempts to write, edit, or

use the multi-edit tool to modify something inside

the queries directory specifically, I'm going to

run the following hook. First, inside this hook, I'm

going to launch a brand new separate copy of

Claude Code. I'm going to ask this new copy

to take a look at the change that was just made and take

a look at some of the existing code inside the queries directory and

see if a similar query is already inside there.

Then if there is an existing query, then

I'm going to take that feedback and send it back to the original

copy of Claude and I'm going to ask Claude to maybe

decide to fix the situation. So remove the added

query and make use of the one that already exists. So

this is going to allow us to make sure that the queries folder generally

stays clean and doesn't have a bunch of duplicate code

inside of it. So let me show you how this would work

in action. First, I'm going to flip back over here.

I'm going to delete the brand new order alerts.

queries.ts file that was made and

the slack.ts file that was made as well. Then

I'm going to find inside the hooks directory the query hook

file. So I already put this hook together for us. Right

now it is currently disabled because I got a process.exit

at the very top. So let's walk through this hook

really quickly. First, I'm going to tell this thing that

it's only going to review changes to the SRC queries

directory. Then, a little bit lower, I'm going to check

and see if the change that was just made was made to the queries

directory. After that, I've then got a long

prompt here that is asking Claude to do a review

on the change that was just made. And then after that is

where I'm launching Claude Code programmatically. Specifically,

these lines right here. This is making

use of the Claude Code TypeScript SDK. I can

give you a lot more information on it in just a little bit. For right

now, just understand that this right here is essentially the same

as us making use of Claude Code at the terminal.

Once Claude Code runs, and I get a response back out of it, I

check and see if Claude decides that, yeah, the changes look

okay, or maybe we've got a duplicate query. And

if we do, then we're going to exit early with an exit code

of two, which is going to give this feedback back

to Claude and hopefully tell it that it needs to make a change.

So now that I've got this additional hook put together

and enabled by removing that process exit zero at the

top, I'm going to again restart Claude Code and

then run the same query again. And hopefully

this time it might initially put in

that duplicate query, but then our hook right here is going to

run and hopefully tell it, hey, we don't want that duplicate code.

You should make use of some already existing query to

implement this functionality. Now, Claude Code

is once again going to attempt to create a brand new, completely

separate query file, not making use of the old

query that already existed. When it tries to create that

file, however, our hook is going to run. It's

going to launch that separate copy of Claude Code, which is going to do

some research and find that there is, in fact, an existing

query that can be reused. It's going to provide

some advice and say, hey, you could probably go and update this

other existing query to suit your purposes perfectly.

And we'll see some feedback from Claude, our primary instance that

we are interacting with saying, ah, yes, there is

this existing query. Let's just modify

that existing query rather than attempting to

write out a brand new one. Now the downside

to this hook is that it's going to take some additional time and

expense to run every single time that I want to edit something

inside the queries directory. But the upside is that

I'm going to end up with a lot less duplicate code inside

of my queries directory. So it really comes down to a set of trade-offs

for you deciding whether or not you want to implement something like this in your

own project. If you do, I would at least recommend

doing what I showed you inside of the query hook.

So this one right here, and only watching maybe a handful

of directories like really important folders inside of your project,

just to minimize the amount of extra work that is being

done.

---

#### Lesson 18: Another useful hook

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/312427](https://anthropic.skilljar.com/claude-code-in-action/312427)

There are more hooks beyond the PreToolUse and PostToolUse hooks discussed in this course. There are also:

Notification - Runs when Claude Code sends a notification, which occurs when Claude needs permission to use a tool, or after Claude Code has been idle for 60 seconds
Stop - Runs when Claude Code has finished responding
SubagentStop - Runs when a subagent (these are displayed as a "Task" in the UI) has finished
PreCompact - Runs before a compact operation occurs, either manual or automatic
UserPromptSubmit - Runs when the user submits a prompt, before Claude processes it
SessionStart - Runs when starting or resuming a session
SessionEnd - Runs when a session ends

Here's the confusing part:

The stdin input to your commands will change based upon the type of hook being executed (PreToolUse, PostToolUse, Notification, etc)
The tool_input contained in that will differ based upon the tool that was called (in the case of PreToolUse and PostToolUse hooks)

For example, here's a sample of some stdin input to a hook, where the hook is a PostToolUse that was watching for uses of the TodoWrite tool. For reference, that is the tool that Claude uses to keep track of to-do items.
{
 "session_id": "9ecf22fa-edf8-4332-ae85-b6d5456eda64",
 "transcript_path": "<path_to_transcript>",
 "hook_event_name": "PostToolUse",
 "tool_name": "TodoWrite",
 "tool_input": {
 "todos": [{ "content": "write a readme", "status": "pending", "priority": "medium", "id": "1" }]
 },
 "tool_response": {
 "oldTodos": [],
 "newTodos": [{ "content": "write a readme", "status": "pending", "priority": "medium", "id": "1" }]
 }
}
And for comparison, here's an example of the input to a Stop hook:
{
 "session_id": "af9f50b6-f042-4773-b3e2-c3a4814765ce",
 "transcript_path": "<path_to_transcript>",
 "hook_event_name": "Stop",
 "stop_hook_active": false
}
As you can see, the stdin input to your command will differ significantly based upon the hook (PreToolUse, PostToolUse, Stop, etc) and the matcher used (in the case of PreToolUse and PostToolUse). This can make writing hooks challenging - you might not know the exact structure of the input to your command!
To handle this challenge, try making a helper hook like this:
"PostToolUse": [ // Or "PreToolUse" or "Stop", etc
 {
 "matcher": "*",
 "hooks": [
 {
 "type": "command",
 "command": "jq . > post-log.json"
 }
 ]
 },
]
Notice the provided command. It will write the input to this hook to the post-log.json file, which allows you to inspect exactly what would have been fed into your command! This makes it a lot easier for you to understand what data your command should inspect.

**Code Examples:**

```
PreToolUse
```

```
PostToolUse
```

```
Notification
```

```
Stop
```

```
SubagentStop
```

```
PreCompact
```

```
UserPromptSubmit
```

```
SessionStart
```

```
SessionEnd
```

```
PreToolUse
```

```
PostToolUse
```

```
Notification
```

```
tool_input
```

```
PreToolUse
```

```
PostToolUse
```

```
PostToolUse
```

```
TodoWrite
```

```
{
  "session_id": "9ecf22fa-edf8-4332-ae85-b6d5456eda64",
  "transcript_path": "<path_to_transcript>",
  "hook_event_name": "PostToolUse",
  "tool_name": "TodoWrite",
  "tool_input": {
    "todos": [{ "content": "write a readme", "status": "pending", "priority": "medium", "id": "1" }]
  },
  "tool_response": {
    "oldTodos": [],
    "newTodos": [{ "content": "write a readme", "status": "pending", "priority": "medium", "id": "1" }]
  }
}
```

```
{
  "session_id": "9ecf22fa-edf8-4332-ae85-b6d5456eda64",
  "transcript_path": "<path_to_transcript>",
  "hook_event_name": "PostToolUse",
  "tool_name": "TodoWrite",
  "tool_input": {
    "todos": [{ "content": "write a readme", "status": "pending", "priority": "medium", "id": "1" }]
  },
  "tool_response": {
    "oldTodos": [],
    "newTodos": [{ "content": "write a readme", "status": "pending", "priority": "medium", "id": "1" }]
  }
}
```

```
Stop
```

```
{
  "session_id": "af9f50b6-f042-4773-b3e2-c3a4814765ce",
  "transcript_path": "<path_to_transcript>",
  "hook_event_name": "Stop",
  "stop_hook_active": false
}
```

```
{
  "session_id": "af9f50b6-f042-4773-b3e2-c3a4814765ce",
  "transcript_path": "<path_to_transcript>",
  "hook_event_name": "Stop",
  "stop_hook_active": false
}
```

```
PreToolUse
```

```
PostToolUse
```

```
Stop
```

```
PreToolUse
```

```
PostToolUse
```

```
"PostToolUse": [ // Or "PreToolUse" or "Stop", etc
  {
    "matcher": "*",
    "hooks": [
      {
        "type": "command",
        "command": "jq . > post-log.json"
      }
    ]
  },
]
```

```
"PostToolUse": [ // Or "PreToolUse" or "Stop", etc
  {
    "matcher": "*",
    "hooks": [
      {
        "type": "command",
        "command": "jq . > post-log.json"
      }
    ]
  },
]
```

```
post-log.json
```

---

#### Lesson 19: The Claude Code SDK

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/312001](https://anthropic.skilljar.com/claude-code-in-action/312001)

**Video:** 014 - The Claude Code SDK.mp4 | **Duration:** 2m 46s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

As we are looking at the query review hook

a moment ago, we got a brief look at the Claude code SDK.

The SDK allows you to use Claude code programmatically.

You can use the SDK via the CLI, TypeScript

library or Python library. This is the exact

same Claude code that you will already use at the terminal. It

has all the same tools and will use them to complete a given

task. The SDK is most useful

as part of a larger pipeline or tool as we saw

in that hook a moment to go. You can easily wiring

Claude Code as part of a larger process to add

in a bunch of intelligence to some given workflow. I'd

like to give you a quick demonstration of the TypeScript

SDK in particular by adding it into our existing

project. Back inside of my editor, I'm

going to find the SDK.ts file inside of the root

project directory. Inside of here, I put together just

a little bit of code to get us started with the SDK. I'm

going to update the prompt at the top and ask Claude to

look for duplicate queries inside the SRC

queries directory. Then I'm going to save this file and

to run it, I'll open up my terminal and execute NPMRun

SDK. Now, this is not a built-in

command or anything like that just so you know, but in the scenes, it just executes

this file as a normal TypeScript file. I just put

together this little shortcut for us to make running a TypeScript file

a little bit easier. When we run this, we'll see the raw

conversation between our local copy of Claude Code and

the Claude Language model, message by message. Eventually,

we'll get kicked back to the command line. The very last message

printed out will contain the final response from Claude.

Now there is a little bit of a gotcha around the SDK.

And that is that by default, it only has read abilities.

So in other words, it can only read files, directories,

do grep operations, and so on. It does not

have the ability to write or edit or create and

so on files. To give it right permissions,

you can either manually add in right permissions to the query

call right here, or alternatively, you can add in

some permission settings to your settings file

inside of your dot-Claude directory. Let me show you how

we can allow the SDK to use the edit tool

within this project. I'm going to find the prompt argument

right here. Right after it, I'll add in options, put

in an object, allow tools, that'll

be an array, and I'll put in edit. I'm

going to update the prompt at the top and I'll ask it to

add a description to the package.json

file. Now I'm going to save this and

run npmrunsdk once again. And

then once it is complete, I can open up the

package.json file and I will see that it did in fact

add in a description. So now definitely has the ability

to edit files. As I mentioned earlier,

the Claude Code SDK is most useful as

part of other tools. So I would encourage you to think

of opportunities to use it in helper commands, scripts,

or probably most notably hooks inside of your

own projects.

---

### Wrapping up

#### Lesson 20: Quiz on Claude Code

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/308391](https://anthropic.skilljar.com/claude-code-in-action/308391)

**Assessment (8 questions):**

**Q1:** What is the fundamental limitation of language models that necessitates the use of a tool system in coding assistants?

- [ ] They can only generate code in specific programming languages
- [ ] They have limited memory capacity for large codebases
- [ ] They cannot understand complex programming concepts
- **[CORRECT]** They can only process text input/output and cannot directly interact with external systems

**Q2:** What permission configuration is required when integrating MCP servers with Claude Code in GitHub Actions?

- **[CORRECT]** Each MCP server tool must be individually listed in the permissions
- [ ] No special permissions are needed if running in GitHub Actions
- [ ] Permissions are automatically inherited from the GitHub repository settings
- [ ] A single blanket permission for all MCP operations

**Q3:** What is the primary difference between Plan Mode and Thinking Mode in Claude Code?

- [ ] Plan Mode is for writing code while Thinking Mode is for debugging
- [ ] Plan Mode is faster while Thinking Mode is more accurate
- [ ] Plan Mode uses fewer tokens while Thinking Mode uses more tokens
- **[CORRECT]** Plan Mode handles breadth (multi-step tasks) while Thinking Mode handles depth (complex logic)

**Q4:** Which of the following correctly describes the three types of Claude.md files and their usage?

- [ ] Project level (debugging), Local level (testing), Machine level (production)
- [ ] Project level (personal use), Local level (team sharing), Machine level (repository specific)
- **[CORRECT]** Project level (shared with team, committed), Local level (personal, not committed), Machine level (global for all projects)
- [ ] Project level (configuration), Local level (documentation), Machine level (automation)

**Q5:** How do you create a custom command in Claude Code that accepts runtime parameters?

- [ ] Use the @parameters decorator in the command file
- [ ] Define parameters in settings.json configuration
- [ ] Add command line flags when executing the command
- **[CORRECT]** Include $ARGUMENTS placeholder in the markdown command file

**Q6:** Which type of hook can prevent a tool call from happening if certain conditions are met?

- [ ] PostToolUse hook
- [ ] Project hook
- [ ] Global hook
- **[CORRECT]** PreToolUse hook

**Q7:** A developer wants to prevent Claude from reading sensitive .env files. Which type of hook should they set up, and what tool names would they likely match?

- [ ] PostToolUse hook, matching Write and Edit
- [ ] PreToolUse hook, matching Write and Create
- **[CORRECT]** PreToolUse hook, matching Read and Grep
- [ ] PostToolUse hook, matching Read and Delete

**Q8:** What is the primary purpose of hooks in Claude Code?

- [ ] To manage project dependencies.
- [ ] To automatically generate new code snippets.
- **[CORRECT]** To run commands before or after Claude executes a tool.
- [ ] To provide a user interface for Claude.

---

#### Lesson 21: Summary and next steps

*Source:* [https://anthropic.skilljar.com/claude-code-in-action/303238](https://anthropic.skilljar.com/claude-code-in-action/303238)

**Video:** 010 - Wrap Up.mp4 | **Duration:** 0m 53s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

I hope you've enjoyed this overview of Claude

Code. Before we finish up, I want to give you some advice on

where to go from here. First, keep in mind that

Claude Code is constantly changing and in active

development. So keep an eye on the homepage of Claude

Code. I've got the address to it right there. And watch for new features

and techniques to come out. Secondly, I really recommend

you experiment. There's a lot of different ways to customize

Claude Code and really tailor it to your particular use case.

Try to author some custom commands or put extra instructions

in your Claude MD file. And also try out a couple

of different MCP servers beyond the ones we looked at inside

this course. Finally, automate.

Take a look at the GitHub integration, and think of some

different common tasks that you go through all the time, and think

of some ways you can delegate those to Claude automatically based

upon events that occur inside of your GitHub repository.

Well, again, I hope you enjoyed this course, and enjoy

your time working with Claude Code.

---

*Extracted from Anthropic Academy via authenticated session | Deep Extraction v3 | 2026-04-12*
