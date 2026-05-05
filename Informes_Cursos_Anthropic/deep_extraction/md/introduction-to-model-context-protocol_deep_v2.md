# Introduction to Model Context Protocol

> **Source:** [https://anthropic.skilljar.com/introduction-to-model-context-protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol)
> **Category:** mcp | **Difficulty:** intermediate | **Domain:** Model Context Protocol
> **Tags:** mcp, protocol, tools, resources, prompts, python-sdk
> **Extracted:** 2026-04-11 | **Version:** v3 (with YouTube transcripts + quiz content)

---

## Extraction Statistics

| Metric | Value |
|--------|------:|
| Total Lessons | 14 |
| Sections | 4 |
| JW Player Transcripts | 12 |
| YouTube Transcripts | 0 |
| Modular Text Lessons | 1 |
| Quiz Assessments | 1 |
| JW Transcript Chars | 65,138 |
| YouTube Transcript Chars | 0 |
| Modular Text Chars | 10 |
| **Total Content** | **65,148** |

## Curriculum Structure

- **Introduction** (3 lessons)
- **Hands-on with MCP servers** (4 lessons)
- **Connecting with MCP clients** (5 lessons)
- **Assessment and wrap Up** (2 lessons)

---

## Complete Lesson Content

### Introduction

#### Lesson 1: Welcome to the course

*Source:* [https://anthropic.skilljar.com/introduction-to-model-context-protocol/303756](https://anthropic.skilljar.com/introduction-to-model-context-protocol/303756)

**Video:** 001 - Welcome to the Course.mp4 | **Duration:** 1m 4s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Welcome to this course focused on getting started with

model context protocol. My name is Stephen Grider

and I'll be guiding you through everything you need to know around MCP.

Let's first begin by understanding exactly what we'll cover in

the coming videos. We'll first get an overview

on MCP and understand what problems it is intended

to solve. We'll then start to look at the basics

of MCP architecture by covering the responsibilities

of MCP clients and servers. Then

it is on to the three basic components of an MCP

server. First, we'll look at tools, which are intended

to be consumed by language models. After

that, we'll study resources, which allow a server to

share data with clients. And finally, prompts,

which will provide tune directions to language

models. Now there's a lot of content for

us to get through, so there are a couple of requirements on

your side. First, you need to have some basic Python

knowledge. Second, we will be writing out some code,

and this will require a local Python installation. We

will be managing our project with the UV CLI.

And if you don't have it installed, I recommend grabbing it now. I'll

get a link to it on the screen.

---

#### Lesson 2: Introducing MCP

*Source:* [https://anthropic.skilljar.com/introduction-to-model-context-protocol/296689](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296689)

**Video:** 09 - 001 - Introducing MCP.mp4 | **Duration:** 4m 40s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this module, we are going to focus on model context

protocol. MCP is a communication layer

designed to provide Claude with context and tools

without requiring you, the developer, to write a

bunch of tedious code. When you first get started

with MCP, you will see diagrams that look like this very

often. It shows two major elements of

MCP, namely the client and the server. The

server often contains a number of internal components,

named tools, resources, and prompts. And

there's a lot of terminology here. So to help you understand

all of this, we're going to imagine that we are building

a small app and see how MCP fits

into it. Our sample app is going to be another

chat interface. It's going to allow a user

to chat with Claude about their GitHub data.

So if a user asks a question like what open

pull request do I have across all my different repositories,

the expectation is that Claude is probably going

to make use of a tool to reach out to GitHub,

access the user's account, and see what open pull

requests they have, maybe open repositories

or whatever else. The point here is that we would implement

this probably by using a set of tools. Now,

one thing I want to mention really quickly is that GitHub has

a tremendous amount of functionality. There

are repositories, pull requests, issues,

projects, and tons of other things. So

to have a complete GitHub chatbot, we would

really have to author a tremendous number of

tools. If we wanted to build that sample app, we

would be on a hook for authoring all these schemas and

all these functions. And this is all code that you and

I, as developers, would have to write, test,

and maintain. That's a lot of effort, a lot

of burden being placed on us. This

challenge of making developers maintain a big

set of integrations is one of the primary difficulties

that model context aims to solve. MCP

shifts the burden of defining and running tools

from your server to something else called an MCP

server. So no longer would you and I have to author

this tool right here. Instead, it would be authored and

executed somewhere else inside of this MCP

server. These MCP servers can really be thought of

as like an interface to some outside service. So

I might have a GitHub MCP server that provides

access to data and functionality provided by specifically

GitHub, where essentially wrapping up a ton of functionality

around GitHub and placing it into this MCP server

in the form of a set of tools. So at this point,

we have a very basic understanding of what a MCP

server is. It gives us access to a set of tools

that exposes functionality related to some outside

service. And the benefit here is that you and

I do not have to author all these different tool schemas

and functions and so on. Now that we

have this basic understanding, I want to address some

very common questions that a lot of people have

when they first learn about MCP servers. So,

three common questions that seem to always come up. The first

common question is, who authors these MCP servers?

The answer is anyone. Anyone can make an MCP

server implementation. But very often, you'll

find that service providers make their own official

implementation. So for example, AWS might

decide to release their own official MCP server

implementation, and inside of it, it might have a wide

variety of different tools available for you to

use. The second common question is, how

is using a MCP server different than just

calling a services API directly? Well,

as we just saw, if we wanted to call a API

directly, such as GitHub, then we would

have to author this tool ourselves.

And now we can call

GitHub directly. So what did we gain here? Well,

all that really changed was we are now having to author the

schema ourselves and the function implementation ourselves.

So simply by adding in the MCP server, we

are saving ourselves a little bit time. The final column

question is more of a common criticism

that you're going to see people have around MCP. And

this criticism is most often coming from people who don't

quite understand what MCP is all about. So

very often, you will see people saying MCP and

tool use are the same thing. Well, as I have just

laid out to you, MCP servers and tool use,

they are complimentary. They are different things, but

they are complimentary. The idea behind MCP

is that you do not have to author the tool function

and the tool schema. That is something is done for you

by someone else and is being wrapped up inside of this MCP

server. So at some level, yeah,

they're kind of similar because we are talking about tool use

in both cases, but MCP servers are really

talking about who is doing the actual work. So

if you ever see this criticism, again, it's usually because

people don't quite understand what MCP is all about.

---

#### Lesson 3: MCP clients

*Source:* [https://anthropic.skilljar.com/introduction-to-model-context-protocol/296690](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296690)

**Video:** 09 - 002 - MCP Clients.mp4 | **Duration:** 4m 56s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next portion of model context protocol that we're going to investigate

is the client. The purpose of the client is

to provide a means of communication between your server

and an MCP server. This client is going to

be your access point to all the tools implemented by that server.

Now MCP is transport agnostic. This

is a fancy term that just says that the client and the

server can communicate over a variety of different

protocols. A very common way to run an MCP

server right now is on the same physical machine as

the MCP client. And if these two things are running

on the same machine, then they can communicate over standard

input output. And that's what we are going to be setting up

later on inside this section. There are,

however, other ways we can connect the MCP client

with the MCP server. So they can also connect

over HTTP or Web Sockets or

any of a number of other varieties or techniques.

Once a connection has been formed between the client and the

server, they communicate by exchanging messages.

The exact messages that are allowed are all defined inside

of the MCP spec. Some of the message types

that you and I are going to be focusing are the list

tools request and the list tools result.

As you guessed, list tools request is sent from the client

to the server and asks the server to list out all the different tools

that it provides. The server would then respond with

a list tools result message, which contains

a list of all the different tools that it can provide.

Two other common message types that you and I are going to see are

the call tool request and call tool result.

The first will ask the server to run a tool with some

particular arguments, and the second will contain the result

of the tool run. Now, at this point

in time, we've got this idea of a server and

a client. But I suspect it's probably

not really clear how all this stuff really works together. So

here's what we're going to do in the remainder of this video. We

are going to walk through an example call between

a lot of different things. So it's going to be kind of an involved

process. But we're going to imagine the communication that goes on between

a user or a server that we're putting together.

An MCP client, the MCP server, GitHub

as some provider that we're trying to access some data from, and

Claude. So let's get to it. Again, Stephen Grider, first

thing we would expect to happen is a user to submit some kind of query

or question to our server, like what repositories do

I have? At this point, it would be up to our server

to make a request off to Claude. But in that

request, we want to list out all the different tools that Claude has

access to. So before our server can make the request

off to Claude, it's first going to go through a little side detour

through the MCP client and the server. So here's what

happens. The server is going to realize that it

needs to see a list of tools to send off

to Claude, along with the user's query. So it's going to

ask the MCP client to get a list of tools. The

MCP client, in turn, is going to send a list

tools request off to the server, and the server

will respond with a list tools result.

Now that our MCP client has a list of the tools,

it will give that list of tools back to the server. And

now our server has everything it needs to make an initial

request off to Claude. It has both the original

message from the user and a list of tools to include.

So our server can make a request off to Claude with that query

and the set of tools. Claude is going to take a look

at the tools and realize, you know what, in order to answer

the user's original question right here, I really want

to call a tool. So Claude would respond

with some tool use message part. At

this point, our server is going to realize that Claude wants

to run a tool. But our server is no longer

really in charge of executing any tools. Instead,

our tools are going to be executed by the MCP server.

So in order to run the tool that Claude is asking

for, our server is going to ask the MCP client

to run a tool with some particular arguments that were

provided by Claude. The MCP client, however,

doesn't actually run the tool. It's going to send a call

tool request off to the MCP server. The

MCP server will receive that request and make

a follow request off to GitHub. So

this is where we would actually be getting a list of repositories

that belong to this particular user. GitHub

would respond with that list of repositories. Then

the MCP server would wrap up that data

inside of a call tool result and send

that back to the MCP client. Then the MCP

client in turn would hand the result off to our server.

Now our server has the list of repositories

and it can make a follow up request to Claude with

the tool result part inside of a user

message. So this tool result would include the list

of repositories that Claude was asking for.

And now Claude has all the information it needs to formulate

a final response. So it'll write out some text

of something like your repositories are, and then send that back

to our server, and our server would send it on back to our

user. All right, so this flow,

yes, it is rather complicated. The reason I want

to show you this is that we are going to see all these different

pieces as you and I start to implement our own

custom MCP client and MCP

server a little bit later on.

---

### Hands-on with MCP servers

#### Lesson 4: Project setup

*Source:* [https://anthropic.skilljar.com/introduction-to-model-context-protocol/296694](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296694)

**Video:** 09 - 003 - Project Setup.mp4 | **Duration:** 3m 9s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

To better understand some aspects of MCP,

we are going to start to implement our own CLI-based

chatbot. This is going to give us a better idea of

how clients and servers actually work together. In

this video, I want to do a little bit of project setup and just help

you understand exactly what we're going to make. I've got

a lot of product description over here of what we're going to build.

We're going to go through all this over time. Right now, I just want

you to get a high-level understanding. So as I

mentioned, it's going to be a CLI-based chatbot.

We're going to allow users to work with a collection of documents.

These are going to be fake documents. They're just going to be stored in memory.

We're going to build out a small MCP client

that is going to connect to our own custom MCP

server. For right now, the server is going to have two

tools implemented inside of it. One tool to

read the contents of a document, and one tool to

update the contents of a document. Again, these

documents are here on the right-hand side. They're all fake, so

they are going to be persisted only in memory. That's it.

Now, before we go any further, there is a very

important note, something I really want you to understand

around this entire process. And that is that

on a normal project, typically we

would be implementing either a client or

an MCP server. So on a real project,

we might be authoring just an MCP server to

distribute to the world and allow developers to access some

service that we have built up. Alternatively, we might be building

a project where we make only a MCP

client. And the intent here would be that we would be connecting

to some outside MCP servers that

have already been implemented by some other engineers. So

in this project, we are making both a client and

a server. And we're just doing that in one project so

you get a better understanding of how this stuff actually works

together. All right, now that we have this disclaimer

out of the way, let's go through just a little bit of setup.

Attached to this video, you should find a file named

CLIproject.zip inside there is

some starter code for our project. Make sure you download

that zip file, extract it, and then open up your

code editor inside of that project directory.

Just to save a little bit of time, I have already done so. So

I've already got my code editor open inside of that small

project. Inside this project, I would encourage you to

take a look at the readme.md file. Inside

here, I've placed some setup directions. So it's going to walk you

through the process of making sure you put your API

key into the .emv file inside this project.

And it's also going to walk you through the process of installing dependencies, either

with uv or without uv. Once you

have gone through all this setup, you can then run the starter project

right away. To do so inside of your terminal,

make sure that you are inside of your project directory.

So I called my project MCP. And inside there,

I've got all my different project files and folders. To

run the project, we will run uv run main.py

if you're making use of uv. If you are

not making use of uv, then it'll be just python

main.py. Now I'm making use of

uv. So I'm going to do a uv run main.py.

And then when I run that, I should see a chat prompt

appear. And if I ask what's one plus one,

I should see a response rather quickly. That is it

for our setup. So now we can start to focus on adding

in some new features to this application.

---

#### Lesson 5: Defining tools with MCP

*Source:* [https://anthropic.skilljar.com/introduction-to-model-context-protocol/296697](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296697)

**Video:** 09 - 004 - Defining Tools with MCP.mp4 | **Duration:** 7m 3s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's start to make an MCP server for our

CLI chatbot. As you saw, the

CLI itself already works, and we can already chat with

Claude, but there's no additional functionality around the MCP

server tied to it just yet. So we're going to work on adding

in this MCP server that is going to have two tools

in it for right now. It's going to have one tool to read a document

and one tool to update the contents of a document.

The implementation of the server is going to be placed into the MCP

server.py file inside of the root project

directory. Inside of here, I've already gone through a little

bit of work to set up a basic MCP server. And

then I defined a collection of documents that are going to exist

only in memory. And then finally, I put together some

different to-do items. So these are different tasks that you

and I are going to complete inside of this file. For

right now, as I just mentioned, we're going to be working only on these first

two items, writing out two tools. Now

we have authored tools in the past, and we saw that,

oh, there's a lot of syntax there. There's those big JSON

schemas. But I got good news for you here. In

this project, we're making use of the official MCP

Python SDK. So that's what this MCP

packages we're making use inside of here. This

MCP package is going to create our MCP server

for us with just one line of code, like what you see right

there. This SDK also makes

it really easy to define tools. To define

a tool, all we have to do is write out what you see on the right-hand

side over here. This will make a tool named add

integers with this description and

two arguments that are going to be required to be passed into

it. Once we write out a tool definition like

this, behind the scenes, Anthropic is going to generate

a tool JSON schema for us, which

we can take and pass off to Claude. So

right away, as you can see, it starts to get a lot easier to do

some basic things like defined tools. Now, as I

mentioned, our first task is going to be to implement these two

different tools. So let's go back over to our MCP

server.py file right away, and we're going to start to implement

the first tool of reading a document. So

the only goal here is to take in the name of some document

and return the contents of it. All of our

documents are already placed inside of this docs dictionary.

The keys are the IDs or essentially names

of a document, and the value is a document's contents. So

our tool is really simple. We're going to take in one

of these strings, look up the appropriate value

inside this docs dictionary, and then return it. That's all

we need to do. So to implement this,

I'm going to find the first to do and right underneath it, I'm

going to define a new tool by writing out at

mcp.tool. I'm going

to give this tool a name of read_contents

and a description of read the contents of

a document and return it as a string. And

remember, in a perfect world, we put in a really fleshed

out description right here to make sure it's super clear to Claude,

exactly when to use this tool. But right now, just

as usual, to save a little bit of time and keep you from

having to type out a bunch of text here, I'm just going to leave in a very

simple description. then I will define my

actual tool function. So this is the function to run

whenever we decide to run this tool. I

will call it read_document. It's

going to take in a argument of doc_id that

is going to be a string. I'm

going to set that to a field with a description

of ID of the document to

read. And then we need to make sure that we import

this field class at the top. So I'm going to

go up to the top and add an import

from pydantic import field.

then back down here inside of the function

body, I'm going to put in my actual implementation. So

the first thing I'm going to do is just make sure I handle the case in

which Claude asks for a document that doesn't actually exist.

So I'll say if doc_id not

in docs. So in other words, if the provided

document ID is not found as a key inside of this dictionary,

then I'm going to raise a ValueError with

a f-string of "doc with id {doc_id} not found."

ID not found. And

then if we get past that check, I'll go ahead and return the actual

document. So I'll return docs[doc_id].

And that's it, that's all it takes to define a tool. So

we've specified the name of the tool, its description,

the argument that is expected, its type,

and a description for that argument as well. All

these different decorators and field types and whatnot

are all going to be taken together by this Python MCP

SDK, and it's going to generate a JSON

schema for us. Now that we've implemented

this first tool, I'm going to remove the to-do right there.

And then we will implement our other tool, the one to

edit a document. So we're going to repeat

the exact same process. I'll say MCP

dot tool. I'll give it a name of edit_document

with a description of edit a document

by replacing a string in the document's

contents or semi-content with a new string.

Then for the implementation, I'll call this function edit_doc.

Or so we'll be consistent, call edit_document. And

then we're going to take in a couple of different arguments here. First

is going to be a document ID and then a old

string to find and then a new string to replace

the old string with. So let's write this all

out. We're going to have a doc_id. That

will be a string with a description

of ID of the

document. that will

be edited. old_

string will be a string with

a description of the text to replace

must match exactly including

white space. And

then our new_string. the

new text to insert in place of

the old text. So our document editing here is

just a very simple find and replace. That's it. Once

again, inside of here, I'm going to make sure that Claude

is asking for a document that actually exists. So if doc_id

not in docs, raise

ValueError with a f-string

of "doc with id {doc_id} not

found." And then if we do find the correct

document, here's how we will do our edit. We'll say docs

[doc_id] = docs[doc_id].replace(old_string, new_string)

replace old_string with new_string.

And that's it. All

right. So just like that, we have put together two tool implementations

really, really quickly. I can't repeat it enough, defining

tools with this MCP Python SDK is

a lot easier than writing out the schema definition manually.

Now that we've got both tools put together, I'm going to delete the

Tudu right there. Okay, so this

is a good start. We have put together our MCP

server and we've implemented two tools inside of it.

---

#### Lesson 6: The server inspector

*Source:* [https://anthropic.skilljar.com/introduction-to-model-context-protocol/296693](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296693)

**Video:** 09 - 005 - The Server Inspector.mp4 | **Duration:** 3m 52s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

We have put together some functionality inside of our MCP

server, but we have no idea if it works, so it'd be really

great if we could test this out somehow. It turns out that

by using this Python SDK, we automatically

get access to an in-browser debugger, so

we can make sure that this server is working as expected.

Let me show you how to use it really quickly. Back inside

my terminal, I went to make sure that I have my Python

environment activated. Remember, the ReadMe

document goes into detail on the exact command to run

to make sure that you have activated that environment. Once

you are sure that it is activated, we'll run MCP,

Dev, and then the name of the file that contains

our server. In this case, it is MCPServer.py.

Once I run that, I'll then be told that I have a server listening

on port 6277, and I'll be given a direct

act address to actually access it. I'm

going to open up that address inside my browser. And

once you go there, you'll see something that looks like this. This

is the MCP Inspector. Now right away, there's

something important I want you to understand here. This inspector

is in active development. So by the time you

are watching this video, what you see on the screen right now might

be very, very different than what I am showing. Nonetheless,

it's probably still going to have some very similar functionality.

On the left-hand side, you'll see a Connect button. That

is going to start up your MCP server, so that file

that we just edited. I'm going to click on

Connect, and then right away, we'll see a couple of different

things on the screen appear. I first want you to notice

the top menu bar up here. It lists out resources,

prompts, tools, and some other stuff. Again,

the UI might change by the time you watch this video,

so if you do not see this menu bar up here, all we are really

looking for here is some Tools section.

Once I click on Tools, I will click on List Tools,

and I'll see the name of the tools that we just put together.

If I click on one, the right-hand panel is then going to

change. And I can use this panel over here to

manually invoke one of my tools to make sure that

it is working as expected. So this

is how we can do some live development on our MCP

server without actually having to wire it up to a real

application. In order to use

the Read.Contents tool, all we have to do is put

in a document ID. If I go back over

to my editor and

go up to the docs dictionary right here, I can

copy one of these document IDs so I

will take out deposition.md. I

will put it in as the doc ID and then click

on run tool. I should then see run

tool of success with the contents of the document.

And that is it right there. I can verify it. So same

exact string is what I see right there. We

can use this same exact technique to test out the other

tool as well. So I will change over to

the edit document tool. Now I'll put

in my document ID. My

old string that I want to replace, how about replace the

word deposition? Actually, I have an easier word to type out.

How about just this? That'll be a little bit easier.

So my old string is this. Remember,

that is going to be a capital sensitive, and I'm going to replace

it with a report. And

if I run the tool, I'll then be given a success. Remember,

that tool does not actually return the document's

contents. It just edits the document. So

now to verify that the edit was done correctly, I

can go back over to the redock contents

tool, run that one again with the same document

ID, and I should see a report

deposition, and then blah, blah, blah. All

right, so as you can see, this MCP inspector allows

us to very easily debug a MCP

server that we are implementing without actually having to wire

the server up to an actual application. As

you start building your own MCP servers, I expect you'll

be using this inspector tool quite a bit. And we'll

probably use it a little bit more inside of this module, just

to make sure that our server development is going along pretty well.

---

#### Lesson 7: Course satisfaction survey

*Source:* [https://anthropic.skilljar.com/introduction-to-model-context-protocol/297281](https://anthropic.skilljar.com/introduction-to-model-context-protocol/297281)

---

### Connecting with MCP clients

#### Lesson 8: Implementing a client

*Source:* [https://anthropic.skilljar.com/introduction-to-model-context-protocol/296696](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296696)

**Video:** 09 - 006 - Implementing a Client.mp4 | **Duration:** 7m 26s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that our server is in a good place, we're going to shift gears

a little bit and start working on our MCP client.

The client can be found inside the MCP client.py

file inside the root project directory. Now before we do

anything inside this file, I just want to give you a very quick reminder

here. Remember what I told you about earlier. Usually

in a typical project, we are either making use of a client

or we are implementing a server. It's just in this

one particular project that we are working on that we are doing both. Again,

just so you can see both sides of the puzzle. Now

the MCP client itself inside of this

file is consisting of a single class. You'll notice

there is a lot of code inside of here and it doesn't look quite as

pretty as some of the code we just wrote out inside of the server.

So let me tell you exactly what's going on inside this file and exactly

why it is so large. Okay, so

inside this file, we are making the MCP

client class. This class is going to wrap

up something called a client session. The client session

is the actual connection to our MCP server.

This client session is a part of the MCP

Python SDK. So again, this session

is what gives us this connection to the outside server.

The session itself requires a little bit of resource cleanup.

In other words, whenever we close down our program or decide

that we don't need the server anymore, we have to go through a little bit of

a cleanup process. And I have already written out

a lot of that cleanup code inside of the MCP

client class. So that's really why this class

exists at all, just to make that cleanup a little

bit easier. You can see some of that cleanup code inside

of the Connect function and down a little bit lower.

at the cleanup, async enter, and async

exit functions as well. So it's very common

practice to not just make use of this

client session directly, instead very common to

wrap it up inside of a larger class that's going to manage some of

this different resource stuff for you. The

next thing I want to clarify is why this client exists

at all. So in other words, what is the client really doing

for us here? Well, remember, this full that

we looked at a little bit ago. So we had our code right

here. And at certain points in time, we needed, say,

a list of tools to send off to Claude. And then later

on after that, we also needed to run a tool

that was requested by Claude. In order

to reach out to our MCP server and get this list

of tools or to run a tool, that's where we

are making use of the MCP client. So we can imagine

that this client is exposing some functionality that

belongs to the server to the rest of our codebase. So

inside of our codebase, inside this project, specifically inside

of the core directory, there is a lot of code already

inside there that I put together that is making use of

this class. So there is some other code that's going to

call Some of the different functions you see inside of here,

like list tools, call tool, list prompts, get prompt, and so

on. For right now, in this video, we're going to focus on implementing

two functions, list tools and call tool.

So as you just saw in the diagram, we looked at a moment ago, these

two functions are going to be used in different parts of our code base

to get a list of tools to provide off to Claude, and

then eventually call a tool whenever Claude requests to call

a tool. Implementing these two functions is going to

be really simple and straightforward. So let me show you how we're going

to do it. We'll first begin with list tools. I'm

going to remove the two do inside there and replace

it with result is awaitself.session.

I'm going to call that like a function list underscore

tools. And then I will return result

dot tools. And that's it. So

this is going to get access to our session, which is our

actual connection to the MCP server. It's going to

call a built-in function to get a definition or a list

of all the different tools that are implemented by that server. I'm

going to get back result and then just return the tools and

that's it. Then we can implement call

tool right here in a very similar fashion. So this will

be return a

waitself.session, call

tool, tool name, and tool input.

Once again, getting access to the session, that is our

connection to the server, and I'm going to attempt to call

a very specific tool, the name the tool we passed in,

along with the input parameters or input arguments to it, that

were provided by Claude. Now, at this point

in time, I would like to test out these two functions really quickly.

To do so, we're going to go down to the bottom of this file, where

I put together a very small testing harness for us. So

down here, you'll notice I put together this

testing block, so we can run this MCP

client.py file directly. And if we do so, we're

going to form a connection to our MCP server, and

then we can just run some commands against it and just see what we get

back. Notice that in your version of the code,

there's a comment in there about changing the command and args

right here in case you are not making use of Uvicorn. So

if you're not using Uvicorn, make sure you take a look at that comment.

Inside of this with block, I'm going

to add in a little bit of testing code. So I'll

say result is await underscore

client list tools. And

then I'm going to just print out the result that we get

back. So this should start

up a copy of our MCP server, then

attempt to get a list of all the different tools that are defined

by it, and then just print out the result. To

test this out, I will flip back over to my terminal and

do a uvicorn run, MCP underscore

client.py. And as usual, if you

are not making use of uvicorn, you'll just do a Python

MCP client.py. Okay, so I'll run

that, and there is our list of tool

definitions. So I can see inside of here that I have the read.contents

tool, which we put together a little bit ago, and our edit

document tool as well. Each one has a description

and an input schema as well.

So this is our tool definition, which will eventually

be passed off to Claude. Now before we move on, there's

one other thing I want to test. Remember, we

just implemented the function that's going to allow us to

list out some tools and pass them off to Claude and

the function that's going to allow us to call a tool that is implemented

by the MCP server and then pass the result off to Claude

as well. I have already implemented the code that is

going to call list tools and call tool

for us somewhere else inside this project. So now

that we have added in this functionality, now that we have defined

these tools and the ability to call a particular tool, we

can now run our CLI again and attempt

to get Claude to make use of these tools. In other

words, we can ask Claude to inspect the contents

of some particular document and even edit a document.

So let me show you how we do that. Inside of my

MCP server, I just want to give you a reminder that there is

a document with a ID of report.pdf,

and it has some texture of something like a 20 meter

condenser tower. I'm going to go back over

to my terminal, and I'm going to run

my project with a uvicorn run main.py.

And then I'm going to ask Claude what is the contents

of the report.pdf document.

And make sure you put in exactly report.pdf

here. And when we run this, we're

sending off along with the request our list of tools.

Claude is going to decide to use the read document tool.

And it's going to get the contents of the document. And then we will see

that yes, Claude was able to get the contents of

that document. We are told that the report is something

about a 20 meter condenser tower. All

right, so at this point, we have added in some functionality around

our client. Remember, the client is what allows

us to access some functionality that is implemented inside

of the MCP server. At this point in time, we have

been able to list out some tools that are created

by the server and execute a tool that has been implemented

by the server.

---

#### Lesson 9: Defining resources

*Source:* [https://anthropic.skilljar.com/introduction-to-model-context-protocol/296699](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296699)

**Video:** 09 - 007 - Defining Resources.mp4 | **Duration:** 9m 45s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, we're going to move on to the next major feature inside

of MCP servers, which is Resources. To

help you understand resources, we're going to be implementing another

feature inside of our project. Here's what we're going to add in.

I want to allow a user to mention a document

by putting in an @ symbol and then the name of a document.

Whenever they do so, I want to automatically fetch the

contents of that document and insert it into the prompt

that we send off to Claude. So in total, there's kind

of two aspects to this feature. Whenever user types

out the @ symbol inside the message, we're going to automatically

show a list of all the different documents that they can mention

inside of a little autocomplete window. Then whenever

user submits a message with a mention inside of

it, we're going to automatically get the contents of that document

and insert it into the prompt that we send off to Claude.

So for example, if a user says something like what's

in the @report.pdf file, I

would want to assemble a prompt like this and send it to Claude.

So we're going to have the query inside there from the user, and

then we're also going to tell Claude that the user might have referenced

some document, and here is the contents of the document.

So the approach here or the idea here is that we will

not have to rely upon Claude to go and make

use of some tool to figure out what is inside of the

report.pdf file. Instead, the user can just

preemptively mention the file, and we're going to automatically

insert some context ahead of time. Now, one thing I

want to clarify here is that we're kind of talking about two

separate features. The first feature is that whenever

a user types in the @ symbol, we really need

the MCVP server to give us a list of all the

different documents that the user can possibly mention.

And then the second aspect here is that whenever a

user submits a message that contains a mention, then

we need the MCP server to give us the contents of a single

document. To get this information out of our MCP server,

we are going to be making use of resources. Resources

allow our MCP server to expose some amount

of data to the client. We usually define one resource

for each distinct read operation. So in

our example, we need to get a list of documents and

read the contents of a single document. So we would

probably end up making two separate resources. One

resource would be responsible for returning just a list

of document names so we can put them inside the autocomplete,

and then we would probably make another resource that will expose

the contents of a single document based upon its

document ID. When we define these

resources, they are going to be accessed through our MCP

client. So the entire flow that we're going to eventually

put together here, whenever user types in something

like what's in the @ and then presumably

they're going to put in something right there, as soon as they type in that @

character, we need to display a list of document

names to put in the auto complete. So our

code is going to reach out to the MCP client,

which in turn is going to send a read resource

request off to the MCP server.

Inside of that read resource request, we're going to include

something called the URI. That is essentially

the address of the resource we want to read.

This URI gets defined whenever we put together

our resource initially. So the URI is that

right there. When we send

off this read resource request, the MCP

server is going to look at the exact URI that we put inside

of here, and then run the function we

put together right there. Take the result and

send it back to us inside of a read resource

result message. We can then take the data

inside there and display it inside of our autocomplete or do

whatever else we need to do with it. There are two different

types of resources, direct and templated. You'll

also sometimes see direct resources referred to as static

resources. A direct resource just has

a static URI, so it's always going to be the exact

same thing, such as docs, colon slash slash documents.

A templated resource will have one or more parameters

inside of its URI. So for example, we might have documents

slash, and then kind of a wildcard right here. So

we can put in any document ID we want to. And

whenever we ask for this resource, that document

ID right there inside the URI will be automatically parsed

by the Python MCP SDK and

provided as a keyword argument to our function.

The keyword argument will have the exact same name of whatever

string you put in right there. So Doc ID right there will

be Doc ID right there. As

you can probably guess, we'll make use of templated resources anytime

that we want to allow a little bit more selection or variety

or customization in what someone is asking for

out of our MCP server. Implementing resources

is pretty straightforward. So let's go back over to our editor and we're

going to add in some resources to our server right away.

All right, so back over inside my editor, I will find the MCP

server.py file. I'm then going to scroll down a

little bit and I'm going to find some comments for writing

a resource to return all document IDs and

writing a resource to return the contents of a particular

document. Now for this first one right here, I

put in the comment Document IDs. Remember

for us, our document IDs are essentially the

name of the document. So for us, we're really just returning

these IDs. They're going to serve the purpose of the name. That

means we can put them directly into that autocomplete element.

All right, so to make our resource, I'm going to delete

that to do. and then I'll add in an MCP.resource.

The first argument is going to be the URI for accessing

this thing. Again, it's kind of equivalent to a route handler.

So I will use docs, colon slash

slash documents, and I'm also going

to add in a MIME type of application

slash JSON. A resource can

return any type of data, so it can be plain text,

it can be JSON, it can be binary data, anything.

It's up to us to kind of give our client a hint

as to what kind of data we are returning. To do

so, we're going to define this MIME type. A MIME

type of application slash JSON is a hint to

our client, who's eventually going to ask for this resource

right here, that we're going to be sending back a string that

contains some structured JSON data. And

so it would be up to our client to de-serialize

that data, or essentially turn it into some usable data

structure. Underneath that decorator, I'll

write out my function of list_docs, and

I'm going to return a list of strings. And

then inside there, I will return list_docs

keys. So just take all the keys out of that dictionary and

turn it into a list, and I'm going to return it. Now,

you'll notice that we are not returning distinct JSON here.

In other words, we're not actually returning a string. The MCP

Python SDK is going to automatically take whatever we return

and turn it into a string for us. All

right, let's take care of our second resource. So I'm going

to delete that comment and then replace it with MCP

resource, docs, colon

slash slash documents. And then this time I

want a templated resource because I'm putting in this

wildcard right here. And

then my mind type this time around, just for a little

bit of variety, I'm going to be returning plain

text because it's going to be just the contents of the document.

And I'm not going to wrap it up in any kind of structure. Now,

just so you know, in a real application, something

like read a document, I would probably return

an entire document record. So some kind of

dictionary that contains maybe the ID, the

content, the author name, the author ID, and

stuff like that. But just for the sake of an example, I'm

going to return just the text at the document to show

you how we would normally return plain text. So

in this scenario, my MIME type would be text slash plane,

and then I will make fetch_doc.

I'm going to take doc_id, which is going to be a string,

and I'm going to return a string. Once again, whatever

word you put right there, it's going to show up as a

keyword argument inside of your function. If we

added in some additional parameters inside of here, such

as maybe doc_type or something like that, it would

just show up as an additional keyword argument

like so. Then

inside of here, I'm going to first make sure that the ID that this person

is asking for actually exists. So if doc_id

not in docs, I'm

going to raise a ValueError with

an f-string that says doc with ID not

found. And then if we get past that check, I'll

return docs[doc_id]. And

that's it. Now let's try testing this stuff out inside

of our MCP Inspector once again. So

remember at our terminal, we can run the command UVicorn,

mcptest.mcpserver:app --reload.

That's going to start up a web server at port 6277

or C_VI 6274 as the default. So I'm going

to make sure I open that up inside my browser. Here

we go. I'll click connect. I'll then find

resources. And then I should be able to list

out all the different resources that are available. Now when

I list out resources, this is going to be specifically static

or direct resources. So I'll see only docs

slash documents. And then I can separately list

out all my different resource templates. And so I'll see

that I have one resource template of fetch_doc.

I can first try to run the slash documents

right here. We'll see what we get back. So this

is the actual message, the exact structure that

gets returned from our MCP server. You'll

notice that it has a text property and inside there is all

the data that we are returning serialized as JSON

string. So again, it would be up to us inside

of our CLI application to take this text right here and

deserialize it from this JSON string into

a usable list of strings. Then

we can also test out fetch_doc. So I'll click on that.

I have to enter a doc ID. So I'm going to put in.

I want to read the report.pdf

file. And I'll read

the resource. And now I should see the contents

of that particular document. And you'll notice this

is around. Once again, I get a text slash plain. So that's

a hint to me that this is plain text. And I should

not attempt to deserialize it from JSON in

any way.

---

#### Lesson 10: Accessing resources

*Source:* [https://anthropic.skilljar.com/introduction-to-model-context-protocol/296695](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296695)

**Video:** 09 - 008 - Accessing Resources.mp4 | **Duration:** 4m 38s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

We have defined two separate resources inside of

our MCP server. So now our client needs

the ability to request these resources. To

do so, we're going to add in a single function inside

of our MCP client. And remember, this

MCP client is going to have some functionality that we're

putting together that is going to be used by the rest of our application.

And I've already put together that code already. So somewhere

else inside this project, something is going to try

to make use of this function that we're about to add into

the MCP client. To get started, I'm going

to open up the MCP client file again. I'm

going to scroll down and find

read resource right here. So

our goal inside here is to read a particular

resource by making a request off to our MCP server

and then parse the contents that come back depending upon its

mind type and then just return whatever data

we get. So you'll notice that a argument

to it is the URI. This is going to be the URI of

the resource that we want to fetch from the server.

In order to make request, just to get all

of our types nicely, we're going to add two imports

at the very top of the file. I'm going to add in an

import for the JSON module. And from

PyDientTik, I will import any URL.

Then I'll go back down to

our read resource function. I'm going to clear

out the comment in the return statement. Then I'll

get a result from calling a wait. Self

session. I want to read resource. And

then again, this is really just to get the types to work out. We're

going to put in a any URL with the input

URI. Then

I'm going to take from that result. response

or excuse me, result contents

at zero. And I want to make this clear

right here why we were adding this in. So just a moment ago inside

of our inspector, we saw the response we get back. So

this is essentially that result variable. Result

has a contents list. And there's going

to be a list of elements inside there. We really only care about

the very first one. So I want to get the first dictionary.

I want to access the type property and the mind

type. I want specifically the MIME type because

it's going to help me understand what kind of data we got back. If

it is JSON, then I want to make sure I parse the text

as JSON and return that result. So let me show

you how we're going to do that. I'm going to add in a

if is instance of

resource types text resource

contents. And inside there, if

resource, mime, type is

equal to application JSON. So this

is our hint in use. If the server told us that it's

giving us back some JSON, we need to make sure that we parse

the text content as JSON. So

I will return in that case a JSON loads of resource.text.

And then otherwise, if we don't fall into that if statement and return

early, I want to just return resource.text.

So in this scenario, we'd be returning the text as just plain

text or not parsing anything. So this would really

be the case in which we get back the contents of a single

document. All right, so

that should really be it. We've got our read resource

put together. Now again, I want to remind you, I

know I've said this several times, but I just want to remind you because I

think it might be a little bit unclear. The code that we're

writing inside of the MCP client is being used from several

other places inside of this code base. So

somewhere else in this code base, we're going to be calling that

function that we just put together to get the list of document

names and then eventually get the contents of a document

to put into a prompt. So at this point,

everything should essentially work because the rest of the work has already

been done for us. So with that in mind, let's

go back over to our terminal and we're gonna test out our CLI application

again and see if this mention feature works. Okay,

so back over here, I'll do a uvrun

main.py and now I should be able to say something

like what's in the at and there

we go, I see my list of resources and I can use the arrow

key to scroll through. Once I am at a resource,

I like, I'll just hit space and we'll insert

that resource. So what's in the report.pdf

document And now, I can tell you

that everything is working as expected here. In other

words, the contents of this document is being sent off

to Claude inside the prompt. So if I submit this,

I should see an immediate response and it's going to tell me what is inside

of Report PDF. So this time around, Claude did

not have to use a tool to read the contents of

the document. All right, so that is resources.

Again, we make use of resources to expose some

amount of information from our MCP server.

---

#### Lesson 11: Defining prompts

*Source:* [https://anthropic.skilljar.com/introduction-to-model-context-protocol/296698](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296698)

**Video:** 09 - 009 - Defining Prompts.mp4 | **Duration:** 7m 44s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Last major focus we're going to have inside of our MCP server

is going to be on prompts. Once again, just like

we did with resources, we're going to implement a small feature

inside of our project. And we're going to use this feature to

understand what prompts are all about, just like we did with

resources a moment ago. Let me tell you about the feature we're

going to add into our program. We're going to add in

support for slash commands. So

for example, I want to have a format command. I've

got some screenshots over here of how it's going to work.

Whenever user types into slash, we're going to list out some number

of commands that are supported by our application. For

right now, we're going to have just one command called format. So

if I type in just slash, I should see a little autocomplete

right here, and the only autocomplete option should be format.

If I then select Format, I should be prompted

to add in some document ID after it. So

one of our different document names like report.pdf or

whatever else. Then whenever user runs

this command, the goal is to get Claude to

reformat this document using Markdown

syntax. So in other words, take the plain

string that we have without any special formatting tied to

it inside of each of our documents right now. Remember,

inside of our MCP server, our current document

content is just plain text. We want to feed

this into Claude and somehow get Claude to rewrite

it using Markdown syntax. So I would

expect to see some output like this, something that says, I'll

help you reform out the document. Claude is then going

to use a tool to read the contents of the document. And

then finally, inside the final response, I want to see the content

of that document rewritten down here in Markdown

syntax. Now, there's something interesting about

this feature that I want to point out. The real core

of this feature, like the real goal here, is to allow

a user to reformat a document into

Markdown syntax. And that is an operation

that actually doesn't require you and I,

the developers, to write out any code to implement.

What do I mean by that? Well, a user can already

launch our CLI and say something like reformat

the report.pedia file in

markdown syntax.

I use your can already do this. No issue whatsoever.

And Claude is going to do a reasonable job of it. It's going to take

the contents of our document and reformat it into markdown.

And as you can see right here, it worked entirely perfectly.

So what are we really doing with this feature? Well,

the thought process here is that if we just left this up to

users and allowed them to manually type in something

like convert this to Markdown, they might get a OK

result, but they might get much better result

if they had a really strong prompt that is custom

tailored for this particular scenario of converting a

document into Markdown. So a user might be a lot

happier if you and I sat down as

the MCP server authors and wrote out and

tested and evaluated and went through the entire process of evaluating

our really thorough, fantastic prompts

like the one you see on the right hand side. So again, just

repeat, yes, a user can execute this entire workflow

on their own, but if they use this fancy prompt over

here, instead, well, I think they would be all the better.

This is the real goal of the prompts feature inside

of MCP servers. The thought here is that

ahead of time, we can define a set of prompts inside

of our server that are custom tailored to whatever

our server is really specialized to do. In our case,

our server is all about managing documents, reading

documents, editing documents, and so on. So we might

decide to add in a set of prompts that are very

high quality that have been evaluated and tested, and

we know that they work in a wide variety of different scenarios. We

can then expose these prompts for use inside

of any client application, like the CLI app that

we are putting together right now. Now, one thing I want to point

out here is that we could develop this prompt and just

put it directly into our CLI code base.

That is totally possible. We could do that, obviously. But

again, the thought here is that your MCP server that

might specialize in some particular task might

expose some number of prompts that people can just come and use

without having to worry about developing them ahead of time.

To define a prompt inside of our MCP server, we're going to write

out a little bit of syntax very similar to the tools and

resources we have already put together. We will use the prompt

decorator. We'll add a name to the prompt and

optionally a description as well. Then whenever

the client asks for this prompt, we'll send back a list

of messages. These are actual user and assistant

messages. So we can take the messages and send them off

to Claude directly. All right, so let's go over

to our server, and we're gonna try putting together our own prompt.

And just like you see right here, it's gonna be all about taking the contents of

a document and somehow rewriting it in Markdown

format. Okay, so back inside my editor,

I'm gonna find my MCP server file. I'm gonna go down

a little bit to the comment about rewriting

a document in Markdown format. I'll

delete that to do, and then I'll add

in a MCP prompt, the

name of format, and

a description of rewrites the contents

of the document in Markdown format.

I'll then add in an actual implementation. So

format document, I can receive

as an argument a doc ID, and

then optionally we can add in a field description here

as well, just like we did with our tool earlier

on. So I can optionally add in a field with

a description of ID of the

document to format. And I'm also going to add

in a type annotation of string. Just make sure that's

really clear as well. From this function, we are going to return

a list of messages.

I'm going to make sure I add in an import for this base thing at

the top right away. So right underneath

the existing MCP server import, I will add in from

MCP server fast MCP

prompts import base. Then

back down at the bottom. Inside of here, we're going to define

our very well-tested, very well-evaluated prompt.

I wrote a prompt out ahead of time. I'm going to paste it in like

so. So this prompt is just asking Claude

to take in a document ID. Implicitly,

we are kind of asking Claude to fetch the document ID's

contents using the redocument tool. And then after

getting that document, just go ahead and rewrite it with Markdown syntax.

And finally, after rewriting it, edit the document

as well to save those updates inside of our server.

Now, after defining this prompt, we're then going

to return a list of messages. So down here,

I'm going to return a list with base

user message, and I'm going to feed in

our prompt that we just wrote out to it, like so.

Now I'm going to save this file, and then let's go start

up our MCP development inspector and test

out this prompt from that interface. So at my

terminal, I'll run that same command again, and then

navigate to that address inside of my browser. I'll

make sure I connect to my server. I'll then find the

prompts section. I'm going to list out all the different

prompts that are available to us. And at this point in time, we have one

prompt, just format. So I click on

format, and then I have to enter in a document ID right here.

Let's, this time around, maybe we'll put in a

document ID of how about outlook.pdf.

So I'll put that in. And then get

prompt. And then here is our list of messages.

So these have been put together ahead of time. I've got one

message part here. So a text part with

our full prompt right there. We could see that

the document ID was interpolated into it. Now

that we have these messages, we can send them off to Claude.

And hopefully we're going to get back some appropriate kind of response.

So once again, the entire idea here behind these

prompts, we might implement inside of our MCP server, is

that the prompts we are defining are going to be well-tested,

well-evaluated, really specialized to one particular

use case.

---

#### Lesson 12: Prompts in the client

*Source:* [https://anthropic.skilljar.com/introduction-to-model-context-protocol/296692](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296692)

**Video:** 09 - 010 - Prompts in the Client.mp4 | **Duration:** 3m 1s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Our last major task is to implement some functionality

inside of our MCP client and allow us to list

out all the different prompts that are defined inside the MCP

server and also get a particular prompt

with some variables interpolated into it. So

let's first implement list prompts. I will delete the

comment and replace it with a result is

await, self, session,

list prompts, and then I will return

result.prompts. And that's pretty much it.

And then get prompt. Now to be clear, when we get a

individual prompt, we're going to be given some number of arguments.

These arguments will eventually show up inside

of our prompt function. So for example, inside

a format document right here, we expect to receive a document

ID. Inside of this args

dictionary, the expectation is that there will be a document

ID key. And that will be passed in to

the appropriate function over here. And then we will get that

value interpolated into the prompt itself. So

inside the get prompt function, I will get a result

from self session, get

prompt. I'm going to pass in the prompt name. That's the

name of the prompt I want to retrieve. And then I'll pass in the

arguments. And then I will return result

.messages. So those are the messages coming

back. They form some kind of conversation that we want to

feed directly into Claude. And that's

it. That's all we have to do for our client. So

now we can test this out inside of the CLI itself. I'll

flip back over, run the project again. And

now if I put in a slash right here, I'll see that I

can access this format command. Now format

is really just the name of the prompt that we're going to invoke.

So if I select that and then hit space, I'll

then be asked to select one of the different documents and

you'll go with plan.md. I'll hit enter.

And then we're taking that entire prompt, really just

that single user message, and finiate directly

into Claude. So Claude now has the instructions

to go and reformat a document into Markdown syntax.

And it has also been given the ID of the document that

we want to reformat. So the first thing it needs to do here

is go and fetch that document's contents. And it

will do so by using the Git document tool.

And then finally, Claude is going to respond with the markdown

version of this document. So here is the document

with a bunch of markdown syntax inside of it. All

right, since it looked like this work just fine, let's do a

quick recap on prompts and make sure we understand what they are all

about. We begin by writing out an

evaluating a prompt that has some relevancy

to our MCP server's purpose. In our case,

we were making a document server. So having some functionality

or something about rewriting a document in a different

style, I think it kind of makes sense.

Once we have put our prompt together, we'll define a prompt

inside the MCP server. And then our client can

ask for that prompt at any point in time. When

we ask for the prompt, we will put in some number of arguments

that will be provided to this prompting function

right here as keyword arguments. And then our function

can make use of those keyword arguments inside the prompt itself.

---

### Assessment and wrap Up

#### Lesson 13: Final assessment on MCP

*Source:* [https://anthropic.skilljar.com/introduction-to-model-context-protocol/297196](https://anthropic.skilljar.com/introduction-to-model-context-protocol/297196)

Loading...

**Assessment (7 questions):**

**Q1:** You're building an MCP client to connect your application to an MCP server. What are the two main components you need?

- [ ] A frontend and a backend
- [ ] A database and a web server
- [ ] A REST API and a GraphQL endpoint
- **[CORRECT]** An MCP Client class and a Client Session

**Q2:** Your MCP client needs to find out what tools are available from an MCP server. What message type should it send?

- **[CORRECT]** ListToolsRequest
- [ ] CallToolRequest
- [ ] ToolDiscoveryRequest
- [ ] GetToolsMessage

**Q3:** You've built an MCP server and want to test if your tools work correctly before connecting to a full application. What's the easiest way to do this?

- [ ] Write separate test scripts for each tool
- [ ] Test everything manually in the terminal
- **[CORRECT]** Use the built-in MCP Inspector with `mcp dev mcp_server.py`
- [ ] Connect directly to Claude first

**Q4:** You're building a chat app where users ask Claude about their GitHub data. Without MCP, what's the main problem you'd face?

- [ ] GitHub doesn't allow API access
- **[CORRECT]** You'd have to write and maintain all the GitHub tool code yourself
- [ ] Claude can't understand GitHub data
- [ ] Users can't ask questions about repositories

**Q5:** You're deciding how to implement a new feature in your MCP server. Users should be able to click a button to trigger a 'summarize document' workflow. Which MCP primitive should you use?

- [ ] Resources - because you need to fetch document data
- [ ] Functions - because it involves processing
- **[CORRECT]** Prompts - because users control when to start the workflow
- [ ] Tools - because the AI needs new capabilities

**Q6:** You're using the Python MCP SDK to create a tool that reads files. What's the easiest way to define this tool?

- **[CORRECT]** Use the @mcp.tool() decorator on a Python function
- [ ] Create a separate configuration file
- [ ] Write JSON schemas manually
- [ ] Send HTTP requests to register the tool

**Q7:** You want to create a resource that fetches different documents based on their ID, like docs://documents/report.pdf. What type of resource should you use?

- **[CORRECT]** A templated resource with parameters in the URI
- [ ] A tool instead of a resource
- [ ] A direct resource with a static URI
- [ ] A database query resource

---

#### Lesson 14: MCP review

*Source:* [https://anthropic.skilljar.com/introduction-to-model-context-protocol/296691](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296691)

**Video:** 09 - 011 - MCP Review.mp4 | **Duration:** 4m 12s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

We are all done with our project, but before we move on, I want

to do a quick recap on the three server primitives

that we learned about. So tools, resources, and prompts.

In particular, I want to highlight something interesting about each of

these. Namely, what part of an app is really

responsible for running each? In other words, in

a typical application, who is really running each

of these things and who benefits from them? Well,

we would say that tools are model controlled. This

means that Claude alone is really responsible for

deciding when to run a given tool. Resources

are app controlled. In other words, some code

running inside of your app is going to decide that

it needs some data provided by a resource. It will

be your app's code that decides to execute a resource

and use the return data in some way, maybe by

using that data in the UI or something like that. In

our case, we fetch a resource and then use

that data inside the UI to provide a list of autocomplete

options. We also fetch a resource

to augment a prompt. Both of those things were really application-related

code that was authored by you and I to

put together. And finally, prompts

are really user-controlled. So a user decides

when a prompt is going to run. A user might

start the invocation of a prompt by clicking on some UI

element, like a button or a menu option,

or they might make use of a slash command, which is what we

did. The reason I highlight what is controlling each

of these is to give you some idea of their purpose.

So if you ever need to add capabilities to

Claude, you're probably going to want to look at

implementing some tools inside of your MCP server or

consuming some server's tools through

your MCP client. If you ever

want to get some data into your app for the purposes of showing

content in UI or something similar, then you

probably want to use a resource. And if you ever

want to implement some kind of predefined workflow, you

probably want to look at prompts. Now

you can see examples of all these ideas inside

of the official Claude interface at

Claude.ai. So here's what it currently looks

like for me. You'll notice that underneath the

main chat input are some buttons right here. If

I click on one, and then click on one of these

examples, you'll see that I immediately dove

into a chat. So this was a user-controlled

action. I, as the user, decided to start

off this particular workflow, and I'm making use of a

prompt that was probably already written ahead of time

and probably has been optimized in some way. So

to implement that list of buttons right there, we would probably want

to put together a series of different prompts inside of a MCP

server. Likewise, if I go back and

maybe click on this little tab right here, the plus button,

you'll notice that I have a add from Google Drive button.

Now, I'm not going to click on it because it's going to show some of my internal

documents. But if I click on that button, I'm going to see some

documents that I can add into this chat as some context.

Knowing what documents to actually render in that list,

and then whenever I click on one, automatically injecting its

contents into the context of this chat, that is all

application-related code. So it is solely

the application that needs to know the list of documents

to render here. And that's, again, specifically

UI-related elements. So to implement

that listing of documents from Google Drive, I

would probably look at implementing a resource inside

of an MCP server. And then, finally, if I

enter in a message to this chat of something like,

what is squared three use JavaScript to calculate the value

and send it off, I'm clearly expecting Claude

to somehow execute some JavaScript code, which would

likely be done through the use of a tool. In

this case, the decision to use a tool was 100% model

controlled. It is the model that decided to use some

JavaScript tool execution. To implement something

like this inside of an MCP server, we'd likely

want to, you guessed it, provide a tool.

So in total, that's our three different server

primitives. And each one is really intended to

be used by a different portion of your overall application.

So we got tools which are generally going to serve your model,

resources, which are generally going to serve your app,

and prompts which are going to serve your users. And

once again, these are high level guidelines. And the only reason

I mentioned them is to just give you a sense of when

you should use each of these primitives, depending upon what

you are trying to put together.

---

*Extracted from Anthropic Academy via authenticated session | Deep Extraction v3 | 2026-04-12*
