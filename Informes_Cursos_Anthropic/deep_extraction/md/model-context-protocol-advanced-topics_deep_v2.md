# Model Context Protocol: Advanced Topics

> **Source:** [https://anthropic.skilljar.com/model-context-protocol-advanced-topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics)
> **Category:** mcp | **Difficulty:** advanced | **Domain:** Model Context Protocol
> **Tags:** mcp, sampling, notifications, transport, stdio, sse, http, production
> **Extracted:** 2026-04-11 | **Version:** v3 (with YouTube transcripts + quiz content)

---

## Extraction Statistics

| Metric | Value |
|--------|------:|
| Total Lessons | 15 |
| Sections | 4 |
| JW Player Transcripts | 10 |
| YouTube Transcripts | 0 |
| Modular Text Lessons | 4 |
| Quiz Assessments | 0 |
| JW Transcript Chars | 65,394 |
| YouTube Transcript Chars | 0 |
| Modular Text Chars | 61 |
| **Total Content** | **65,455** |

## Curriculum Structure

- **Introduction** (1 lessons)
- **Core MCP features** (7 lessons)
- **Transports and communication** (5 lessons)
- **Assessment and next steps** (2 lessons)

---

## Complete Lesson Content

### Introduction

#### Lesson 1: Let's get started!

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296349](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296349)

**Video:** 001 - Introduction.mp4 | **Duration:** 1m 28s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Hello and welcome. My name is Stephen Grider

and I'm a member of Technical Staff at Anthropic. In

this course, you're going to learn a wide variety of advanced

topics around model context protocol. Before

we dive in, I want to give you a quick overview of some

of the different topics we will be discussing.

We will begin with sampling, which allows an MCP

server to request a client to call a language model

like Claude to generate some amount of text. We'll

then take a look at providing better feedback to clients accessing

your MCP server by using logging and progress

notifications. After that, we'll spend some

time discussing routes, which allow you to point an

MCP server to specific files or folders that

it should access. From there, we'll take a deeper

look at the MCP spec itself to

really help you understand the technical side of server

client communication by looking at the specific

message format that MCP uses. We

will then immediately apply that knowledge to see how the standard

IO transport works and then close out with a very

deep dive on remotely hosted servers using

the streamable HTTP transport.

There is a lot of content here, so to make sure we can

get through all these different topics, there are a couple of things

that you need to know ahead of time. First, we will

be looking at a lot of Python code. Now you don't need

to be a Python expert, but you should at least be able to

read Python. Second, you should already have a

basic understanding of MCP, including clients,

servers, and tools. So with that, let's

dive into our first technical topic.

---

### Core MCP features

#### Lesson 2: Sampling

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296288](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296288)

**Video:** 002 - Sampling.mp4 | **Duration:** 5m 17s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Sampling allows a server to access a language model like

Claude through a connected MCP client. To

help you understand what that means and what sampling is all about,

I want to show you a quick demo application. So

here we go. This is a chat application that

is powered by Claude, so I can ask it what's one plus

one, and I'll get a response back. This chat

application is also connected to a single MCP

server that implements one tool called the Research

Tool. I can use this tool to ask Claude to maybe

write a report on archaeology. And when I do so,

Claude is going to decide to use that research tool, is saying

you're going to go and do some research, synthesize all the results,

and then present a report back to me. Now

that you have seen this research tool run, I like to show

you what is going on behind the scenes in this application and how

the research tool actually works. All right,

so here's a high-level overview of what's going on. First,

at the very top left, I've got a next JS application

that's what's actually rendering some content inside the browser, and

that's got an integrated MCP client inside of

it. A user at some point in time is going to ask

us to research a topic like archaeology. We're

going to send that query off to Claude, and Claude is going to decide

to run the research tool that it has been provided

ahead of time. Our MCP client

on the next JS application is going to translate that into a

tool called Request and send it over to the MCP

server. Then on the MCP server, the

research tool is going to run. It's going to make a number of

requests off to Wikipedia and try to find some articles

around archaeology and then some related content

and so on. Once the research tool has fetched some

number of pages from Wikipedia, we need to take all that

content and synthesize it into a final report that

can be displayed to the user. And there's more than one way

that we could do that. Let me show you two different options we have.

In option number one, we could have the MCP server

reach out directly to Claude or some similar LLM

and ask it to summarize all the results that found

from the Wikipedia searches. So in this case, we

would be giving our MCP server direct access

to a language model. This would absolutely

work. It is definitely something we could do. However, this

adds a lot of complexity to our MCP server. We

would have to write in some amount of code to allow the MCP

server to make a request off to Claude, get the response back,

extract the generated text, and so on. We would also

have to make sure that the MCP server has an API

key to access Claude or whatever other language

model we were using. So again, option number one would

work, but it adds a decent amount of complexity.

So on to option 2. In option 2, we're

going to have our MCP server make use of the technique

referred to as sampling. With sampling, we're

going to have our MCP server ask the client

to run a prompt on his behalf. So

in short, the MCP server is going to write up a prompt,

send it off to the MCP client, and say, hey, could

you feed this into Claude for me? The MCP client

that we've put together isn't going to take that prompt and send

it off to Claude. It will get a response back and

then send the result of that text generation back

to the MCP server, where it can then do whatever it wants

to do with that generated text. This

approach moves the complexity over to the MCP

client. And in this case, it's kind of OK. Because

as you saw, our MCP client or that next JS

application already has an existing connection to

Claude. It is already making requests off to Claude. So

it's not that much more to just run one additional

request on behalf of the MCP server. The

other obvious benefit here is that the MCP server

does not need a API key to access Claude

at all. And if this is a publicly accessible MCP

server, now it doesn't need to worry about paying for

tokens generated on behalf of someone else making

use of the server. So this technique is referred

to as sampling. It allows a MCP server to

ask the client to run Claude or any other

language model to generate some amount of text. You

can really think of sampling as moving the responsibility

of calling Claude from a server off to the client.

Sampling is most useful anytime you're putting together a publicly

accessible MCP server. You don't want to have

a MCP server that is publicly available for anyone to use

that is just going to allow anyone to come and generate some text.

For your publicly accessible server, you would want to make use

of sampling and move the responsibility of generating

text from your server off to whatever

client is connecting to it. Making use of

sampling requires a little bit of setup on both the server

and the client. First off, on the server, inside

of a tool function, you will call the Create Message

function. And you're going to pass into that a list of messages

that you want to be eventually handed off to Claude. This

list of messages is going to be formulated into a request

that gets sent down to the client. Then on

the client, you have to write out a little bit more code,

specifically something called a sampling callback. I've

got an example sampling callback at the top of this code

snippet on the right-hand side. Your sampling callback

is going to receive the messages that were sent from the server.

Then inside this callback, it is up to you to call

a Claude or whatever other language model you are

making use of, generate some text, and then return

a create message result. All

right, so that is sampling. As you can see, it's not terribly

complicated. It's really just this concept or this idea

of shifting the burden of generating some text from the

server back over to the client. And again,

this is a technique you're definitely going to want to look at anytime

you're putting together a publicly accessible MCP

server.

---

#### Lesson 3: Sampling walkthrough

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/295172](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/295172)

← Previous Next →

---

#### Lesson 4: Log and progress notifications

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296284](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296284)

**Video:** 003 - Log and Progress Notitications.mp4 | **Duration:** 2m 41s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Next up is logging and progress notifications.

These notifications are really easy to set up and greatly

improve the user experience around your MCP server.

So let me show you once again a quick demonstration. You

might recall the app I showed you just a moment ago with this research

application. And if I ask Claude to

generate a report on archeology, it is going to make a

tool call through that MCP server that we discussed a moment

ago. It's going to call specifically the research function.

Now, it takes a while for this research function to complete.

And as it is running, a user is not really getting any

feedback. So as far as the user knows, this tool

call might have actually failed, and it might just be in a

stalled state or something like that. So it

would be really nice if we could give users a little

bit more insight into what is going on behind the scenes.

To do so, we can make use of logging and notifications.

So let me show you what that exact same query would look like if

I turn on logging and notifications, which

I did when I just refresh the page right now. So I'm

gonna ask the same query again, and now I'm gonna get the

same research tool call, but now I'm going to

get a progress meter and some log statements to go along

with it. The progress and log meter is not

fake data. These are log and progress statements

that are being emitted inside of the tool call, inside

of the research tool. So let me show you a little bit of

code and help you understand how this works. To

get started with logging and progress notifications inside

of a tool function on our server, we'll receive the

context argument, which is automatically included as the

last argument to our tool function. On that context

object are a variety of different methods that allow us to either

log information or report the progress

of this tool run back over to the client. So we

get methods like info and report progress.

Anytime you call these functions, a message will be automatically

sent back to the client. To make use of the log

statements and the progress updates on the client, we'll write

out a little bit of code similar to what we saw just a moment ago around

sampling. So we'll put together a callback function.

They'll be called whenever we receive a logging statement

from the server. will also make a separate callback

that will receive updates on progress from the server. We'll

then take the logging callback and pass it off to our client

session and the progress callback and that gets passed

off to the call tool function. Inside

of these callbacks, it is up to you on how you're going to report

these log statements and the progress to your user.

You can just print them out at the terminal if you're making a CLI

application. If you're making a web app, you'll

have to come up with a little bit more clever solution to get that information

down to the browser. You, of course, also do not

have to actually include any of these log statements

or progress statements. You don't have to show them to the user at all if

you do not want to. These are just user experience

enhancements. Once again, to give your user a better idea

of what is going on.

---

#### Lesson 5: Notifications walkthrough

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/291036](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/291036)

← Previous Next →

---

#### Lesson 6: Roots

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296289](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296289)

**Video:** 004 - Roots.mp4 | **Duration:** 7m 55s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Our next topic is the root system. Roots

allow users to grant a server access to some particular

set of files and folders. You can really think of roots

as being like a codified way of saying, hey,

MCP server, you can access these files.

But roots do more than just grant permission. Let

me walk you through a quick example to help you understand

how they work. In this example, I'm going to first

show you a common problem that we would run into if

Roots did not exist. Once we understand the issue,

we'll then see how Roots solve that problem. So

in this example, we're going to have a very simple MCP server

with one single tool called Convert Video. This

tool is going to take into a path to a video file

on the user's local machine, and it's going to convert

that video file into some other file type,

so maybe a MP4 to a MOV.

Now let's imagine how a user would actually make use of this. A

user might type into to some CLI application or

something like that, asking Claude to convert

a biking.mp4 video file into

MOV format. Claude would then take a look

at the list of tools that are provided by this MCP

server and see that the convert video tool is available.

So Claude would probably decide, fantastic. I'm

going to call that tool and I'm going to pass in a path

of Viking.mp4. Because

that's exactly what the user asked for. The user asked

for a conversion of a video file named

Viking.mp4. And here's what

I would probably expect to see in response from that tool. I

would probably expect to see an error come back, saying

something like, there's no such Viking.mp4

file available. So why would I expect

to see that error exactly? Well, remember, the

user's file system might be really complex. They

might have a wide variety of different files and folders,

tons of different documents all over the place. So

a user might know that the Viking.mp4 file

is inside this movies directory, but there's no real

way that Claude would understand that. So

if a user just asks for Viking.mp4, Claude

doesn't really have the ability to search over the user's file system

and figure out exactly where that particular document is.

Now, one way that we could solve this would be to just require

a user to always pass in a full path

to some video file. So we might say, you know what,

if you want to use this tool, you must pass in a fully qualified

path, like movies slash Viking.mp4.

And now probably this would work,

but it's not super convenient. Users

don't really want to sit there and have to type out full paths

to every file they ever tried to access. They really probably

just want to put in something like convert this video and then just

put in the name to it to some other format.

So now that we understand the issue, let me show you how we could solve

it by using the idea of roots. So

we're going to solve this problem by adding in some additional tools

to our MCP server. We're so going to have the

same convert video tool, but we're also going to add

in a tool of read directory. I bet you could guess what

that does. It's just going to list up all the files and folders in

some specific directory. And then the third

tool that we're going to have is going to be called List Roots.

This is going to return back a list of roots. Our

root is a file or a folder that the

user has granted permission to be read ahead of time.

So in other words, when they first start up this MCP server,

they might pass in as command line arguments, a list

of files and folders that the server is allowed to read.

On top of that, we're also going to put in a little requirement

in our other tools. We're going to add in some code to

 our read directory tool and the convert video tool.

And we're going to make sure that whenever they try to access some directory

or some video file, they only get to access

files and folders that are contained inside

of one of these different roots. To help you understand

how these three different tools come together, I put together a very

small sample application. So let me give you a

quick demo right away. To run this program,

I execute uvrunmay.py. And

then the program is set up to accept a list of additional

command line arguments. So if I want to, I could put in desktop,

like so. And that's going to be set up as a root

inside the MCP server. So I'm essentially saying

that I want the server to be able to access the desktop

folder and all the files inside of it. Then

on the right-hand side over here, you can see my desktop directory

inside there is a file called Viking.mp4.

So now I'm going to run this, and I'm going to ask Claude

to turn the Viking.mp4

file into a MOV file. Now

I'm going to run that, and we'll see a couple of tool calls printed

out. First, Claude is going to take a look at all the

different files and folders that it can access by calling the List

Roots tool. It's then going to see that there's only one

directory that it can access, the desktop folder, because

that's the only one that I granted access to in this program.

It's then going to try to read that directory, and it's

going to discover the Viking.mp4 file

inside there. And so at that point in time, it now has everything

it needs to actually successfully run the convert

video tool. So it can run that tool with a

path of the fully qualified path to my desktop

folder, Viking.mp4. Now

remember, roots are intended to limit what files and

folders the MCP server can access. So in

addition to that desktop folder, I also have a documents

folder inside of here. Inside of that directory

is a swimming.mp4 file. So

now I'm going to ask Claude to convert the swimming.mp4

file into a MOV as well. And this time

around, I'm going to provide the full path to the MP4

file. So now in theory, Claude doesn't need to

take a look at the list of roots. It can just directly call

the convert video tool because it's already got a fully

qualified path to the particular file it wants to convert.

So I can run this and we'll see what happens. So

it's going to merely try to call a convert video, but it's going to return

early because Claude is going to say, sorry, but I

got an error around running that tool. It was not able

to find the particular file. Claude is then going

to try to take a look at the roots that are available. Read

the only root that is available, in this case, the desktop.

And then Claude is going to realize, hey, it looks like I actually

can't access that file at all. The only directory

I can access is desktop. And if you want me to convert

the swimming file, well, I just can't access

it. So try to give me access or move the file

or whatever else. Now, based upon that

demonstration, you might notice that roots really have two

distinct purposes. On the one hand, they

allow users to grant access to particular files and

folders. But on the other hand, the other really

nice benefit to them is that they allow Claude

to focus on just particular areas of your file

system. So as we saw, we don't have to put in fully

qualified paths to some particular directory or

file that we might want Claude to access. Instead,

Claude can autonomously decide to take a look

at the available roots and then search through those roots to

find some particular file. The

one thing that I haven't quite mentioned here, but is very critical

for you to understand, the idea of roots is kind

of loose. And there's not a tremendous amount of implementation

around them. So in other words, there's nothing inside

of any Anthropic SDK that will actually

automatically limit access to particular files

and folders. Instead, it is up to you

in your Anthropic server to make sure that whenever

a tool tries to access a file or a folder, it

is listed or contained inside of one of these different

roots. And you might do that by implementing a

function like you see on the top right-hand side here, something like, is

path allowed. Inside that function, it takes

in some requested path, it's then going to get a list

of roots from the client, and then see if the path

that the tool wants to use is contained within

one of those routes. And if it is, fantastic, we'll

allow access. Otherwise, nope, we're not going to allow

access at all. Now, the last thing I want

to mention is that I showed implementing a tool

of something like list roots and allowing Claude

to call that tool at any point in time. That is

not strictly required. You can also just take the

list of roots and toss them all into a prompt

manually. So you don't have to make that tool. It's just a pattern

that I found was kind of helpful for allowing Claude

to look at the list of roots whenever it decides it needs to figure out

what files and folders it can access.

---

#### Lesson 7: Roots walkthrough

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/295839](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/295839)

← Previous Next →

---

#### Lesson 8: Survey

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/297276](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/297276)

Loading...

---

### Transports and communication

#### Lesson 9: JSON message types

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296290](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296290)

**Video:** 005 - JSON Message Types.mp4 | **Duration:** 6m 45s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

We have gone through a couple of topics, and before we

move on, I just want to give you a little heads up.

You see, the next two or three videos are going

to be focused on MCP messages and the standard

IO transport. These videos might seem a little

bit dry and a little bit boring, but there's

a very important reason that we're going to cover these topics.

One of the big goals of this course is to help you understand the

streamable HTTP transport, which

allows clients to connect to remotely hosted MCP

servers. The issue is that in some cases,

there are some big limitations on what a MCP

server can do when it is using the HTTP

transport. Understanding those limitations can

be rather challenging and is a lot easier

to understand if you have a solid footing in MCP

messages and a standard IO transport.

So that's why we're going to spend some time on these first two topics.

So with all this in mind, let's take a look at the format that

MCP uses to communicate, specifically the messages

format. Clients and servers communicate

using JSON. We refer to these snippets of JSON

as messages. There are many different types of messages

defined inside the MCP spec, each of which are

designed for a distinct purpose. So let me show you an example

right away. As an example, if a language

model connected to a MCP client decides

to call a tool provided by MCP server, the

client will send a message over to the server. This

type of message is named a call tool request.

And I've got an example of a call tool request at the top of this

diagram. The MCP server will then run the tool

and then put the result of the tool run into another

message type named a call tool result. And

I've got an example of that on the bottom of the diagram as well.

Now, as I mentioned, the MCP spec defines

a full list of all the different message types. You

can find the full list inside the MCP spec

repository hosted on GitHub, and we're going to take a look at that in

just a moment. But first, to be clear about this

repository that we're going to take a look at, this specification

repo is separate from all the different SDK

repositories, like the Python or the TypeScript

MCP SDKs. This specification

repo has some different documents that describe how

the MCP spec works. So in this repository,

the full list of message types is written inside

of a TypeScript file. Again, to be clear here,

this TypeScript file isn't ever executed by

anything. It's not included in any of the different SDKs.

The types are just written in TypeScript because TypeScript

is a really convenient language for describing type

data. So I'd like to show you this schema file

that lists out all the different message types, just because there

are some really interesting insights to be pulled out of it. So

I'm going to navigate to the address you see up here at the top of the screen.

And then inside this repository, you will find at a certain

path a file called schema.ts.

The schema.ts file contains all the different message

types that are available to us. So inside this file,

I can do a search for call tool request.

And here we go. Here's an example of what a call tool request

looks like. So a call tool request must have

a method of tool/call, and then

a parameter object that has the name of the tool we want to call in some

arguments to pass into it. You might notice that in the diagram

I showed you a moment ago, back over here, there's also this

JSON RPC and an ID on there as well. Those

are actually defined on a separate object back inside the schema

file called a JSON RPC request.

So if I look that up, I'll see, okay, here is JSON RPC

request and it also have must have an ID as well.

Now out of this entire file, what I really want you to focus

on are some different types that are defined at the very bottom. So

I'm going to scroll down to the very bottom, very, very bottom of the file.

I'll then scroll up just a little bit, and I'm going to find a comment

that says server messages, and a comment that

says client messages. You'll notice that inside

these two sections, there are some kind of similarly named

types. So inside of client messages, there are client

request, client notification, and client

result. And then down inside the server section, there

is server request, server notification, and server result.

So let me show you a diagram. It can help you understand what these different

types inside this file and specifically the client

and server sections are really telling us. Okay,

here we go. So inside that type file, we can

kind of divide all these different types of messages

into two or three different categories.

First, on the left-hand side of this diagram, there are request-result

messages. These are message types that always

come in pairs. They're always going to have a name of

something-something-request, and then a paired

message type of something-something-result. So

as an example, we have call-tool-request that gets paired

up with a call-tool-result. We have an initialized

request that gets paired up with an initialized result.

All these different message types, I bet you could guess what they do

for us. They describe messages that we send off

either to a client or a server, and then the type

of message that we expect to get back in response. So

if I ever send off a call to request, I would expect

to get back a call tool result. The

other type of messages that we're going to work with are notification

messages. These are more like events. They

tell the client or the server about something that just occurred,

but they don't really need a response. So we have

types like progress notification, logging

message notification, tool change notification,

and so on. Now, back inside of the type file that we're looking

at a moment ago, you may have noticed that we have the headers here

of server messages and client messages. These

comments and the types inside of each one are meant to indicate

whether or not these types of messages are meant to be sent by the

client or the server. So for example, this

client request type describes all of the

different types of requests that are expected to be sent

from the client. And likewise down here, these

are all requests that are expected to be sent from the server. And

the same thing for server notifications, these are all notifications

issued by the server. And these are all notifications

that are issued by the client. So we can kind of summarize

everything in a diagram a little bit like this.

Now this doesn't show every type of message. I just mean to indicate

that there are some requests that are meant to come from

the MCP client, and I've got examples of those right here. There

are results that are meant to come from the server. There

are results that are meant to be sent from the client. There

are requests that are meant to be sent from the server, and so on.

All right, so here's the critical thing that I want you to understand.

The big takeaway from this video that's going to become really

important as we start to talk about the streamable

HTTP transport. The big critical thing to understand

here is that there are a bunch of different messages that

are meant to be sent from the server over to

the client. So the server request

types right here and the server notification types. These

are all messages that are going to be sent from the server over

to the client. And I know right now that might

seem like just completely irrelevant, just why is

that important to know at all? Again, this is going to become

really important as we start to look at the streamable

HTTP transport. So just keep that in mind for

a little bit.

---

#### Lesson 10: The STDIO transport

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296291](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296291)

**Video:** 006 - The Stdio Transport.mp4 | **Duration:** 9m 28s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

As we discussed a moment ago, clients and servers communicate

by exchanging JSON objects that we refer to as

messages. Now, JSON in general

can be transmitted between a client and server in a wide

variety of different ways. For example, we can make a HTTP

request. We could use web sockets. We

could even write out a postcard with some JSON

and then send it to someone else and have them manually type that

JSON into a server. So there really are a tremendous

number of ways to send and receive JSON. In

the MCP spec, the thing that we used to actually move

JSON between a client and a server is referred to

as the transport. When you are initially

developing an MCP server or a client, a very commonly

used transport is the standard IO transport. The

idea with this transport is that our client is going to launch

a server as a separate process. By doing

so, the client has a handle on that process.

and the client can send messages into the server

by writing them into the server standard in channel. And

it can receive messages by watching the server standard

out channel. Something that is really nice

about the standard IO transport is that communication between the client

or the server can be very easily initiated on

either side. So in other words, at any point in time,

the client can communicate or send a message off to the server

by writing to standard in. And the server can communicate

back to the client by writing to standard out.

But the standard IO transport also has one big downside, and

that is that we can only make use of this transport when the

client and the server are running on the same physical machine. To

help you better understand the standard IO transport, let me give

you a quick demonstration. I put together a very

small MCP server. I've got some print statements

up here at the top just to help you understand what's going on. But

besides those print statements, the server doesn't really have a whole lot

to it. I'm creating a server, I'm defining one

single tool, and then starting the server up with the standard IO

transport. Now I could create a client

to connect to the server using the standard IOTransport,

but I can also just connect to the server directly

from my terminal without creating any distinct

separate client. Let me show you what I mean by that. If

I run UVRunServer.py right here, it's going to start up that

server. And now that server is going

to be listening to standard in and then writing

any outgoing messages to standard out. Well,

in my terminal, in case you don't know, whenever I run a program,

if I type anything down here, I am writing to standard

in of this running program. So I can actually

paste in JSON messages down here at the bottom, execute

them, and they will be received as input to the server.

So let me give you a quick demonstration of that. I'm going to restart

the server really quickly. And

then I'm going to copy this first example message up here. I'm

going to paste it right here. And it's going to occur almost

instantly when I hit enter. I'm going to immediately get

a response back. So I've written to standard

in right here with a message. And I am seeing a output

message on standard out right there. I'm

then going to send another message. Here

we go. And this time around, I'm not going

to see any response. And then finally, I'm going to run

one more message. down

here. And when I run this one, I'll immediately get

back one response, and then another response and another response

after that. So three objects in total. There's one,

there's two, and there's three. So

let me show you a couple of diagrams to help you understand what I'm really doing as

I paste these different messages in. Okay,

so back over here. On the left-hand side, I've got what

I have labeled my MCP clients, but really it's just me

at my terminal pasting messages in. By pasting

those messages in, I'm writing to standard in of the MCP

server. The server is then going to process these given messages

and then possibly send a result back by just

printing it to standard out, which I see directly

printed at my terminal. The first message that

I sent in was something called an initialize request.

Let me just give you a little bit of backstory here. Whenever a client

first connects to the server, the MCP spec says

that we must send a sequence of three different

messages back and forth. The very first message must

always be an initialize request. And again,

that is what I initially pasted in right here. That

was initialize request. Because

I sent in a request type message, I would

expect to get back a result. And that's exactly what happened.

I got back something referred to as a initialized result. So

that was that text right there. Then

the NCP spec also says that after

exchanging these initial messages, we must

then also send a initialized notification

from the client to the server. As a reminder, notifications

do not require a response. So I did

send in that initialized notification right there.

And as we noticed, we didn't get any immediate response

back. Again, that's just because notifications do not

require a response. Once we have exchanged

these three messages, our connection to the MCP server

is considered to be initialized. And at that point

on, we can then run call tool requests

or run prompt listing requests,

whatever else we want to do. So in my

case, as you saw, I sent in a call

tool request. That was the last one down here.

I attempted to call the add tool with arguments of

five and three. Now the way that I put

together the add tool, it is set up to send back a couple

of different logs and then eventually a called tool result.

So if I looked through the logs, I actually changed

it from what you see in that diagram. First, I got a message

notification. So a login statement that's coming

from right there. There's my login statement.

I then got a progress statement. So there's the progress

update right there. Those are both notifications being

sent from the server to the client. And then finally,

I got my call tool response right there, and

inside of it is the calculated result of adding

3 plus 5, I see 8. So

now that we've seen an example of the standard IO transport, there

are some really critical ideas that I want to point out

around this transport in particular that are going

to be very relevant or very important to understand as

we start to take a look at the streamable HTTP

transport. First, I showed you the diagram a little

bit ago. And I showed you this diagram to help you understand that there

are some message types that are intended to be sent from the client

to the server and some types that are meant to be sent from the server

to the client. The other thing that I really wanted you

to understand from this diagram is that there are some instances,

specifically with these messages on the top left-hand side, where

we can kind of imagine that the client is initiating

communication with the server. So in other words, the

client is saying, I am making a request and I expect

to get back a response. Likewise, there

are some situations where the MCP server is

sending the initial request off and expects to get

back a response. So that would be like the create

message request, which is what is used to initiate

sampling. So the server needs to send

off this request to the client and expects to get

back some kind of result. Now to put that in

slightly more clear terms, here's what

I really mean to indicate with that. There are

really four different scenarios with these different transports,

like the standard IO transport, that we need to be able to

handle. We need to be able to handle the initiation

or kind of a initial request from the client to the

server, and the transport needs to be able to handle

sending a response from the server to the client. Also,

the server needs to be able to send an initial request to

the client, and then likewise, the client needs to be

able to respond. So I want to walk

through all these four different scenarios and think about how

we would implement them with the standard IO transport. So

first is an initial request from the client to the server.

So the scenario here would be any time the client wants

to send something off to the server, like maybe a call

to a request or something like that. To implement

this with a standard IO transport, all we have to do

is write to standard in. And the MCP

server will receive that message, process it, and then hopefully

formulate a response. Once it has

a response, it would respond by just writing

a message to standard out. Now

the third scenario would be where we have an initial

request to be sent from the client to the server. So this

would be where maybe the server wants to do some sampling,

and that's going to require the server to send some kind

of initial message off to the client. Whenever

the server needs to send an initial request to

the client, all it has to do is write to standard out.

And then likewise, to respond, all the

client has to do is write to standard in. All

right, now I know that the last couple of minutes in

this video and the sequence of diagrams I just went over are

probably a little bit confusing. And you're probably thinking, what

is this about initial requests and responses and whatnot? Well,

here's the point. The whole point of all this is to help you understand

that the standard IO transport is really fantastic

because at any point in time, the client

or the server can initiate communication.

either one can send a request at any point in time and

expect to get back a response. Here's

the key thing. That is not going to be the case with

a streamable HTTP transport. There

are some scenarios where the streamable HTTP transport

does not allow for this situation.

There are some cases where the server cannot send some

initial request off to the client. And

that's the tricky thing to understand about the streamable

HTTP transport. So now we're going to

take a pause right here. Come back. We're going to start to take a look

at the HTTP transport. And we're going to see

this particular scenario and understand that, yeah,

there's something a little bit tricky about this that you definitely need

to understand when you are developing your own MCP

servers.

---

#### Lesson 11: The StreamableHTTP transport

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296287](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296287)

**Video:** 007 - The StreamableHTTP Transport.mp4 | **Duration:** 6m 26s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Time to discuss the Streamable HTTP

transport. This transport allows us to send messages

between a client and a server over an HTTP connection.

The nice thing about this transport is that it really enables remotely

hosted MCP servers. So whereas with the

standard IO transport, we always had to run the client

and the server on the same machine. With the Streamable HTTP

transport, we can remotely host our server. So

our remote server might be hosted at MCPServer.com

or something like that. This really opens the door to a much

wider range of possibilities around MCP servers,

because you can make a public server that anyone can

connect to. However, as I've hinted

at over the last couple of videos, there are some settings

that you might need to apply to this transport that

will limit the functionality of your MCP server,

specifically limit the types of messages that

you can send from the server back over to the client.

So that is the big issue that I want

you to be aware of. There are some settings that are going to restrict

the functionality of the server when you are using this

particular transport. So if you are ever developing

an application on your local machine and everything

is working just fine with the standard IO transport and

then you deploy and you start to use the HTTP transport

and things aren't working quite so well, this is the video you want

to come back to to understand what is going on.

To get started, I would like to give you a quick demonstration of

an app that I showed you previously inside of this course. You

might recall this Wikipedia research assistant. It

makes use of a next JS application that is connected

to an MCP server that implements a research

tool. This server is using the Streamable

HTTP transport, so I will be able to use

this application to show you a couple scenarios where the

Streamable HTTP transport doesn't quite

work as expected. First, I'm going to

send off a request here, just going to ask for

a report on archaeology, just to remind you what this application

looks like. So usually, when I send in a query

like this, I'm going to see a call tool request

here, and I get a nice progress bar, I get status

updates, and eventually, if I wait just

a little bit, I will get a full

response. Now over here inside the source code for

the MCP server, you'll notice that there are two settings that

I have commented out. Stateless HTTP and

JSON response. By default, these settings

are set to false, but there are going to be some scenarios

where you very much have to enable them or set them to true,

and it will go into more details on what those scenarios are a little bit

later on. Changing these settings to true is going

to impact the functionality of your MCP server,

and in some cases, it might even break how your client

works. So let me show you an example of this right away. I

want to change stateless HTTP to be true.

I'm going to save the file. Then I'm going to reload

the page and run the exact same query again.

And now you're not going to see a big difference

here, but there is something you'll notice right away. You'll

notice that now I don't get a progress bar anymore.

So no progress bar whatsoever above the log

statements. In addition, if I let this just sit here for a

while, and I'm going to speed the video up, We

will see that eventually the request fails entirely without

generating any text. Now I'm going to refresh

the page, I'm going to turn on JSON response

to be true, save the file, and then run

the exact same query again. Now we'll see that with

both these settings set to true, we get some even more surprising

results. Now I don't see any progress bar, I don't get

any log statements, and take my word for it if we let this

just sit here, the request is going to fail again.

So right away, we can see at these two settings, although seemingly

innocuous, have a big impact on our MCP

server. So the rest of this video is all about helping you understand

what these settings are talking about, why we might set them

to true, and exactly what's going on here.

First, I want to give you a very quick reminder of a diagram I

showed you in the last video. And I made a big deal about how

the standard IO transport had the ability to

initiate a request from the client to the server and then get a

response back. And likewise, the server

at any point in time could initiate a request

off to the client and get a response back.

So keep in mind for just a moment, as I give you a quick

review on HTTP communication.

So this is going back to some of the basics around HTTP,

and this is all HTTP communication, not

just MCP related stuff. So

as a reminder, if we have a client and a server, at

any point in time, a client can very easily make a request

off to the server. For example, on the right-hand side, the

client can make a post-request off to the server and

expect to get back some kind of response. No

issue with this setup whatsoever. So

translating this over to the MCP world, that means that if we

want to make an initial request from the client to the server, no

problem is going to work. And if we want to get a response

from the server backward the client, no problem whatsoever is

going to work just fine. However, if we consider

the reverse scenario, if the server wants

to initiate a request down to the client, that's

not quite so easy with HTTP requests.

At a very basic level, the server doesn't know the

address of the client, and the client might not even be publicly

accessible. So it's very challenging in traditional

HTTP for the server to initiate a

request down to the client. And that means that in

our MCP world, it's really hard for the server

to send that initial request down, and it also means

that it's kind of hard to imagine how you'd ever expect

to get a response from the client back to the server.

So if we consider this diagram that we looked at a moment ago,

where I had told you that there are some requests that

are being issued from the server down to the client, that

means that in this HTTP world, there

are some message types that are just plain

tough to implement with normal HTTP

requests. Specifically, sampling request,

listing routes, progress notifications, and logging notifications,

along with some other message types that I'm just not showing on this diagram,

are tougher to implement in an HTTP world.

And sure enough, that's kind of what you saw back over here

with this demo. As soon as I started to flip some of these

properties from false to true, well, you saw some

different parts of the application start to break and just not work

as expected. And what exactly broke?

Well, that's right. The progress notification broke, the

logging broke, and sampling, or essentially the

create message request broke as well. Sampling was being

used to author the fund research report.

Now I do have some good news. Even though making requests

from a server down to a client is challenging

in a pure HTTP world, the Streamable

HTTP transport does have a clever solution.

But there are some caveats that you need to be aware of. Let's

take a look at how the transport actually works and exactly what

those caveats are in just a moment.

---

#### Lesson 12: StreamableHTTP in depth

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296286](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296286)

**Video:** 008 - StreamableHTTP in Depth.mp4 | **Duration:** 10m 28s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's do a quick recap on the last couple of videos just to make

sure that we are on the same page. The first thing that we understood

was that some MCP functionality, namely

things like sampling and notifications and logging,

relies upon the server making a request to

the client. Shortly after that, we learned that when

we are making use of HTTP in general, it's

kind of hard to allow a server to make a request to

a client. So these first two points are kind

of butting heads. They are at odds. We

need a server to build and make a request to a client to get full

functionality, but at the same time, that is hard to

do when using HTTP. Now, as I

mentioned, Streamable HTTP has a workaround

to fix this. And I'm going to show you exactly what that workaround

is and how the transport works in general in

this video. So we're going to finally get going to get clarity on

exactly what's going on. Lastly, keep in mind

that in some scenarios, we are going to set those two flags

to true, and we'll discuss why we've ever set them to true.

And when you do so, that breaks the workaround. And

that's kind of why streamable HTTP as a transport

is a little bit tough to wrap your head around, because we've got

this limitation around HTTP. We got the workaround,

but in some cases, we want to not use that workaround

for say, that's why it's a tricky subject.

Well, without further ado, let's get to it. Let's understand

how this transport actually works. I'm going

to begin by showing you a couple of different diagrams to help

you understand the behind the scenes process. And I'm going

to show you a short demonstration where you're going to see all

these requests actually made and the entire system come

together in a very small demo application. So

here we go. First thing I want you to recall is what happens

when a client initially connects to a server. According

to the MCP spec, the client must send an initialized

request to the server, server replies with a result,

and then the client has to make a follow-up request with the initialized

notification. At that point in time, the

server then considers the client to be connected and everything

is good to go. Now, as soon as we start to use the HTTP

transport, this flow changes ever

so slightly. So as soon as you start using this transport,

the initialized result that gets sent back from the server

is going to have a header inside the HTTP response.

This header is the MCP session ID. This

is a random string of numbers and letters that gets assigned to

our client as essentially an identifier for our

connection to the server. As soon as we receive that

header, we are required to include it in all follow-up

requests we make to the server. This allows the server

to identify our client. Now

after we have done this initialization and gotten that session

ID, here's where the magic part begins. So this

is kind of the big workaround that allows the server to make

requests to the client. As soon as we finish that

initialization, the client, optionally, it

doesn't have to do this, optionally, it can make

a GET request to the MCP server and

include that session ID inside the request.

The response we get back is very special. It is an SSE

response. SSE is short for Server-Sent

Events. This is a kind of response that can be held

open for an arbitrary amount of time. Once

this response has been established with our client,

the server can then stream back little bits of information,

essentially individual messages, down to our client.

So once this connection has been made, now at this

point in time, this is the real critical part. This

now allows the server to send down messages to

the client at any point in time. And this connection

can be used, essentially, to allow the server

to make a request to the client. So this

is the trick. This is the workaround that the HTTP

transport uses. It makes use of this long-lived

SSE response, and it's going to stream down messages that

it wants to send to the client. So now,

let's go a little bit further and walk through what happens now

whenever the client might want to call a tool, because

the complexity is not quite done just yet. There's one

other critical part for you to understand. So

now at the top of this diagram, I've got that SSE response

that we just created. And remember, that response,

that open connection, it has a session ID tied to

it. So the MCP server knows exactly what

that connector, which client that connection belongs to. So

then later on at some future point in time, while

that response is still running, our client might

decide to make a call tool request to the server.

When it makes this request, it's going to include its session ID

as a header. Then the MCP server

is going to open up a second SSE

response. So now at this point in time, we have

two separate SSE responses. The

first one at the top, it is intended to

be used for requests that are going from the server down to the client.

The second brand new SSE response is

intended to be used for messages that are related to

this call tool request. And importantly,

this is the critical part, this second SSE response,

it is closed automatically as soon as the call

tool result message is sent. So the

bottom response, closed automatically, very shortly

as soon as we get a result, and the upper response

is meant to be held open for an arbitrary amount

of time. Then, remember, our ultimate

goal here was to actually call a tool. So

maybe we call the add tool that we've seen many times.

And the implementation of that that I've shown you a couple times, it has

some logging messages inside of it and some progress notifications.

And eventually, it returns a result, which would be our call

tool result. Now here's another kind

of little tricky part here. Technically, both

the logging message and the progress notification

are really tied to the call tool request. So

you would kind of think that both these first messages

would be sent back in the bottom response because they're both really

tied to this call tool request. Well, that's

not quite how many of the SDKs work right now. The

progress notification ends up being considered to be separate

from the incoming call tool request. So the progress

notification actually gets sent in the first SSE

response. So that's the one that is meant to be held open for a long

time to allow the server to make a request down to the client.

And then the logging message and the actual call tool result

is sent back in the response to the POST request or the

GET tool request that was made. So that is

the entire flow. Now to make sure that all this is crystal

clear, I want to walk you through a very quick demonstration where

you can see all these different requests being made in a very visual

way. So I put together a little demonstration. First,

I've got a simple MCP server put together once

again with a simple add tool. The add tool is going to

log some information, wait for two seconds, make

a progress report, and then return a result. I've

connected to this MCP server with this

client that is running inside the browser. This client

will allow us to make a handful of different requests to the server and then show

the exact response that we get. Now, in total, this

client is going to go through the flow that you see on the screen.

So I know there's a lot here, but in essence, we're going to first

go through the entire initialization process with the stuff up here

at the top. We're then going to form the GET SSE

connection, which allows the server to send requests to

the client. And then we'll do a call tool request

that's going to form a second SSE connection that's

going to be responsible for handling messages related

to this particular call tool request. So let's

run this and see what happens. First, I'm

going to make the initialized request. So I'll send that off. That's

going to get me my session ID, which uniquely identifies

my client to the server on any future request. Remember,

the session ID is only provided when you are using the streamable

HTTP transport. It is not used with the standard

IO transport at all. You'll notice it begins with EAA.

This header is automatically taken and

applied to all future requests. So if I scroll down to

the next request, you'll notice the MCP session ID has

automatically been applied with the correct session ID

that I got from the request right above. So now that

we have sent the initialized request, that one

right there, our second request is initialized notification.

So I'm going to send that off. Okay, so now at

this point in time, we've taken care of the first three

boxes on here. So now we're going to make our GET request

to the server. This GET request is going to be

held open for a long time. This is what allows the

server to send a request down to our client at

any point in time that it wishes. It's going to be used for things

like sampling or any kind of server initiated

request. To make that request,

I'm going to use this little box down here on the bottom

right hand side. So I'm going to click on Start GET

SSE. This request is also going to include

that session ID as well. And now I have formed

that connection. So now in theory, at any point in time,

the server can send down a message to my client for

things like sampling or logging or progress notifications

and so on. And if I receive any of those, they

should appear inside of this box.

So now here's the last step. I'm going to call the

Add function. I've once

again got the correct session ID inside there. Now, to

remind you, when I click on this, in theory, we

would kind of want to see the log statement, progress

statement, and the final call to a result, all

to appear in this box right here, which represents

that part of the response. But in reality,

just because the way that the MCP SDK for

Python is set up, the progress notification is actually

going to be sent as a part of this response up here.

So we should see a log statement and

a call tool result right here. And we should see

the progress statement down here on the bottom right in that box.

So let's run it and see what happens. Okay,

so I'm going to run it. And then after a little delay,

because remember there's the two second pause inside there, we're

then going to get our result. So sure enough, down

here on the bottom right hand side, I've got a notification/progress.

So that is the progress statement. I'm at

80 out of 100% completion. So

that was sent in that response channel

right there. And then the actual response

to my call tool request has a logging

statement in the form of notification/message. And

then after that, I've got the actual result of the call tool

request. So this is my call tool result and

the answer to adding those two numbers together is eight.

And then remember, as soon as we get back that call tool

result, this connection is automatically closed. So

I see right there, yes, the connection was closed and

I can no longer receive any messages along this

SSE response we got. All

right, so that's it. That's the entire flow. So

now you understand what's going on behind the scenes with the streamable

HTTP transport. But we're not quite

done just yet. Remember, I said many times

that there are scenarios where you're going to want to set these flags

to be true and it's going to break portions of

this flow. So that's the last thing we need to understand.

Why would we ever set those to true? Because it is something that you

probably are going to want to do at some point and exactly what

does it break? So that's the last thing we really need to figure

out.

---

#### Lesson 13: State and the StreamableHTTP transport

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296285](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296285)

**Video:** 009 - Stateless HTTP.mp4 | **Duration:** 6m 29s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The last thing we need to do is understand what the stateless and

JSON response flags are all about. How do they affect our server

and when will we ever set them to true? I first

want to walk you through a scenario where we might want to set these things to

true because it really frames why these flags exist

and how they affect our server. Let's imagine that you

and I build an MCP server and we deploy it somewhere publicly

online, where anyone can connect to it. So maybe

we connect to it with our own client, and then some other

people connect to it with their own clients as well. Over

time, our server might become really, really popular, and

in addition to the three initial clients we had connected,

maybe many, many other people connect to it as well. At

a certain point, running a single instance of our server on a single

machine would probably not scale to the amount of traffic

that is incoming. So one way we might solve this is

through a little bit of horizontal scaling. With

horizontal scaling, we might run multiple copies of our server

and then gate access to them with a load balancer.

So any incoming request would be randomly routed to

one of these different servers. This would allow us to scale up to meet

higher demands of traffic. And let's think about

what would happen if we put a load balancer here, particularly

keeping in mind the fact that we want to have really

two separate connections to our MCP server from any given

client. First, we want to have that running get request

running at all times so we can receive requests from the

server to the client. And our client also needs to make

post requests and then receive a SSE response

with some number of messages inside of it as well.

So let's consider just one client connecting to maybe

two different servers. This client would then make an

initial request, setting up that initial Git

SSC response pipeline. So we then imagine

that we've got this response pending or kind of running continuously

down to the client. Again, remember this is all about allowing

a server to resend a request down to the client.

Then maybe at some future point time, the client decides to

run a tool. So it might make a call tool

request using a post request. And maybe

this request gets routed to the second MCP

server. The second server would then respond by setting

up its own separate SSC response. Now

at this point time, I'm not going to show the load balancer just for clarity.

As the tool runs inside that server, let's

imagine for a second that it needs to make use of Claude, and

it might try to make use of Claude by creating a create

message request. Remember that represents a attempt

to use sampling. Now, sampling requests always

need to go through the Git SSE response.

But that connection has been formed by a completely separate

server. So we would need to figure out some way to get

this request right here over to this other

server and have this server send the request down through

this Git SSC response, have the MCP

client run Claude, generate some text,

send it back to this server, and then somehow get

that generated text back over to this server.

As you can tell right away, coordinating all this would be

really, really challenging. Now, it absolutely could

be done, but it represents a lot of difficulty

and a lot of added configuration and infrastructure. So

if we are building an MCP server that we expect to

scale horizontally and we do not want to go through all

this extra coordination and infrastructure setup, we

might decide to set that stateless HTTP

flag to true. Setting this flag to true

has one immediate but very important effect.

It means that clients do not get a session ID,

and that means that a server can never keep track of a client.

Right away, that has some really big follow-up effects.

Without a session ID, the MCP server can no longer make

use of the Git SSC response pathway to

send requests down to the client. To understand why

that response pathway can't be used anymore, I'd encourage

you to think of a bank where you don't have any account

IDs. So a bank might receive money, but

it wouldn't really know who gave them the money, and it wouldn't really

know who to give money to because it doesn't know who is owed

what. That's the same situation here without any identifying

token. Now without that Git SSC

response pathway, that means that because our server can't

send any request on the client, we also can't use features

like sampling or progress logging or subscriptions

around things like changing resources and so on. There

is another upside to this, however. In stateless mode,

you do not need to go through client initialization anymore.

So that means that back over here inside of this

application, remember whenever we connect to the server, we

had to make that initialized request and then

the follow up initialized notification. When you're in stateless

mode, you do not have to make those two requests, which

definitely cuts down on the amount of traffic that your server is

receiving. So there is a pretty good trade-off

here. Now the other flag that we've been

discussing has been JSON response. Whenever

you set JSON response to true, that just means that the post

requests that you send down to the clients are not

going to have streaming enabled. And I can

give you a very simple and easy demonstration of what that

looks like. So over here, very quickly,

let me give you a reminder of how this application usually works. I'll

send the initialized request, initialize notification,

and then when I call the add tool

function, I'm going to open up that SSC connection,

and I'll first get back a message, and then the call

tool result. Now I'm going to very quickly flip

the JSON response flag to true. And again, that

means that all the responses that I get back are going to be just

the final result as plain JSON. There's

no streaming at all. So now I'm going to go through the same

process again. I'm going to run the initialize,

I'm going to run the notification and

now this time when I call the add function, I'm

not going to get those intermediate messages about

some logging or anything like that. Instead,

I'm going to get the final tool call result and

nothing else. So now if I run this, we'll

see that I'm not streaming response back. Instead, I'm waiting

until the tool call is complete and I get just

the result and absolutely nothing else. No log statements

at all. So you can see right away how these two

flags have a tremendous impact on how your server

behaves. But depending upon how you are

trying to develop and deploy your application, setting

these flags to true might be entirely appropriate. All

right, through a lot of patience and many different diagrams,

I think we've finally got a reasonable idea of how the streamable

HTTP transport works. So keep in

mind these two flags and exactly how they affect

your server. If you are developing your server in

development on your local machine using a standard

IO as your transport, when you deploy to production,

if you are intending to use the streamable HTTP

transport, just keep in mind that your server might behave

a little bit differently. So as you are developing your server,

I would encourage you to use the transport that you plan to

use in production, because it's going to save you a lot of trouble

down the line.

---

### Assessment and next steps

#### Lesson 14: Assessment on MCP concepts

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296301](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296301)

---

#### Lesson 15: Wrapping up

*Source:* [https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296350](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296350)

**Video:** 010 - Wrap Up and Next Steps.mp4 | **Duration:** 0m 48s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Well, it is time to wrap things up, but before I let you go, I

want to give you some ideas on next steps from here. First

off, I highly recommend you engage in the MCP

community. There is a discussion board hosted on

GitHub that has a tremendous amount of discussion around

upcoming changes or ideas in MCP.

Take a look at some of the different ideas that other people are coming up with on

use cases for MCP. Second, I highly

recommend you watch the MCP homepage for upcoming

news and changes to the spec. Finally,

nothing replaces building your own MCP server.

So I highly recommend you take some of the code that I've given you throughout

this course and use it to practice some of the different topics

or implement the different topics that you have learned about. All

right, that is it for now. I hope you've enjoyed this course because

it definitely has been a pleasure to put together.

---

*Extracted from Anthropic Academy via authenticated session | Deep Extraction v3 | 2026-04-12*
