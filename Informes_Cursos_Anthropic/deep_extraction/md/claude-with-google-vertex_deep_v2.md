# Claude with Google Cloud's Vertex AI

> **Source:** [https://anthropic.skilljar.com/claude-with-google-vertex](https://anthropic.skilljar.com/claude-with-google-vertex)
> **Category:** cloud-integration | **Difficulty:** intermediate-advanced | **Domain:** Cloud Integration
> **Tags:** gcp, vertex-ai, api, rag, tool-use, computer-use
> **Extracted:** 2026-04-11 | **Version:** v3 (with YouTube transcripts + quiz content)

---

## Extraction Statistics

| Metric | Value |
|--------|------:|
| Total Lessons | 93 |
| Sections | 13 |
| JW Player Transcripts | 81 |
| YouTube Transcripts | 0 |
| Modular Text Lessons | 1 |
| Quiz Assessments | 0 |
| JW Transcript Chars | 645,825 |
| YouTube Transcript Chars | 0 |
| Modular Text Chars | 1,264 |
| **Total Content** | **647,089** |

## Curriculum Structure

- **Introduction** (1 lessons)
- **Anthropic overview** (1 lessons)
- **Accessing Claude with the API** (14 lessons)
- **Prompt evaluation** (8 lessons)
- **Prompt engineering techniques** (7 lessons)
- **Tool use with Claude** (14 lessons)
- **Retrieval Augmented Generation** (10 lessons)
- **Features of Claude** (8 lessons)
- **Model Context Protocol** (12 lessons)
- **Anthropic apps - Claude Code and computer use** (8 lessons)
- **Agents and workflows** (8 lessons)
- **Final assessment** (1 lessons)
- **Wrapping up!** (1 lessons)

---

## Complete Lesson Content

### Introduction

#### Lesson 1: Welcome to the course

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289145](https://anthropic.skilljar.com/claude-with-google-vertex/289145)

**Video:** 01 - 001 - Welcome to the Course.mp4 | **Duration:** 2m 8s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Hello and welcome to your guide on getting started with Claude.

My name is Stephen Grider, and I am a member of Technical Staff

at Anthropic. In this video, I'm going to give you a quick

introduction of the course. I'll help you understand what topics

we'll be covering, requirements to get through the course, and I'll

give you some tips on how to succeed. We are going

to cover a wide variety of topics throughout the course. We

will first begin with some background on models offered by Anthropic,

then quickly pivot to understanding how to access them through

vertex. From there, we'll focus on prompting,

first with evaluations, then engineering techniques.

Next up, we'll be a deep dive on expanding Claude's capabilities

through tool use. We will understand how to get task-specific

context into Claude with retrieval augmented generation,

then focus on connecting Claude to new services with

model context protocol. We'll walk through

two agents created by Anthropic, named Claude Code

and Compute Use, and understand how to apply them to solve

interesting problems. Finally, we'll spend some time

to learn how to handle more complex tasks with workflows

and agents. There's a lot of content to cover

here, so there are a couple of expectations on

your side to make sure that we can get through everything.

First, you need to have a basic understanding of Python, along

with a Python environment that can run notebooks. The

vast majority of code in this course will be written into and

executed from notebooks. You will also need

a Google Cloud account that has access to both vertex

and the Anthropic models. Lastly, given the

speed at which we'll cover different topics, I do have

some tips to help you find success. First, I

highly recommend you write code alongside me. Watching

someone else author code isn't really enough to absorb it.

Second, consider speeding up the video playback speed

in the video player that you are using. This will help you get

through the content at a faster pace and make it easier

to review specific videos that you might find challenging.

Third, you've got to apply some of the techniques that you learn

throughout the course. Consider expanding or altering

the different notebooks that we author. Fourth,

if you get stuck at any point in time, ask Claude for

help. Claude can get you unstuck from just about any situation

or clarify points that you might find confusing.

Well, that's enough of an introduction for now, so let's start

learning about Claude in the next video.

---

### Anthropic overview

#### Lesson 2: Overview of Claude models

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289146](https://anthropic.skilljar.com/claude-with-google-vertex/289146)

**Video:** 02 - 001 - Overview of Claude Models.mp4 | **Duration:** 3m 56s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, we are going to examine Claude's

three model families and understand which one is right

for your specific use case. To help you understand how

these models differ, I'm going to walk you through each

model's key characteristics and then show you a simple

framework for picking the right one. Before we

dive into the specifics, let me make one thing clear. All

three of these models share Claude's core capabilities, so

they can all handle text generation, coding, image

analysis, and many other tasks. The real

difference between them is how they are optimized. One

is built to focus on intelligence, one for speed and

cost efficiency, and one for more of a balance

between intelligence and speed. The first is

Opus. Opus is Claude's most capable

model. And when I say capable, I need to say that this is a

model that delivers the highest level intelligence that you

can get out of Claude. In practice, that means

that Opus is designed for scenarios where you have complex

requirements that need a high level of intelligence and

planning to complete. It can work independently on

complex projects for a long period of time, like

a task that can run on for several hours where the model

needs to manage multi-step processes and navigate

a lot of different requirements on its own without a lot of

human intervention. Opus supports what we call

reasoning, which means it can provide a quick response

for simple tasks or it can spend some time thinking

for a more complex task. The downside

is that Opus has a moderate latency and a

higher cost, and that's really the trade-off that you are making.

While you get really high intelligence, it also takes a little

bit more time and cost for every request that you make.

Next up is Sonnet. Sonnet sits in a kind of

sweet spot in Claude's lineup. It has a good balance

of intelligence, speed, and cost that makes

it really useful for most practical use cases.

What makes Sonnet great is its strong coding ability, along

with its fast text generation. Many developers

like its ability to make precise edits to complex

code bases, meaning it can make changes to a project

without breaking a lot of existing functionality. Finally,

we have Haiku. Haiku is Claude's fastest

model, and it's made specifically for applications where

response time is really important. One important

thing to note around Haiku is that it doesn't support the reasoning

capabilities that Opus and Sonnet have. Instead,

Haiku is optimized for speed and cost efficiency.

And this makes Haiku a really good choice for user-facing

apps that need some real-time interactions.

Now let's talk about how you decide which of these three models

to use for your particular application. The way to

think about model selection really comes down to understanding the

trade-off between these different models. On

the one hand side you've got really high intelligence and

on the other side you've got more cost and speed.

Opus sits on the intelligence side. It's really intelligent,

more expensive, and also has higher latency. Haiku

sits on the cost and speed side. It has

moderate intelligence, low cost, and the highest speed. And

Sonnet is right there in the middle, striking a good balance between

these different qualities. So here's how you decide which

model to use. You really need to identify or figure

out what matters most for your specific use case. If

intelligence is your top priority, meaning you have a

complex task that needs really strong reasoning, then

you probably want to make use of Opus. You are choosing

quality, over speed, and cost. If speed is

your priority, meaning you have real-time user interactions,

or you've got some high-volume processing, where you need to get some

responses back as fast as possible, then you want to choose

Haiku. If you need more of a balance between intelligence,

speed, and cost, which is often the case for most

applications, then Sonnet is probably your best choice.

One important thing to note here is that many teams don't

just pick one model and stick with it. Instead, you

might use multiple different models in the same application.

You might use Haiku for user-facing interactions

where speed is really important, maybe Sonnet for your

main business logic, and Opus for the really complex

tasks that need some deeper reasoning. So that covers

Claude's three model families and how to choose between

them. Just so you know, we are most often going to use Claude

Sonnet in this course just because it gives us a really

fantastic balance of these three different qualities.

---

### Accessing Claude with the API

#### Lesson 3: Accessing the API

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289151](https://anthropic.skilljar.com/claude-with-google-vertex/289151)

**Video:** 03 - 001 - Accessing the API.mp4 | **Duration:** 5m 12s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this module, we are going to examine how we access Claude

and use it to generate some text. To help you understand how

this works, I'm going to walk you through the full lifecycle of a request

sent to Claude. We are going to also take a brief look

at what is going on behind the scenes inside of Claude. To

get started with this walkthrough, we are going to consider a straightforward,

standard chatbot app. Let's imagine that you are

building a web app and want to show a chat window to a user

in the web browser. When the user enters a message

and clicks send, their expectation is that some

response will just magically appear. Now,

like I said, I want to examine what is going on behind the

scenes here to generate this text and display it on

the screen. We are going to break this down into five

separate steps, which I've outlined at the top of this

diagram. And we're going to walk through each step one by

one. When a user enters some text and clicks

send, that text is going to be sent off to a server

that you, the developer, implement. I mentioned

this step just to make one thing clear. You

should not attempt access Vertex directly from a web

or mobile app. Whenever you make a request of Vertex, you

are required to include secret credentials. And the best

way to make sure that these stay secret is by never including them

in your client-side app, and only making requests to Vertex

through a server that you implement and control. On

to step two. Once your server has received a request from

the client, the server will make a request to Vertex. Usually,

you will make this request through one of the SDKs that Anthropic

has published. There are official SDK implementations

for Python, TypeScript, Go, and Ruby.

To be clear, you are not required to use an Anthropic

SDK. You can also use one of the official Vertex

SDKs published by Google. When you make this request,

you are required to pass long several pieces of data. In

particular, you need to include the name of the model that you wish

to run, a list of messages, which will include the text

that your user submitted, and a max tokens

value, which limits the length of text that

Claude will actually generate. Next up

is the Claude model itself, which is where our text

will actually be generated. This is where we are going to go

into a little bit of detail on the text generation process

within the language model. This process is complex,

so I'm going to give you a simplified high-level overview.

We are going to break down the text generation process into

four separate stages. In the first stage, the

user's input will be broken down into smaller strings.

Each of these text chunks are referred to as a token.

These tokens can be whole words, or a part of word, or

even a space or a symbol. To keep things clear,

we are going to assume that each word forms one single

token. Each token is then converted into

an embedding. An embedding is a long list of numbers,

and you can think of these lists as being like a number-based

definition of a given word. Now, an interesting

aspect of written language is that a single word can

have many possible meanings, and it is only the word's

position in a sentence and presence of other words

around it that narrows the definition down to one particular

meaning. For example, quantum is a word

that has many different definitions, and when we see this

word, we don't really know what it means until

we see other words around it. Likewise, each

embedding can be thought of as containing all possible meanings

of each word. To refine each embedding down to a single

precise definition, a process known as contextualization

is used. In contextualization, each

embedding is adjusted based upon other embeddings

around it. This process helps highlight the meaning

of each embedding that makes the most sense given its

neighbors. The last step is generation, which is where

the text actually gets written. By this point, each

of the embeddings has absorbed a tremendous amount of information

from their neighbors. The final process embeddings are

then passed to an output layer, which produces probabilities

for each possible next word. Now, the

model doesn't automatically pick the highest probability.

Instead, it uses a mix of probability and randomness

to select words, which helps create more natural and

varied responses. The selected word is then

added onto the end of our list of embeddings, and the entire

process repeats itself all over. After generating

each output token, the model will then pause and ask

itself several questions to decide if it is done generating

text. First, it will count the number of tokens

it has generated and see if it is larger than the max

tokens parameter that was provided with the input request.

This max tokens parameter will limit the total number

of tokens that the model will generate. There is also

a special end of sequence token that the model can

generate. This is not a regular word. It

is a special signal that the model uses to indicate that it

has reached what it considers to be a natural end to

its generation and that it should stop. Once the generation

is complete, the API will send response back to your

server. The response will contain a message which

has the generated text inside it, along with usage

and stop reason. The usage is a count of the number

of tokens that you fed into the model and the number of tokens

that were generated. The stop reason will tell you

exactly why the model decided to stop generating

text, whether it hits a natural end of sequence token

or maybe it exceeded the allotted number of tokens.

Once your server has received this response, it will send

the generated text back to your web or mobile app,

where you will display it on the screen. So that is the entire

flow. Now, we covered many topics in

this video. I don't expect you to memorize any of this

just yet. The only goal is to start to get you familiar

with some common terminology around accessing Claude through

the API.

---

#### Lesson 4: Vertex AI Setup

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/307525](https://anthropic.skilljar.com/claude-with-google-vertex/307525)

In the next video we will be making a request to Vertex AI in order to call a Claude model. To do so, you need to go through a little bit of setup.
Step One: Ensure Anthropic models are enabled in Vertex

In your browser, navigate to https://console.cloud.google.com/vertex-ai/dashboard
In the left hand nav, click on 'Model Garden'

In the 'Search models' box, enter 'Anthropic'

Click on the model that you want to use.

Step Two: Enable the Model

Once you've found the model you want to use, you may need to enable it. On the model information page, click the 'Enable' button
If you don't see an 'Enable' button then you already have access to the model

Step Three: Install the gcloud CLI
If you don't already have the gcloud CLI installed, follow the directions here to install and authenticate with the CLI: https://cloud.google.com/sdk/docs/install
Step Four: Login and set up authentication with the gcloud CLI
If you have not already logged in to the gcloud CLI, do so by running:
gcloud init
gcloud auth login
Then, set your project ID and set your default credentials:
gcloud config set project YOUR_PROJECT_ID
gcloud auth application-default login
That's it! The Anthropic SDK will automatically use these credentials when attempting to access Vertex.

**Code Examples:**

```
gcloud init
gcloud auth login
```

```
gcloud init
gcloud auth login
```

```
gcloud config set project YOUR_PROJECT_ID
gcloud auth application-default login
```

```
gcloud config set project YOUR_PROJECT_ID
gcloud auth application-default login
```

**Resources & Links:**


---

#### Lesson 5: Making a request

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289155](https://anthropic.skilljar.com/claude-with-google-vertex/289155)

**Video:** 03 - 003 - Making a Request.mp4 | **Duration:** 5m 28s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

I think we've done enough talking, so it's time for us to actually write out

some code and get our hands dirty. In this video, we're going

to go through three different steps in order to make a request off to

Vertex. Step one, we're going to first create

a notebook and install the Anthropic Python SDK.

This SDK is going to allow us to make a request off to

Vertex. I've already created a notebook

ahead of time, and I would encourage you to do the same so you can follow

along. So for step one up here, we're going to write

out a magic command so we can install the Anthropic SDK.

We're going to do that with a percent, pip install,

and then inside of double quotes, Anthropic,

square brackets, vertex. I'm going

to run that cell. Alright, after

that, we're going to create an API client. From

the Anthropic package that we just installed, I'm going

to import Anthropic Vertex. This

is a special version of the Anthropic client that is designed

to connect specifically to Vertex. I'm

going to create an instance of that. And

whenever we create this instance, we also have to pass in two keyword

arguments. The first will be region. I'm going to put

in global and our project ID.

Now, your project ID is not going to be the same as mine. You will have

to go over to your Google Cloud console and look up your

project ID using the project selector in the

header. For me, my project ID is course

460319. But

again, you're not going to use the same ID as I. After

that, I'm going to specify the specific model version

that I want to use and assign it to a variable just so I don't

have to type this out everywhere repeatedly throughout all the

following notebooks we make inside this course. So

to model, I'm going to assign the specific model version that

I want to run. I'm going to use Claude,

Sonnet, Dash 4, then AtSign,

and 20, 25, 0, 5, 1,

4. Now, before we move

on to step number three, where we are going to make a request, I

want to go over just a little bit of terminology. So

the first thing to understand here is that we are going to access Claude

by using the create function inside the Anthropic

SDK. This function requires three different

keyword arguments, a model, max tokens,

and messages. The model keyword argument is

just going to be the name of the model we want to run. We already

defined that variable ahead of time in our previous cell.

The second required keyword argument is max underscore

tokens. This sets a maximum budget

on a number of tokens that Claude can generate. For

example, if we pass in a max tokens of 1000, if

Claude tries to generate anything longer than that, then

the generation will be automatically stopped, and we will

receive back the first 1000 tokens that were generated.

One thing to note here is that Claude doesn't try to target

your number of max tokens. In other words, Claude

won't try to write a response of 1000 tokens,

it'll just write whatever response it thinks is appropriate.

And as such, you should really view max tokens as being

like a safety mechanism to ensure that you're not

generating too much text. Finally, messages.

And this is the part that I really want to focus on because

messages are going to be a huge focus for us in the coming videos.

To understand what messages are all about, I would like

you to think back to the chat application we discussed a

moment ago. So a user might type

in some question to Claude and then expect to get an answer back.

The messages that we're talking about when we pass these things

into this create function are meant to represent exchanges

like this. There are two types of messages, a

user message and assistant message. User

messages contain text that we want to feed into Claude.

The content inside of a user message is text that either

a user or you and I as developers have

authored. So in other words, a user message will contain

text that has been written by some person.

The second type of message is an assistant message. These

messages contain text that have been produced by a model

and sent back to us. Now, at this point,

I think we have enough knowledge to at least make our

first request. So let's do that and then discuss

messages a little bit more. Back inside of my notebook,

in the very last cell, I'm going to declare a variable of message.

Now we'll come from client messages create.

And I'm going to pass in those different arguments that we just discussed.

So I'll put in a model of model, a max tokens,

and I'll use 1000 here, which I think is definitely a safe

limit, and then a list of input messages. So

inside here, I'm going to put in one single user message,

and it will contain my question or my query that I want to

send off to Claude. To create a user message,

we'll create a dictionary that will have a role

of user, and then a content that will

contain the actual string that we want to send into Claude.

So in this case, I'm going to ask Claude to define quantum computing

with something like what is quantum

computing answer in one sentence.

Then I'm going to run this. We'll take a moment or two

to run because we are actually accessing Claude here. And

then in the next cell down, I'm going to try to print out the message

variable. We'll see what we get. All

right, so inside of here, we can see there's a lot of stuff coming

out, but noticeably, we have a definition

right around here of what quantum computing actually

is. So inside of this message variable that

we got back, our text is kind of deeply nested.

We very often want to get just the text that Claude has generated,

and very often we don't really care about any of these other properties that

are contained inside this thing. So to access

just the generated text, we would write out message.content[0].text

like so. And if I run that cell again, now I'll

see just the generated text and nothing else.

---

#### Lesson 6: Multi-turn conversations

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289156](https://anthropic.skilljar.com/claude-with-google-vertex/289156)

**Video:** 03 - 004 - Multi-Turn Conversations.mp4 | **Duration:** 8m 54s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The code we've written out so far simulates a very simple

exchange with our model. And we can kind of visualize this conversation

inside of a chat box like this. We sent in

a request asking something like what's quantum computing,

answer in one sentence. And we got a very simple

single sentence reply. Naturally, we might want

to continue this conversation at some point in time. So

we might want to be able to send in a follow up asking something

like write another sentence. And we

would then expect to get back a response that expands on

quantum computing in some way. To have a multi-message

conversation like this, there's something really critical that you

need to understand around the Anthropic API and Claude

itself. And that is that the Anthropic API

and Claude do not store any messages that you

send to it. None of the messages you send get

stored in any way, and none of the responses

that you get back are stored in any way. So if you

ever want to have some kind of conversation going on, where

you have multiple messages that kind of maintain a context

or flow, then there are two things that you need to

do. You need to manually, inside of your

code, maintain a list of all the messages that you are

exchanging. And second, you need to make sure that

you provide that entire list of messages with every follow-up

request that you make. So let's go into some detail

on this entire idea, just make sure it's really clear and

you understand what's going on here. The first thing I want to

do is write out a little bit of sample code just to prove to you

that Claude doesn't store any messages or anything

like that. And I can prove this by trying to simulate this

kind of conversation where I first ask what quantum computing

is and then ask right another sentence.

So back inside of my notebook, I'm going to go to the cell where I initially

asked what is quantum computing. And I want to paste

in a second request to Claude that

I wrote out ahead of time. So in this second request,

I'm asking Claude to write another sentence, and

I'm going to print out the text inside of that follow-up

request. So now we've kind of got a simulation

of what's going on right here, where we ask that first question and

then send in a follow-up. And we're going to see that we don't get

back any kind of legible or any usable

text here. So I'm going to run this and we'll see what happens.

So back over here, I'm going to run that cell now and we're going to see that

we get back something that has absolutely nothing to do with

quantum computing at all. So again, to make sure

that it's really clear why we are seeing this result and

not seeing something about quantum computing, let's go over

a couple of diagrams. All right, so in

this diagram, I'm going to first show you exactly what's going on with

the query code that I've written out, where we are getting back a response

that has nothing to do with quantum computing. So

initially, I make a similar quest to Claude, where I have

one user message, and I'm asking Claude to define quantum

computing in one sentence. I then get back a response

that is exactly what I would expect. Claude

gives me back a one-sentence definition of quantum computing.

Then I make a second request where I have only

one message inside the body. And the only message is

asking Claude to write another sentence. When

I send this in, Claude has no memory of any past conversation

or any previous messages that I exchanged with it. So

Claude is just going to do the best it can to fulfill

my request. It's going to write out some sentence, but

it definitely is probably not going to be about quantum

computing. So now let me show you what

we need to do to fix this problem. Here's how we're

going to solve the issue. First, we're going to

once again make that initial request with just one user

message. Then we're going to take that assistant message

that we get back and append it into a list

of messages. So we're going to take the assistant right there and we can

imagine we're going to add it into our list on the left-hand

side. Then, when we want to follow

up on this conversation or continue it in some way, we're

going to append on a user message at the bottom.

So now we can read this as like a real conversation. I

asked to find quantum computing, I got back a response,

and now I'm adding in another question or another

query that I want to ask Claude. In this case, write

another sentence. Now when I send

in this list of messages to Claude, it will have the entire

context and history of the whole conversation. It's

seen all the previous messages that we've exchanged around

this line of questioning. And hopefully, Claude

will be able to give us back a more reasonable answer, hopefully

a one sentence follow up that's going to extend its previous

answer a little bit more. To see this entire flow

in action, I'm going to go back over to my notebook and we're going to try to write

out some code that will allow us to maintain the full

context for a conversation. Back

inside of my notebook, I'm going to get started by making three

different helper functions that are going to aid us in

maintaining the history or context of a conversation.

We're going to end up using these helper functions quite a bit throughout the

remainder of this course. So in this cell right

here, I'm going to give myself a little bit of space at the top and

then define our first helper function that will aid

us in maintaining this history. I'm going to name this

function add user message. It's

going to take in a list of messages and some text.

I'm then going to make a variable of user message. That's

going to have a role of user and

some content of whatever text we pass in. And

then I'm going to append this new user message into the

list of messages. Next,

I'm going to add in a second helper function that's going to specialize

in adding in assistant messages to a history.

So I'm going to copy this function right here just to save a little bit of time.

I'll rename it to add assistant message.

And I'll go through and wherever I see the word user, I'm

gonna change it out to Assistant. So right there, right

there, and right there. Okay,

now onto our third helper function. I'm

going to take our messages.create function call

down here. And I'm going to rename it to chat.

Whenever I call chat, I'm gonna pass in a list of messages.

So this is gonna be like my message history. Then

I'm going to indent our call right here.

I'm going to replace messages with the Messages argument,

and then return from this function is going to be message

content at zero dot text. All

right, so here are the three helper functions. And

again, we're going to use these quite a bit throughout the remainder of this entire

course. These helper functions are going to make it significantly

easier for us to have a conversation that maintains some

history or context over time. So now let

me give you a demonstration of how we're going to put them to use.

All right, so down here in the next cell down, I'm gonna write in a

couple of comments that she's gonna guide us through the process of

maintaining a conversation that has some history tied

to it. I'll first begin by making an empty

list of messages. So this message is variable

right here, we can imagine is storing our entire conversation

history. Over time, we're gonna add in a collection

of different user and assistant messages to it.

Next, I'm going to add in my initial user message.

So I will call the add user message function.

I'll pass in the list of messages that I'm appending messages

to, and then my user text is

going to be define quantum computing in one sentence. Now,

just to make sure we're going down the right path here, I'm going to print

out the list of messages and run the cell.

And we can see right away that we have a correct structure

of messages. So I have a list. It has a dictionary

inside of it with a role of user and a content that

contains something that I want to feed into Claude. So

now we can easily call Claude by making use of that chat

function that we just put together. I'm going to call chat and

pass in my list of messages. And then out of that, we'll

get back some kind of answer. I'm going to print out

the answer and run the cell again. So

we get the response, we should see a sentence here

about quantum computing. So now we are in this

situation. We have sent an initial message into

Claude and gotten an assistant message back in response.

Now we need to take this answer and append it into our

conversation history. So we need to add in or

append it in by making use of the add assistant message

function that we just defined. So back

over here. I'm going to call add assistant

message. I want to add into our list of messages

and I want to add in specifically the content out

of the answer that we just got back. So now let's

do another check and make sure that our list of messages is

looking correct. If I print out messages,

I should see my user message, then the followup assistant

with the content that we got back from Claude. Okay, so that

looks good. So now onto the last step. We're

going to append in one last user message and

send the entire conversation history into Claude once

again. So for that, I'll

do another add user message with

my list of messages. And then my followup question here or my

followup request is going to be write another

sentence. I'm then going to call

chat again with the updated

list of messages. I'll assign that to

answer, and then I will print answer out. So

let's now run this and see how we are doing. All

right, after a brief pause, we get what is definitely

a follow-up message that is definitely still

about quantum computing. And so it appears that we have correctly maintained

our entire conversation history. All

right, so this is looking pretty good. We now have three reusable

helper functions that we're going to continue to make use of throughout

the remainder of the course.

---

#### Lesson 7: Chat exercise

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289150](https://anthropic.skilljar.com/claude-with-google-vertex/289150)

**Video:** 03 - 005 - Chat Exercise.mp4 | **Duration:** 3m 54s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's go through a quick exercise just to make sure everything's

making sense so far. In this exercise, we're going to

be building a very small chatbot that is going to run out

of our Jupyter notebook. Here's how it's going to work. Whenever

we run a cell, we're going to prompt the user to enter

in some text using the built-in input function.

We're then going to take whatever the user enters and add it into

a list of messages. We'll then take the list of messages and

pass it off to the API through the use of our chat function

that we just put together. That's going to give us some feedback

from Claude, so some generated text. We're going to take

that generated text and add it into our list of messages. We'll

print that generated text and then we will loop and

go back to step one so that we repeat the entire process

all over again. I'm going to show you how this thing

is intended to work very quickly. So I've already put

a solution together. I've hidden it inside this cell,

and I'm going to run this cell again just so you can see how I intend

for this thing to work. So whenever I run the cell, I'm

going to immediately prompt the user for some inputs using

the built in input function. And I'll show you how to use that in just

a moment in case you're not familiar with it. Then I'm going

to enter in something like what's one plus one.

I should see my message printed right away, and then I should

make use of the chat function to get a response from Claude and

print that up as well. And then I should be prompted once

again to add in some more text. So now I could say something like

add to that answer. And

then I should see that I'm maintaining the history or the context

of my conversation. So I should now get a response back

that says taking the previous answer to and adding to it

should result in four. And again, this should go on

forever until I eventually interrupt the process

by clicking the interrupt button right here and hitting

escape. Now, as I mentioned, if

you're not familiar with the built-in input function, no problem.

I'm going to give you a little hint right now and just make sure that

it's really clear what we want to do. So I'm going to paste in a little bit of

code that you can use as a little template. All

right, so here's the general structure that we want to use.

We want to initialize a starting list

of messages that's going to start off entirely empty. And then we're going

to have a while true loop that is going to run forever. And

then inside the while loop, we're going to ask the user to enter

in some text, making use of the, again, built-in input

function. Whenever the user types into the displayed

input, we'll be assigned to this user input variable. And

then I put some comments in here just to guide you through the steps of what

we need to do. All right, so go ahead and

pause the video right here. I would encourage you to give this exercise

a shot. Otherwise, stick around and we'll go

over a solution right now. So let's get

to it. Let me show you how we could put this together. So

to implement the rest of this, we really just have to follow the different comments

that I put in here. The first thing we're going to do is take

that user input and add it into our list of messages using

the add user message function that we just put together

a moment to go. So I'm going to call add user

message. I'll pass in the list of messages and

my user input. Then

I'm going to call Claude using the built in chat function and

pass in my list of messages. That's going to give

me back some answer. I'm going to take

that answer and add it in as an assistant message

to my list of messages. So add assistant

message. like

so. And then I just need to print out the generated

text. And optionally, I can put in some delimiters

in the form of little dashes. Just make sure that it's clear

to whoever's using this application that it's being generated

by our AI. So I'll print a

dash, dash, dash. And

in between two of those, I'll print out my answer

that I got back. And that's it. So

now to test this out, I'm going to run the cell. And

then I should see some output up here underneath the cell after

I start chatting with Claude. So I'm going to ask Claude what's

one plus one. And I'll get my response

back and two more. And

I should see adding two more to one plus one should give us four.

All right, very good. So there is our very simple implementation

of a looping chatbot.

---

#### Lesson 8: System prompts

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289153](https://anthropic.skilljar.com/claude-with-google-vertex/289153)

**Video:** 03 - 006 - System Prompts.mp4 | **Duration:** 6m 20s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, we're going to take a look at how we can customize the tone and

style of response that Claude generates. To

help you understand why this is important, I want you to imagine

that we are making some kind of math tutor chatbot.

So a user will use this chatbot to ask for help in solving

math problems. For example, a user might ask for help

in solving 5x plus 2 equals 3. Now

there's a couple of things that we would want our math tutor to do

and a couple of things that we would definitely not want it to do. So

for example, we might want Claude to initially only give

the students some hints. Maybe just give them a little tip

or two in how they might initially approach the problem. And

then if the student still doesn't quite understand how to solve the

problem, only then maybe walk the student through

a solution step by step. We might

also want Claude to show solutions for a similar problem to

give the student a little bit of inspiration on how they might approach

this particular problem. Likewise, there are some

things that we would definitely not want Claude to do. For

example, we would not want Claude to just immediately respond

with a complete answer. And we would also not want Claude

to tell the student to just go use a calculator to solve

the problem or something like that. So to solve

this problem, we're going to use a technique known as system

prompting. System prompts are used to customize

the style and tone that Claude will respond with.

We define a system prompt as a plain string and then pass

it into the create function call. The first

line of a system prompt will usually assign Claude a role,

so we might directly tell Claude that they are a patient math

tutor. This will encourage Claude to respond in the same

way that a real math tutor was respond. He

would probably end up being patient, provide a lot of explanation,

but probably not directly answer a student's question.

They'll instead guide them to a solution. Now,

to see some action, let's go back over to our notebook and see how Claude

responds to math questions with and without a

system prompt. So back inside of my notebook,

I've made a new notebook and I've carried over just our

initial client creation and those three helper

functions. You do not have to create a new notebook. I'm

just letting you know that I did just to organize my code.

Then down here inside the next cell, I'm going to ask Claude a very

simple question. I'm going to ask it to solve a simple math problem.

And we'll see how it initially responds. It will probably just give us

a direct answer. And then we'll go back and add in a system

prompt to encourage it to give us a little bit more explanation,

kind of a tutor approach. So let's see how Claude

responds to us without a system message at all. I'm going

to make a list of messages. I'll add in a user

message to my list of messages. And I'm going to ask it to

solve 5x plus 3 equals 2 for x.

I'll then get an answer by calling chat with my list

of messages and print out the answer. And

then if I run the cell, I'm probably going to see an exact

step-by-step solution on how to solve this. Now

this probably is going to be useful for a student because it's going to

show them a step-by-step solution, but it's not quite

what we are going for. We want to make a student think, and

we want them to arrive at the solution on their own.

We just want to give them small steps and kind of guide them in the right direction.

So we're going to customize the way in which Claude responds

by using a system prompt. Let me show you how we do that. Up

inside my chat function, I'm going to make a new variable of system.

I'm going to assign to it a multi-line string. And

inside there, I'm going to put together a system prompt that I wrote

ahead of time. So I'm going to tell Claude that it is

a patient math tutor. It should not directly

answer student's questions. Instead, give them a little bit of guidance

on how to solve the problem. I'm going to make sure that I

pass in the system prompt as

the system keyword argument to the create function. I'm

then going to rerun the cell. I'll

then go back down and let's see how Claude responds

now. All right, this looks

like a much better answer. Rather than just directly telling

the student how it's solved the problem, Claude is now prompting the

user to go through a solution step by step. Claude

is asking the student to first maybe isolate x

on one side of the equation and then ask the student how

we might go about that. So now we've got a much more

interactive experience for the student. And this will help

them hopefully help them learn what's going on here a little bit

better than just giving them a direct answer.

Alright, so clearly using a system prompt is

a powerful tool for steering Claude in a particular

direction on how it should answer a given user input.

Before we move on, I want to do a little bit of a refactor to our

chat function. Rather than having a hard-coded system

prompt inside of here, I want to be able to specify a system

prompt whenever we call the chat function. So

in other words, I want to cut this right here, put

it down inside the cell underneath, And

then I want to be able to pass in a system prompt like

so. So now we have a much more reusable

chat function that we can use on a wide variety of different problems

in the future without having a hard-coded system prompt inside

of it. So now we need to make sure that we take this system

argument and pass it into the create function. Now,

doing so is going to require just a little bit more work than you might

think. Let me show you why. I'm going to very quickly add

in a system keyword argument to the chat function, and I'll

default it to be none. If I now run

the cell, and then run the cell down here, everything

is going to work fine, exactly as expected.

However, if I go down to the chat function and I decide

that I do not want to provide a system prompt here at all,

so if I delete that and then run the cell,

I'll end up getting an error message. So we are not allowed

to pass in a system prompt of none.

So we need to assemble our parameters. We're going to pass

into the create function a little bit more dynamically. And

if we have a system of none, we do not want

to include this parameter at all. So let me show you how

we are going to do that with a small refactor. First,

I'm going to make a parameter dictionary right above. I'm

going to cut and paste in model max

tokens and messages. I'm

going to convert this to dictionary syntax. So

I use double quote, double quote, colons,

like so. I'll

then check and see if a system prompt was passed in. So

if one was passed in, then I want to add it in

as the system key inside

of the params dictionary, like so. Then

I'm going to update the create call down here to

star star parameters. And that's

it. So now I'm going to rerun that cell. I'll

go back down to the next one. And if I call chat

without any system keyword argument being passed in, no

problem. Everything is going to work just fine. And

if I decide that I do want to provide a system prompt, yep,

that's going to work just fine as well. OK,

so this looks good. So we now got support for a system prompt

inside of our chat function.

---

#### Lesson 9: System prompts exercise

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289157](https://anthropic.skilljar.com/claude-with-google-vertex/289157)

**Video:** 03 - 007 - System Prompts Exercise.mp4 | **Duration:** 1m 25s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's go through a quick exercise on system

prompts. I've updated my notebook and I'm now asking

Claude to write out a Python function that is going to check a string

for duplicate characters. If I run this

and print out the answer, I'm going to see a tremendous

amount of code gets generated here. So some

of it is going to be a little bit of code, but there's also going to be a lot of explanation

and a lot of comments as well. So I would

like to go through an exercise here where we try to reduce

the amount of code that's being generated. I want to get

down to as concise an implementation of this function

as possible. To do so, I would like you to write out

a system prompt and pass it into the chat function call. Your

system prompt should assign a role to Claude and encourage

it to respond as concisely as possible. So

again, go ahead and pause the video here, go ahead and give it a shot,

and we'll go over solution right about now.

To solve this, I'm going to pass in a system prompt to

the chat function call. And inside that, I'm going to assign

a role to Claude that will encourage it to write very concise code.

I'll say you are a Python engineer who

writes very concise code. So

let's now run the cell and see what kind of response we get back

now. All right, that is definitely much more

in line with what I was looking for. You'll see that the actual

code we had to write to implement this uniqueness

check is very, very short, much shorter

than the code we saw a moment ago. Hopefully you had some

success with this exercise. And if you didn't, that is totally fine.

There are going to be many other exercises throughout the course where

you can test out your skills.

---

#### Lesson 10: Temperature

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289154](https://anthropic.skilljar.com/claude-with-google-vertex/289154)

**Video:** 03 - 008 - Temperature.mp4 | **Duration:** 6m 7s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Earlier on inside this course, we spoke very briefly

about how Claude actually generates text. Remember,

we feed some amount of text into Claude, like the

words, what do you think. Claude is then going to tokenize

this text or break it up into smaller chunks. Claude

is then going to go through a prediction phase where it decides

what possible words could come next and assign

a probability to each of those different options.

Finally, in the sampling phase, a token is

actually chosen based upon these probabilities. So

in this diagram I have on the screen, given inputs of

what do you think possible next tokens

might be about, wood, and

so on. Everything you see here on the right-hand side. Each

of these gets assigned a probability. And then maybe

in this case, Claude settles on about as

being the best possible next token. So

we would end up with a phrase, what do you think about?

This entire process is then repeated to complete

the sentence or complete the entire message. Now

just to make sure things are really clear, the numbers I'm

showing here are probabilities, the percentage

chance of each token being selected. And

just to make things a little bit more clear with these probabilities, I'm

going to display them in a chart for the rest of this

video. So still the same probability is just in a

format that's easier for us to understand. You

also notice I've kind of sorted them from left to right. There's

no actual internal sorting going on. I'm just sorting

them greatest to these probability just

to make this chart a little bit easier to understand. So

now that we have a reminder on how Claude generates text,

I want to show you one way that we can directly influence

these probabilities and control which

token Claude might actually decide to select.

So we can control these probabilities using a parameter

called temperature. Temperature is a decimal

value between 0 and 1 that we provide

when we make our model call. So whenever we call

that converse function, temperature is going

to influence the exact distribution of probabilities.

This is a little bit tricky to understand. So you can look at the plot

or these charts I've got right here. Or alternatively, I put

together a quick little demo with plot itself just

to give you a better idea of what's going on. So let me show you that demo.

Okay, so this is the same chart we were just looking at in that diagram

a moment ago. Whenever we provide a temperature

value going down to zero, as you'll see, I got

temperature right here, the highest probability

becomes more likely to occur. So

our highest probability was about, and it's going

to increase all the way up to 100%. So

at temperatures of zero, we start to get what we call a deterministic

output, where we always select the token that has the highest

initial probability. Then, as we start to increase

our temperature, it increases the chances of us selecting

a token that has a lower initial probability.

So we go from maybe having a 0% chance of

selecting we as the next vexed token,

although it to say 9%. So this is the theory

behind temperature, but what does this actually mean in the real

world? Well, we start to use different values of temperature,

given the actual task that we're trying to complete. These

are some example ranges and tasks that might fit

into each sample range. For something like, say,

data extraction, we really don't want a lot of randomness

or creativity. If we give Claude a big chunk

of text and ask it to extract very specific pieces

of information, no real creativity required

there whatsoever. We just want Claude to look at the exact

text we provided and pull out the most relevant information.

And then on the higher temperature side, this is where we start to get more

creative. And we start to see less common

tokens being used. We probably are

going to want to use higher temperatures anytime we are doing any

kind of really creative focus task, such as brainstorming,

writing, maybe doing some really creative marketing, or

something like a joke where a lot of jokes really depend

upon using words in ways that are not

always quite expected. Now that we understand what temperature

is all about, let's go back over to our notebook and understand how we can

adjust temperature on the fly. I would like to update our

chat function so that it takes in a temperature argument

that we're going to pass through to our create function call. So

inside of the list of arguments, I'm going to add in temperature

and I'm going to default my temperature to be 1.0. So

I want to fall on the more creative side of things. Then

I'm going to take in that argument and add it into the Params

object as temperature. And

that's all we have to do to add in support for adjusting

the temperature inside of our application. So now to

test this out, I'm going to rerun this cell. I'm

then going to go down to the next cell, and I'm going to ask

Claude to generate a one sentence

movie idea. And initially, I'm

going to provide a temperature of 0.0.

So now in theory, I should be getting back movie ideas

that always tend to be a little bit similar in nature.

So I'm going to run this. And

the first time, I'm going to get back a time-traveling archeologist.

You're going to see that this is a very common pattern, at

least for me. I very often, when I have a temperature of zero, get

movie ideas that are about a time-traveling something.

So if I run this again, I'm probably going to see another time-traveling

thing. Yep, same thing. Maybe one more time.

And yeah, same kind of idea, a jaded

time-traveling historian. Let's now try adjusting

our temperature a little bit to hopefully encourage Claude to give us some more

original or creative ideas. I'm going to try adjusting

my temperature up to 1.0. Now

if I run this again, I hopefully will not get an idea

about a jaded time traveler or something like that. And

almost immediately you can see that I do. So this is something

to be aware of. Just because you dial up the temperature

doesn't mean you're always going to get dramatically different ideas.

It just increases the chances of getting a different one. So

if I run this again, I might end up seeing out more creative idea.

Okay, that's definitely more creative. Nothing about time travel this

time and be one more test year. And

there we go, again, not about a time traveler or

anything like that. All right, so that is temperature.

Now remember, there's some general guidance here. Whenever

we are doing tasks that require less creativity, or whenever

we want to have a very deterministic output, we want to use

that lower temperature value. And whenever we have a

task that requires a little bit more creativity, that's when

we want to start to think about dialing up the temperature

a little bit.

---

#### Lesson 11: Course satisfaction survey

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/297285](https://anthropic.skilljar.com/claude-with-google-vertex/297285)

---

#### Lesson 12: Response streaming

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289162](https://anthropic.skilljar.com/claude-with-google-vertex/289162)

**Video:** 03 - 009 - Response Streaming.mp4 | **Duration:** 8m 23s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

I want to think back to the original chat interface example that we

looked at earlier on inside this section. So remember, the

thought process here is that we've got a chat window running inside of

a web app or a mobile app. A user is going to enter a question.

That's going to be submitted to our server. We're thinking of stuff that into

a user message and send it off to Claude. Claude is

then going to send us back an assistant message. We

are going to extract the text from it and send it back down to our

mobile app or web app. And hopefully, that content

is going to appear on the screen. Now, this all sounds

pretty straightforward and easy at this point in time, but

there's one little issue here that we haven't really addressed

just yet. You see, the time between sending

that user message to Claude and then eventually getting an assistant

message back can very easily take a lot more

time than we expect. In some cases, it might

take 10 seconds or all the way up to 30 seconds

depending upon the size of the input user message

and the output assistant message. Now during

this entire time that the user is waiting for a response, we

could just show a spinner on the screen. But that's

not really a great user experience. Most users'

expectations are that whenever they enter in some kind of initial

message, like what is quantum computing, they

should almost immediately start to see some response

up here on the screen. To get this better user

experience, we are going to use a technique known as streaming.

So let me tell you a little bit about how streaming works. Our

server is still going to send an initial user message off

to Claude, but then Claude is going to almost immediately

send back an initial response to us. This

initial response doesn't actually contain any text content.

Instead, it is really just a sign to our server that Claude

has received our initial request and that Claude is about

to start to generate some amount of text. We are then going

to start to receive a stream of events. We're going to

go into a lot of detail around exactly what these events

are, but right now, just understand that they contain

pieces of the generated response that we want to send

back and eventually display to our users. The number

of events that we receive depends upon how much text we are

generating. Each event is going to contain just a little

bit of the overall message that is being generated. So

maybe the first event just has the text, quantum, and

then the second one says computing, and the third one is, and

so on. Now each event doesn't just contain one

word. It might contain many words, or even in entire

sentence. It really just depends upon how much time

it takes for Claude to generate each little bit of text.

Now, as I mentioned, our server is going to receive these events

and our server can optionally take the text out of each

event and immediately send it back down to our web

app or mobile app or whatever else where we can display

that little chunk of text on the screen. We can then repeat

this process for each additional event that we

receive on our server. So the net effect is that a

user is going to start to see some text, start to appear

chunk by chunk in the chat interface. Let's

now go back over to our notebook and we're going to write out a little bit of code

to better understand how streaming works. All

right, so back inside of my notebook, I still have these three helper

functions put together. Now, we are going to ignore

the chat function inside of this video, because

when we start to use streaming, it doesn't work quite so well with

the chat function as we have implemented it. So

I'm going to instead, down here, make a list of messages,

and then manually call the clientmessages.create

function. So I'm going to make an empty list

of messages. I'll add in a user message

to messages. And I'm going to ask Claude to write

a one sentence description of a fake

database. I'm then going

to call client messages create.

I will pass in the name of the model. Still

need to provide a max tokens. Provide

our list of messages. And then finally,

we'll put in an additional keyword argument here of stream is

true. And this is going to give us back not

a final answer, but instead we're going to get a stream

of different events. We can iterate through this thing

because it is a normal iterator. So we can say for event

in stream and then print out event.

Now, if I run this, we're going to very quickly see a stream

of different events up here on screen. So each

of these represents a different little chunk of data that is

being sent back to us by Claude. You'll notice that

we start off with a event named raw message store

event. We then get a raw content block

start, a raw content block delta.

We get several of those as a matter of fact. And

then, down towards the bottom, we eventually get a content

block stop event, a message delt

event, any message stop event. So

these are all events that are being sent back to us inside

of the context of a single request, all coming from

Claude. Each of these different events has some meaning

in the context of the overall response that we are getting back from

Claude. However, there is one event type

that we usually care about a little bit more than all the others, and

that is the raw, content block Delta

event. This event is what contains the actual

text that is being generated by Claude and sent back

to us chunk by chunk. In practice,

we usually end up getting the same sequence of events over

and over. So when we get a response back from Claude, we're almost

always going to start off with getting a message start, then

a content block start, and then we are going to get a sequence

of content block deltas. And again, those are

what contain the actual text. So we usually want to

collect all those different events and extract the text from them

and send that text back down to our web app or mobile

app or whatever else we are using. Now, back inside

of our notebook, inside this for loop right here, we could

add in a check to take a look and figure out what

kind of event we are dealing with. And then if it is one

of those raw content block delta events, we could

reach into it and get the text we actually care about. But that

would require a lot of extra code from us. Thankfully,

the Anthropic SDK exposes a different

way of creating a stream than what I'm showing to you right

here. This alternative way of creating a stream,

which I'm going to show you in just one moment, makes it a lot easier

to just get the text out of the response. And again,

the text is usually the part of the response that we really

care about. So let me show you an alternative way of

streaming a response. I'm going to go down

to the next code cell. So down here, I'm

going to again make a list of messages, add

a user message with

a write a one sentence description

of a fake database. And

then we're going to call a slightly different function and wrap it

inside of a with block. So say with

client messages dot stream.

And inside of here, we will again put in our model, our

max tokens, and

our messages. But

we do not need to add in the stream to true argument.

We'll then say as stream, colon, all

then indent, and inside of here, it will say for textinstream.textstream,

like so. So now text is gonna be

just the text part of those different events. So just

the text we actually care about, again, that's almost always the

thing that we actually really care about when we are streaming our response

from Claude. Now to show you how this actually works,

I'm going to add in a print statement and log

out that text. I'm going to add in a end true

of empty string. And true of empty string, just make

sure that these print statements are not going to add in a new line

character to the end of the print statement. So we'll see each bit

of text logged out next to each other. Now

I'm going to run this and it's going to occur really quickly,

but you'll see that now we are getting a response streamed

back to us chunk by chunk. So let me do that again.

So run again. I'll see chunk, chunk, chunk. There

we go. You'll notice that each chunk contains multiple

different words. So again, we're not guaranteed to

just get back one single word inside of each event.

We might get several. There is one last feature here that

I want to show you. Now, as I've mentioned, we very

often want to stream a response back to a mobile app or

a web app so that a user can see each chunk

of text appear on the screen as soon as possible. But

something else we very often want to do after completing a stream

is take the entire message and maybe store it inside of a database.

So we have a record of the entire conversation that was had

with a particular user. Let me show you how we can collect

all these different events and present them all assembled

together inside of one single final message.

I'm going to replace this print statement right here with a

pass, just so we don't have any printing there. And

then after it, I'll do a stream.getfinalmessage.

And now if I run this again, we are still streaming back

a response and we could print it if we wanted to, but

we're also going to take all the individual events

we get back and assemble them together into one final

message, which we could then store inside the database or do

whatever else we need to do with it.

---

#### Lesson 13: Controlling model output

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289160](https://anthropic.skilljar.com/claude-with-google-vertex/289160)

**Video:** 03 - 010 - Controlling Model Output.mp4 | **Duration:** 6m 27s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Besides just changing our prompts we send into Claude,

there are two other ways we could strongly influence the output

that we get out of it. So in this video, we're going to discuss two

techniques. One is pre-filling assistant messages,

and second is stop sequences. Let's first

take a look at pre-filling assistant messages. Okay,

let's imagine that we send Claude some kind of really

tough to answer question. Something like is tea or

coffee better at breakfast? I have absolutely

no idea what kind of response Claude would give me. As

a matter of fact, let's go over to our Jupyter notebook really quickly

and see what kind of response we get in the first place. Back

inside of my notebook, I'm creating an empty list of messages.

I'm then going to add in a user message with text

of is tea or coffee better

at breakfast. I then feed in

the list of messages to our chat function, and then I'm going to

print out the answer that we get back. I'm going to

run this. Then, if we take a look at the response,

we'll see that Claude is not taking a strong stance one way

or the other. Instead, Claude is kind of taking a middle

road here and saying, some people like tea and some people like

coffee. Overall, this response is absolutely

okay, but there might be some scenarios where we want to direct

Claude's response in one direction or another. There

might be a scenario where we want to always direct Claude

to favoring tea, or another where we want to direct

it towards favoring coffee. So one way we could do this

is by pre-filling an assistant response.

With message pre-filling, we're still going to assemble a list of

messages. We're going to put our user prompt inside there, but

there's going to be one extra little difference. You

and I are going to manually put on an assistant message

at the very end, and you and I are going to author

the content inside of that assistant message.

And then in Claude, we can kind of imagine this

is what goes on behind the scenes. We can imagine

that Claude is going to see that first message and say

to itself, OK, the user wants to know what I think

about coffee versus tea. It is then going to take a

look at the second message, which is an

assistant message. And because it is an assistant

message, Claude is going to say to itself, oh, it

looks like I already have some thoughts on the situation.

So I better continue my final response.

I'm going to send back using this as a starter.

So Claude is going to essentially use this as the start

of its response. Because Claude

sees the sentence, coffee is better because that's

going to very strongly steer it in the direction of supporting

coffee as being better at breakfast. So

chances are, Claude is going to give us back a final assistant

message that says something like, it has higher

caffeine, which implies talking about coffee.

Now the one very important thing here to distinguish is that

whenever we put in this final assistant message right here, Claude

is going to assume that that is kind of content that has already

been authored, and it's going to continue its response

from the very end of this sentence. So

you would kind of expect Claude to give you back a full

response like this, where it says coffee is better because

it has a higher caffeine, that is not the case.

It's going to continue the response from the very end of

whatever you pre-filled with. So in other words, this

is not really a complete sentence. And if

you want to use this, you're probably going to have to go back and kind of stitch

together that text right there and that text right

there. Okay, this is

when you explain it, something that's kind of hard to understand. But in

practice, it ends up being really easy once you see a demo or

two. So let's just go right out some more code and see

how this actually works. So back over here, if you want to steer

a Claude in the direction of favoring coffee, right after

adding in the user message, we can then add in an assistant

message. Pass in our list of messages,

and we will then put in our pre-fill here. So I

might say something like, coffee is better because,

and that's all we have to do. We are now

adding in two distinct messages to our initial list of messages

and setting those off to Claude. Again, Claude is going to see

the assistant message and assume that it authored this content.

So the rest of the response we're going to get back is

going to be steered towards favoring coffee. Now

let's run this and see what kind of response we get back.

And there we go. So now Claude has distinctly taken the position

of favoring coffee over breakfast, and it justified

the earlier text that we wrote in. It justified

it by saying coffee gives you an energy boost to start the day.

If we wanted to change the direction of Claude towards favoring

tea, we could just change coffee to tea, like

so, rerun it, and now we'll get some justification

on why tea is better. Finally, we could

also steer a Claude towards totally different directions.

So we could change the assistant message to something like neither

is very good because, and now Claude

is going to try to justify neither tea nor coffee being

very good at breakfast. Now that we have seen message pre-filling,

let's take a look at the other topic for this video, which is stop

sequences. Stop sequences are going to force

Claude to stop generating a response as

soon as it generates some particular string that you provide.

So let's imagine that we provide a prompt of count from

1 to 10, and naturally our expectation would

be that we get back 1, 2, 3, 4, 5 all the way up to 10.

We could stop the generation early by providing

a stop sequence of the string 5.

Then internally, whenever Claude generates the string

5, it's going to immediately stop the response and

send whatever it has generated already back to

us. Again, let's take a look at a quick example

of this. Back inside of my notebook, I'm going to scroll up and

find our chat function implementation. I'm

going to add in an additional argument to this of stop sequences,

and I'll default it to be an empty list. I'm then

going to update my parameters dictionary to add

in that stop sequences argument. Then I'll

go down to the bottom of my notebook where I will add in a new code

cell. I'm going to again make an empty list

of messages. I'll add a user message to

the list and I'll ask Claude to count from 1

to 10. I'll then feed that

list into the chat function and

print out the answer. So let's run this, and as expected,

we'll probably get back one through 10. Now let's

try to cap the sequence at 5. In

other words, if Claude ever generates the character 5, I want

to immediately stop its response and generate no more text after

that. To do so, I could add in a stop sequences

list right here. Inside of it, I'll put a string containing

5. Then, if I run the cell, I

should see 1, 2, 3, 4, the comma and the space,

and then 5 was generated, but because I provided that as

a stop sequence, the entire generation is going to end right

there, and 5 is not going to be included. If

I wanted to clip off that extra space and comma

right there, I could add in to my stop sequence, comma

space 5, like so. And now if I run this again, I'll

get just 1, 2, 3, 4.

---

#### Lesson 14: Structured data

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289158](https://anthropic.skilljar.com/claude-with-google-vertex/289158)

**Video:** 03 - 011 - Structured Data.mp4 | **Duration:** 5m 59s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

stop sequences, and assistant message prefilling

can be combined together in a really powerful way.

Something that you're probably going to end up doing rather frequently, anytime

you need to generate some kind of structured data. So

to help you understand how these things work together, we'll me walk

you through a really quick example. Let's imagine that

we are building a web app like the one you see on the screen. This

is a web app that's going to generate event bridge

rules based upon some user input. If you're

not familiar with them, event bridge rules are used in AWS,

they're essentially little JSON snippets. So, user

is going to enter in some prompt like this and then click on generate.

In chances are, the user is going to want to see some generated

rule just up here that they can very easily

select right away or click on this little copy button

and go use somewhere else. The point there is

that part of the critical user experience here

is that we want to show just the JSON for the generated rule

and nothing else. So if we instead displayed

a response that looks like this, it would definitely not

be as helpful for our users. We're still generating

the rule, but now it also has this header up top and

this commentary footer down at the bottom. So now

a user can't really use this copy all button.

They would have to go in and manually select that JSON right

there. So this is an example where we really

don't want Claude to be that helpful and explains

work. We want just some very particular

data and nothing else. Now to be clear, this

is not a problem that is just limited to generating

JSON. It turns out that any time you are using Claude to

generate any kind of structured data. So it could be JSON,

or it could be Python, or even just a bulleted list

of text items. Claude is very often

going to try to insert a header or a footer or some

additional kind of commentary. And in many of these scenarios,

you don't want that additional commentary. You just want

the raw content that you asked Claude to create.

So to help keep Claude on track here and only give

us the raw content we're asking for and no additional

header or footer or commentary or anything like that,

we can use our stop sequence in combination

with a pre-filled assistant message. Let me show

you how. I'm going to go back over to my notebook.

I'm going to continue on by making a new cell down here. I'm

going to again make a list of messages. I'll

add in a user message. I'll

say something like generate a

very short event bridge rule

as JSON. I'll then pass that off

like so, and then let's just see what we get with this kind

of initial take. So right away, we can see that

we do get back some JSON, but it has unfortunately

that little back tick, back tick, back tick,

JSON right there, and then a matching closing one over

there. And just to make sure it's super clear, these

back ticks are in place to format this all as markdown.

So it gets formatted very nicely if you were to render it as

markdown text. But in our case, we don't want

any of those additional characters. We want just the raw JSON

by itself. So to do so, we

can do two things. We're going to use both an assistant message and

a stop sequence. For right now, we're just going to write out

the code to do so. And then I'll show you a diagram that explains how

it all works. First, I'm going to pre-fill an

assistant message. So let's say add assistant message.

And my pre-fill message will be backtick, backtick,

backtick, JSON. And then on

my chat call, I'll add in stop sequences.

And anytime we see a back

tick, back tick, back tick, I want to immediately stop

generation. So let's now run the cell

and see what we get back. Okay,

so now we get just the JSON by itself. You will

notice that there are some new line characters in here, but that's totally

fine. We can very easily remove those extra

new lines by just parsing the response as JSON

or by doing a strip call. So I could say

text is chat. I'll print out text and

then on the next cell down, I might import JSON

and do a JSON loads with

text and strip on

text as well. And if I run that, yes,

we definitely get back some very well-formatted JSON

here that we can access in any way that we expect. All

right, so what exactly is going on with the assistant message

and the stop sequence? Well, let me show you diagram just to break

it all down and make sure it is super clear. So

once again, we are doing our user message. We're providing

a pre-filled assistant and a stop sequence.

Claude is going to take a look at all the different parts of this request.

It's going to initially take a look at that user message content and say,

all right, it's very clear that I need to write a

full rule. And I should probably also describe it.

So maybe put on a header and a footer because that's kind

of what Claude naturally wants to do. It wants to explain

the work that is doing. But then it's going to encounter

that assistant message. And just as we learned in the last video,

Claude is going to assume that it already wrote that out in

its response. So it's going to say, oh, I've already

started the JSON part. So now all I have to do

is write out the actual JSON. It's

then going to write out all of this JSON

in the response. And then as it gets to the very

end, it's going to naturally want to close off

that markdown code block that it thought it created

earlier. So Claude is going to want to put in a closing

backtick, backtick, backtick. As soon as it does so,

however, it's going to encounter the stop sequence, which

stops the generation entirely and immediately sends us back

the response. So you can really imagine that what's

really going on here is we're kind of saying, start with this

and with that and just give us everything

in between. And that results in us just getting

back the part we really care about, just the JSON by

itself. And like I mentioned, this is a really

powerful technique that we're going to use very often. Anytime

we want to generate some kind of structured data and

get just that data with nothing else besides it.

And remember, this technique can be used for any kind of structured data.

It is not limited just being used on JSON.

So anytime we have any kind of very specific content we want to generate

and get just that content with no additional commentary

on it, we're going to take a look at using assistant message

prefilling along with stop sequences.

---

#### Lesson 15: Structured data exercise

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289152](https://anthropic.skilljar.com/claude-with-google-vertex/289152)

**Video:** 03 - 012 - Structured Data Exercise.mp4 | **Duration:** 4m 57s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's go through a very quick exercise just to make sure

the idea of stop sequences and message prefilling are

super clear. So in this exercise, I'd like you

to write out the exact code I've got right here on the screen. All

this code should be really familiar. If you take a look at the prompt,

it says generate three different sample AWS CLI

commands. Now, when you run this code, you're probably

going to get back some output that looks vaguely like this

right here. Just make it a little bit easier to read. I rendered

it as markdown down here. So here's the

sample starting output that I get. You'll

notice that it does give us three different sample commands, but

has a lot of commentary around them. So I've got a header

and then some numbers listing out each individual command.

For this exercise, I would like you to take

this code and using only message prefilling

and stop sequences, I want you to get all three

different commands in a single response, all

right next to each other without any additional comments

or explanation or anything like that. And

I'd like you to do this using only message prefilling

and stop sequences, so no adjusting this prompt

at all. So go ahead and give this a shot. I

did put a little hint on here, just as a reminder, with

message prefilling, it's not limited just using characters

like the backticks. You can put any

kind of prefill response you want. I would encourage

you to pause this video now and give this an exercise a

shot. Otherwise, I'll go over a solution

right away. So here we go. Here's how we're going to solve

this. To solve this, the first thing I recommend

you do is take a look at the output without any kind

of pre-filling or stop sequences or anything

like that. So if we take a look at what we have right

here, we'll notice that each of our three commands are wrapped

in a series of three backticks. So a good place

to get started would probably be to put in a pre-filled

message of three backticks to

kind of tell Claude, just go right into the command

writing right away and skip any initial commentary.

And then we might also decide to put in a stop sequence of three

backticks as well. Let's see how far that gets us. So

I'll put in an assistant message.

And I'll start everything off with three backticks. And

I'll put in a stop sequence of

closing three backticks. Let's run

this and see how far it gets us. My initial

output looks kind of reasonable, but it's not perfect just yet.

I do get three commands. There's one, two, and three.

But you'll notice that I also get the word bash added at

the very start. So where's that word coming from

exactly? Well, let me show you what Claude

is really trying to do here. We provided

the initial assistant message of those three

backticks. Whenever you put down three back ticks,

it's kind of indicating that you are writing out some markdown. And

when you are writing a markdown code block with back ticks,

you can optionally put in a language identifier right here.

If you choose to put one in, that whenever you render this as

markdown, the content inside of those back ticks,

we rendered using that language's syntax highlighting.

So in this case, Claude decided to put in bash right here

just to say, hey, we should use bash styles

syntax highlighting when we render this stuff out.

Now for us, we don't want that at all. So

one way we could address this would be to adjust

our pre-filled message right here and just include

bash ourselves. So that's now going to

make it super clear to Claude itself that, yes, you

are inside of a Markdown code block. And inside

this code block, you should be writing out bash formatted commands.

So let me try running this again and see how I do now. Okay,

so that looks better. Now I will tell you that from this

point, there are probably two additional errors that you might want to address.

The first is, sometimes you will get back a single command,

which is kind of an indication that Claude might want to write out three

separate markdown code blocks. The other problem that

you might run into, because we are now using a bash

code block, Claude might try to insert some

bash formatted comments in there as well. So it

might be something like, This

command does XYZ, and you

might see that repeated. And so we definitely

don't want those comments really just because that was one of the requirements

of this exercise. So to get rid

of those comments and to also make sure that we get

all three commands more reliably, we can use that

hint I gave you. Remember the hint was message

prefilling isn't just limited to designating

characters like backticks or stuff like that. We can also

use the message prefill to dramatically

guide Claude in how it's going to answer us.

So in this case, we could add in something like

Here are all three commands in

a single block without any

comments. And

then I'll put in a colon right there and then a new line,

just so it starts all the markdown stuff on the next line down. So

I'm gonna try running this and we should now get some

much more reliable output. Okay,

that looks good. And of course I can keep running all

day and we're probably gonna see exactly the result

we want. Okay, this looks good.

---

#### Lesson 16: Quiz on accessing Claude with the API

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289281](https://anthropic.skilljar.com/claude-with-google-vertex/289281)

---

### Prompt evaluation

#### Lesson 17: Prompt evaluation

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289159](https://anthropic.skilljar.com/claude-with-google-vertex/289159)

**Video:** 04 - 001 - Prompt Evaluation.mp4 | **Duration:** 1m 48s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that we understand how to access Claude, we're going to shift

our focus a little bit and look at two new topics,

prompt engineering and prompt evaluation. These

two topics are all about making sure that we are writing

prompts that will get us the best possible output from Claude.

Prompt Engineering is a series of techniques that we will use any

time that we want to write or edit a prompt.

These techniques will aid Claude in understanding what

we're asking of it and how we want it to respond. Prompt

evaluation, on the other hand, is where we do some automated

testing of a prompt with a goal of getting

some kind of objective metric that tells us

if our prompt is effective or not.

In this section, we're going to be mostly focused on prompt evaluation.

After we understand how to measure the effectiveness of a prompt,

we'll then take a look at some prompt engineering techniques.

So let's get to it. The first thing I want to do is help you understand

where prompt evaluation fits in to the prompt writing

process in general. Whenever you first write a prompt,

you generally have three different paths ahead of you. Three different

ways you can go from there. With option number one, you might

take that prompt you put together, maybe test it once or

twice and decide it is good enough to use in production.

With option number two, you might test the prompt a couple of times

with your own custom inputs, and maybe tweak

it a little bit to handle a corner case or two that you've noticed.

Right away, I want you to understand that options, number one

and number two, are kind of traps that all engineers

fall into, myself included. It happens

to everybody. We all start writing out prompts that

are going to eventually be used in serious applications, and

we don't really test them enough to make sure that they are working as expected.

So whenever you write a prompt, I highly recommend going with option

number three. Run your prompt through an evaluation

pipeline to get an objective score that will tell you

how well your prompt is performing. You

can then try to iterate on your prompt a little bit and make

sure that it's performing as well as it possibly can.

---

#### Lesson 18: A typical eval workflow

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289161](https://anthropic.skilljar.com/claude-with-google-vertex/289161)

**Video:** 04 - 002 - A Typical Eval Workflow.mp4 | **Duration:** 4m 36s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, we're going to walk through all these steps implemented

by a typical prompt evaluation workflow. Before

we go through any of these steps, however, I just want you to understand two

important things. First is, there are many different

ways you can assemble a workflow. There's no one

set methodology set in stone that is standard across

0000:00:16,957 --> 00:00:19,481
the industry. The second thing to understand is that

there are many different open source packages and even paid

options online that will help you implement your own

workflows. Now, in this video

and this module, we're going to start to implement our own custom

workflow from scratch inside of a Jupyter notebook.

The reason we're doing this is to, of course, just help you understand

how these workflows behave, but also to help you understand

that you don't have to get a really heavy weight solution

to do prompt evals. You can start small just

to get started and get a sense of how everything works and

then scale up from there. All right, so let's get

to it. Step one of a typical prompt

eval. Step one, we're going to write out an initial

prompt draft. So you and I will sit down

and just write out some kind of prompt that we want to improve

in some way. For this example, we're going

to have a very simple prompt that just says, please

answer the user's question. And then we're going to interpolate

in some user input. So some question provided

by a user. In step two,

we're going to create an evaluation data set. This

data set is going to contain some number of possible

inputs that we might want to put into our prompt.

So for us, our prompt only has one input, a

question provided by user. So for our

eval data set, we'll have a list of different possible

questions that we might want to put into our prompt. My

data set is only going to have three different questions inside of it.

But in real-world evals, you might have tens, hundreds,

even thousands of different records in your data set. Now

you can assemble these data sets by hand, or

you can of course also use Claude to generate them for

you. Once we have our eval dataset,

we're then going to feed each of these different questions into

our prompt. So we get a fully fleshed out prompt

that we can then feed into Claude. So we might have

prompt one right here, where we have, please answer the

user's question, and then a sample question out of our dataset,

like what's two plus two? And then we

will repeat for all the other records inside of our dataset.

So yours two and three. We'll

then feed each of these into Claude and get an actual

response out of Claude. So for the first one, we might get back

a response of something like 2 plus 2 is 4, and

then something about how to make oatmeal, and then something about

the distance to the moon. Once we

have these actual answers coming out of Claude, we're

then going to grade them in some way. During

this grading step, we're going to take each of the questions out

of our data set, and the answers we got out of Claude.

We'll pair them all off together, and we'll feed them into a grader

one by one. There are many different ways we can implement

this grader. We'll take a look at some of the different methodologies a little

bit later. The grader will then give us a score,

maybe from 1 up to 10, based upon the

quality of the answer that was produced by Claude. So

a 10 would mean we got a perfect answer and there's really no

possible way we could improve it. And maybe something like a 4

indicates that there's definitely room for improvement there.

Now, as you can guess, there's kind of a lot of hidden complexity

here with a grader, because you're probably curious or wondering,

well, how do we actually get these scores at all? And

again, don't worry. We're going to cover these grader things in

much greater detail in a little bit. After

we get these scores, we're then going to average them all together.

So in this case, I would add the scores together, divide

by three, and get an average score of 7.66. So

I now have some kind of objective way of

describing how well our original prompt performed.

Now that we have this score, we can then change

our prompt in some way and iterate or repeat

this entire process. So if I want to improve

my score, I might try adding in a little bit more detail to the

prompt to hopefully guide Claude a little bit more

and help to understand what kind of output we want. So maybe

I would add on to the end of the prompt, something like answer

the question with ample detail. Once

I have the second version of my prompt, I would then

run it through this entire pipeline again.

I would then have a score for prompt version one

and prompt version two. I could then compare these two

scores and whichever score is greater or higher.

It's kind of an objective sign, better than

nothing that tells me that prompt V2 in this

case is perhaps the better version of our prompt.

So now that we have a high-level overview of this entire

process, as I mentioned, we're gonna start to implement

our own custom eval framework inside of

a Jupyter notebook. So let's get started on an implementation

in the next video.

---

#### Lesson 19: Generating test datasets

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289163](https://anthropic.skilljar.com/claude-with-google-vertex/289163)

**Video:** 04 - 003 - Generating Test Datasets.mp4 | **Duration:** 4m 44s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's get started on building our own custom

prompt evaluation workflow. We're going to be writing

out a prompt and then writing out some code to evaluate how

well it performs. So let's first focus on making

a prompt. The goal of our prompt is to

help users in writing out some code specific

for AWS use cases. So we're

going to allow user to enter in some kind of task that they

need help with. And then we're going to respond with

one of three types of output. We're either going

to output Python, JSON configuration,

or a raw, just plain regular expression.

Those are our three possible outputs.

So we need to make sure that whenever a user asks for us to

complete some kind of task, we give them some output

in one of these three particular outputs without

any other kind of explanation, or header, or footer,

or anything like that. So that's the overall

goal. Now, the first step of our goal is,

of course, to write out a draft prompt. Now, I've kind of already

done that for us on the right-hand side here. I've got V1 of our prompt,

where it just says, please provide a solution to the following task,

and we'll put the user's task in there. Step two

is to assemble a data set. Remember

that a data set is going to contain some number of inputs

that we're going to feed into our prompt, and then we're going to run

our prompt for every combination of prompt and input.

For our particular case, we're going to have an array of JSON

objects, where every object has a task property.

These tasks are going to describe something that we want

to be done by Claude, so we're going to take each of these tasks,

put them into our prompt, and then feed the result into Claude.

Remember that when we make a data set, we can either assemble

it by hand, or we can generate it automatically with

Claude. Now, as a side note, if you're using Claude

for something like this, this would be a really good opportunity

to use a faster model like Haiku. And

that's what we're going to be doing here. Let's go back on to Jupyter,

we're going to open up our notebook, and we're going to write out a little

bit of code that's going to generate a sample data set, like

the one you see on the left-hand side, using Haiku. Back

over here, I've created a new notebook, it has a lot of the same

code that we've been working on throughout the course. So I'm creating a client

inside the top cell and also loading some environment variables, and

I create those same three helper functions that we've been developing.

Then, a little bit lower, I've defined a function called generate

data set. And inside of here, I've put together a rather large

prompt to get us started. Now, I've taken this

notebook and attached it to this lecture. So I would encourage

you to download this notebook and copy the

prompt right here, or just use this notebook directly to save

yourself a whole bunch of typing. This prompt is

going to ask Claude to go ahead and generate some different

test cases for us. Our test cases are going to

be represented by an array of JSON objects, and

each object is going to have a task property that describes the task

to be done. For right now, I'm just asking Claude to

generate three such objects. This is enough

to definitely get us started and make sure that we can actually create a

data set. So now let's add in some code to

this generate dataset function that we are in. It

will actually take this prompt, send off to Claude, get

back a list of tasks, and then parse them as

JSON. To parse the JSON, we're going to

make sure that we use that same prefilling and stop

sequence method. We spoke about a little bit ago. So

let's get to it. Down here inside of the

function, so I'm going to make sure that I do indent in, I

will declare a list of messages. I'll

add a user message, of

that prompt, I'll then add in an assistant

message, and

I'm going to put in backtick, backtick, backtick,

JSON. I'll then call it chat

with our listed messages and some stop sequences.

In this case, our only stop sequence is going to be backtick, backtick,

backtick. And then finally, I will return

JSON.loads, text. OK,

so I'm going to run the cell to make sure that function gets defined,

and we'll test it out down here really quickly. And

then let's print up that data set just to make sure that

we are getting back some realistic looking data. Okay,

there we go. So there's our three different test cases. We

are getting a case in which we are going to get a Python function, write

some JSON configuration, and then write a regular

expression. So let's say this is a good start. Next,

I would like to take this data set and write it into a file. So

we can very easily load it up later on when we start to

evaluate our prompt to do so. We

will open up a file in my right mode. I'm going to

call the file dataset.json. And

then json.dump with

an indent of two. So I'm going to run

this again. After that cell runs inside

the same directory as my notebook, I should find a dataset.json

file and inside there should be our list of tasks.

Okay, this is a good start. We've got our eval

dataset put together.

---

#### Lesson 20: Running the eval

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289166](https://anthropic.skilljar.com/claude-with-google-vertex/289166)

**Video:** 04 - 004 - Running the Eval.mp4 | **Duration:** 6m 42s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

With our data set generation complete, we

now need to take every record in that data set, which we're

going to refer to as a test case. So we're going to take

each test case and merge it with the prompt. We're

then going to take the result and feed it into Claude. And

then once we have all these different outputs, we're going to feed them

through our grader. Remember, we have not discussed

graders just yet. Don't worry, that's going to come up very

quickly. And once again, just to save a little bit of

time, I've written out a little bit of code here just

to help guide this next phase of our

workflow. I put together three separate functions

with a very clear comment on what each one does. The

first one that's easiest to understand is the run prompt

function. This is going to be called with a test case.

And those JSON objects we generated just

a moment ago, each of these is a test case. So

you can imagine that each of these one by one are

going to flow into the run prompt function. So

inside of here, our goal is to merge that task

that we generated with our prompt, generate

some text with Claude, and then return the result. So

let's do that right away. I'm going to

put in my V1 prompt

right here, which

is very simple. Remember, we are starting off as simple as possible

here. So it'll just say something like, please

solve the following task.

And I want this to be a F string and I'm

going to put in test case task.

Next up, we want to send this off to Claude. So I'll make a list

of messages. I'll add in a user message.

I'm then going to pass this off to Claude by calling chat.

And we're going to get back some resulting text, some result,

or maybe we'll call it output this time around. And then for right now,

I'll just return the output. Now remember,

we don't have any kind of formatting included or any

formatting instructions inside the prompt right now. So we're

going to probably get back a lot more output than we

ever asked for. The real goal of our prompt

is to make sure that we get just Python or JSON

or that regular expression. And we don't have anything for

that right now. So we'll almost definitely have to come back and make

some improvements. But for right now, we at least have

a start to run prompt. The

next thing we're going to work on is run test case.

The goal of this function is to take in one of those individual

cases, call the run prompt function

we just put together, get some output from Claude, and then grade

the result and return a dictionary describing

the and everything that happened there. Now

that sounds really complicated, but in reality, it's

going to be surprisingly simple. So let me show you all we have to do

here. We're going to put in output

that's going to come from calling the function that we were just working

on a moment ago. So this run prompt function. Put

in our test case and then we're going to do some grading

right here that's going to be a to do.

Right now, I'll just say that we have a hard coded score of 10. So

we definitely have to come back and do a lot of heavy

lifting right there. And then at the bottom, we're just going to

return some information that summarizes everything about running

this test case. So I'll return a dictionary with

some output. Give me whatever got back from Claude.

I'll include the test case. And

then our score. And

then one final step here, we have to implement RunEval.

So this function is going to load up our data set or

receive it as an argument, either one is fine. And then

we're going to loop through that data set. And for every test case, we

will call run test case and then just assemble

all the results together. So

for our implementation here, I'll say results.

It's going to start off as an empty list. And

for every test case in data

set, I'm going to get our

result. from

calling run test case

and pass in the test case to it. And

then add that into our list of results. And

then down here, I'm just going to print up all

of our results. Actually, let's actually just go ahead and return

results. That's a little bit better. Okay,

so there's the outline for our three major functions.

Now believe it or not, this is like a vast majority

of what a Eval pipeline is. We just put together the

vast majority with the obvious exception of grading. So

as you can see, there's not a whole lot of code that goes into this.

Let's now test this out. So

down here in the next cell down, I'm going to go into open

up our data set JSON file. And

parse it as JSON. And

then call the runEval function.

That's the one that we were just putting together right here with

the entire data set. Finally,

I'm going to assign the result to that to results.

I'm going to rerun all the cells above, just to make sure

that I executed all of them, and then I'm going to run

the cell. We'll see what happens. And just so you know,

the first time you run this, it is going to take a pretty good amount

of time, even if you are using high-coup. It's

going to end up taking me about 31 seconds to complete

this with high-coup. I'm going to show you some techniques for

speeding up our Eval run time, but for right now, we're just

going to have it take a little bit longer, but don't worry, we will speed it up.

So now let's take a look at results and see what we have. Results

is going to be a rather large JSON object. So I'm going to print

it out really nicely with a print, JSON

dumps, with results,

and an indent of two. There

we go. So now we get an array of objects. Every

object represents the output from one of our

individual test cases. I've got the output

right here. That's the output coming from Claude. And we can see there

is a lot of stuff generated here. And

if I scroll down a little bit, I'll see

the definition of the test case that this was based upon. And

then the score, which again right now is just hard coded at

10. And then that's just going to repeat over and

over again. All right, so at this point in time, we

have successfully gone through this step

right here. We merged together our data

set with our test prompt and we got some output

from Claude and we kind of collated all this stuff together.

So now the last thing we really have to do here is take

the input and the result that we got out of Claude

and feed it into one of these different graders. So

this finally is the time where we're going to start to learn

about graders. We're going to start to discuss them in the

next video.

---

#### Lesson 21: Model based grading

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289168](https://anthropic.skilljar.com/claude-with-google-vertex/289168)

**Video:** 04 - 005 - Model Based Grading.mp4 | **Duration:** 10m 1s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next thing we're going to implement inside of our prompt evaluation

workflow is a grading system. As a

reminder, a grader is going to take in some output coming

from our model. And then our hope is that the grader

is going to give us some kind of objective signal. It might

be a number or a true or false value. It could

be really anything, but very commonly, very frequently,

you're going to see a number output between 1 and

10. where 10 means that we got a very high quality

output, and one means we got a very low quality output.

Again, that's not a requirement. We don't have to get numbers

out of these graders, but it's a very common practice

that you're going to see very often. There's three

different kinds of graders that we're going to discuss in this video.

Code, model, and human. Let's first

figure out what code-based graders are all about.

With a code-based grader, we're going to take the output from our model

and feed it into a snippet of code that you and I author. Inside

this code, we can do just about any kind of programmatic

check you can imagine. So we might verify to

make sure that the output from the model was not too long

or too short. We might make sure that the output does

have or doesn't have certain words. If we are returning

JSON or code, we can do syntax validation

programmatically, and we can even do more complex

checks like implement a readability score, where

we make sure that the generated text is at an

appropriate reading level for our particular use

case. The only requirement here is that when

we run this code, we return some kind of actual

signal we can use. And again, usually that's going to be a number

between 1 and 10, but that is not a hard requirement.

The next kind of grader that you're going to see very often is

a model-based grader. This is where we take the

output from our original model call, so the one that we

already made, and we feed it into an additional

model. So this is another API request. When

we use a model grader, we get a tremendous amount of

flexibility. We can ask a model to evaluate a response

based upon its general quality, maybe how well it

followed prompt instructions, maybe the completeness

of the response, really just about anything you can imagine. Once

again, the only real requirement here is that the model gives us

back some kind of hard objective signal, usually

as a number between one and 10. And then finally,

human-based grading. With human-based grading,

we're going to take all the outputs from our model and then put them in front

of an actual person. This person is

then going to be in charge of evaluating these responses in

some particular way. As you can imagine, humans are very

flexible, so we can ask them to evaluate responses in just

about any fashion or for any metric you can possibly imagine.

The one big downside to human-based grading is that it generally

does take a lot of time, and it's certainly very tedious

work. Now, no matter what style of grading you are using,

you need to decide upfront what your evaluation

criteria is going to be. So in other words, exactly

what aspects of these responses are you going to

be focusing on? For our particular use case,

I've centered on three different evaluation criteria.

I think first off, we should evaluate the responses

to make sure that we're only getting back Python, JSON,

or regular expression without any additional explanation

being provided by Claude. Secondly,

whenever we get that Python JSON or regex, we

should make sure that it has some valid syntax so that

there should be no typos in there or anything like that. And

then finally, we should probably do some general task following

and make sure that the model clearly addressed

the user's task and answered it with some generally

accurate code that doesn't contain any major errors

or logic mistakes. So for these three

different evaluation criteria, I think we can evaluate

the first two with a code grader. So

we can evaluate the format and make sure we got actual

Python JSON or regex with code. And

we can also validate the syntax of that

code using well, additional code. And

then finally, the general response and making

sure that the user's question was clearly addressed,

that would be more appropriate to address through a model grader

given its flexibility. All right,

let's start to implement first the model grader

because that's believe it or not can be the easiest one to put

together. I'm going to first begin by going back

over to my notebook. I'm

going to find that to-do. We had put together right here inside of our

run test case function. And then

right above that cell, I'm going to add a new cell with

a function that I'm going to call grade_by_

model. And I'm going to assume that I'm going to pass

in my test_case dictionary.

Remember, the test_case dictionary is essentially these

objects right here. Each of these dataset values,

these are our test cases. I'm

also going to pass in the output from our original model

call. And then inside

of here, we're going to essentially make a call off

to a model and ask it to grade the output. So

for this, we usually end up writing a fairly long prompt.

And again, just to save us a little bit of time, I'm going to copy paste

a prompt in. So here we go. I'm

going to paste this in. And yes, it

is a little bit long, but this is kind of the bare minimum of

what we want. So this prompt is

going to set a role. It's then going to ask

very clearly for the model to evaluate a

AI generated solution. We're

then going to print out the task. We're

then going to list out the solution that was generated

by the model. And then we're going to provide

some directions on exactly how to respond. In

this particular case, I'm asking the model to give me a list of

strengths and weaknesses of the AI generated

solution, along with some reasoning behind that and

an actual score. Now we could just ask

for a score by itself, but if you do so, you're

gonna see very often you tend to get scores of just six.

So if you don't ask for any additional strengths or weaknesses

or reasoning, you're gonna very often just get very middling

scores because the model kind of assumes, well, could

be better, could be worse, we'll give it a six. By

asking the model to provide some reasoning, strengths and weaknesses,

you really make it hone in and decide upon a more concrete

score. So now that

we have that prompt in here, I'm going to call

our additional grading model. So

right underneath it, I'll again make a messages list.

I'll add in a user message. And

then because we are getting back some JSON here, we

need to once again, make sure we extract that cleanly by

using a pre-filled assistant message and a stop

sequence. So we'll add an assistant

message. with `json`

JSON, and

then I'll get back some eval_text, and

we'll call chat_with_messages and a stop

sequence or stop_sequences of, once

again, closing `json`. Now

this eval_text should be a JSON object

with this kind of structure right here. So I'm going to

parse that and just return it. So return

a json.loads with

eval_text.

Okay, so that is our model grader. That's really

all it takes to at least get started. So now

we need to make sure we actually call this grader to

call the grader. I'll go down to our to-do right here.

I'm going to replace score with model_grade.

And that's going to be coming from our grade_by_

model function. And remember, we have to pass in the

test_case, along with the output from

actually running the prompt. And

then from this, we're going to get a score from

model_grade. And

I'm also going to extract from that dictionary that gets returned the

reasoning behind the score. Inside

of this model_grade dictionary that we are returning,

there is also going to be the strengths and weaknesses

list. You could definitely extract those as well as you want, but

I'm just going to keep our example a little bit more concise. I'm

going to take the score and reasoning and put them into this

final output dictionary. So

I will add in some additional keys here of

score. Oh, I already have score right there. My mistake.

I don't need that, but I do need reasoning.

And that

will be reasoning. Okay,

so that looks good. I'm not going to make sure I run

these cells. I'm going to run that one, update

run_test_case. And

then I'm going to rerun my

actual evaluation. That is going to take

a while to complete. For me, it takes about 22 seconds

this time around. And now if I print out

those results, let's see what we get. So

I've now got the generated output here. And if I scroll down a

little bit, I can take a look at the score

that was generated by the model and some reasoning behind

that score. So in this case, I got an eight. That's

not bad. And that's why I got the eight. And

if I keep going down, the next one got a seven. And

then finally, I got a six. So the last thing

we would probably want to do here is take all these scores,

add them together, get an average, and print that out.

So we get a final, very objective score to tell

us how well our prompt is currently functioning.

So to average all these scores out and print

the results, I'm going to find the run_eval function

right here. And I will calculate the average

score with a comprehension

of result['score'] for

result in results. And I'm going to wrap that

with a mean function call. And

then I will import the mean function from

the statistics package. One

last step. Let's make sure we actually print out that average score. We'll

do a print("Average score: " + str(average_score)) like so. All right,

now I'm going to run this code just one more time to make sure everything

is working as expected. And

after it runs, I see that I do get, in fact, an average score

of 7.33. And once again, this gives

us finally an actual objective metric. Yeah,

it's being graded by a model that might be a little bit capricious sometimes.

And maybe we could give a better guidance on how to grade things, but at least

we have a score that we can start to focus on and try to

increase.

---

#### Lesson 22: Code based grading

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289167](https://anthropic.skilljar.com/claude-with-google-vertex/289167)

**Video:** 04 - 006 - Code Based Grading.mp4 | **Duration:** 7m 26s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Next up, we need to implement our code grader. So

our code grader is going to take in some output from the model and make

sure that we get back just plain Python,

JSON, or regular expression without any kind of explanation.

In addition, we should also make sure that we have valid

syntax for whatever type of code we actually got. You

might be kind of curious, how are we going to validate

the syntax of, say, Python at all? Well,

we use a little trick for this. We're going to define

three helper functions, one will be called Validate

JSON, another Validate Python, and another

Validate Reg X. Then inside of each of those,

we're going to take whatever output we got from the model and try to

either parse it as JSON, we'll try

to parse it as a Python abstract syntax

tree or AST, or we'll try to compile

it as a regular expression. And for each

of these, if we successfully parse or load or

whatever else, we'll return a full score of 10.

Otherwise, if we get an error during this parsing operation,

we'll assume that we completely failed the syntax check and return

a zero. There is one other thing to be

aware of here. In order to know which of these different

validators or these kind of grading functions to run, we

need our test case data set to include the

expected format that we're going to get back for each output.

So in other words, back here inside of our data set,

On our first task, for me, at least, I was expecting

to get back a Python function and then JSON and

then a reg X. So we need to update our data set

to include something like a format key that will say,

hey, this output should probably be Python. This

one should be JSON and this one a

reg X. Now, of course, I could just edit this file manually,

but instead, we will update our prompt that is generating

our data set so that we can eventually generate really large

data sets for testing purposes. Now, total

to do all this stuff, couple of different steps we have to go

through. So just to help you understand the code side

of it and keep everything in line, I came up with this quick

checklist of items that we're going to go through. So our first

item, adding functions to validate JSON, Python,

and regular expressions. For this, I'm going to flip back

over to my notebook. I'm going to find the run

test case cell. I'm going to add a new cell right

above it. And then inside there, I'm going to add those three

functions you just saw inside that diagram. Once

again, to save a little bit of time, I'm going to paste them in here. You

can always copy the completed code out of the finished

version of this notebook. So at the top of the cell,

I'm importing these two helper modules. I've then got the

three different validator functions we just saw. And

then at the bottom, I have kind of a general

purpose function to figure out which these different validators to

use. So I've got grade syntax right here. That's

going to take a look at the test case. It's

going to look at the format in particular. So we need to make sure

our test cases have that format property that I just

mentioned a moment ago. And then depending upon that, we're going to

call the appropriate format function. Okay,

that is step one. Now step two, we

need to update our data set to make sure we include that format

key. So for that, we'll scroll up

a little bit and

find our data set.

Here it is right here. So

generate data set and I'm going to add onto

the example output. On task, I'm

gonna add a comma at the very end and I'll add in a format

key And inside of here, we'll say simply

JSON or Python or

RegX. That's really all we have to do. So

now if I rerun that cell and

rerun the cell underneath it that actually generates the data

set, there

we go. Now we'll go back over to my data set file.

And I'll see, yes, I did, in fact, get the format inside there.

And it looks like it matches up with the task perfectly. So

the first task is create a JSON configuration, got

JSON, write Python, got Python, and

then write a regular expression, and I got regx.

OK, on to step number three. Now

this, we're going to update our draft prompt template,

just to make sure that it's really clear that we only want JSON

Python or regular expression. Because right now, our draft

prompt just kind of says, yeah, try to solve the task. So

inevitably, we're going to get back some non JSON

or non Python content and we'll always be failing

the actual validation check. So we're just going to give our

prompt a little help here, give it some work that we know

that it needs. So for step three,

will go back down to our run prompt, which is where

our draft prompt is. And

I'm going to update the prompt just a little bit. I'm going to

add in some notes, and I'll ask it to respond

only with Python, JSON,

or a plain regX. And

do not add any comments,

or commentary, or

explanation. Next

up, I'm going to make sure that we get back just

that raw content that we really care about. And once again, to do

so, we'll use a prefilled assistant message

along with a stop sequence. So

I'll add in a assistant message

right here. In

my assistant message, in this case, I can put in three

backticks, and then usually, as we saw previously,

we might put in something like JSON or

Bash or Python right here. But

in this particular case, we don't really know ahead of

time the exact format that we expect to get back.

We don't know if we're going to get back Python or JSON or RegX.

So one little cheat code here, one little work

around, we could just put in code and that kind of

pre-fills the assistant message and tells Claude, hey,

you're going to put some code inside of here without us having

to specifically say this is going to be Python or JSON

or reg X. I'm then going to add on

the closing stop sequence with

backticks like so. Lastly, we need to actually

merge the scores from our model grader and the code

grader together. So for that back

over here, I'm going to scroll down once again, and

we will find our run

test case function. So this is where we are running our

model grader right underneath it. I'm going to put together

the syntax grader per code grader,

whichever you want to call it. So I'll say my syntax score

is grade syntax.

We need to pass in the output. and

our test case. And then finally,

we're going to merge the syntax score together with the model

score. I'm going to first rename score right

here to model score, just to be clear. And

I'm going to take the average of these two scores. So

I'll say score is going to be model

score plus syntax score divided

by two. And that should be

it. So that's all it took to add in a little bit of code

grading. So last thing to do is test this

all out. To do so, we'll go down just a little

bit here. So right underneath the runeval function

is where we actually call runeval and

calculate our overall average score. So I'm going to rerun

this and remember it usually takes a decent number of seconds

to complete. And after a short pause, I

get a final score of 8.166. So now

the question is, is this good or not? Well,

the real answer to that is that we just don't know. The

only way we're going to know is if we now try to change our

prompt in somebody and hopefully get a better score. So

let's try out an exercise in the next video where we will

try to change our prompt a little bit and hopefully improve

our score.

---

#### Lesson 23: Exercise on prompt evals

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289164](https://anthropic.skilljar.com/claude-with-google-vertex/289164)

**Video:** 06 - 007 - Exercise on Prompt Evals.mp4 | **Duration:** 4m 44s | **Platform:** jwplayer | **Captions:** English, French, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's try out an exercise to improve our prompt

evaluation workflow. So here's the task

I'm going to give you. I want to improve our model

greater a little bit by providing it with more context

on what a good solution should actually look like.

Now, at first glance, that might sound a little bit challenging, but it turns

out you only really have to go through two steps to add

in this additional context. So in step one,

I would encourage you to go back to the prompt where we generate

our data set. And inside that prompt, try asking

it for some solution criteria to be included

in every test case. So ideally,

our test cases that could output should now have

some additional solution criteria key, which

might look like what you see right here. So it might say something

about what a good solution would look like. Maybe you say, well,

a good solution would include this characteristic and this characteristic

and this characteristic. Once we have this additional

solution criteria, we can then insert that into

our grade by model prompt. So

you might find the existing area of that prompt where

we put in our solution to evaluate, and then

right after it, you might add in that newly generated

solution criteria. And that's all it

would really take to give our model greater a little

bit better idea of what a good solution would actually look

like. As usual, I would encourage you to pause

the video right now and give this exercise a shot.

Otherwise, we're going to go through a solution right now. So

the solution really is just going to be these two separate steps.

Should be pretty straightforward. To get started, back

inside my notebook, I'm going to find our generate dataset

function. And inside there, I'll find the really big prompt

we put in. And then when we ask for each

of these different test cases, I'm going to say in addition to a

task in the output format, I also want to

get some solution criteria.

And then I'll put in a string right here just to give our model

an indication of what this key should actually be. So

I'm going to ask for some key criteria for

evaluating the solution. And

that's pretty much it. So I'm going to rerun

the cell. I'm going to go to the cell underneath

it and regenerate the data

set. Okay,

just a couple of seconds, it should be done. There we go. So

now we should have an updated data set.json

file. I'm gonna open that file up. And I should now see

some updated tasks in here, still with the format, but

now I've also got some solution criteria. So

the solution criteria, we can read over, of course

yours is gonna look different than mine, but it's gonna get

going to give some idea on, again, what a good

solution will actually look like. Next up is

step number two. We're going to find our grade by model

function and specifically the prompt inside there.

And we're going to include this newly generated solution

criteria. Again, just to tell the model grader

what a good solution looks like. So for that, I

will go back to the notebook. I will scroll down and

find that grade by model function. Here

it is right here. So I'm going to find the prompt. We

are already putting in the original task, the

output that was generated. And then right after that, I'm going

to put in some note to the model and just say, here's

some criteria that you should use to evaluate the solution.

So criteria you should

use to evaluate the solution.

I'm going to put in some tags. And I'll tell

you why we are adding in these tags very shortly as

we start to discuss prompt engineering.

And then I'm going to interpolate in from the test case,

our solution criteria. And

that key right there, remember our test case is really these

objects, each of these objects one by one. So we know

because we see it right here inside this file, there is a key inside

that dictionary of solution criteria. So

we're taking that sentence right there and putting it

right here. All right, so

now time to run the cell. And

we're going to rerun our pipeline and see how everything

is working. So I'll go down to

the run eval function. And then right after that is where

we actually execute everything. So I'm going to run that.

And then we get our updated score back. Now, I

want to print out the results really quickly, just so we can

see how this is going to affect the actual output.

So we'll do another print of JSON, dumps,

results with an indent of two. So

now we can see the output from our model, so

that's the actual produced output. Here's our test

case, so we can take a look at the task in the solution criteria.

Here's the score, in this case it was 9, and now hopefully

our reasoning section, which is produced by the model grater,

is going to be a little bit more fleshed out than it was before

because we are including that solution criteria.

---

#### Lesson 24: Quiz on prompt evaluation

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289279](https://anthropic.skilljar.com/claude-with-google-vertex/289279)

---

### Prompt engineering techniques

#### Lesson 25: Prompt engineering

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289169](https://anthropic.skilljar.com/claude-with-google-vertex/289169)

**Video:** 05 - 001 - Prompt Engineering.mp4 | **Duration:** 10m 50s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that we've got a handle on prompt evaluation, we're

going to move on to the world of prompt engineering. Remember, prompt

engineering is all about taking a prompt we've written and improving

it in some way to get more reliable outputs and higher

quality outputs. To understand prompt engineering,

we're going to go through a series of videos in this module, and

I want to very quickly help you understand how the module is set up.

In this video and the next, we're going to write out an initial

prompt. And then in the coming videos, we're going to

try to improve it step by step by implementing

new prompt engineering techniques on that original

prompt. So in short, in this video, we're going to set

a goal. So something we want our prompt to do, we're

then going to write an initial version of that

prompt. So kind of like a really poor first attempt.

We will then eval the prompt, and then we're going to

see right away we get a very poor evaluation

score. And then as I mentioned in the coming videos,

we're going to learn about and apply some different prompt engineering

techniques. And as we apply each of these, we're going

to run our evaluation again and see

that we are getting better performance with every single improvement

we make. Now to run these evals, we're

going to use that same kind of eval pipeline that

we put together in the previous module. Just

one little twist here, something you really need to be aware of if

you want to follow along and code with me. I

took our original eval pipeline that we put together

in the last module, and I made a couple of different

improvements to it to make sure that it can work with just

about any prompt, as opposed to the very specific

prompt we were working on previously. So

to get this updated notebook that has this more flexible

evaluation pipeline, make sure you download

the accompanying notebook named 001

underscore prompting. Before you open up that notebook,

however, I want to very quickly tell you about the goal of our prompt.

So this initial prompt that we're going to write and exactly what

it is intended to do. All right, so we're

gonna make a prompt that's going to hopefully generate a

one-day meal plan for an athlete based

upon their height, weight, some kind of physical

goal that they might have, and any dietary restrictions

they might have. So you can imagine

that we are going to take in some kind of sample input that

describes an athlete. Maybe there are height, weight, goal,

and dietary restrictions. We're then going to interpolate

all those inputs into our prompt. And then

we're going to send that off to our model. And hopefully we'll

get back some kind of output, like what you see on the right-hand

side. This is what we're really going for. This is our ideal

output. In the first version of our prompt, we're

going to get some output that looks nothing like what you

see here on the right-hand side, but through a variety of different

prompt-engineering techniques, we're going to eventually refine the prompt

and eventually hopefully get something that looks almost exactly

like this. All right, so now that

we understand our goal, let's open up that

new notebook. So remember, 001 prompting. I

can give you a very quick tour of it because there are a couple of

things have changed compared to the last module. And just make

sure everything inside there is super clear. We'll then

use the notebook to generate our initial data set.

All right, so I've opened up that notebook. Right away, you'll

notice there are a couple of collapsed cells at the top. So

this is a lot of different setup code. Just make sure you execute

those cells at least one time. So I can do so right

away. Next up, you'll see

that I'm creating an instance of something called a prompt evaluator.

Prompt evaluator is a class I created that wraps

up all the data set generation, all the model grading,

just about everything is wrapped up inside of this class.

The class takes one argument, max concurrent

tasks. So this class supports concurrency.

We can make multiple API calls at the same time.

The upside to this is that it's going to dramatically speed up our

eval process and the data set generation process as

well. But I do need you to be aware that

depending upon your service quota, you

may or may not very quickly start to run into some rate

limit errors. So if you see any rate limit

errors at all, as you go through this module, I would highly

encourage you to change this value right here all the way

down to the default of one. which means no

concurrency at all. For me personally, I

have super high rate limits. So I'm going to dial

this all the way up to a concurrency of 50. Chances

are you are not going to be able to use 50. So don't

try 50. I would really recommend maybe starting off at three.

And then if you see any rate limit errors, start to go down to two

or one. Again, I'm going to use 50

just so you can see some immediate feedback on my screen as

I run all these different steps. I'm

going to make sure I run that cell. And then let's

get started on generating our actual data set. So

to generate the data set, I've added this new generate data set

method for us. To use this method, we're going to

describe the overall purpose of our prompt.

So kind of what our prompt is supposed to do. For

you and I, we're trying to work on a prompt that is going to

write a compact, concise,

one day meal plan for

a single athlete. And

then inside of this prompt input spec, we're gonna have a dictionary

that's gonna list out all the different inputs that our

prompt requires. As we saw just a moment ago,

our prompt is gonna require a height, a weight, a

goal, and some dietary restrictions. So

these are some extra properties that are gonna be generated

as a part of the data set. And eventually we're gonna take them, test

case by test case, and interpolate them into our prompt.

So I'm gonna fill out all four of these different properties. My

height is going to be the height in CM

and just be clear I'll put in athlete's height.

And I'm going to duplicate that because it's going to be just about the same. We're going to do

our weight in kilograms. My

goal is going to be the goal of the athlete

and my restrictions will

be a dietary restrictions

of the athlete. And

the last input for you to be aware of is number of test cases

to generate. I would really recommend that you just leave

this at three because it's going to allow you to get through this module

way faster because the evals are going to run much more

quickly. Just remember, as I mentioned many

times whenever we do an eval in reality, we want to have

a really solid, really large number of test

cases. So I'm going to dial mine personally

way up. I do not recommend you do this. I recommend

you leave it at like two or three, just

to make sure all your evals run very quickly. But

again, I'm going to dial mine all the way up to 50. Once

I put this all together, I'm going to run the cell and that's going to generate

my data set. Once I have generated

my data set, I can open up the data set.json

file, which should be created in the same directory. And we're

going to see all these different individual data sets have been generated.

So they have a pretty similar structure to what we were doing on

our previous module when we were talking about prompt evals. I'm

going to go back over to my notebook and then scroll down

a little bit to the run prompt function.

This is where we are going to write out our prompt and then eventually

improve it over time. This function gets called

one time for every test case that you generated. Whenever

this function is called, it's going to receive your test cases

prompt inputs as its only argument. So

in other words, prompt inputs right there is going to be that

dictionary. And then that function is going to be called again, and

it will be that dictionary, and then again, and it will

be that dictionary and so on. So we're going to

take this dictionary and we're going to interpolate

those inputs into this prompt that we're going to write out right

here. Let's immediately write out a first

version of our prompt. And it's going to be very simple,

very naive. We're going to get a very bad eval score,

but it will at least get us started. So I'm going

to write in my initial starting frontier and I'm going

to use a very bad prompt. I'll say, what

should this person eat? And

then I'm going to list out their height. their

weight, their goal, and

dietary restrictions. And

then for each of these, I'm going to interpolate in a value from

prompt inputs. So the first one will be the height.

And I'm going to copy paste that just

to save a little bit of time and update the keys on each

one. So make sure you have first height and then we

want the weight and then our goal and

then restrictions. All

right, once we have our starter prompt in here, I'm

going to run that cell. And then let's do

our eval. So we can run our eval down here

at the very bottom. Now, before we run our eval,

I want you to know that this function that's going to actually kick off the evaluation

process, it takes in one additional keyword argument

that I'm not showing here. It's called extra criteria.

It's going to be a string. This string is going to be used during the model

grading process. This extra criteria thing

just allows you and I as developers to put in some

extra criteria that the model should consider whenever

it's doing some grading. So I'm going to say specifically

to make sure that the output should

include a daily

caloric total, a

macro nutrient

breakdown, and meals with

exact foods, portions, and timing.

Again, this is just going to add in a little bit of extra

validation or a little bit of extra grading criteria. All

right, so now let's run our evaluation for the

first version of our prompt and see how we're doing.

All right, we get a absolutely terrible

score. I get a 2.32. Now,

just so you know, you are probably going to end up getting a much

better score than I get. The reason I have a

very bad score here is that I'm using a model,

an older model, that is not super smart. So

it's going to tend to give me really bad output unless

I'm very specific in how I prompt it. I

am using this very bad model just so you can see

the increase in score over time as

we go throughout this module and add in all these different

prompt engineering techniques. So again, you

are probably going to get a better score. That's totally fine. Now,

before we move on, there's one last thing I want to mention really

quickly. Whenever you run any valuation, a

file will be created in the same directory as your notebook

called output.html. If you

open up that file inside of your browser with a simple

drag and drop, you're going to see a really nicely formatted

report that gives you output on every single test case that

was executed along with the score, the reasoning, solution

criteria, and so on. And you can also see the actual

output too. So I'm going to use this little dashboard

quite a bit in order to take a look at the output of the eval

and understand how I actually need to improve my prompt.

All right, I apologize for the long video here, but now

hopefully you have an idea of some of the setup

that we're doing inside of this module. So now all we really

have to do, as you can see, we have really bad score

right now. All we have to do is start to improve our prompt. So

let's start to take a look at our first prompt engineering technique

in the next video.

---

#### Lesson 26: Being clear and direct

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289170](https://anthropic.skilljar.com/claude-with-google-vertex/289170)

**Video:** 05 - 002 - Being Clear and Direct.mp4 | **Duration:** 2m 5s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

With a starting grade of 2.32, we

can definitely only go up. So with that in mind, let's take

a look at our first prompt engineering technique that we're going to use

to improve our prompt. Alright,

so we're going to be discussing the idea of being clear and

direct. These two rules are really talking

about the very first line of your prompt. The first line

of your prompt tends to be the most important. In that first

line, you want to use simple and direct language,

telling Claude, with a kind of action verb, exactly

what its task is. So for example, we

might want to have a first line of a prompt be something like write

three paragraphs about how solar panels work.

That tells Claude that it's going to have a job and use to write

or generate or create something. It also clarifies

a little bit of information about the expected output and

exactly what that output should contain. So

we're really setting an action and providing a

task in that very first line. Another

great example would be identify three countries that use geothermal

energy and for each include generation stats.

Again, we are telling Claude to do something or give it an

immediate task and a little bit of information about the

expected output. Let's take this idea of

being clear and direct in the very first line of our prompt and

see if we can't use it to improve the outcomes of our prompt

that we're currently working on. Using that rule that

we just learned, I might update this line to say something like,

generate a one day meal plan,

for an athlete that

meets their dietary restrictions.

So again, I'm being direct by making use of an action

verb at the very start, and then in very simple language,

I'm providing a direct task for Claude to fulfill.

Now let's rerun the cell to get our updated

prompt and then rerun the Eval itself. And

see if this does anything to improve our score. And I bet as

you can guess, yeah, we're probably going to do a little bit

better than we did previously. So I think before

I had a 2.32, now I'm up to a 3.92.

Definitely an improvement, but

still not great. So let's move on to the next video

and take a look at our next prompt engineering topic in

order to improve our prompt a little bit more.

---

#### Lesson 27: Being specific

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289165](https://anthropic.skilljar.com/claude-with-google-vertex/289165)

**Video:** 05 - 003 - Being Specific.mp4 | **Duration:** 5m 14s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next topic we're going to discuss in the world of prompt engineering is

the idea of being specific. To be specific,

we want our prompts to list out some sort of guidelines

or steps to somehow direct our model in a particular

direction. For example, consider the prompt to

have on the left-hand side of the screen. In this prompt, I'm

asking Claude to write out a short story about a character

who discovers a hidden talent. If I just put that

prompt by itself into Claude, Claude can go

in any of an infinite number of directions.

It can decide to vary the story length significantly.

It can decide to add in extra elements or remove elements

from the story. It might have just one character, it might introduce

five different characters. If I want to ensure that

I'm going to get a particular kind of output, I might

decide to put in a list of guidelines, as you see on

the right-hand side. These guidelines will provide some

high-level guidance or kind of direct Claude in

a specific way when it starts generating the response. So

for example, I might decide to add in some guidelines of

keeping the story under a thousand words, add in some

rising actions, and including at least one supporting

character. Now I've provided a little bit of guidance

to direct Claude towards writing a particular kind

of short story. Now there are

two kinds of guidelines you're going to see very often in prompts.

Type A on the left hand side is kind of like what I just showed you

in the previous diagram. You might decide to put in a

list of guidelines and those are going to list out some qualities

that you want your output to have. So you might try

to control maybe the length of the output or the structure

of the output or maybe list out some different attributes

that the output should have. On the right

hand side, the second type of guidelines that we can provide are

to provide some actual steps that the model should follow, with

the intent of making the model think about specific

things or choose between different directions that

would hopefully increase the quality of our output. So

for example, we might instruct Claude to maybe first

brainstorm three special talents that would be really

interesting and then pick the most interesting one.

We might then ask Claude to try to outline or think

about some kind of interesting scene that would reveal that talent,

and then think about different kinds of supporting characters that

could make the story a little bit more interesting. So

on the left hand side, we're really guiding attributes in

the output. On the right hand side, we're trying to be

a little bit more specific in how Claude arrives at

the final product. You can absolutely,

and you're gonna see this very often in professional prompts, you'll

absolutely, very often see these two techniques mixed together.

So you might have a list of guidelines that intend to control

some attributes of the output, and then a list of steps

that the model should follow as well. Both of these

are examples of being specific in your prompting.

So now we've seen some idea around what it means to be

specific. Let's go back over to our prompt in progress

and see if we can incorporate this idea of being specific.

All right, so back over here, I'm taking a look at my run prompt

function. Now, just to save a little bit of time, I'm going

to first paste in a list of guidelines. So

this is kind of like that first type of being specific,

where I include a list of attributes that I really want

to see inside of the output. I'm

going to run that cell and

then go down and run the eval again. And

let's see what we get here. So after a quick

pause, I'm going to get back a final score of 7.86.

That is an incredible improvement

over our previous 3.92, just

by adding in a little bit of guidance and telling

Claude precisely what things we want to see inside

of the output. Now I'm going to try to put in a little

variant of this where I use that second variation

of being specific. So I'm going to provide some

steps that Claude should follow when deciding exactly

how to build up this meal plan. So now in this scenario,

I'm telling Claude to first do a calculation and

then think about this and then do a little bit of planning. You

kind of get the idea. I'm providing some steps that Claude should

go through. I'm going to run this cell again. And

then run down here, and I'm going to remember that score of 7.86, that

is really, really high, might be a little bit of a

statistical anomaly. And

now we get 7.3. So still a dramatic improvement,

but not quite as good as listing out some

attributes that we would want to see inside the output. So for me, I'm

going to revert and go back to listing

out some guidelines. So when would you want to use

one technique versus the other? Well, I would generally

recommend almost always listing out qualities

that the output should have as I'm showing on the left hand side on

just about any prompt you ever work on. And you will usually

want to provide steps that the model should follow, as shown

on the right-hand side, any time you're asking Claude to work

on a more complex problem, where you want to kind of force

Claude to consider a wider view or some extra

topics beyond what it naturally might want to consider.

For example, consider the prompt on the right-hand side of the screen, where

I ask Claude to figure out why a sales team's numbers

have dropped in the last quarter. In this scenario, we

might want to force Claude to consider some extra

viewpoints or extra pieces of data that it might not otherwise

immediately consider. All right, so now that we've got a better

idea of what it really means to be specific and this

idea of adding guidelines or steps as the situation

warrants, let's take another break right here and then move

on to our next prompt engineering topic in just a moment.

---

#### Lesson 28: Structure with XML tags

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289171](https://anthropic.skilljar.com/claude-with-google-vertex/289171)

**Video:** 05 - 004 - Structure with XML Tags.mp4 | **Duration:** 4m 0s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next topic we are going to examine is the idea of

providing structure in your prompt by using XML tags.

Now, let me give you a little bit of backstory on this. Very

often, whenever we write out a prompt, we're going to interpolate some

amount of content into it. And we've been doing that already. Inside

of our example, we have been interpolating some heights, weight, goal,

and restrictions. Now each of these values are rather

small, but it's entirely possible that we might

eventually write a prompt where we need to put in a lot of

content into a prompt. For example, examine

the prompt on the right-hand side. We might decide to paste

in 20 pages of sales records and

try to get Claude to analyze them in some way.

Whenever we dump a lot of content into a prompt, it

can be a little bit challenging for Claude to figure out exactly

what text really means what or

how text is actually grouped together. One way that

we can make the structure of our prompt a little bit more obvious is

by wrapping different pieces of content in XML

tags. So for example, I might provide a little

bit more structure to this prompt on the right by wrapping

the sales records right here with an XML

tag of sales records. Like

so. Now, there is no

official XML tag called specifically sales

records. This is a name of a tag that I just

made up that will probably give Claude a little bit of insight

into the nature of the content that exists inside these

tags. I could have just as well called this records,

or perhaps even data. But of course,

being a little bit more specific here is definitely

better. So providing a tag of something like sales records

would probably get us the best output. Now

I want to make sure it's really clear why XML tags like

this are necessary. So let me show you a little exaggerated

example. In the prompt on the left hand side, I have

a leading line of debug my code below using

the provided documentation. So this kind of implies

two things. It implies that underneath this

header statement right here, I have some amount of code that

was written by me, that is buggy, and some amount

of documentation as well. And if you

just look at the code that's listed out here, it's absolutely

not very clear what content is the code and

what content is the actual documentation. One way that

we could clarify this to Claude would be to wrap each

chunk of code with appropriate XML tags. For

example, on the right-hand side, I might wrap my code with

some XML tags that simply say my code

being very direct and obvious, and then the code

that represents some amount of documentation in a docstag,

again, being very clear and obvious. Now

it is much easier for Claude to understand what code

it is trying to debug and which code provides some

source of documentation. Let's take this idea

of providing structure via XML tags and try

to use it to improve our prompt that we are working on back inside of

our notebook. Now, unfortunately in this particular

scenario, we don't really have a big blob

of content that we really need to delineate in any way.

All of our interpolated content like the height, weight,

goal, and restrictions are sufficiently short that Claude

is probably not going to be confused by them in any way. Regardless,

we can still use some XML tags to make it really clear that

this is some kind of external input or maybe

some information about the athlete that should be considered

when generating the meal plan. So we might decide

to wrap this entire block right here with some XML tags

that just make it really clear that this is information

about the athlete. So I might put in tags like

athlete information. and

then a closing tag on the other side. Now

let's try to measure and see whether or not this has any kind of impact

on the quality of output. So I'm going to rerun the

cell, I'll go down to my eval cell and

run this one. And then you might recall that before adding

in those XML tags, I had a score of 7.3.

So let's see if we go up or down. And I

end up going up quite a bit. Now, you

probably not going to see an improvement quite this large. As

a reminder, I'm using a little bit more simple and basic

model just so I get some exaggerated returns

in these improvements to the prompt. So if you do not see

quite a big a jump in quality, that is totally fine.

---

#### Lesson 29: Providing examples

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289177](https://anthropic.skilljar.com/claude-with-google-vertex/289177)

**Video:** 05 - 005 - Providing Examples.mp4 | **Duration:** 6m 44s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

I'm really excited about this next prompt engineering technique

we're going to discuss because it is probably one of the most effective

that you're going to find. It's the idea of providing examples

inside of your prompt. This is often referred to

as one-shot or multi-shot prompting,

depending upon whether or not you are providing just one example or multiple

examples. Understanding this concept is definitely easiest

if you take a look and example, so let's do that right away.

Consider the prompt on the right-hand side. I'm asking Claude to

categorize the sentiment of a tweet.

Just be clear, when we say sentiment, we mean kind of, does

this seem kind of happy or positive in nature

or unhappy or negative? In this

particular instance, I provided an input

tweet of, yeah, sure, that was the best

movie I've ever seen since Plan 9 for Matterspace.

Now if you're not aware, Plan 9 from Adder Space is

a famously bad movie. So if someone

were to tweet something like this, they're actually probably being

sarcastic and they probably did not like the

movie they just watched at all. So we would probably want to

classify the suite as being negative. But

Claude could potentially have some issue categorizing this. One

way to solve the problem would be by using multi-shot prompting.

So here's how we would fix this. We would take our

starting prompt we have on the left-hand side and add in some

examples, which I've added in on the bottom half of the

prompt right here. To add in an example,

we will very directly tell Claude that we are about

to give it some example input and an ideal,

perfect world kind of response. We'll almost

always wrap these inputs and outputs inside of some XML

tags, just to better structure our prompt and make it super

clear to Claude with the purpose of the input and output

R. So in this particular example, I have

given a sample input of great game

tonight, which I would say is definitely positive in nature.

So right after that, I would then put in an ideal output of

simply positive. This gives Claude a

concrete objective example of how to deal

with some kind of input. So now Claude knows that

if it ever sees some kind of input like this again in the

future, well, it should probably label it as positive

because that's how it was done in the past. We

can make use of multi-shot prompting, that's where

we provide multiple different examples whenever

we want to handle corner cases. And dealing with sarcastic

tweets like this is definitely a corner case that we kind

of want to highlight to Claude. When adding

examples that highlight corner cases, add in some

context to Claude, until it should be especially

aware of certain scenarios. So for example,

we might say, be especially careful with tweets that contain

some sarcasm, and then provide an immediate

example of that. So now, in this case, I've got

a example tweet or a sample input of, oh

yeah, I really need a flight delayed tonight, excellent.

If you didn't understand the concept of sarcasm, this would seem

like a positive sentiment tweet. But of course,

we can probably understand that this is sarcasm and so it

probably is actually negative. Once again, Claude

can take a look at this example when grading our

provided input up here, the original input, and

Claude will have a better chance of recognizing that, oh

yeah, this looks like it's sarcasm too, this is also

probably negative in nature. Now,

multi-shot prompting like this can be used not only

for capturing corner cases or giving a little bit more clarity

to Claude, but also helping Claude understand

more complex output formats. So if

you ever need to generate a JSON object that is rather

complex in nature, you might provide a sample

input and an example output and show

that kind of complex JSON structure to Claude.

and now it will have a better idea of the exact structure

of output that it is going for. Providing examples

is especially effective whenever you are doing prompt

evals as we currently are. Remember whenever

you run a prompt eval using our little framework inside

the notebook, it creates an HTML file inside the same directory.

So we can hunt through this file until we find a perfect

10, or hopefully just a test case

with a rather high score. If I scroll through, I

will find a 10 right here. Now, you

might not have any tens inside of your output. If you don't,

that's totally fine. Just try to find the record with the highest score.

So this is an example of where we had some input and

output that was gauged to be pretty much as

good as we're going to get by our model greater. So

we might decide to provide this as an example inside of

our prompt. And hopefully, that will guide Claude to

producing output that looks like this a little bit more often.

Let's try this out. I'm going to copy this input

right here. Go back over to my prompt.

I'm going to scroll underneath the guideline section. And

I'm going to explicitly tell Claude that I'm about to provide

it an example that's going to contain a sample input

and an ideal output. So I'll say here is

a or an example with

a sample input and an ideal

output. I'll then put in my sample input

inside of XML tags. and

a ideal output. And

inside those tags, I'm going to go back over and copy

paste the output from right here. I'll

then paste it in like so and

fix some indentation. Before

we rerun our eval, there's one last thing I want to show you.

This last step is completely optional, but I personally have

had great success with it. It's often very

beneficial to help Claude understand exactly why

this is ideal output. If we go back over to

our report, remember we have this last column over here

that explains exactly why the greater thought that

this was some ideal output. So we can copy

just the kind of first half of some message over here where

it says or lists out why this is a good response.

Take that back over, and then underneath the closing

ideal output tag, we could paste in that

reasoning. And then maybe update the grammar just a little bit

to say, this example meal plan

is well structured, blah, blah. So now Claude has a better idea

of exactly why this is considered to be ideal

output. And it's going to better reinforce the idea

that Claude needs to return a well structured output

that contains some detailed information on the food choices

and quantities, and most importantly, matches

the athlete's goals and restrictions. Okay,

so let's now run that cell and

then rerun our eval and see how we are doing. So

I'm going to rerun this and are we going to go

up or down. We end up going

up just a little bit to 7.96. Well,

let's wrap things up. As a reminder, this technique is

often referred to as one shot or multi-shot prompting.

One shot is where you provide a single example, multi-shot

is where you provide multiple examples. And this

is a technique you're going to very often use anytime

you want to make sure Claude handles corner cases, or

especially when you want Claude to make sure it matches

some kind of complex output format.

---

#### Lesson 30: Exercise on prompting

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289173](https://anthropic.skilljar.com/claude-with-google-vertex/289173)

**Video:** 05 - 006 - Exercise on Prompting.mp4 | **Duration:** 5m 22s | **Platform:** jwplayer

---

#### Lesson 31: Quiz on prompt engineering techniques

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289278](https://anthropic.skilljar.com/claude-with-google-vertex/289278)

---

### Tool use with Claude

#### Lesson 32: Introducing tool use

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289172](https://anthropic.skilljar.com/claude-with-google-vertex/289172)

**Video:** 06 - 001 - Introducing Tool Use.mp4 | **Duration:** 2m 54s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this module, we are going to discuss tool use.

Tools allow Claude to access information from the outside

world. Now, understanding tool use can be a little bit

challenging, so in this video, I'm going to give you a really

soft introduction. We are going to walk through the entire

flow of tool use and understand what it's all about. I

want to first begin by giving you an example of where Claude

can, unfortunately, sometimes hit its

limits. Remember, by default, Claude

only has access to information that was actually trained on.

So in general, it doesn't really have any information about very

recent current events. As an example

of this, if we had a user making use of our chatbot, ask

a question of something like, what's the weather in San Francisco,

California right now? And so if that off to Claude, we

would probably get a response back of something like, I'm

sorry, but I don't have access to up to date weather

information like that. To fix this and give the user

a better response, we can make use of tools.

Let me show you a diagram that's going to break down tools with really

simple terminology. And I'll show you another one that's

going to give you an example of how we would solve this specific

weather problem. OK, so here's the entire

flow that we're going to eventually implement when we start to make

use of tools. We're going to send off an initial

request to Claude. We're going to ask a question or maybe

give Claude a task. And along with that, we're going to

include instructions on how Claude can get some extra

data from the outside world. Claude

will then take a look at whatever question it was asked or whatever

task it was given, and it might decide that it needs to

ask for some extra data. So it'll send a response

back to us where it asks for some extra data, and it's going

to give us some details on exactly what information it

needs. Then on our server, we

are going to run a little bit of code that will go in, get

the information that Claude asked for, and then respond

with that on a follow-up request back to Claude.

Now Claude has all the information it needs in theory

to give us a response. So it will generate a final

response that will be hopefully augmented or

improved by that extra data. Now

I'm going to show you the same exact flow, but I'm going to customize

each of these little steps for this scenario where a user

asks us for some current weather in a particular location.

So here's what happened. We would send an initial query

off to Claude, and it would include a prompt where the user asks

about the weather. And inside of that initial request,

we're going to include details on specifically how

to retrieve current weather data. Claude

would take a look at the prompt and decide, hey, to answer this

question, I need to get some current weather data. It

send response back to us, where we would then run some

code that would reach out to some maybe third party

weather API and actually get some live

details on what the current weather is for a particular

location. Once we have those details

from that outside API, we would then make a follow-up

request to Claude with that current weather data. And

now, Claude has all the information it needs. It has

the original prompt along with the up-to-date

weather data so it can generate a final response and

send it back to us.

---

#### Lesson 33: Project overview

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289175](https://anthropic.skilljar.com/claude-with-google-vertex/289175)

**Video:** 06 - 002 - Project Overview.mp4 | **Duration:** 2m 23s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

To learn more about tools, we are going to set ourselves

a little goal. This is going to be a small project that

we implement inside of a Jupyter notebook. We are going

to try to teach Claude how to set reminders

that occur at some point in time in the future. This

is going to require us to implement several different tools.

And right now, we're just going to focus on one tool at a time,

but just know that we're going to eventually have to deal with multiple

tools. So I want to eventually be able to send

a message to Claude of something like, set a reminder

for my doctor's appointment, it's a week from Thursday.

And I want Claude to respond to something like, okay,

I will remind you at that point in time. When

you first look at this task, you might think it seems really easy,

but it turns out that there are actually several different challenges

that we're going to need to tackle, and we're going to solve all of them

through the use of tools. So in particular,

Claude does know the current date. In other words,

if you open up a prompt right now, you could ask it what the current date is

and it will give you an exactly correct answer.

However, Claude doesn't always know the exact time

of day. So if we were to ask Claude to do something like

set a reminder for 24 hours from now

and expecting it to be exactly

24 hours, Claude doesn't really know what

24 hours from now actually is because it doesn't

know the current time. Secondly, Claude

does not always perfectly handle time-based addition.

So if I were to ask it, what is 379 days

from January 13, 1973? Claude

will very often give you the correct answer, but sometimes

it will get that addition incorrect. And

finally, Claude just doesn't know what it means to set

a reminder, as no concept of it. It does know

conceptually what setting a reminder is, but there's

no mechanism inside of Claude whatsoever for setting

reminders in the future. To solve each

of these issues, we are going to make a dedicated tool.

So we have three issues right here. We are going to make three

separate tools, one at a time. Here's what

each tool is going to do. We're going to have a very

simple tool that we're going to get started with. It's going

to help us understand what tool calling is all about. Its

only job is to get the current date time. So

that means the current date plus the time.

The second tool we will make will add a duration

to a date time. So this will allow us

to say something like take the current date and add

20 days to it and what would the resulting day

be. And then finally, we will make a reminder

setting tool as well.

---

#### Lesson 34: Tool functions

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289176](https://anthropic.skilljar.com/claude-with-google-vertex/289176)

**Video:** 06 - 003 - Tool Functions.mp4 | **Duration:** 5m 22s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's get started working on our first tool, which is going

to allow Claude to retrieve the current date time. Before

we go any further, I want you to know that I've created a new notebook

for you to use. This notebook is titled 001

Tools, and it is attached to this lecture. Inside

this notebook, you're going to find a lot of the same code we've already written out

inside the course. However, I've also added in

a new cell down here, titled Tools and

Schemas. Inside this cell, I've placed a tremendous

amount of boilerplate code just to save us a little bit of time

later on. In particular, you're going to find the add

duration to date time function, which you are going to use a

little bit later on. So again, I would encourage you to download

this notebook that is attached to this lecture and use it as the

starting point. All right. So now,

once again, we're going to be focused on implementing this first tool

of Git the current date time. I'm going

to walk you through this entire process step by step. We're going to

write out a lot of code inside of our notebook, and we're not

going to use any of those helper functions that we've set up inside

there. The ones like add user message and add assistant message

and so on. The reason for this is that you're going to see that we

need to refactor those functions just a little bit to

suit tools. So rather than trying to mix updating

those helper functions and learn about tools at the same time,

that would be really confusing. So we're going to instead just focus

on making a tool call without using any

helper functions as much as possible. OK,

so let's get to it. I've broken down this entire

process into several different steps. Step one,

whenever we are adding in a tool to our implementation, is

to write out a tool function. A tool function

is a plain Python function that is going to be executed

automatically at some point in time when Claude decides

that it needs to retrieve some extra information in order

to help the user in some way. I've got an example

of a possible tool function on the right-hand side called

get weather. Claude might be able to make use of this

tool function in order to retrieve the current weather at some

particular location in the world. Now there's

a couple of best practices around tool functions. First,

we always want to use well-named and descriptive

arguments. So the actual function itself and the

arguments to receive should be reasonably well-named

and at least give us a hint of what they are about. Second,

we want to validate these inputs and raise an error if

anything is wrong with the input itself. So for example,

if we failed to receive a location or if the location

is an empty string, we would want to raise an error immediately.

And then finally, whenever we do raise an error, we want to

make sure that it contains some kind of a meaningful error message.

In some cases, if Claude tries to call a tool

function, and it results in an error, Claude is going

to see the exact error message. And Claude

might decide to try to call your tool function again and

call it in a slightly different way that attempts to correct for

that error. So for example, you can imagine if that if

Claude tries to call this get Weather function, and

it passes in an empty string, the validation

check at the very top would fail, and we would raise an

error. Claude would see the error message of location

cannot be empty. And Claude might then decide to try

to call this tool function again, making sure that it passes

in not an empty string anymore. All right, so

let's go back over to our notebook, and we're going to put together our first

tool function. Remember, the goal of the tool we are

putting together is to get the current date time.

So back over here, I'm going to add

a new cell at the very bottom and I will define a new

function called get current date time.

This is going to take in an argument that I will call date format.

I will give it a default value. It's going to be a little bit

of a complicated string here. I'm going to put in percent

capital Y, percent lowercase M,

percent lowercase d, and then a space,

a percent H colon, percent

M colon, percent s. Now

that string is a little bit complicated, so I would encourage you

to pause the video right here and double check the

string you've put in, make sure it exactly matches what I have.

Then inside this function, I'm going to use that date format

to get the current date time and format it in a way that

matches this date format string. So I will

return datetime.now string

format time, I'll pass in that

date format. So now as a quick example

of how we would actually use this function, we could call get

current date time. And if we ran it just like

this, we would get back a date time in the format of

year, month, day, hour, minute, second.

Or alternatively, I could put in a custom date

format string of something like percent

H, colon, percent, capital M. And

that will print out just the hour and minute of my

current time. A good improvement to this function would

be to add in some validation of the date format argument.

Unfortunately, we can't very easily validate the exact

structure. Make sure that this thing is a valid string format

time formatter. But we can at least check and make sure

that we are not passing in an empty string. So

I might decide to add in a little bit of validation here with

a if not date format.

And then if we fail that validation check, I might raise a value

error and say something like date

format cannot be empty. So

now if I try to call get current date time with an empty

string, I would end up getting an error message and it's going to tell me

date format cannot be empty. Now to be

honest with you, it's kind of unlikely that Claude is going to

make this mistake of passing in an empty string here, but

at least from the off chance that it does, we are providing some

signal back to Claude and we are kind of telling it how

it can fix up the error. It can try to call get current

date time again and make sure that it passes in a date format

that is not empty.

---

#### Lesson 35: Tool schemas

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289174](https://anthropic.skilljar.com/claude-with-google-vertex/289174)

**Video:** 06 - 004 - Tool Schemas.mp4 | **Duration:** 4m 39s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that we've got our tool function put together, we are going to

move on to step two, which is where we are going to write

out a JSON schema. We are going to eventually send

all this configuration off to Claude. Claude is going to use

it to understand the different tool functions that are available and the

different arguments that must be provided to these tool functions

as well. The first thing I want you to understand here

is exactly what JSON schema is all about. So

this entire object you see on the right-hand side, this is

not technically a JSON schema per se. Instead,

at the very top, there is a name and a description. I'll tell

you what those are about in just a little bit. Underneath that,

there is a key of input schema. And then

assigned to that is that dictionary right there. What

I've now highlighted, that is technically what a

JSON schema is. So again, let me give you a little

bit more background. The idea of JSON schema

is not specifically tied to language models or tool

calling or anything like that. JSON schema is

a data validation specification. So

it is a set of rules that can be used to validate any kind

of JSON data. So again, it is not specifically

tied to language models or tools or anything like that.

The language model community decided at some point in time that

JSON schema is just a really convenient way of

wiring up and handling tool calls. This is a

widely understood technology that has been around for many,

many years. Now, at this point, I still haven't

really explained what the JSON schema spec is all about. So,

in total, this thing is used to inform its Claude

about the different tools that are available to it. We are going

to provide a name for the tool, so in this case it might be GetWeather,

and then a description for the tool. This description

is meant to tell Claude what the tool does, when

to use it, and what kind of data it is going to return. Best

practice is to make sure you have a description around three to

four sentences long. So even though right here I'm showing

only retrieved current weather, in reality, I would definitely

want to have a much longer description than this. Then,

under this input schema key is going to be the actual

JSON schema spec. This is going to describe the

different arguments that should be passed into our function. So

in this example back over here, if I had a git weather function

that received just a location, I would put in

input schema with location right here, it

needs to be a string, and here's a description of the purpose

of that argument. Again, we would want this description

of the argument to also be about three to four sentences

long, and help Claude understand exactly what

this argument controls and how it affects the overall function

call. Now, like I mentioned, it might be a little bit intimidating

to think that you have to write out all this configuration on your own. Luckily,

I've got a trick that is going to help you write out a almost perfect

JSON schema spec for every tool you ever put

together. So let me show you the trick. First,

I'm going to go back over to my editor and I'm going to find our

tool function. So for us, it is the get current date

time function. I'm then going to take this over

to a Claude window. So I'm at Claude.ai

here. I'm going to write out a very simple prompt. I'm

going to ask Claude to write a valid

JSON schema spec for the purposes

of tool calling for this function.

And then I will also ask Claude to Follow

the best practices listed in the

attached documentation. Then

I'm going to go into put in my tool function, like

so. And then here's the real trick. I'm going

to go over to the Anthropic API documentation. In

the User Guide section, there is a entire page on

tool use with Claude. This entire page has

a lot of different best practices, and examples of good

tool descriptions and bad tool descriptions. So

I'm going to just copy all the text here, go

back over to my Claude window, paste it in as an

attachment and run this. Claude

is then going to respond with probably a very strong

JSON schema spec. So I'm now going to copy

this, take it back over to my editor, and

I'm going to paste it in right underneath my existing get

current date time function. So I'll say get current

date time schema,

like so. Now, as a little naming pattern

that I like to use here, I'll give my tool function,

whatever name I want, and then the schema to match up with it

will be underscore schema. So the same name underscore

schema. And it makes it a lot easier to keep track of my

different schemas. There's one last thing I'm going to do.

At the top of the cell, I'm going to add in an import from

anthropic.types. I will import

tool program. I'm going to take

this tool param and wrap it around this entire dictionary.

So I'll put in right here, tool param, opening

parentheses, and then a closing parentheses down here at

the bottom. Adding in this tool param

thing is not strictly necessary. In other words, our code

is still going to work without it, but it's going to prevent a type

error later on when we eventually take this schema and make

use of it.

---

#### Lesson 36: Handling message blocks

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289179](https://anthropic.skilljar.com/claude-with-google-vertex/289179)

**Video:** 06 - 005 - Handling Message Blocks.mp4 | **Duration:** 5m 44s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

On to step three, we're going to call Claude with

his JSON schema and some user message. So

from our server, we're going to make a request off to Claude just as

we've been doing before, but now we're going to also include this

tool schema. This helps Claude understand that there is

a tool available to it. Let's go back over to our notebook and

we're going to try to make this request by hand without using any

of those helper functions we previously put together, like the

chat function. Okay, so back over here, I'm

going to go down and create a new cell. I'm going

to make an empty list of messages. I'm going to append

in there manually a new

message with a role of user and

a content of what is the exact time

formatted as our

minute seconds. Then,

underneath that, I'm going to do a call off to the clientmessages.create

function. So I get a response from clientmessagescreate,

all designate my model, my max

tokens, My

list of messages, and now we want to also include

this JSON schema that tells Claude that it has

a tool available to it. To do so, we'll include

a Tools keyword argument. This is going to be

a list, and inside of it is going to be all the different JSON

schema specs that we have created. At this point in time,

you and I have only created one, and it's called Get

Current Daytime Schema. So we're going to take that and

put it in right here. Then I'm going to print

out response at the very bottom and let's run this and see

what happens. We're going to get a response message

back here that has a structure that we have not quite seen before.

All the messages that we have ever received before would have a

content field that has a list and inside there would be

a text block. And as I mentioned many times

before inside the text block is the text that we actually

want to display to the user. But now that we are making

use of tools, this content list is going to be a little bit

different. So you might notice that inside the content list,

there's a second block called a tool use

block. So here's that entire structure right here. Let

me show you a diagram just to make sure this thing is really clear.

Okay, so this is our first experience with a multi-block

message. Remember, a message is either an assistant

message or a user message. We are often going to

have some amount of text stored inside of a message, and

that's what we've always seen previously. But in addition to

just text, there are other types of data that can be

stored inside of a message. When Claude decides to

make use of a tool, it's very often going to send us back an

assistant message that contains both a text block and

a tool use block. The text block is intended

to be some text that is displayed to the user to

help them understand what is going on. So in this

case, the text block might contain something like, I can help you

find the current time. Let me find that information for you. Then

in addition to this text block is the tool use block.

This tool use block is a sign to a UNI as

developers that Claude wants to make use of a tool.

The tool use block is going to list out the name of the tool

function that it wants to call. So in this case, Claude wants to

call the Get Current Daytime function we put together. And

then it also provides some inputs or essentially arguments

that we need to pass into that function. So the next thing

we're going to do as a part of this entire process is to find

the appropriate tool and actually run it. But before

that, there's something really critical that we need to

take care of around this idea of having a content

list with multiple blocks inside of it. Okay,

so here's just a quick reminder for you. At

this point in time, we have made a request from our server

off to Claude, and in that request we had a single user message

that also included a tool schema. We

have now gotten a response back. And inside this response,

there is the assistant message, and it has two separate blocks

inside the content list, a text block and a tool use

block. Now, there's something I want to remind you about

Claude. Remember that Claude does not store any message

history or anything about the conversation you are having.

If you ever want to maintain a conversation or a history with

Claude, you have to manage it manually. And what

this means is that when we eventually take this tool use block

and eventually call some actual function, we need to eventually

respond back to Claude. And when we do so, here's

the critical part, we need to make sure we include the

entire conversation history just as we've

been doing throughout the course. So we already have an idea

of how to do this. The only difference this time around is that

we need to make sure that we deal with messages that might have

multiple blocks inside them. So let me show you how we would

do this by hand. And then eventually a little bit later on

inside this section, we are going to go back to our helper

functions, specifically add user message and

add assistant message and make sure that these can support

messages that have multiple blocks inside them. Because right

now they only support single text blocks. Okay,

so to manage these messages, I'm

going to go back down to our bottom code cell where we are currently

getting our response. I'm going to take our

response and make sure I append in a new

assistant message to our list of messages. So

I'm going to delete response right there. We'll say messages

dot append. I'm going to put in a new

role of assistant. And

then our content is going to be the exact list

of content blocks out of the response we

just got back. So all we have to do is add in response

dot content. There

we go. So now if I print

out messages and run the cell again, We

should see that we end up with our user. So

that's our original message right there. We now have our assistant

message. And inside there is a text block and

the tool use block. So now we are correctly building

up our conversation history over time by including

all the different blocks from all these different messages that

we are collecting. So once again, I just want

to remind you that we are going to eventually have to go back to the add

user message and add assistant message, those

two helper functions, and update them to account for

dealing with multiple blocks like this.

---

#### Lesson 37: Sending tool results

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289184](https://anthropic.skilljar.com/claude-with-google-vertex/289184)

**Video:** 06 - 006 - Sending Tool Results.mp4 | **Duration:** 9m 22s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

On to step four, where we run the tool function that Claude

requested us to run. Remember, in the last step, we got

back a response from Claude, that included a tool

use block. Let's print that out inside of our notebook really

quickly. So back over here, remember we've got this response

variable, I'm going to go down, create a new cell, and

print out response. Now inside of here, we get back

a message that has a content property, and the second

block inside that list is a tool use block.

So to access that thing, I would do response content

at one. Then inside of here,

we're given a input field. This is the input

or the arguments that Claude is requesting that we pass into the

get current date time function. So to get that dictionary

right there, we would chain on a dot input.

Now when we add on the dot input, you might end up getting a

type error here. We're going to ignore type errors

just in this video when we're going to come back very, very quickly and

fix all the type errors. But just so you know, if you see any type

errors in this video, totally fine. Just ignore them for right now. So

now our goal is to take this dictionary right

here and provide it to our get current date time function.

Just one thing to be aware of here. Remember our get get

current date time function. defined

back up here doesn't take in a dictionary. It takes in a

keyword argument of date format. So

to convert that dictionary into a list of keyword arguments

and apply them to the function, here's what we would do. I'm

going to call it get current date time star

star and the response content one input.

And now if I run that, I'll get back my current date time

in the real world. So for me, it's 241 or 1441.

Besides the type error that we need to fix up, that ended up being

pretty easy. So let's now move on to step five. So

in step five, we are now going to send a follow-up request

back to Claude. This request is going to include our full

conversation history. So we'll have our original

user message. It'll have the assistant message that we just

processed with a tool use block. And now we

are going to append onto the very end another user

message. This user message is going to have a new kind

of block that we have not seen before called the tool result

block. Let me tell you about how this block works. The

tool result block is going to be placed inside of a user

message. The tool result is going to contain the result

of running a tool. So we're essentially taking whatever we get back

from the tool function that we just called and we are feeding

it right back into Claude. The tool result block is

going to have a couple of different keys inside of it. And it's

important for you to understand exactly what these keys are doing.

The first one is probably the trickiest to understand, the tool

use ID. So let me very quickly tell you what the tool use

ID is all about. I want you to imagine for just a moment that

we create a new tool called calculator. And this

tool is meant to evaluate a math expression. And

then maybe a user sends in a message of something like, what's

10 plus 10? Also, what's 30 plus 30? In

this case, Claude might want to make two separate calls to the

calculator tool. One call to solve 10 plus 10

and a second to solve 30 plus 30. To

do so, Claude will respond with an assistant message that has

multiple tool use blocks inside of it. So

we might have tool use block one right here, where

the expression that we need to evaluate is 10 plus 10. And

then in the second, we might have an expression of 30 plus

30. We would then execute our calculator tool

twice, once for this expression and once for this

expression. And then we would send a follow request back

to Claude. Inside of our follow request, we would add in

a user message that has two separate tool result

blocks. So we'd have tool result one and tool result

two. Now when we send these back into Claude,

Claude needs to be able to figure out which result belongs with which

request. So we've got request one and request two,

and then result one and result two. Claude

doesn't want to just rely upon these things being ordered in

the same order. Instead, it's going to make use of

IDs. So inside the original tool use,

we have an ID up here of AB3. And

then in a second, we have the ID of PO9.

Inside of our follow-up request, we send back to Claude. We need

to make sure that the ID, so we put down here, match up

with the output. So in other words, PO9.

being tied to 30 plus 30, then we would want to make

sure that we have P09 tied to 60 down here. And

likewise, AB3 with 10 plus 10, we'd

want to have that tied to AB3 with an output of 20. So

that's what the tool use ID is all about. It helps us

tie tool use requests to tool

result outputs. The other properties

on here that you need to be aware of is content, so asking me whatever

output you get from your tool function. Even if

your tool function will return something like a number or

a dictionary or a list, you're just going to turn

it into a string, usually by just converting into plain

JSON. And then finally, optionally, we can

also put in an is-air field. If

anything goes wrong with running your tool function, you will set this to

be true. By default, it's always going to be false.

Now that we have a better idea of what this tool result block is all

about, I want to give you a quick reminder of what we need

to do next. So we just got back an

assistant message from Claude that asked us to run a tool.

We know that was asking us to run a tool because it had a tool use

block inside of it. We then executed our tool

with the provided arguments. So now that we have the result

of the tool function, we need to make a follow-up

request back to Claude. Inside of this request,

we're going to include our full message history. So

it's going to be our original user message, the assistant

message with a tool use block inside of it. And now

we are going to append in one additional message, a

user message, that has a tool-result block.

That's what we just discussed. So it's this thing right here.

Inside of this tool result block, it's going to have the result of the

actual function call. So let's now go back over to our notebook

and we're going to get our list of messages and add in this new

user message with the tool result block inside

of it. All right, so back inside of my notebook, I'm

going to get my list of messages. I'm going to

append in a new message that has a role

of user. And then a content

list that will contain just one block, it's

going to have a tool result block. So we'll

give it a type of tool underscore

result. a tool use

ID that matches the ID of this

tool use block right here. To get access

to that ID right there, we will refer to

response content 1.ID.

And when I put that in, I'm going to once again get a type error.

Remember, we are to ignore type errors for right now. We're

going to ignore it and we'll fix it up very shortly. I'll

then add in some content. So that's going to be the

result of calling my function right here. So

I'm going to assign the result of calling get current

date time to how about just result.

You're going to rerun that. And then I'll

refer to content result. And

then finally, when we ran this function, there was no error. So

I'll put in is error false,

not strictly necessary, because that is the default, but I'll

put it in there. Anyways, Okay,

so now that we have updated our list of messages, I'm

going to print out the list. just

to make sure we are doing everything correctly. So now we

have our entire conversation history here. We have the

original user request. We've got Claude's request

for us to use a tool. And now we have appended in

a new user message that has a tool

result block inside of it. So now the last

thing you need to do is take this list of messages and send it

back into Claude. I'm going to add in another code cell

down here at the bottom. And once again, call client

messages create with my model

max tokens. the

list of messages. And then whenever we make a follow

up request that includes some tool use, we need to also

include the original tool schema. Even though we

are not probably going to use any tools here, we still have to

tell Claude about the existence of this tool because we

are referring to it inside of the tool use block right here

and the tool result block right here as well. So

we need to make sure that we still include our list of tools, which

would be a list of get current date

time schema. And

that should be it. So now let's run this. And

we should see a final response out of Claude. And

so there it is right there. Here's our final response. We have

a text block that says the current time is 1504.

Well, that is a successful tool called. So we've

gone through the entire process. Let's do a very quick

review. So everything began with us writing out a tool

function and then writing a tool schema to describe it.

The goal of the tool schema was to help Claude understand the different

tools available to it and how to actually call those different tools.

We have to include that tool schema with every request that

we make from here on out. So that's why I'm showing it right here and

down here as well. When Claude responded to us, it

sent back an assistant message that had two separate blocks

inside of it. So a text block right here and

a tool use block right here. The text block is intended

to be displayed to a user, so the user understands what's going

on. And the tool use block includes

some information about a tool that Claude wants to call. So

it includes the name of the tool it wants to call along with some

input arguments to it. Then on our server,

we executed the tool function, and then

we sent a follow-up request back to Claude. The

follow-up request included the entire conversation history, along

with the list of tool schemas as well. The final

message inside of our request was a user message,

then included a tool result block. The tool

result block is used to inform Claude about the result

of running some tool function. So inside this block,

we put the current time, which is what Claude was really asking

for. then Claude sent us one final result

that was just an assistant message with only a text block.

And it made use of the input that we fed into it through

this tool result block.

---

#### Lesson 38: Multi-turn conversations with tools

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289178](https://anthropic.skilljar.com/claude-with-google-vertex/289178)

**Video:** 06 - 007 - Multi-Turn Conversations with Tools.mp4 | **Duration:** 9m 11s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

We've now gone through an example of wiring up one single

tool to Claude. But as a reminder, the goal of this project

is to wire up multiple different tools to Claude. So we want to have three

different tools in total. I want to think about what's going to happen

inside of our code when we wire up three different tools to Claude.

So let's go through a quick example. Let's imagine that

we submit a user message to Claude asking it what

day is 103 days from today. Now

to answer this, Claude needs to use two separate tools. First,

it needs to use Get Current Date Time to find out what the current date is,

and then it needs to use Add duration to date time to add

103 days to that. So here's what's gonna go on

behind the scenes. Initially, Claude is going to immediately

respond back to us with a tool use block asking

us to call Get Current Date Time. We

will call that function, and then respond back to Claude, telling

it what the current date is. After that, Claude

is going to realize that it doesn't quite have enough information

to answer the user's original question. It now needs to take

the current date and add 103 days to it.

So Claude is then going to respond to us with another separate

tool use block asking us to call add

duration to date time. We will call it, and

then pass the response back onto Claude. And now Claude

has enough information to respond to our actual query.

Now here's why I'm showing you this example in particular.

If we are getting our input for our original user

message from an actual user, like an actual person, we

can't always predict exactly what they are going to be asking

of Claude. So a user might ask some wild

query that's going to require multiple different tool calls

in order to actually answer. So when we add tool calling

into our application, we really need to allow for this kind

of situation. Whenever we submit some query to Claude,

we need to assume that Claude might want to use multiple

tools in a row. And whenever Claude responds to us,

we need to take a look at the response and see if

Claude is asking to use a tool. If it isn't, then

we know that we have a final response that we can finally

deliver back to our user. Here's a pseudo code example

of how we might implement this. We could make a function

called something like Run Conversation that would take in an

initial list of messages. then inside of a while

loop, we'll reach out to Claude, get a response back.

We'll then take a look at that response. And if Claude is

not asking for a tool use, then we know that we have

some response we're ready to send back to a user. Otherwise,

if Claude does want to use a tool, we can run the tool, get

the resulting tool, result blocks, add

them into a user message, and then run Claude all

over again, still inside of the while loop. In the

remainder of this video, we are going to spend some time to refactor

our notebook, to build up a function just like this. So

we are going to build out a function like run conversation that's

going to go through the exact same series of operations.

In order to put this function together, however, we are going to have

to do a little bit of work. We're going to have to do a little

bit of a refactor on our add user message

and add assistant message helpers and the chat function

as well. I've put together a list of all the things

that we're going to do inside of our notebook to get ready for defining

this run conversation function. In step

one, we are going to upgrade our add user message and

add assistant message helper functions so that they

can better deal with multiple message blocks.

Remember that whenever we start working with tools, we are

going to get back responses from Claude that might have multiple

different blocks inside them. And at present, our add

user message and add assistant message helper functions are

entirely set up, always assuming that we are always working with

a plain text block and nothing else. So

let's take care of that back inside of our notebook right away. Back over

here, I'm still inside of the exact same notebook we have been working

on. I just deleted a couple of the cells at the bottom that

had some of the example tool calls, just so you can better see

what I'm doing on the screen. All right, so I'm going

to expand the helper function cell. I'm going to

find add user message and add assistant message. So

once again, right now we are assuming that we are always getting back

some piece of text and we are assigning that directly to the content

property. So now we want to allow for a little bit more flexibility

here. So here's how we are going to do it.

At the top of the cell, I'm going to add an import from

Anthropic.types. I will import message.

Then I'm going to rename the second argument right here. Instead

of text, I'm going to call it message. I'm

going to expand this dictionary like

so. And I'm going to update text

to be message.content if

is instance message capital

in message else message.

And then I'm going to repeat the same refactor on add

assistant message as well. So down here,

I'm going to rename that to message. I will

expand the dictionary. And then to save time,

I will copy that statement right there to right

there. All right, so now I'm going to rerun the cell and

I'll show you what this refactor is going to do for us. So

back down here. I'm going to add in a quick

example call like so. So

I'm just asking Claude to print out the current time in our

minute second format. And I'm providing our get current daytime

tool. I'm then going to print out the message or response

we get back. So if I run this, we'll see that we get the usual

message like so. And inside there

is the content property that has both a text block and a tool

use block. So now to very easily add this in

to my message history as a assistant message,

I would call Add Assistant Message

with Messages, and then I can now put in that entire

response, the entire message that I just got back. So

I'll call that and then print out Messages

on the next cell down. And there we go.

I've got my entire message history being built up. Another

way that I could run this is to put in response.content,

like so. This will work just as well. So if I do that, and

then printout messages, I still get the correct thing. And

then, of course, if I want to, I could always put in a plain

string here as well. And

printout messages. and we'll see that yep,

still building up that response history. So now we have a much

more flexible helper function in add

user message and add assistant message. We could put in a

plain string or a list of blocks or an entire

message and it will digitize the thing for us. This is going

to make dealing with a message that has some tool use

blocks inside of it much easier down the line. Onto

step two of our refactor. We are going to update the chat

function to receive a list of tool schemas. And we'll

take that list of schemas and pass it through to the client

messages create function call. In addition,

from the chat function, we are no longer going to return plain

text out of the first block that comes inside

of the assistant message. Instead, we will return the entire

message that we got back from Claude. Once again, this

is because we are now anticipating getting back responses

from Claude that have multiple blocks inside them. And at present,

our chat function is always assuming that we are only

ever getting back one block, just a single text

block and nothing else. So back over here,

here's the chat function. I'm going to add in a tools.

They'll be defaulted to be none. And then we are going to wire

it up in the same way that we did system right here. So we'll say

if there are any tools that were passed in, we

will add that in as the tools parameter. Next

up, I'm going to go down to the return statement. So right

here. As I just mentioned a moment ago, our

chat function is currently set up assuming that we're always going to get

back a single block from Claude, and that the block

is always going to be a text block. That's why we have this code

right here. We are making a really big assumption that we're always

getting back that one single block and it's always going to contain

some text. Because we are now making use of tools,

that is no longer the case. We might

get back a message that has multiple blocks inside it, so

multiple entries inside this content list. One

of them might be a text block, but we don't necessarily

have a guarantee. So rather than always making

this assumption, I'm now going to return the entire

message. This is going to be a little bit less convenient

for us because now if we ever want to get access to the text,

we're going to have to do a little bit more work, but it's definitely a lot

safer because again, this really reflects reality.

Okay, that's that. So

now on that same kind of note, we're going to now

add in a little helper function. We're going to call it text

from message. And the goal here is to take a look

at a message, take a look at all the blocks, find all

the text blocks, and just extract the text from those. So

this is kind of replacing the functionality that we just removed.

It's going to make it a lot easier to extract all the text out

of a given message. So I'm going to add in that

helper function right underneath chat. I'll

call it text from message. It's

going to receive a message. And inside of here,

I'm going to return a new log new line that

is going to join together a comprehension with

block.text. for block in

message.content if block.type

is equal to text. So

this is going to take a look at all the different blocks inside

of a message. And if the block is a text block,

then we're going to just extract the blocks text and

then join all the block text together and return it. So

again, just a helper function to make it a little bit easier

to get all the text out of a particular message.

All right, so we've taken care of most of our refactor. So

now the last step, which we're going to take care of in just a moment, is

add in support for multiple tool calls inside of a

single conversation. So essentially, we need to implement

a function like this. We need to make a function that's

going to take in the list of messages, and then continue calling

Claude until we get back a sign that Claude doesn't

want to call a tool anymore.

---

#### Lesson 39: Implementing multiple turns

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289182](https://anthropic.skilljar.com/claude-with-google-vertex/289182)

**Video:** 06 - 008 - Implementing Multiple Turns.mp4 | **Duration:** 16m 25s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that we are done with that refactor, we are going to start to implement

a function like this run conversation function. And

reality, our real implementation is going to look almost identical

to what you see here on the right-hand side. Remember, the

entire goal of this function is to keep calling

Claude until it no longer asks to use a tool. When

it doesn't ask to use a tool anymore, that is a sign to us that

Claude has a final response that is ready for us to send

back to our users. And the first thing for us to really understand

here is how we know if Claude wants

to use a tool or not. We could just take a look at

the response message and see if there's a tool use block

inside there. But there's a little bit more convenient way

of doing this. Back inside my notebook, I'm going to

run that little sample again where I'm making use of

client messages, create directly, not using our chat

function. I can run that, and here's my

message response. Now very inside of here, you'll

notice that there is a field named Stop Reason, and

it is set to a string of tool underscore use.

So let me tell you about that field just a little bit. This

field tells us about why Claude decided to stop

generating any more text. Our current value of

tool use is a sign to us that Claude has decided

that it needs to call a tool. So if our response

message, the assistant message that we get back from Claude has a

stop reason of tool use, that is a very clear and

immediate sign that Claude wants to use a tool. There

are some other possible values of stop reason. And

we could definitely check for these, but definitely the one you're going to check for the most

is probably going to be tool use.

So that's how we're going to implement that little if statement right there.

All right, so let's go back over to our notebook. We're going to start to

implement this run conversation function. So

back over here. I'm going to clear out that cell. It

was just there for demonstration purposes. I'm going

to define my run conversation

function. It's going to take in a list of messages,

and then we will set up our loop. Inside of here, we

will get a response from calling Claude through our newly

upgraded chat function, which now supports tools. So

I'll pass in my list of messages, along with some tools that

Claude can call. In this case, we currently only have one

tool. So I'll add in right here. It's our get current

date time schema. Then

I'm going to take that response I get back and add it into my message

conversation history using the newly upgraded

add assistant message function. I'm

then going to print out that response using the text

from message function we just put together. I'm printing it out

just we have an understanding of what Claude is currently doing. So

I'll print out text from message

with response. Okay,

now here is the part where we are going to use the stop reason.

We need to take a look at the message that we just got back from Claude

and understand whether or not Claude wants to use a tool. If

it doesn't want to use a tool, then we want to immediately break

out of this while loop. So we'll say if, response

dot stop underscore reason is

not equal to tool underscore use, then

that is a sign that Claude is all done and it doesn't need to make

use of any more tools. So we will immediately break.

If we get past that if statement, then we know that Claude wants

to call a tool. So we're going to put together a new

function in just a moment. We're going to call it Run Tools.

We're going to pass in the message that we just got back from Claude. The

goal of Run Tools is to take a look at all the tool

use blocks inside this message and run the appropriate

tool for each one. I'm going to define the Run Tools

function in a new cell right above Run Conversation.

So up here, I will put together a new function called Run

Tools, and this is going to take in a single

message. Now this function is going to be

just a little tricky to put together because we have to write it out

assuming that there might be multiple tool calls inside

of here. So let me show you a diagram to just make sure it's really

clear what needs to happen inside of run tools. As

a very quick reminder, whenever Claude gives us back an assistant message,

it can possibly have more than one tool use block

inside of it. And we took a look at this earlier. So

if we ask Claude initially to add together 10 plus 10

and 30 plus 30, it can send back to us two

separate tool use blocks. One might ask us to run

a calculator tool to evaluate 10 plus 10. And

the second tool use block might ask us to evaluate

30 plus 30. So we need to set up this

run tools function, assuming that we might have more

than one tool use block. So here's how this

function is going to work. We're going to take a look at

that message that we just got, specifically the content

property on it. Remember that content property is going to be a

list of blocks. Inside there, we might have a text

block that tells us what Claude is currently thinking

or what it's currently doing. We don't really care about that text block

too much, so I'm going to delete it out of this diagram. And

then we're left with just the two separate or possibly more

for that matter, tool use blocks. So

inside this RunTools function, we are going to iterate

over all the different tool use blocks we got. And

for each one, we're going to run the specified tool with a

given inputs. So we'll take a look at this name

field right here. We'll find the appropriate tool function

to run, and we'll run it with the given input.

Then we're going to take all the outputs from each of these different

tool runs, and we're going to assemble them into separate

tool result blocks. Remember, a tool

result block is how we communicate the result of running

a tool back over to Claude. Once we have

assembled all these different tool-resolved blocks, we're

going to put them all together into a list and return them

from the Run Tools function. Okay,

so let's try to implement this. I know it's confusing. I know there's a

lot going on here, but the code itself is actually

not as bad as it might seem initially. So back

over here, inside of Run Tools, first thing

I'm going to do is take a look at this message's content

property. That is the list of blocks.

And I'm going to extract only the tool use

blocks. So I'll say tool request.

is block for block in message.content

if block.type is equal to tool

use. So again, a little bit of a filter operation here.

We are getting just the tool use blocks because those are the

only ones we care about. And I'm calling this specifically

tool request because I think it makes a little bit more sense than

tool use. These are requests by Claude for us

to use a tool. Then I'm going to make

an empty list called tool result blocks.

This is going to eventually contain all the different tool results

that we create. Then I'm

going to iterate over all these different tool requests.

So for tool request

in tool request. So now we are iterating

over each individual tool request. So this is where we

now need to run a specified tool with the given

inputs. And we know which tool we want to run based

upon this name property. So we will say if

toolrequest.name is equal

to get current date time. Then I want to run

the get current date time function

with the star star inputs from the tool request.

So tool request dot input.

That's going to give me some tool output.

And I'm now going to take this tool output and use it to assemble

a brand new tool result block.

It has been a while since we have made use of a tool result block,

so let me just give you a quick reminder on what these things are. All

right, so on the left hand side is a tool use block. This

is what we are currently working with. This is Claude's request

to use a tool. On the right hand side is a

tool result block. So this is the response

that we are formulating to Claude's request to run a

tool. Remember that a tool result block

has a couple of different properties that we need to assign to it. First,

it's going to have a tool use ID. This needs

to be exactly equal to the ID from

the tool use block that is causing us to run

a particular tool. Note here that the

ID field over here on the left-hand side, it's called ID, and

then on the tool is a block, it's a totally different property. It's a tool

use ID, but they need to be exactly equal. Then

content is going to be the output from our tool

run, so the actual tool function. We need to make sure we just encode

it as a string, no problem there. We can then also add

on that optional is air property, if an air occurred

when we ran the tool. And then finally, we also

need to add in a type of tool underscore

result. All right, so back over here,

now that we have our tool output, we're going to assemble our tool result block. And it's going to have all those

properties I just pointed out to you. It will have a type

of tool result, a

tool use ID of

the tool request.id.

It will have a content And I'm going to

take whatever I get out of my tool, and I'm going

to encode it as JSON using JSON

dump string. I

need to make sure that I import JSON, so I'll do that at the top this

cell. There

we go. And

then finally, the is air. I'm

going to set that to false for right now, and we're going to add

in a little bit more robust air handling in just a moment. So

now that we have created our tool result block, we're going to add

it into our list of two result blocks. So

I'll then do a tool result, blocks append in tool result block.

And then finally, outside of the for loop, I will return

tool result blocks. Okay,

so this is the start to our run tools function.

So we've at least got an idea of what it does for us. We're

going to filter out all the different tool use blocks for each

one. We're going to run some given tool function and

then put the result into a tool result block, assemble

all the results and return that list. So now we're going

to add in two quick improvements to this function. First,

we're going to add in a little bit better air handling. So we

are currently always saying that there is no air. That's

definitely not accurate. There might be a scenario where we run into some

kind of air when we are running our tool function. So

I'm going to immediately make a small improvement here to capture any

air that might occur as we run our tool to

do so. I'm going to wrap that with

a try. Accept

statement. I'm

going to fix my indentation like so. And

then if I get down into the accept statement down here, I

still want to put together a tool result block and

add it into this list. But now I want to have an

is error of true. And I probably want to take the error

message and put it into the content field right here so

that Claude gets some better understanding of what error just occurred. So

I'm going to copy tool result block right here, paste

it down inside of the accept statement. I'm

going to change is error to true. And

then for content, I'm going to put in an F string where

I put in error with E.

So again, I'm providing some information back to Claude, help you

understand why an air occurred. And remember, whenever

an air does occur, Claude might try to run your tool

again with some better arguments or better formed arguments.

Okay, so that's our first improvement. Now, the second

improvement I want to make right now, we only are considering

one single type of tool, the get current

date time tool. Remember, later on, we might have

multiple different tools. So besides just get current

date time, we're going to eventually support adoration

to date time and set a reminder. And honestly, we're

going to add in another one even after that. So using

this pattern right here, where we have an if statement that's just

checking for get current date time, not really going to scale

too well. So to figure out what tool to run

and actually run it, I'm going to make another helper function

right above run tools. And I'm going to call it run

tool. This is going to take

in a tool name and an input

to that tool. And then inside of here, this is where we

are going to do a series of if statements or any kind of check to

figure out which tool function we need to run and then actually run

it and return the results. So if tool

name is get current date

time, Then I'm going to return,

get current, date time, with

star star, tool, input.

So now with this approach, if we ever add in additional tools,

we can just put in additional if checks right here. So

if tool name is whatever other tool we have,

we can run that particular tool function. So we are going

to very shortly come back to run tool and add in some additional tools

in just a little bit. All right, so now to make

use of that function, I'll come back down here.

I'm going to indent that block

right there to the try, the accept, and the tool results.

I'm going to remove the if statement and

then replace get current daytime right here with run

tool. And I'm going to pass into it our

tool request.name and tool request.input.

There we go. Okay, so this was

a little bit of a painful refactor, but this

is our run tools function. No more changes required.

It's going to work pretty well. And we've also got our

run tool function put together, also working pretty well. So

now the very last thing we need to do is go back down to

our conversation function and

make use of run tools. So

here's our call to run tools right here. So run tools

is now going to return our list of tool result blocks.

So I get tool results. I'm going to add

that into my conversation history. So add user

message with messages and tool

results. then outside of the

while loop, so I'm making sure them outside of while I'll

return the list of messages. And

that's it. Okay, so now this run conversation

function captures that entire loop that we discussed. So

whenever we go into run conversation, we're going to call

Claude, we're going to get back some assistant message.

If the assistant message is asking for any tools, then we're

going to continue on past the if statement. We're going to run

those tools, get the results, and add them in as

a user message to our list of messages. Then we're

going to go back up to the top of the while loop again, and

call Claude another time with the list

of tool results inside of those messages. And

we're going to repeat this process over and over again until Claude

doesn't ask for a tool use anymore. So

now here's the point where hopefully everything's

going to work. We'll do a quick test down here. So

I'm going to make a list of messages. I'll add

a user message to it.

And I'm going to ask Claude to do something that's going to probably require

two separate tool calls. So I'm going to ask Claude what the

current time is in our hour, hour, minute format,

and then same thing for second format. So in theory, Claude

is probably going to break this up into two separate tool

calls. I will then call run. conversation

and passing the list messages. I'm

going to rerun all the cells inside this notebook because

we have now changed a tremendous amount, so we'll do a run

all, and then we'll take a look at the response we get.

So it looks like it definitely is the right answer right here, but I want

to take a look at the list of messages to really understand what is happening.

So initially, we have our user message. We then get

the initial response back from Claude. It has a text block

and a tool use block. So once again, a message

with multiple blocks inside of it. And this is why it's so critical now

to make sure that all of our code will correctly handle multiple different

blocks. Inside this first message, we have a tool

use block where Claude is trying to get the current time in

our minute format. We then

respond with a tool result. And then here's the interesting

part. Claude then decides to make a second tool

call back to us. So in the second tool call, we

don't have a text part anymore, once again highlighting

the importance of correctly handling multiple different

tool parts inside of a single message. Inside

this second message, we've now got a tool use

block. Claude is now going to try to call get current daytime

in seconds format. We then send the

result back to Claude, and then we get a final response

from Claude that has just a text block that says, here's

the answer to your original query. So this

is a perfect result that definitely highlights every

step that we just went through. The entire process of

running our conversation until we have a response

that is not asking for tool use. And

inside of our run tools function,

the importance of taking a look at all the different blocks

we get back, pulling out just the tool use blocks, and

then running a tool for each of those blocks, formulating

the response into a tool result, and then sending all

the different tool results back into Claude. This video

has been long and probably rather confusing, but we've now got

an excellent example of multi-turn tool

calling. So now the last thing for us to do inside of

this project is make sure that we can support multiple

different tools. We need to add and support for the adoration

to daytime tool and the set reminder tool as well.

---

#### Lesson 40: Using multiple tools

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289185](https://anthropic.skilljar.com/claude-with-google-vertex/289185)

**Video:** 06 - 009 - Using Multiple Tools.mp4 | **Duration:** 3m 38s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The last thing we need to do is add in the Add Duration to

DateTime tool and the Set Reminder tool. This

is going to be a little bit anti-climactic because last

video was rather challenging. This one is going to be really easy,

short and straightforward. Turns out I've already put together

a lot of the code that we need for this inside of the

Tools and Schemas cell. You'll find that

I've already got an implementation of add_duration_to_datetime,

but together inside of here. And if you scroll down, you'll

see I've also got our set_reminder function put together. Now

set_reminder doesn't actually set a reminder or anything like

that. It's just going to print out a statement that says, hey, we

set a reminder at this time with some given content.

I've also provided us a add_duration_to_datetime

schema and a set_reminder schema.

So all we really need to do is pass these two schemas

into Claude, and we also need to make sure that if Claude ever asks

to use either tool, we call the appropriate tool function.

So let's get to it. Should be pretty straightforward.

First off, I'm going to find the run_conversation function.

Inside of here, I'm going to find the list of tools, and I'm going to add into

it, add_duration_to_datetime,

schema and the set_reminder

schema as well. So now Claude is aware of

the existence of these two other tools. Next,

all I have to do is go up a little bit here to

the run_tool function. So this is the function where

we're going to get a tool name and some arguments. All we have

to do is find the appropriate tool function call, call

it, and return result. So adding into the thing

is really easy. Let's add in an if

case. So check and see if the tool name

is add_duration_to_datetime.

And if it is, we'll return a

call to add_duration_to_datetime and **tool_input.

I'll then repeat that for the other tool.

So the tool name is set_reminder, return

set_reminder with **tool_input.

And that's it. So

as soon as you put together this run_tool function and

the run_conversation function, after that initial

difficulty, everything around tool use starts to become really

easy and straightforward, because adding in additional tools

is super simple. Just update run_tool, add

in a tool schema, add in an implementation for the actual

tool function itself, and that's it. You're all done. So

now let's test this out. I'm going to make sure I rerun that cell.

I'm going to rerun run_conversation. And

then down here at the very bottom, let's update our

query. I'm going to ask Claude to set a reminder. And

I'm going to say that the reminder needs to be set 177 days

after January 1st, 2050. This is definitely

going to result in more than one tool call. Claude is going to first

have to add_duration_to_datetime, and then set

a reminder after that. Let's then run this and

see how it does. Claude initially tells us

that it needs to figure out 177 days after January

1st. Once it figures that out, it's then going to attempt

to set the reminder. Then we see a log statement right here.

This log statement is coming from the set_reminder function. Remember,

set_reminder doesn't actually do anything, it just prints out the arguments

that it's given. And then finally, we get a response from Claude

telling us that our appointment has been set on the correct

date of Monday, June 27th of 2050.

We can also go down to the message conversation history.

So once again, we've got the user message, the

assistant right here that has a text block.

And in addition to the text block, once again, a tool

use block. So yet again, we're seeing an example here of a message

with multiple different blocks inside of it. We then respond

with the tool results. We then get some follow up. And from

there, I think you understand the process. All

right, so that's it. We have wired in multiple different tools

to our notebook. Excellent progress.

---

#### Lesson 41: The batch tool

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289189](https://anthropic.skilljar.com/claude-with-google-vertex/289189)

**Video:** 06 - 010 - The Batch Tool.mp4 | **Duration:** 8m 26s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

I've now repeated several times that a single assistant message

can have multiple tool use blocks inside of it. So for

example, if we ask Claude to evaluate 10 plus 10 and

30 plus 30, Claude might send us back an assistant

message that has two separate tool use blocks inside of it.

Claude has realized that these two operations can be ran in

parallel. So we can do both tool calls

at the same time and then send a single follow-up back to Claude

that has the results of both evaluations.

However, we'll notice that in practice, getting Claude

to do this can sometimes be a little bit challenging. Let

me show you why. So back inside my notebook,

I've updated my prompt. I'm now asking Claude

to do two tasks in parallel. I'm asking it to

set two separate reminders on the same date. The

first reminder is going to have that text right there, and there's a

second reminder right there. Now there's no reason whatsoever

that Claude cannot send us back a single response

with two tool use blocks inside of it. But

if I run the cell, we'll see very quickly that that is

not what actually happens. If

I take a look at the messages that get output, we'll

notice that I get back an initial assistant message

that actually only has one single tool use block

inside of it. I then go through another round

of requests right here, and the second assistant message

that I get back has another tool use block. So let

me show you what's going on here in diagram format. OK,

so here's what's happening. We are sending the initial user

message off to Claude asking to set the two separate reminders.

And then in the first response we get back, there's only one

tool use block. We then respond to that with the tool

results, and then we get another tool use block separately.

This additional round of requests right here is completely unnecessary.

Ideally, this is what would have happened. We would have

sent the initial user message off and then we would have gotten back an

assistant message that has two separate tool use blocks inside

of it. One to set the taxes due appointment and

one for doctors appointment. Although Claude has

the ability to send a response back with multiple tool use blocks

inside of it, it doesn't do so quite as often as we might want.

However, there's a little trick we can use to greatly

increase the chance of Claude sending back multiple tool

uses inside of a single message. The trick is

to implement a batch tool. So let me tell you exactly

what a batch tool is. The batch tool is deceptively

simple. This is another tool, just like get

current date time or add duration to date time. The

tools we already put together. So you and I are going

to define the schema and a function for this

tool. We are then going to pass it into Claude, just

like we are passing in all the other tools we have already created.

The batch tool schema tells Claude that it can run multiple other

tools in parallel. If Claude decides that it does

want to run multiple other tools, rather than calling

those tools directly, it's going to instead call the

batch tool. And it's going to provide some arguments that

look like what you see right here. it will be a list

of objects, or each object, is meant to represent

some other tool that Claude wants to call. So

we might have a object right here to represent setting

a reminder for the doctor's appointment, and then another one

right here to represent setting a reminder for taxes being

due. Whenever we get a response back that has

a tool use of the batch tool, you and I are

going to write out some code to take this array of objects right

here. We're going to iterate over it, and we're going to invoke each

of the listed tools here. So you can think of this as

being like an abstraction on top of these tool

use blocks. The issue here again is that Claude

doesn't really want to respond with multiple tool use blocks, so

we're kind of giving it this higher level abstraction that does

the exact same thing as having multiple

tool use blocks. The only difference is that you and I are

handling manually through the implementation of this batch

tool. It might sound crazy that this works, and

I think it kind of is a little bit crazy, but

like I said, it very much is a trick. We are kind

of tricking Claude into calling multiple tools in parallel.

So let's go back over to our notebook, and we're going to try to implement

this batch tool. OK, so back over

here, to help us out inside of the Tools

and Schema section, at the very bottom of it, I have

already provided us a schema for the batch tool.

Whenever Claude decides to call the batch tool, it's going to provide

us a list of invocations. So this list

is a description of all the other tools that Claude wants to

call. inside of this invocations list, there's

going to be a name of some other tool that Claude wants

to invoke and then some arguments to provide to that

tool. I would like to give you a quick demonstration of how

this thing works. So I'm going to collapse that cell. I'm

going to go to our run conversation function

right here, and I'm going to add in that batch

tool schema. I'm

then going to make sure that I run that cell. I'm then going

to go down to the demonstration cell that I have down here, where

I'm asking Claude to do two things, hopefully in parallel.

And now I'm going to run this again. Before I look at the results,

there's something very important that I want to point out here. We

have now added in the batch tool schema, but we haven't actually

provided an implementation for it. So in other words, there's

no code to actually take that list of invocations

that Claude wants to do and actually run them. So that's

something we still have to implement. Let's take a look

at the list of messages and see what Claude decided to do.

All right, so we've got our initial user message, and then a

follow-up assistant message. Inside of that, there is

a text block, and then a single tool use block.

And if you look carefully, Claude did in fact decide

to use the batch tool. So Claude wants to run

two separate tools. We can see them listed out inside the

list of invocations. So we are going to make two

separate calls, one to set reminder with

the content of I have a doctor's appointment, and then a second

with content of taxes are due. So

it is clear that Claude has decided to use the batch

tool in order to parallelize the two separate

set reminder calls. So now all we have to do is provide

an actual implementation for the batch tool. Let me show you how

we do that. First, I'm going to scroll up to

our run tool function. Here it is right here. I'm

going to add in an additional else if case.

So if Claude wants to run the batch

tool, I will return a call to a new function

that we are going to implement named run batch.

And I'll once again do a star star tool input.

I'm then going to implement the run batch function just right above

this one. So we'll add in a run batch.

It's going to take in a list of invocations. And

I'll default that to be a empty list. Inside of

here, we are going to write out some logic very similar to what we did

down inside of run tools. So we are going to iterate over

all the different invocations that Claude is asking for. We're

going to run the appropriate tool. Well, then formulate some

kind of response, add all these different responses

into a list, and then return a list at the very end. So

here's how we do that. First, I'm going to make a list

that is going to hold the output from all these different tool calls we

make. I'm going to name it batch output. I'm

going to make sure that I return that at the bottom of the function. In

between, I'm going to iterate over all the different invocations that

Claude requested. So for invocation in invocations,

I'm going to extract out the name of the tool that Claude wants to run along

with the arguments to it. Now

the arguments that are being passed in here are encoded as JSON.

So we need to parse that JSON using the JSON module, which

we already imported right there. So I can wrap that with a

JSON load string. Then

we're going to run the requested tool by making

use of the run tool function right here. So run tool,

it already takes in a tool name and some arguments and calls

the appropriate tool. So we can leverage that to make sure that we call the

appropriate tool. I'll get some

tool output by calling run tool

with the name and arcs. Then

I'm going to add in a new record to our batch output list

that's going to describe this invocation and the results that

came out of it. So I'll add in a batch

output, I'll pen to it, a

tool name of name and

a output. of

tool output. Let's now test this out.

I'm going to make sure I run the cell. I'll then go down

to my test cell at the very bottom. I'm going

to run this again. And now that we have provided an actual

implementation for invocations, we should

see very quickly two separate reminders being set

absolutely in parallel. Very good. Definitely

worked. If we take a look at the listed messages, we are

once again getting our assistant block right here. It has

a tool use block that is trying to call the batch

tool with the two separate invocations right

there. And then we are responding with a two result.

And inside of that, we can see the results of our two separate

calls to set reminder. The output is null, which is

expected because right now the set reminder tool doesn't actually

return anything.

---

#### Lesson 42: Tools for structured data

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289181](https://anthropic.skilljar.com/claude-with-google-vertex/289181)

**Video:** 06 - 011 - Tools for Structured Data.mp4 | **Duration:** 7m 56s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Earlier on inside this course, we spoke about how to get structured

output from Claude by using some clever techniques.

In particular, we discussed using a message pre-fill

and stop sequences, along with a carefully structured

prompt in order to get some JSON out of Claude.

Now, this definitely worked well, and it was very

easy to set up, but we can get some more reliable

output by a very clever use of tools.

So we're going to take a look at how we can implement structured

output using tools alone without having to

worry about any message prefilling or stop sequences. Now,

I anticipate one of your very first questions is going

to be, why did we learn about this style

of structured output when we could have just used tools all along?

Well, the answer is very simple. Using tools for structured

output is a lot more set up. There's a lot more complexity.

So having both these abilities of getting structured

data at your disposal is really valuable because

in some scenarios, you might want to just make use of this prompt

based structured output. In other scenarios, you might want

to make use of tools. All right, so let's take a look at how

we can make use of tools to generate structured data. Now,

as I just mentioned, this is an alternate method of extracting

structured data, primarily JSON, out of some

data source. This is more reliable than past techniques

we took a look at, but again, much more complex

to set up. The general idea here is that we are going

to write out a JSON schema spec for a tool

whose inputs are going to be the structure

of data that we are looking for. So back

over here a moment ago, when we looked at this prompt, we can imagine

that we were asking Claude to take a look at a financial statement

and extract a balance that was an integer and

a list of key insights that was going to be a list of strings.

So if we wanted to approach this using tool-based

structured outputs, we would write out a JSON schema

spec where the inputs would be a balance that's

going to be an integer and key insights that's going

to be a list of strings. Then

we're going to feed this JSON schema spec into

Claude along with the financial data that we might want to

get some information out of. Now, at this point, let me show

you a diagram of the flow because it's a lot easier

to understand in diagram format. Okay,

so just as before, we are going to write out a reasonable

prompt for Claude. So we might say, analyze a filing

financial statement and then call some provided tool. Along

with this prompt, with all the statement data inside of it, we'll

also provide that schema. So that's going

to go off to Claude. Claude is going to take a look at the prompt.

It's going to see the tool that is available to it and it's going to say,

ah, fantastic. I will call this financial analysis

tool and I'll make sure that I provide arguments that

match this structure right here. So

Claude is then going to respond back to us with a tool use block.

Inside that block, it's going to ask to call the financial analysis

tool. And the input to it is going to be the exact

input that we specified inside of this financial

analysis schema. So we will get back a balance

that's an integer and key insights that's a list

of strengths. Once we've got that data, we are all done.

So unlike usual tool calls where we would usually

respond with a tool-result block, we don't have

to do that here because our only goal was to get the extracted

JSON right here. That's it. So once we get the

assisted message in response, we kind of just

say to Claude, thanks to the JSON, we're done and we're

not going to make any more follow-up requests. The last thing

I want to mention is that a critical part of this technique is

to make sure that Claude calls the tool that we have provided

to it. To force Claude to call a specific tool,

we can provide a tool choice parameter when

we call the clientmessages.create function. Specifically,

we can provide a tool choice that is a dictionary with

a type of tool and the name of the tool

that we want to force Claude to call. So in

this case, if we provide a schema that has

a name of analyze financial statement, we would

put in analyze financial statement right there like so.

Now that we've got an idea of how all this works, let's go back

over to our notebook and get some hands-on experience.

Back over here, I'm inside of a new notebook called 002

Structured Data, and it should be attached to this lecture. It

has all the same code as the previous notebook we were working

on. The only difference is I added in this additional cell down

here at the bottom. This cell is going to ask Claude

to write a one paragraph scholarly article about computer

science and to include a title and author name.

I'm going to run this really quick and just take a look at the generated

article. This article has a title and

author name, and then some text to go along

with it. So I want to try to extract some JSON

data out of this text. In particular, I want to

extract the title as a string, the

author as a string, and then I want to extract a

list of strings that contain some key insights

out of the article. To do so, we are going to write out a

schema definition for a new tool. Our schema

is going to make it clear to Claude that in order to call that

tool, it must provide arguments of a title

that's a string, an author that's a string, and then a

list of key insights. There are going to be a list of strings as

well. And remember, the easiest way to put

together a new tool definition is to make use

of Claude itself. So I once again have opened

up my browser. I've got the documentation open

on tool use right here. I'm going to again just copy the page.

I'm going to ask Claude to write out a tool schema for a function

named Article Summary. And this function should

be called with a title, this is string, an author that is a

string, and a list of key insights. I'm

going to paste in the documentation and

run this. In response, I'll get back my article summary

tool definition. So I'm now going to copy this,

take it back over to my notebook. I'm going to go up to

the cell that has all of our other tools and schemas. I'm

going to paste it in here and I'm going to call

it article summary schema.

There we go. I'll make sure I run that cell as well. The

next thing I would like to do is update our chat function implementation.

So in the cell right above, helper functions, I'll

find the chat function. Remember that a key aspect

of this JSON extraction operation is ensuring that Claude

always calls your specific tool that you have made. So

we want to make sure that our chat function can take in a tool

choice argument, and that the tool choice will be passed

on through to our actual client messages

create function call. So back over here,

I'm going to add in yet another argument of tool

choice. And again, I'll default it to be none. We're

then going to set it up in the same way that we set up tools right here. So

if a tool choice is provided, then

params.tool_choice is

going to be tool_choice. I'll make sure I

run this cell as well. And I think we have everything

we need to do a little test here. At the very bottom of my

notebook, I'm going to add in a new cell. So

down here, I'll add in messages. I'll

add a user message.

And I want to add in the text that we just got back from the

previous cell's response right here. So I'm going to add

in some text

from message, response. So

that's going to take all the text out of this response and

add in as a plain user message. I'm

going to call chat with a list of messages. Then

we need to provide our list of tools, which is going to be just

the article summary.

schema. And then finally, we want to force

Claude to call that particular tool. So we'll put

in a tool choice, which

will be a dictionary with a type of

tool and a name of article

_summary. And then I'm going to save

this file just to reformat the code. There we go. That looks

a little bit better. All right, let's now

run this and see what we get back. Inside of the

response message, we have a tool use block that

has a inputs as usual. And the inputs here

is going to be a dictionary with all the data that we asked for.

So there is a title, there is an author, and

then key insights, which is going to be a list of

different strings. So if we wanted to just access

that data alone, we could assign the results

of calling chat to response and then print out response.

content[0].input like so. So let me

run this again and now we've got our structured data.

---

#### Lesson 43: The text edit tool

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289180](https://anthropic.skilljar.com/claude-with-google-vertex/289180)

**Video:** 06 - 012 - The Text Edit Tool.mp4 | **Duration:** 8m 41s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

As we saw earlier on inside this module, usually

you as developers author all the different tools

that we want to pass off to Claude. But there is one tool

that Claude has access to by default. This

is called the Text Editor tool, and it is built

directly into Claude. This tool gives Claude

a wide variety of abilities related to just

about everything you can do inside of a standard text

editor. So for example, this tool gives Claude

the ability to open up files or directories

and read the contents. It can take a look at specific

ranges of text inside of a file. It can

add or replace text inside of a file. It can make

new files. It can do undo. Essentially,

everything you would do inside of a normal text editor.

So this dramatically expands Claude's abilities and

almost right out of the gate kind of gives Claude

the ability to act as a software engineer. Now,

understanding the text editor tool is just a little

bit confusing, so I want to walk you through a couple of different diagrams

and clarify what this tool does for you and

what you and I have to do to actually make

use of it inside of a project. So the first thing to understand

here is that only the JSON schema part

is actually built into Claude. And let

me clarify what I mean by that. Remember

that when we want to make use of tools, we really have to author

two separate things. First, on the left hand side,

we have to write out that JSON schema spec. This

gets provided off to Claude and tells Claude about some

tool that it can make use of and all the different arguments that

the tool requires. And then on the right-hand side, you

and I had to write out a tool function implementation

to pair up with that JSON schema. These were

actual functions implemented inside of our code

base that would be called at some point in time when

Claude wanted to use our tool. So we really

had to write both sides here. We had to do both the JSON

schema and the tool function implementation.

So when we make use of the text editor tool,

the only thing that is actually kind of provided for us

or built into Claude is the JSON

schema. That's set of instructions that tells Claude

how to make use of this tool. You

have to provide an actual implementation

to handle all of Claude's requests to use the text

editor tool. That does not exist. It is something

that you have to write out inside of our codebase.

So in other words, whenever Claude decides to say,

maybe create a new file, and it sends back a

tool use part to us that says, I want to create

a new file, we have to provide an actual function

that will actually make a new file somewhere on our

hard drive. So using the text editor tool

is not free, so to speak. It requires a little bit

of effort on our side because we have to write out a couple

of different functions. Now, let's go over to

a Jupyter notebook, and we're going to demo the use of this tool

and take a look at how we would write out some of these different

functions. Back over here, I'm inside of a new notebook

called 005 Text Editor Tool. As usual,

you can find this notebook attached to this lecture. Inside

this notebook, there's a lot of the exact same helper code that we've

been working with so far. But if you take a look at the third

cell down, which has a comment at the top of, implementation

of the text editor tool, you're going to see that there is a tremendous

amount of code inside of here. So this is a class

that I put together ahead of time. It contains all the different

functions that are required to use the text editor tool. So

in other words, this class provides this piece of the

puzzle over here. Remember, I just told you a moment ago

that we have to write out some code to handle all of the Claude requests

to use the text editor tool. I wrote out that code

for you inside of this particular class. Inside

of this class, you'll notice that there are some methods, if you scroll down

a little bit, like view, which can be used to view the

contents of a file or a directory. There is also

a string replace function, which will replace a

string inside of a file. There is a function to create

a file and so on. So everything has already been

provided for you inside of this class. I'm going

to collapse this cell. And the next thing I want to point out to

you is the cell with the comment of make the text edit

schema based upon the model version being used. Now, this

is where things get just a little bit confusing. So let me very quickly

show you a diagram to help you understand what's going on here.

Now, I've repeated several times that this text editor

tool schema is already built in the Claude, and we do not have

to include it. That's kind of mostly true,

but also just a little caveat here, just something to make

it slightly confusing. When we make our request

off to Claude, and we want to make use of this text

editor tool, we do need to include a very,

very small schema. So we need to send a lot of a schema

that's going to look like this right here. The exact

type string that we put in here, notice how it has a date, is

going to change depending upon the exact version of Claude

that we are making use of. So inside this function, I

am checking to see if you are making use of Claude 3.7 Sonnet.

And if you are, I'm going to return that schema that

has a date of that right there. And if you're making

use of Claude 3.5, it's going to have a slightly different date.

So you are going to have a slightly different date

depending upon the exact model version. When

we send this very small schema off to Claude, it is going to be

automatically expanded into a much, much larger schema.

That looks a little something like this. So Claude

is going to see that we are including this very small

stub schema that has a name of string replace editor.

And it's also going to notice the exact type that we are putting right there.

Then behind the scenes, we can imagine that this very small

schema gets replaced with this much larger one. That

lists out a ton of information to Claude on exactly

how to use the text editor tool. Now

that we have a slightly better idea of what's going on here, I'd like

to give you a quick demonstration of what the text editor tool

can do. Inside of the same directory as my notebook,

I'm going to make a new file called main.py. And

inside there, I'm going to make a very simple function called

greeting. that will print out hi

there, like so. I'll then make sure that I save that file.

I'm then going to go back over to my notebook and down at

the very bottom, I've added in a cell that's going to

add in a empty user message and then send the list messages

into run conversation. I'm going to ask Claude

to open up the main.py file and just

tell me what is inside this file. So I'll ask

Claude to open the ./

main.py file and summarize its

contents. I'll then run that. And

then inside the response, we can see that Claude did,

in fact, get the contents of that file. And it's going to be

a summary of what's going on inside there. If we take a look

at the list of messages, we'll see that we get a tool

use block right here, where Claude is asking to view

the contents of the main.py file. The

code inside of that text editor tool class that

I showed you a moment ago is going to receive that command. It's going

to open up the file automatically, and then send that contents

back over to Claude. We can actually see the contents right

here. Now, at this point, you might be kind of curious why

the text edit tool exists at all. In other words, what does

it really do for us? What functionality does it really offer besides

the obvious fact that it can somehow work with files on the file

system? Well, chances are right now you

are making use of a code editor that has a really

fancy AI assistant built into it. And you can ask

that assistant to refactor files or create files

or do whatever else. It turns out that we can largely

replicate all the functionality of your fancy code

editor by just making use of this text edit tool.

So for example, I'm going to update the prompt that I'm sending

off to Claude. I'm going to ask Claude to open up that file

and write out a function to

calculate pi to the fifth digit.

And then after doing so, I'm going to ask Claude to then

create a ./test.py file

to test your implementation. I'm

going to run this. After the request is complete,

I'm going to scroll down to the list of messages that were exchanged.

So down here, I've got my initial user message, then

our assistant message, in which Claude decides to use the

text edit tool, and specifically, it wants to try to view

a file. We then send back the contents of that file.

Claude then says, OK, great. I know it's inside this file. I'm

now going to try to replace its contents by writing in some

new content. So we can see right here is

the actual implementation of calculating pi.

Then if we go a little bit further down, we respond

and say that we did the update to the file successfully.

Claude is then going to attempt to create the test.py

file and write some text into it, specifically some

test to test out the implementation it just put together. We

can verify that this all happened by taking a look at

the newly updated main.py file. So

we will now see an implementation for calculating pi, and

then an accompanying test.py file as well, where

we've got some tests. So once again, using

this tool, we can very easily approximate a rather

fancy code editor. And you might be thinking,

OK, why don't I just use my code editor? Well, there

are probably going to be some scenarios on some different applications

you might work on, where you might want to edit some files

inside of some file system, or something similar, where

you don't really have access to a native, full-featured

code editor. And this would be a scenario where you would

want to make use of the text edit tool.

---

#### Lesson 44: The web search tool

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289183](https://anthropic.skilljar.com/claude-with-google-vertex/289183)

**Video:** 06 - 013 - The Web Search Tool.mp4 | **Duration:** 7m 13s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

There's another tool built directly into Claude

named the web search tool. As the name

implies, this tool allows Claude to search the web

for up-to-date or specialized information to answer

a user's question. For example, if we ask about

current events in quantum computing, Claude might decide

to use this tool to find some up-to-date articles related

to quantum computing and then use that content to

formulate an answer. Unlike the text editor

tool, we do not have to provide an implementation

to actually run the search. The search is done entirely

by Claude, and this makes this tool really easy

to run and use. Let's write out some code to

understand how this tool works. I'm back inside of a

notebook. I've created a new one called 006 web

search. And I've got a cell down here at the bottom with some typical

code for running a request off to Claude. In

the cell right above, I'm going to create a new variable called

web search schema. This is

going to be a schema that we author that we are going to include

in our request off-to-Claude, and we're going to list

it as a tool. This schema is going to enable

the web search functionality. So just like the text editor

tool, we have to provide this very small schema that

behind the scenes is going to get expanded into a much larger

schema. We're going to add in a couple of fields here,

in particular a type with web

search underscore 2025 0305

than a name of web underscore search, a

max uses of five, and

that's it for right now. Now the max uses is

the number of times that Claude can run a search.

A single search can return multiple different search results, but

depending upon the content in those search results, Claude

might decide to do a follow-up research. This

process can repeat several times, so we are capping the number

of times that Claude can search in total to just five.

I'm going to go down here after running

that cell. And I'm going to ask Claude what's

the best exercise for gaining

leg muscle. And I'm going to add

in that schema that we

just put together. So web search schema

like so. Now I'm going to

run this, and it's going to take a little bit of time to

get a response back. The response we get back

is going to be quite large, so I can scroll through

it here, and we're going to see that there is just a tremendous amount

of information here. So to help you understand the response we

got back, I want to show you a little part-down version

of this response, where I took this messages,

content list, and I removed a ton of content out of

it just so we can better understand what is going on. So here

is a slightly redacted form. Again,

this is the content list inside the response message.

The content list is going to contain several different blocks, several

blocks we have not seen before. Initially, we

get back a text block, which is kind of framing the entire

response that Claude is giving us. Claude is saying that it's

going to do a web search to better understand how to answer

the question. Then we're going to see a server

tool use block. And inside there is the

input to the search tool. We can see that's the exact

query that Claude is going to use to search the web.

After that, we're going to see a listing of web

search tool result block, and inside there are going to be many

different web search result block. These are

the different search results that Claude has received

from that initial query. Now, an actual query

response will probably have many different search results. In this

case, I removed all of them, but one, just to better understand

what's going on here. So this is an actual web

search result. We can see the title of the page that

Claude fetch, and the actual URL. There's

no content inside of here just yet. This is just telling us

exactly what Claude found when it did this search.

then Claude is going to begin by answering the user's question.

And it's going to answer the user's question with a variety of different

text blocks that might include a citations list.

The citations list is text that is supposed to support

the statements that Claude is making in some way. So

in this case, Claude has cited some particular web

page right here. And it is using this specific

text to support the point or the argument

that it's trying to make. When we define the web

search schema, there are a variety of different fields that we can add

in. There's one field in particular that I really

recommend you consider using if you ever have a good understanding

of exactly what your users are going to be asking

about. So in our case, we asked about

the best leg exercises for gaining leg muscle.

I don't know if you've ever searched online for exercise advice,

but there are a tremendous number of blogs out there

with probably just AI-generated content. And

the advice that you get out of those blogs might not actually

be the most accurate, or even the best idea of how to actually

gain leg muscle. On the other hand, there

are some websites that collect different publications such

as PubMed. So this is a website maintained

by the US government. It contains a ton of

different scholarly articles around medicine. So

we could search through here and find a tremendous amount of evidence-supported

exercise advice. So it would be really

fantastic if we could somehow tell Claude to only search

this web page and content inside of it. That would

allow us to make sure that we are giving the best possible advice to

our users and not just some randomly generated stuff

that we found online. In order to get Claude

to only search this page, we're going to find the domain,

which is nyh.gov. I'm

going to go back over to my notebook. I'm going to find my web

search schema, and I'm going to add in an additional field here

of allowed domains. I'm going to put in

a list with NIH.gov. This

is going to constrain Claude Search to only that

domain right there, and it won't try to find anything else. So

now if I run this cell again, and then

make my request off to Claude again, I'm going to have to wait

for the response to come back. But when we

do get a response, we should be able to scroll through it a little bit

and eventually see that we have a URL right

here. And we should only have URLs belonging to the NIH.gov

domain. We shouldn't see anything else. So again, this

will allow us to make sure that we are giving at least some scientifically

supported advice to our users. Now, last

thing I'm going to do is show you exactly how we are really intended

to use this giant list of different types of blocks

that we get back when we make use of this tool. The

thought process here is that you're going to render all

the text blocks as plain text, and then

whenever you get a web search result block or

a citation web search result location,

you might render those out inside the UI in such a way that makes

it obvious to a user that you are trying to support your information

in some way. Here's an example of how you might do that.

I wrote out a small page that is going to take all

those different blocks we saw inside the response message and render

them out. At the very top right here, I've got a list

of all my web search tool result blocks.

So these are the different pages that Claude found when it did the web

search. I'm then going to iterate through the entire

list of blocks and show the text out of every single

text block. Whenever I found a text block

that has a citation web search result

location, I know that's a long term, so

it's one of these right here. Whenever I find

one of those, I might render it with a little citation

like so, where I'll show the domain, show the

title of the page that I found, show the exact address

of it, and then the exact cited text as well.

Again, this just allows our users to better understand

how Claude is actually getting its information.

---

#### Lesson 45: Quiz on tool use with Claude

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289280](https://anthropic.skilljar.com/claude-with-google-vertex/289280)

---

### Retrieval Augmented Generation

#### Lesson 46: Introducing Retrieval Augmented Generation

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289191](https://anthropic.skilljar.com/claude-with-google-vertex/289191)

**Video:** 07 - 001 - Introducing Retrieval Augmented Generation.mp4 | **Duration:** 5m 51s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this module, we are going to discuss a tremendous

amount about a technique referred to as retrieval

augmented generation, or rag for short.

In this video in particular, I want to give you a really solid idea

of what rag is all about. To help you understand

rag, we're going to walk through a very quick example.

So I want you to imagine that you have a very large

financial document, like the one seen on the right-hand side. There

might be a tremendous amount of text in this. It might

have anywhere from, who knows, a hundred to a thousand

pages. And we might want to ask, Claude,

very specific questions about very specific areas

of the document. For example, we might want to ask a

question like, what risk factors does this company

have? Now, presumably, this document might have

some relevant information inside of it. So we

need to solve a very fundamental issue here. How do

we get some information out of this document and into Claude

so it can help us answer our question? I

want to show you two possible ways that we could solve this problem.

So option number one, we could take all

of the text out of this document and just place it directly

into a prompt, like the one you see on the right hand side. So

we might ask Claude to answer a user's question, we'll

then put in the user question, and then take all the

text out of the document and put it into the prompt as well.

Now, this is perhaps not the best solution.

It might work, it also might not. Just so

you know, there is a hard limit on how much text we can

feed into Claude. So if this document is really,

really long and we take all the text out of it and feed all

the text into Claude, we might immediately end up getting

an error, which means just right off the gate, this

solution would not work if our document is really,

really long. The second problem with this approach

is that Claude gets a little bit less effective as

your prompt gets longer. So if you start putting

a tremendous amount of text into a prompt, Claude

is going to have just harder time understanding exactly what

you want and answering your question because there is just

a tremendous amount of information inside the prompt. And

then finally, larger prompts cost more

money to process and take longer to process.

So there's a financial burden here as well and a

user experience burden because they just have to wait

around longer to get back some kind of answer. So

option number one might work in some scenarios, in

other scenarios, it might fail entirely. So

at that point, let's take a look at option number two. Option

number two is a little bit more complex. So Option

number two has two separate steps. In step

one, we'll take all the text out of the document and

break it up into small chunks. Then

whenever a user asks a question, we're going

to take their question and put it into the prompt as before.

But we're also going to go through an extra little step. We're

going to examine the user's question very closely. And

we're going to find a chunk of text that seems

most relevant to the user's question.

In this case, if a user asks us what risk

does this company face, and we have a chunk of text

right here that seems to be about risk factors, we

would then take that chunk of text and include

it inside of the prompt. So

now we are focusing all of Claude's attention on just

this very small snippet of the overall financial document.

And hopefully Claude can do a much better job of answering

the user's question than before when we were just putting

all of the text of the document into the prompt.

So option number two has a distinct set of upsides

and downsides. The upsides here are that

Claude can focus on just the relevant content. Secondly,

this can scale up to really, really large documents

with a tremendous number of pages. And it

also works if we have multiple documents. We can

take all these different documents, separate them all into chunks,

and then once again, only include chunks relevant

to user's question inside of a prompt. This

technique also generally leads to much smaller prompts, which

means it's going to take less time to run and it's

going to cost us a lot less. But there

are some big downsides to this approach as well. First

off, there's just naturally a lot more complexity.

This requires a pre-processing step, where we take all

the text out of the document and split it into

chunks. We also have to figure out some way

of searching through all these chunks to find the ones that are most relevant

to the user's question, and we even need to define

what it means to be relevant to the user's question.

When we do find some relevant chunks and include them in the

prompt, there's really no guarantee that they will

contain all the context that Claude needs to actually answer

the question. If the user asks what risk does this

company face and include only the risk factor

section, that might include some other important area

of the document, maybe strategy outlook, where some

of those risks get addressed in some way. And

then finally, there are many different ways in which we can split

the text up. So we could just take all the text of

the document and divide it into equal portions.

Or we could go through the document and find all

these different headers and say for every header,

we're going to make a new chunk. So we might have chunk one and

then two and then three somewhere down here. There

are many different ways in which we can define what a chunk is.

And so we have to do a little bit of evaluation and decide

which technique is the best for our particular application.

So as you might guess, option number two is

rag. It is retrieval augmented generation. As

we just discussed, rag has many big

upsides and many big downsides as well. There's

a lot of technical challenges around it. It requires

a pre-processing step. We also have to figure out some

kind of searching mechanism to find those relevant chunks.

We have to chunk documents. All in all, there's just

a lot more work than option number one. So

whenever we are considering implementing rag inside an application,

we really have to analyze all these different steps and figure

out whether or not it is right for our particular use case.

All right, so now we have kind of a very, very high level

understanding of what rag is all about. Let's start

to take a look at the actual implementation of this process

in just a moment.

---

#### Lesson 47: Text chunking strategies

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289208](https://anthropic.skilljar.com/claude-with-google-vertex/289208)

**Video:** 07 - 002 - Text Chunking Strategies.mp4 | **Duration:** 13m 8s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Inside of this video and the next couple of videos, we're

going to start to implement our own custom RAG workflow

inside of a series of different notebooks. We're going to first

focus on just making the most simple basic RAG

setup we can possibly make, and then we're going to add in some additional

steps over time. Now, as a reminder, a typical

RAG pipeline looks a little bit like this to really simplify

things. We're going to take a source document, break

it up into chunks of text, then whenever user asks

us a question, we're going to find some relevant chunk of text,

put it into a prompt, and that's pretty much the entire thing.

So step one of this entire flow is to take a source document

and break it up into chunks of text. Now believe it or

not, this process of taking a document and breaking

it up into separate chunks is one of the more complex

steps of the entire RAG pipeline. Simply because

how we chunk our document up has a huge

output on the quality of our RAG pipeline. And

I want to give you an example right away to help you understand

why that's the case. So take a look at

this source document. It's just a couple of little lines,

and it's supposed to represent some kind of report from a

company or something like that. And just reading

through it really quickly, we can see that there's really three general areas.

We have a header, we have a section about medical research,

and then a section about software engineering. Now

there are many ways in which we could divide this thing up into

separate chunks, but I'm just going to suggest one way. I'm going to say

for every kind of distinct line inside this document, we're

going to make a separate chunk. So we'd end up with about five separate

chunks like the ones you see right here. If you consider each of these

different chunks now, you will notice something really interesting.

The third chunk of text right here is all

about medical research. That's what this text is about. It was

inside of the medical research section. But it contains

the word bug. So at kind of a high level,

if you just glanced at this paragraph alone, it

is almost like it's kind of about software engineering, just

because it contains the word bug. And then likewise,

down here, we have the software engineering section, and

inside of it is the word infection vectors. Infection

vectors is a little bit more of a medical term. So

once again, we have a section that is about software engineering,

but the language inside of it is kind of about medical research.

So now we want you to think about what would happen if we took these

chunks and we added them into our RAG pipeline.

Let's imagine that a user asked a question of something like,

how many bugs did engineers fix this year? So

now our job as a part of the RAG pipeline would

be to find the chunks of text we have that

are most relevant for the user's question. Well,

the user said something about bugs. So, well,

at first glance, this chunk of text right here seems relevant,

just because it contains the word bug. So we might

decide to take this chunk of text and add

it as context into the overall prompt.

And as you can tell right away, this is a huge error.

The user wants to understand something about software engineering

from the report. So we definitely wanted this section,

but we erroneously got something about medical research

instead. So this is an example

where a chunking strategy can easily introduce

huge errors and very bad context inserts

into your prompt. So to solve this problem, we're going to spend a lot

of time thinking about how we're going to take our original source

document and break it up into different chunks of text.

In this video, we're going to cover three different chunking

strategies or methods to divide our document

into separate chunks of text, each of which have some

feature or some technique meant to address the problem that

we just saw. So we are going to discuss size-based

chunking, structure-based, and semantic-based.

The first one we're going to cover is size-based chunking.

This is where we take our big old document, so a big

chunk of text, and we just divide it into a number of strings

of equal length. This is by far the

easiest technique to implement, and in some, also

probably the one you're going to see most often in production implementations.

So let's take a look at how size-based chunking is done. With

size-based chunking, we're going to take our original document and

divide it into some number of strings of more or

less equal length. In our particular case,

we have a source document with about 325 characters.

So we could decide just completely arbitrarily to

divide that into three separate chunks. And that means each

chunk would have about 108 characters or so.

So we might take the first 108 characters,

put them into chunk 1, the next 108 put them into chunk

2, and just repeat for the entire document.

Now, very simple technique, but right away it has

a big downside. And that is that each chunk is

probably going to end up with some number of cutoff words

inside of it. You can see right away the first chunk has

the word significant cutoff. So it's just significant

key. in the first chunk and then ends the word in the next

one. In addition, each chunk ends up lacking

context. So for example, the third chunk

down here unfortunately does not really include the section

header that was right above it. And this section header would

have provided a lot of context on what this text right

here is really talking about. So to solve

this problem that starts to come up right away if you use size-based

chunking, we can implement a overlap strategy.

An overlap strategy is where we are still going to do size-based

chunking, but we're also going to include a little bit of overlap

from the neighboring chunks. So for example, we have

the original chunk one right here, but we

might decide to include just a number of characters from

the next chunk down. So in this case, we might

include the rest of the word significant plus the end

of that entire sentence. So we would end up with

a chunk that looks like this that just has a little bit more meaning to

it. And then for chunk 2, we would still

have the body be this area right here, but we'd

include an overlap of some number of characters from

before the chunk and after the chunk. So with

the strategy, we are going to end up with a decent amount of duplicated

text. For example, in this case, we have section

1 medical research inside the second chunk, and that

was also included inside the first one as well.

So there is duplication of text, but the upside

here is that each chunk of text has, in general, a little

bit more context provided for it. The

next kind of strategy that you're going to see is structure-based

chunking. This is where we are going to divide off the

text based upon the overall structure of our

document. So we might try to find headers or paragraphs

or general sections and use those as our dividing

lines for each chunk. Implementing this strategy of chunking

with our document would be really easy because our document

is written with markdown syntax. We know that because it has

a little pounds right here, the double hashes

for each section. So we might look for these little

pound symbols, and then say that every time we see this kind

of symbol, that means we must be starting a brand new section. So

we could very easily write out some code to programmatically split

on the double hash characters. And we would end up with some

pretty well-formed sections, like what you see right here. Now

this might sound like a fantastic strategy, but unfortunately,

reality just doesn't favor it quite so often.

In many cases, you are going to be trying to ingest documents

that are not formatted with Markdown syntax at all. They

might be plain PDF documents that just contain

plain text, in which case you will not get these

very clearly delineated sections. So

again, even though this seems like a great technique, implementing it

can be really challenging, especially if you do

not have any guarantees around the structure of your

different documents. The last chunking strategy that we are

going to discuss is semantic-based chunking. This

is where you might take all of your text, divide it up into

sentences or sections, and then use some kind

of natural language processing technique to figure out how

related each consecutive sentence is.

you'll then build up your chunks out of groups

of these somehow related sentences or sections.

Now, as you can tell just by the description, this is by

far definitely more advanced technique, so we're

not going to look too closely into the actual implementation. The

only reason I mention it at all is just to make it clear that

there's really no set finite fixed number of chunking

strategies. There's really an infinite number of

ways in which we can decide to divide up our text. And

so deciding upon which method you use really comes down to your

particular use case and what guarantees you have around

the documents that you are trying to ingest. Now

before we move on, I want to go over a very quick example

with you. So I've got a Jupyter notebook put together

with three different chunking strategies implemented inside

of it. So I would encourage you to find a notebook called 001

chunking. Also make sure that you download the accompanying

report.md file and place

it inside the same directory as that notebook. This report.md

file has a little sample kind of fictional report

inside of it that we're going to use for testing purposes as

we learn about how to implement a RAG pipeline. So

inside of here, you'll find a couple of different cells. The first one

contains a sample implementation of a chunk

by character. So this is an implementation based

upon the size-based strategy, where we are going

to divide up our text into strings of equal length that

also have some amount of overlap on them.

You'll notice that the arguments are going to be the text, the

size of each chunk, and then some amount of chunk

overlap. So again, that is the number of characters we want to have

on either side of the chunk. The next cell shows

how we might chunk by sentence. So very similar idea,

but now I'm using a regular expression to split

the text up into individual sentences, and then

each chunk will be formed out of some number of sentences

with optionally a little bit of overlap on each side.

And then finally, if we have really strong guarantees

around the structure of our document and its exact contents,

we might try to use a chunk by section, which would be

an example of structure-based chunking. So

in this example, it's going to look for a new line character, and

then two pound signs, and then a space. And that

is going to be our separation criteria. So we would

get kind of executive summary

would be the first chunk. Well, technically the second one, this

would be the first chunk up here. But then we would get everything

inside the executive summary all the way down to the table

of contents that would start off our second chunk.

And then the next chunk would be the methodology and then section

one and so on. This will give us the best formatting

for each chunk, because each chunk will consist of exactly

one section, but it really only works because

we have a guarantee around the structure of the document. We

know it is marked down, and we know that we're only going to see

that new line, pound, pound space, in

the case that we have a new section beginning. Now let's

test each of these really quickly. So back inside my

notebook, I'm going to go down to the bottom cell and

I'm going to first try out the chunk by character. So

I'm opening up the file, getting all the text out of it. I'm going to

chunk by character and then just print out each chunk with

a little separator between each one. So I'll

run that. and I will see that we get our first chunk

right here, second, and so on. And right away, you can

see that the default settings do not produce

very good chunks. So the default settings are

a chunk length of 150 with a overlap

of 20. So in this case, each chunk

doesn't really provide a whole lot of meaning. Like, what

does this sentence right here really do for us? And can we really

use it to answer any user question? I

don't know, maybe not. So we might decide to dramatically

change our default settings here. Maybe

I want a chunk length of 500 with

a overlap of 150. Let's see if that gives us something

a little bit better. Okay, that's a little

bit better than what we had before. So now I can

start to see the formation of actual individual sections

here that give us a little bit of information. You'll

also very quickly start to notice the overlaps. So

I can see addressing complex challenges.

Let turns out that exact phrase is included

inside of the chunk right above. So that's an example of

the overlapping that we get. All

right, next up, let's try our second strategy, which

is chunk by sentence. And

again, I'm going to use the default arguments. And

this one actually looks like it's pretty strong. So this should give us five

sentences by default in each chunk with one sentence

of overlap. And we are using a regular expression

to split up each sentence. So there might be

cases where it doesn't split a sentence correctly. But at first

glance, yeah, I'd say this looks pretty good. Each chunk appears

to give us a solid amount of information. And

then finally, we can try out chunk by section.

Now run that. And now we can see that the first

chunk is not going to contain a lot of useful information, but

everything after that is really, really strong because we

are getting exactly a single section each

time. I get just the executive summary, and

then the table of contents, and then section one, section

two, section three, and so on. So once again,

which strategy you use entirely

comes down to the nature of your document

and what guarantees you have around its structure. For

us, chunk by section looks fantastic. But

if we are expecting to receive user-provided documents where

there are no guarantees around the formatting of each document,

then using chunk by section is probably not going to

work out in the long run. In

that case, we might fall back to chunk by sentence. But

even this might not work pretty well, work out pretty well. Imagine

that we are trying to chunk user-provided code, for example.

Well, if we try to split code up into individual

sentences, we are probably going to get a lot of unexpected

results, because code tends to have periods

in very unexpected places. So

that might mean that we just fall back to the old reliable

standard, which is chunk by character. Chunk

by character is not guaranteed to give you the best results, but

it's going to work vast majority of the time and it's going

to work out reasonably well.

---

#### Lesson 48: Text embeddings

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289188](https://anthropic.skilljar.com/claude-with-google-vertex/289188)

**Video:** 07 - 003 - Text Embeddings.mp4 | **Duration:** 3m 45s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

After extracting some number of text chunks

out of a source document, the next step inside of our rag pipeline

is to wait for a user to submit a question or query or something

like that. And whenever that occurs, we need to take a look

at all of our different text chunks and find some number

that seems to be somehow related to the user's question so

that we can add them as context into our prompt.

Now, this process of finding some number of text

chunks that are related to the user's question, oh,

there's a lot of complexity hidden there. But when

we really think about it, this truly is a search

problem. We want to take the user's question and

search through all of our different chunks until we find some

related content and then surface those in some

way. The most common way of implementing this inside of a rag

pipeline is by implementing a system known as semantic

search. Semantic search utilizes something called

text embeddings to better understand what each chunk

of text is all about and somehow find the

chunk of text most related to the user's question. Now

we're going to spend a decent amount of time now to focus on text

embeddings and really understand what they are

doing for us. So let's take a look at a couple of diagrams.

A text embedding is a numerical representation of

the meaning contained in some text. These

text embeddings are generated by something called an embedding

model. We feed text into an embedding

model, such as I'm very happy today, and

the embedding model is going to spit out a long list of numbers.

That long list of numbers is our actual embedding. The

numbers inside the embedding can range from negative 1

up to positive 1. So now the question is,

what do these numbers really mean? Each number

inside of an embedding represents a score of some

quality of the input text. Now, this

is where things get a little confusing because I'm showing two

conflicting ideas in this diagram. Let me break

this down for you and just be super clear. In reality,

we do not know what quality each number inside

the embedding is actually tied to. So when I

label that first number and say, this is a score of how

happy the text is, that's not entirely accurate. We

simply don't know what that first number truly represents.

Nonetheless, it is very helpful to think of these numbers

in that way. It is helpful to imagine that the first

number might be one score of how happy the

text is. And the second is how much the text

is talking about fruit, et cetera. Again, these

labels are completely made up by me, and we don't actually

know what each number represents, but it's extremely helpful

to think about embeddings in this way. So

that's how you really want to picture each of these numbers. They are kind of like

scores of some different qualities of the input

text. The last thing you need to understand is how to actually

generate these embeddings. And Claude cannot make

the embeddings. Instead, on Vertex, we're going to use a slightly

different model. One dedicated, solely to a generation

of text embeddings. The name of the model that we're going to use is

Claude 3.7 Sonnet. Let's

take a look at a notebook that's going to show you how to make use of this model

to generate some embeddings. So back over here, I've

made a new notebook called 002 underscore

embeddings. To access this model, we need to make

use of the Vertex SDK. You can install this

by running PIP install Google-GenAI.

We'll then create a client specifically to access this particular

model. You'll need to fill in your project ID or

right there. To actually make an embedding, I've put together

a helper function for us called generate_embedding. This

is going to take in some amount of text, pass it through

the model, and then return our embeddings.

To test this thing out, I've got a little bit of code down here

that's going to load up our report.txt file, chunk

it by section, and then just pass the first chunk into

that helper function. So I'm going to run this now, and

we'll see what we get back in return. In our response,

we get our big list of embeddings back. So as

you can see, generation of embeddings is not particularly

hard. It's really understanding how we actually use them. So

let's come back the next video and really understand how these embeddings

fit into the larger picture.

---

#### Lesson 49: The full RAG flow

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289190](https://anthropic.skilljar.com/claude-with-google-vertex/289190)

**Video:** 07 - 004 - The Full RAG Flow.mp4 | **Duration:** 8m 0s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

At this point in the module, I've given you a high-level overview

of how that RAG pipeline works. We've spoken a little

bit about text chunking, and we've got just a taste

of text embeddings. So now we're going to take these three

different topics, our high-level overview of the RAG

process, text embeddings and text chunking, and

we're going to merge them all together and really understand the

entire RAG pipeline. So we're going to go through a

complete RAG example and go through a lot of

detail and really understand everything step by step.

So let's get to it. Step number one, just as

before, we're going to take some source document and chunk

it into separate pieces of text. So for this example,

I'm going to assume I just have two pieces of text here,

just section one, medical research, and section two,

software engineering. Step two, we're

going to generate embeddings for each of these different chunks

of text. Now in this example, we're going to pretend

that we have this imaginary super perfect embedding

model. And this embedding model has two very

important characteristics. First, we're going to assume that always

returns embeddings of length two, so just two separate

numbers. And we're going to also assume that we know

exactly what each number is really scoring

about the source text. Remember, in reality, that's not

the case. But in this scenario, we're going to imagine we know exactly

what each number is really talking about. So we're going to say

that the first number is how much the text is

talking about the medical field, and the second is how

much the text is talking about software engineering.

So for the first chunk of text, when we embed it,

this thing is definitely talking about medical research. So

I would give it maybe a score of .97 to say, yes,

absolutely, this is very much talking about the medical field.

And then it also uses the term bug, which has a

slight software engineering connotation. In addition,

medical itself is pretty heavy on software

engineering. So I'm going to give it a score of .34 for software

engineering. then for the second

piece of text here. Well, it's definitely talking about software

engineering, so I'm going to give it a score of .97 for that. And

then it also mentions infection vectors, which has

that connotation of medicine. So I'll

give it a slightly higher medicine score as well of

.3. Now that we have generated

these embeddings, We're going to go through

an extra little step of mathematics here,

something referred to as normalization. Now, you

do not really have to understand normalization that much.

This is already going to be done for you in the vast majority of cases

by the embedding API that you are using. This normalization

step is going to scale the magnitude of each of these

pairs of vectors to 1.0. And if you don't understand

that terminology, totally fine. Don't sweat it too much.

Just understand that we're going to do a slight little adjustment

to the actual magnitude of each number. Once we have

generated these embeddings and normalized them, we can

kind of visualize them on a plot like this. So

on this plot, I've drawn a unit circle, and each

of our points representing both those embeddings will

lie exactly on the circle because we have normalized their lengths

to exactly one. So we've got the software

engineering section up here, and here's medical research

over here. So now that we have these embeddings,

we're going to move on to the next step. In this step, we are

going to take these embeddings and store them inside of something

called a vector database. This is a database

that has been optimized for storing, comparing, and

looking up long lists of numbers exactly like

what our embeddings are. Now, at this point in time,

we pause, we take a break, because this

is all been pre-processing work that we did ahead of

time. So at this point, we just sit around

and wait for a user to actually submit a query to

our application. So we will imagine that at some

point in time, finally, a user will come to our app and

maybe type into a chatbot or something like that in

their question or their query. Maybe in this case,

their question is going to be something like, I'm curious about the company,

in particular, what did the software engineering department

do this year? Now at this point in time, we're going to take

that user's question and we're going to run it through the exact

same imaginary embedding model. In

this scenario, because the user's question is asking

specifically about software engineering, I'll give it a score

of 0.89. And then because it's also talking

about company and again software engineering is kind

of tied up in the medical field, I'll give it a very slight

medical score as well of 0.1. Now

that we have this embedding, we're going to go and go through

that normalization step again. And

then finally, we're going to make use of our vector

database. We're going to take the user's query. We're going

to feed it into the vector database and say,

please search through all the vectors we have stored inside

of you and give us the vector that is closest

in nature to this one. So in our

case, I would kind of expect to get back Section 2

software engineering because that's kind of what the user asked

about over here. But let me tell you exactly what

is happening inside of the vector database that is

able to give us this very closely related result.

Okay, so a little bit of math here, don't worry, won't be

too much. So when we take the user's query

and add it onto this chart, we can see right away that

visually the user's query is just really

close to software engineering. So you and I as humans,

we could look at this chart and say, oh yeah, clearly these two things

are very close. The user's query is very similar

to software engineering. So obviously, if we want

to find some chunks inside the vector database related

to the user query, this would be the one that we want.

But of course, we are using computers here. And our computer doesn't

actually just make a chart like this and then look at it. There's some

actual calculation going on behind the scenes. So

let's examine exactly what that calculation is. And

it's kind of important for you to know it because eventually

when you start using vector databases, they're going to use a lot

of terminology that's related to this kind

of math going on behind the scenes. And to actually

interface well with the vector database, you kind of

need to have at least a very basic understanding of the math.

So that's why I want you to understand it. All right, here's

a high-level look at the map that is being done inside

of your vector database. To find which embeddings

are most similar to the user's query, we want to calculate something

called the cosine similarity. This is the

cosine of the angle between the user's query

and each of the other embeddings stored in the database. So

we'd want to find the angle A, right here,

and take the cosine of it, and angle B right

here, and take the cosine of it. The math

for this is shown on the right-hand side. The result

of this calculation will be a number between negative 1

and 1. If we get a result close to 1,

as we did right here, then that means that we have found

an embedding very similar to the user's query. Results

closer to negative 1 mean we have found an

embedding that are not at all similar to the user's query.

In our case, the cosine similarity between our user query

and the software engineering chunk is 0.983,

meaning that these two embeddings are very similar. So

this is a sign to us that we would want to take the

software engineering chunk of text and include it in our

prompt with the user's question. Now, before we move on, one

other quick thing that's going to be a little confusing right now,

but it's going to be very, very helpful to know later on when

you start working with vector databases. In

a lot of vector database documentation, you're going to see something

referred to as a cosine distance. This

is different than the cosine similarity. It

is calculated as one minus the cosine

similarity. As adjustment is often done,

just to give us an easier to interpret number. With

a cosine distance, values close to zero mean

you have a large similarity. And larger

values than that mean we have less similarity.

Again, this is something you're going to see very often

in vector database documentation. So just

be aware of it whenever you see the term cosine distance and

cosine similarity. So now that we understand some of this math

at a very high level, let's get back on track.

Once we have found a text chunk with a high similarity

to the user's question, we're going to take the user's question, add

it into our prompt, and the text chunk that we found

that's most relevant and put that into our prompt as well. We

then take that prompt and send it off to Claude.

And that's the entire process in great, great detail.

So now that we understand everything from start to finish

with all the kind of tech behind the scenes going on and even

some of the math, let's start to implement this inside

of a notebook in just a moment.

---

#### Lesson 50: Implementing the RAG flow

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289186](https://anthropic.skilljar.com/claude-with-google-vertex/289186)

**Video:** 07 - 005 - Implementing the Rag Flow.mp4 | **Duration:** 4m 57s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that we understand the entire rag flow, we're

going to walk through an example inside of another notebook called

003 VectorDB. So

in this notebook, I've provided a sample implementation

of a vector database. And I've called it Claude

vector index right here. If you want to, feel free to

take a glance at it, but I'll walk through everything you need to

understand about it. Now in this notebook, we're going

to walk through the entire rag flow by implementing five

different steps, the same five steps we just spoke

about in the last video. So let's get to it.

Step number one, I have already opened up the file and

read the text from it, specifically our report.md

file, which should be in the same directory as the notebook.

So in step one, we're going to chunk the text by

section. I've already added in a function

to help with that. So the same chunk by section function we had

previously. So to do our chunking, chunking

process, I'll say chunks is chunk by

section and pass in all that text. And

now just to test things out and make sure I've got everything

working correctly, I'll try printing out chunks

at about two. And

I should see a printout of the table of contents.

And then if I go to three, I should see the

next section down and then the next section

and so on. Then,

on to step two. In step two, we're going to create an embedding

for each chunk. We will call generate embedding,

and pass in all the chunks, and then assign the result to embeddings.

Next up, in step three, we are going to create an instance of the

vector store. Once

the store has been created, we will then loop over all the different pairs

of chunks and embeddings. We're going to zip them

together, and then as we take each pair, we're going to insert

them into the store. We'll do that with a

four embedding and chunk in

zip embeddings and chunks. And

again, for each of those different pairs of embeddings and chunks, we'll

do a store, add, vector, put

the embedding in. And then as the second argument, we'll

put in a dictionary with content of chunk.

Now, I went over this step rather quickly. So let's do a quick aside

and explain why we are looping over all these things, why

we are chunking it, and why we are adding in this extra dictionary

with the content of chunk. As we just discussed,

eventually at some point in time, we're going to reach out to our vector database

and give back a list of all the different related embeddings

to the input. Now, when we get back this list right

here, just getting the number by itself, just

getting the embedding is not really useful to us because

the embedding doesn't really have a lot of meaning to you and

I as developers. What we really care about is the

text associated with that embedding. So usually

whenever you store these different embeddings inside of your vector

database, you're also going to include either the

text from the chunk that the embedding was generated

from, or at least the ID of the chunk, something

to at least point you back to the original chunk

text. So in this case, I'm going to include

the original chunk text along with

each embedding. Again, just so when we do the look up later

on, and I get back the most similar chunks, I've

got the actual text that I'm looking for now onto

step four. So in step four, at some point in time in the future,

a user is going to ask us a question. We need to take that

question and generate an embedding for it. So I'll make a

user embedding by calling

Claude 3.7 Sonnet. And then my

question here is going to be, what did

the software engineering department

do last year. Finally, on just

at five, where we are going to try to find some relevant documents.

So I want to search the store with the embedding and

I want to find the two most relevant chunks. Not

just the most relevant, I want to get the two chunks

that seem to be most relevant to this question right here. So

for that, I'll do a results store.search.

I'm going to pass in the user embedding And

I'm going to pass in another argument here of two because I want to find the

two most relevant chunks. And

then I will print out for

doc and distance in results.

I'm going to print out the distance, a new line, and

then the documents content. And because

each chunk here is really, really large, I'm going

to print out just the first 200 characters. And

then another new line like so. And

I'll run this. And there's our result.

So we get back section two as our best result.

We also see the cosine distance here. So it's

0.71. And the next

closest chunk is at .72, and that was the

methodology section. So these were the two

chunks that were found most relevant for the user query

that we just submitted. All right, so that is our entire

rag workflow. Now all this works, but

there is one or two scenarios where everything doesn't

quite work as expected. So there are still

a couple of improvements we could add into our workflow. And

let's start to discuss those in just a moment.

---

#### Lesson 51: BM25 lexical search

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289195](https://anthropic.skilljar.com/claude-with-google-vertex/289195)

**Video:** 07 - 006 - BM25 Lexical Search.mp4 | **Duration:** 10m 0s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

We've got the first iteration of our RAG pipeline put

together. Everything looks good right now, but we're going

to very quickly realize that, well, maybe we are

not getting the best search results. Let me show you an

example. If you open up the report.md

file and scroll down just a little bit to

the software engineering section, here

it is right here. You'll notice that it has the statement

of INC, which is short for Incident, 2023

Q4-011. And

it looks like that search term occurs three times

inside of this paragraph. So here's one right here, two

right there, three right here. And if I continue

searching throughout the document, I'll see that it is also mentioned

down here inside of Section 10, Cybersecurity Analysis.

It's mentioned inside the header, and then one time inside the actual

paragraph itself right there. Now, I

want to try searching for this term, this incident

2023 Q4011. And we're just

going to see what happens. In other words, what search

results do we actually get back using semantic search?

So back inside of my notebook, I'm going to update the user

query right here to be what happened with incident

2023. Then I'm going to rerun

all cells and we'll see what result we get.

All right, so take a look at this. It's a little bit

surprising result. We get section 10, which

is good. That's definitely the result we would

want to see at first, in the list, because section

10 is all about this incident. But then

very surprisingly, the next result is section 3,

financial analysis. Well, if you open up section

3, right here, you'll

notice that nowhere inside of section 3

is that incident ever mentioned. So we

are getting some output from our semantic search that is a little

bit surprising here. What we really wanted to get

back was section 10 and then section 2,

but what we got was section 10 and then unfortunately

section 3. And section 3 appears to be

completely irrelevant when it comes to investigating

this incident. So even though the semantic search

technique we put together is really fantastic and it's going

to work well a lot of the time, there are these

corner cases where it really just doesn't quite work as

expected. So let's take a look at a technique

we can use to improve our search results and hopefully

get the results we want, which is Section 10

and then Section 2. All right, so here's

the general strategy we are going to use. Whenever

a user asks a question, we're going to feed that question

into our semantic search side of the equation, which

is generating those embeddings and using the vector

database. But then in parallel, at the same

time, we're also going to implement a separate lexical

search system. Now, lexical search is more

like classic text search, where we are going to break down

the user's question into individual words and then trying

to find chunks of text that seem to include

those words. Once we go through the search

process in both different systems, we'll get two

sets results and then we will merge the results together.

And the hope here is that we'll get a little

bit better balance of search results where we

get both the kind of semantic aspect and the plain

text search aspect included in one result

set. So hopefully we will eventually get a result that

looks like this over here. Now

to implement this lexical search, there are

a tremendous number of methods for implementing a text

search, but a very common method that you're going to see

used in RAG pipelines, like the one we are building right now, is

a technique referred to as BM25. Now

this is short for Best Match 25.

In the rest of this video, I'm going to give you a high-level overview

of how this algorithm works, and I'm going to take a look at

a notebook that actually implements BM25, so

we'll be able to play around with it directly and see what kind of search

results we get. So here's the general idea behind

the BM25 algorithm. Now, again, I'm going

to give you a high-level overview, and I'm going to leave out a couple

of smaller steps just to simplify things and make it

easier to understand. Everything is going to begin with

us receiving a user's query. And let's imagine this

case, they put in a search string like this right here, just

A, so the word A, and then incident 2023Q4011.

In step one, we're going to tokenize the user's query.

And that means we're going to break it up into separate chunks.

There are different ways in which we can tokenize a user's

query, but right now we're going to use a very simple method,

which is to just remove punctuation and break

up the return all terms based upon spaces. So

in this case, I would end up with separate search query

terms of A and an incident 2023.

Next, we're going to see how often each of these different search

terms occurs across all of our different documents, or

in our case, really text chunks. So let's

imagine that we only have two text chunks in this scenario. So

we're going to see how often the word A, and the word

incident, blah, blah, blah, occurs across each

of these chunks. And it looks like this first chunk right here has

A right there, A right there, and

then the second one has A, A, A.

So in total, I would count all those up and I would have five

A's. And then I would see how often I have incident

2023. It looks like there's only one

right here. So I'd end up with a frequency of

one. Next up, we're going to assign a relative

importance to each term based upon its usage

frequency. So in the case of the word A, it

was used five times. And because it was used rather

often, we're going to say this term is not super

important because it is used all the place across all

of our different documents, or again, our case, our text

chunks. But incident 2023, that

was used very infrequently, which means it is

probably going to be of greater search importance.

Then finally, in the last step, we're going to find the text chunk

that uses the higher weighted terms more often.

So in this case, the first text chunk

right here, it only has two A's, whereas the second

one has three A's, but A's are not

super important because they're used rather frequently across

all over different chunks. However, TextChunk 1

uses Incident 2023 one time,

and that is a highly weighted term. It's a really important

term. So in this case, we would say this is probably

our best text chunk, and we would want to return this

as a prime search result. Now again, to see

all this in action, let's take a look at a quick Jupyter Notebook.

So back inside of my editor, I'm going to

find a new notebook. This one is called 004

_BM25. Again, at

the top, I've got some code relating to a chunking by section.

I've then got a basic implementation of BM25

in the form of this class called BM25Index.

So I'm going to collapse that cell, make sure I run it. I'm

going to read the contents of our report file. And

then we're going to go through three separate steps here. We're going to first

chunk the text by section. We're going to create a BM25Index

store. And we're going to add each text chunk to it. And

then we're going to attempt to search the store. And once

again, our hope here is that we're going to maybe get

some search results that look a little bit closer

to this. Maybe not exactly these results, but

I definitely want to see the sections that use Incident

2023 before I ever see some

results that don't include that search term at all.

So let's see how we do. Okay, let's

take care of step one here. We need to chunk the text

by section. So we've gone over this a couple times

now. We'll say chunks is chunk by

section with text. Next up, I'm

going to create a store. And

I'm going to loop over all my chunks and add them in

as documents to the store. So I'll say for chunk

in chunks store add

document. And I'll pass in

a dictionary with a content of chunk. I'm

gonna run that. And I'll finally, I'm going to search

over the store. I'll say store

search. And I'll use that same term that I used in

the previous notebook that did not give us the very good result. So

I'll ask what happened with incident

2023 Q4011. And

I'm going to ask for the first three search results.

And then I'm going to print up the results very nicely just so we can interpret

them really well. We'll say for doc, distance

in results. And I'll print out the distance,

a new line, doc with

content. And again, I'm only going to print out the first 200 lines.

And then how about a new line, a couple of separators

in another new line. I'm going to run this and

we'll see what we get. All right, so that's a

much better search result than what we had before. Now

I'm going to see software engineering first and then cybersecurity

after that and then methodology down here. So

now I am actually prioritizing the sections that use the most

important search term inside my query, which was the

incident 2023. And you'll notice that

I don't really have quite as much importance around the other terms

like what happened with. Those aren't quite as

important terms, and they might be used several times inside

of the original report, so I would not weigh those as heavily

in the output results. But this incident 2023,

that's a very rare term inside

of a report, so it should definitely have a much higher weighting.

And we can see that reflected very clearly inside of our search

results. All right, so now,

at this point in time, we have two separate search

systems. We have semantic search put together, and

we have this kind of more lexical, a little bit more classic

text search system. And you might notice that

in the implementation of these two stores, back

up here in the cell right here, I put them together with

a rather similar API. They both have

an add document function and they both have a search

function down here as well. So now

that we have these two separate search systems, one

which implements semantic search and one which implements

lexical search, we're going to come back in the next video and

we're going to merge these two search systems together.

Whenever a user submits a query, we're going to forward it off

to both of these different search systems. We're going

to get back a set of results from both and we're going

to merge those results together. And hopefully we'll

have all the best outcomes of semantic search along

with some of the more classic results of lexical

search as well.

---

#### Lesson 52: A Multi-index RAG pipeline

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289193](https://anthropic.skilljar.com/claude-with-google-vertex/289193)

**Video:** 07 - 007 - A Multi-Index Rag Pipeline.mp4 | **Duration:** 6m 45s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

We now have an implementation for semantics search

and an implementation for lexical search. So now

we need to wire these things up together. Let me show you how

we're going to do that. The first thing to notice is

that the implementation for both these searching functionalities

have the almost exact same public API.

So we have a vector index class on the left hand side

that has methods like add document and search, and

we have almost identical methods inside of our BM25

index as well. So to connect these two things

together into a single search pipeline, we're going to wrap

them up inside of a new class that we will call retriever.

This retriever is going to receive a user's question and

then forward it on to the search methods of vector

index and BM25 index. The retriever

will then receive the results from both them and figure out some

way of actually merging the results together. Now

it turns out that the merge operation is actually a

little bit tricky. So I want to go into all bit of detail

on how you can merge results that are coming out of these

different search methodologies. To combine the results together,

we're going to use a technique known as reciprocal rank

fusion. The easiest way to understand this technique

is to go through an example. So let's do that right now. Let's

imagine that we run a search on the vector index and we

get outputs of section 27 and

then 6. And then we do the same exact search on

BM25 and we get 6, 2, and

7. So now we need to take these two

list of results and combine them together in some way. To

do so, I'm going to take all the search results and put them together

on a single table, like so. So now I've

got text chunk 27 and 6

and I've recorded the rank from the vector index output

and the rank from the BM25 index output.

And to be clear, when I'm talking about rank, I just mean kind

of search output position. So rank 1,

2, 3, rank 1, 2, 3, I'm just kind of putting

those same exact numbers on this chart down here. Once

I have all those ranks in place, I'm then going to apply a formula.

Here's the exact formula right here, and I know it looks really

terrible, but don't worry, it's not as complicated as

it looks. Here's how it works. For every rank

column we have, so like that column right there and that column

right there, we're going to write out a separate term. So

here's the term for the first column, here's the term

for the second column. In the first term, we're

going to write out 1 over 1 plus

whatever number is right there. So we end up with

1 over 1 plus 1. And

then the second term will be 1 over 1 plus

whatever number is right there. So 1 over 1 plus 2.

Once we have calculated the score for each text chunk, we're

then going to sort the table based upon score from greatest

to least. So we're going to end up with something like this.

So we'd end up with text chunk for section 2

as being the most relevant search result. Section

6 would be the second most and section 7 would

be the least relevant. And this kind

of makes sense. We can kind of visually confirm that these

outputs make sense if you just look at the individual rank

outputs from each search methodology. So section

2 was rank 1 and 2. That means,

hey, in general, it's trending up towards the top.

Section 6 is 1 and 3. That's kind

of like in the middle. It has a good score in a bad score. And

then section 7 is 2 and 3. And so it trends

down towards the bottom. So with a visual inspection, the

results, I think, do make a decent amount of sense. All

right. So now that we understand how we're going to combine the results together,

let's go back over to our Jupyter notebook. And we're going to take a look

at a sample implementation of a retriever

class and a sample implementation of

merging the results. Okay, so back over

here, I move on to the next notebook, which is

005 hybrid. Once again, there's

a lot of setup up here. So I've got the

vector database implementation, the VM25 implementation,

and now I've added in a implementation for the retriever

class as well. The retriever has method of

add document. And if you call add document,

it's just going to take whatever document you pass in and pass

it off to each of the different indexes that are

contained inside the retriever. So in our case, our indexes

are the vector index and the BM25 index.

Then the retriever also has a search function.

If you pass in some query text to it, that

query text will be passed off to each of the different indexes

that are contained inside the retriever. We then take

all the results that come back and combine them

together. So here is the merge logic that

implements that reciprocal rank fusion. All

right, so time to do a little test here. Now, I want you

to recall what led us down this entire path was

back on our vector database implementation.

So this notebook over here, we found that if we search for something

like what happened with incident 2023,

we got back some unexpected results where

we had section 10, which was good as the first result.

And then section three was the second result. And that was really

unexpected. We want that second result to be

software engineering. So when we now run this hybrid

approach that combines together multiple different indexes, my

hope is that we're going to get first section 10 and

then whatever section the software engineering one is. I think

it's section two. So let's test this out inside

of our new notebook. I'm going to go down to the bottom.

And I'll do a results is retriever,

search what happened with

incident 2023 Q4011.

And I'm going to get the first three search results.

And then once again, I'm going to print them all out like

so. And I'll do the score, a

new line, the

content of the document, but just the first 200 lines. And

then just a little separator between each chunk. So

I'm going to run this. And now we get, hey,

some much better search results than what we had before. So

I've got section 10, and then section 2, exactly

what we wanted. And then section 5, but that one's not

super relevant here. So we now have a

much better output by combining together these two

different search techniques. And the nice thing about this

is we were able to author each of these indexes kind

of in isolation. They're their own separate classes. And

because we made each implementation have the same exact

API with that search function and the add document

function, we were able to easily wrap them up into

this larger retriever class. So if you wanted to,

we could absolutely add in some additional search

index here that maybe implements some other completely

different searching functionality. And as long as it has that

search function and the add document function, we

can very easily add it, have it generate

some results, and then merge the results along with the

results coming from the other search methodologies as well. Okay,

so let's say this is a good success, but we're

not quite done yet. There's still some other techniques

that we're going to go over to improve the accuracy of

our RAG pipeline.

---

#### Lesson 53: Reranking results

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289192](https://anthropic.skilljar.com/claude-with-google-vertex/289192)

**Video:** 07 - 008 - Reranking Results.mp4 | **Duration:** 6m 9s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The hybrid-based retrieval approach that we have implemented

is working pretty well. So as we saw at the

end of the last video, if we search for what happened with this incident,

we're going to get first the cybersecurity and then software engineering.

However, there are still some weak points inside

our retrieval process. Let me show you an example.

I'm going to update the query here to be, what

do the engineering team? And notice I put in not engineering,

but just in abbreviation of ENG. What

do the engineering team do with incident 2023?

So now that I am asking specifically about the engineering

team and the incident, I would kind of expect

to see section two pop up a little bit. Because remember,

section two is about software engineering and the

software engineering team and inside of the body

of the section, there is mention of this incident.

So now this query in my mind personally, I think

this really is the most relevant section. But

if I rerun this, we're going to see that we still end

up getting section 10 and then section

2. So it's clear that even though

we have added in a lot of complexity, well, again,

still a couple of rough edges. So in this video,

we're going to take a look at yet another technique that we can add in to

improve our retrieval accuracy. This technique

is referred to as re-ranking. And the

idea behind this is super simple. After

going through everything that we just covered in the last video, so we're going

to still run our vector index and the BM25 index

and merge the results, we're then going to add in another

post-processing step. Something called a re-ranker.

The re-ranker is going to take some number of our search

results and pass them off to Claude inside of a prompt.

So here's a sample prompt that we might use for

a re-ranker. We are going to ask Claude to take

a look at the user's question, specifically what

happened with incident so and so, and then we're going to

provide all the different documents that we have currently found

that seem to be somehow related to the user's

question. And then we're going to give Claude a very simple

task. We're going to ask Claude to return the three

most relevant. And it doesn't have to be three, just me

some number of the most relevant documents in

order of decreasing relevance. So in other words,

go through all the supposedly relevant documents and

just reorder them or re-rank them so

that the most relevant document is at the top.

So Claude is going to take in the instructions and of course it's

going to execute the task perfectly and send us back

a reorder list of relevant documents.

To understand how this really works, let's take a look at a notebook

where I have implemented this reranking strategy. So

back over here, I've opened up a new notebook called 006

underscore reranking. There is a ton of

setup code inside of here, and then eventually we get to the

implementation of a function called re-rankerfn.

This function is going to be called automatically by the retriever, after

we have ran the initial search process with the

vector index and the BM25 index. So we've already

gotten back the initial results, we've already merged them, and

now we're going to take these merge results and pass them into

this re-ranker function. So

we are going to iterate over all those documents that we found.

We're going to print them up in a nicely formatted XML structure.

We're then going to insert that list into a larger prompt,

the one you see right here. This prompt is asking Claude

to take a look at the user's question and take

a look at the documents that we have found already. We are then

going to ask Claude to return a list of documents

in order of decreasing relevance. So the first

documents we get back should be the most relevant

results. Then as usual,

we're going to go ahead and use a Assistant

Message Prefill and a Stop Sequence just to ensure that we get

back some well-formatted JSON. Remember, we could

use tools here to ensure that we get back well-structured

JSON, but in this case, it would be a lot of

extra work just to get some structured data back.

And I think using this Prefill with the Stop Sequence is

definitely appropriate. Now, before I say anything

else, there's something I want to clarify that might be a little confusing.

You'll notice that in this prompt, I'm referring to some document

IDs all over the place. But in the diagram

I showed you just a moment ago, there is no mention of any IDs

whatsoever. So what are these document IDs exactly?

Well, it really comes down to efficiency. If we

use the prompt I showed you in that diagram just a moment ago and

asked Claude to just give us back the most

relevant documents or text chunks, we're essentially asking

Claude to send us back the full text of every

single text chunk. This would be extremely inefficient

because we would just be sitting around and waiting for Claude to copy

the text out of each individual chunk. So a

better solution would be to generate some random

IDs ahead of time and assign them to each document

or essentially text chunk. And then ask Claude to

just return those IDs. This will be significantly

more efficient because Claude can return just a very

simple little bit of text that's going to tell us the exact order

of chunks that we should be making use of. Well,

now that we understand how everything is working, let's actually run

the notebook and see if we get some reasonable results.

Now, I've already ran all the different cells inside of here. Make

sure you run all the cells as well. I'll

go down a little bit and get

down to the very bottom here. We're going to ask that same question as

before. What happened with incident 2023? So

I'll run that and I'll get back same results we

had previously back when we had the just hybrid

approach. So I got section 10 and then section

two. So nothing bad. But now I'm going to update

the query. to the one that gave us just a little

bit of trouble a moment ago with the hybrid approach.

So what did the engineering team do with Incident

2023? And again, my expectation here, my

real hope is to see section two pop up

to the top. There's no guarantee that's going to happen. You

might get different results than I, but that's personally what

I'm going to hope for. So I'm going to run this. And

then sure enough, we do, in fact, get software engineering

popped up to the top. So that's definitely a good

result. Claude has noticed that the user

query here really cared about specifically the software

engineering team and their relationship to this incident.

Well, adding in this re-ranker was definitely a success.

On the downside, it increases the latency of our

search pipeline, because now we have to wait for a Claude

to resolve. But on the plus side, it also

without a doubt increases the accuracy of our search

pipeline.

---

#### Lesson 54: Contextual retrieval

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289187](https://anthropic.skilljar.com/claude-with-google-vertex/289187)

**Video:** 07 - 009 - Contextual Retrieval.mp4 | **Duration:** 6m 27s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, we're going to take a look at another technique for

improving the accuracy of our rag pipeline. This

technique is known as contextual retrieval. The idea

here is that whenever we take our original source document

and split it up into chunks, each individual chunk

no longer contains context of the original document.

Contextual retrieval aims to fix this by adding

in a pre-processing step before we insert each text

chunk into our retriever database. So

we're going to take each individual chunk that we have produced,

and our original source document, and place it into this

prompt and then send it off to Claude. This prompt,

as you can read, is going to ask Claude to take a look at this individual

text chunk and the contents of the overall source

document. We then ask Claude to write out a little

bit of text to situate or kind of place or

add some context to the individual text

chunk. We're then going to repeat this process for

each text chunk we have over here on the left hand side.

So as an example of the output we might get

from this, let's imagine that we put in Section 1

software engineering right here, which includes a mention to that

2023 incident. And there's also

a similar mention down inside of Section 2 cybersecurity

analysis. The added context

that Claude might generate could look like this, might say

something like this is a section from a larger report, and

this section includes a mention of this incident, and

that incident is also mentioned in this other section.

So now we're taking this input chunk and adding some

additional ties to the larger document.

Once Claude generates this extra little bit of context,

we're then going to join together that context with this

input text into something that we refer to as

our contextualized chunk. So right here

is the extra context that Claude generated, and

out here is the original chunk text. We

will then use this contextualized chunk as the input

to our vector index and our BM25 index

as well. Now right away, a very common problem that you're probably

going to run into. Your original source document

right here, we're saying that we want to take all of the text out of that

original document and put it into a single prompt and then

send that off to Claude. In many cases, this

original source document might be simply too large to

fit into Claude by itself. If you're in that scenario,

don't worry, there's still a way we can make use of contextual

retrieval. If our source document is too large to fit

into a single prompt, here's what we might do.

Let's imagine that we are trying to contextualize chunk

9 down here. So this is the one that we really want to feed into

Claude, and ideally, we would provide the original

source document in its entirety. But instead, we

might decide to include some of the chunks from the very start

of the document, so maybe chunks 1, 2, and 3 right here, and

then some of the chunks right before chunk 9.

The idea here is that the starter chunks at the

very top of the document provide possibly a summary

or an abstract or something to kind of explain

what the entire document is about. And then the chunks

right before chunk 9 are going to provide some context

for chunk 9 itself. And chunk 4, 5, 6, while

they might be important, they're probably not going to provide quite

as much context as all the others that we might

include for chunk 9. So this is how

we can significantly tear down the amount of text we're going to push

into Claude to provide this context when trying

to contextualize chunk 9. Now, once again, let's

take a look at a Jupiter notebook to get a better idea of how

this stuff works. All right, so back over here, I've opened

up a new notebook called 007 underscore

contextual. We still have a ton of helper

code, and then I've added in a new cell with a function

named add_context. This function is

going to take in a single text chunk that we're trying to generate

some context for, and some source text.

So that would be the text from the original source document. We're

going to ask Claude to write out some

succinct context to kind of place or give us a better

idea of what this particular text chunk is really all about

in the context of the larger document. We're

then going to get back our response. We're going to add together

whatever response we got with the original text

chunk and return it. So I'm going to run

that cell and I've already ran all the cells above it. Now

let's test this out really quickly. So I'm going to chunk

the source document like so.

I'm going to add in a new cell right here and I'm going

to call add_context with

chunks at five and

the report text. And let's see what we get out.

All right, here's my output. Now, this might look like a lot,

but remember, this is both the added context,

which is really just that part right there, plus the text

from the original chunk, so section two

software engineering right there. So in this case, our

added context says this is a chunk of section two

from this larger report, and it is following

the methodology and it's before financial analysis,

and it is a part of a larger report that covers 10 separate

research domains. So I would say this is some

pretty effective context. It really gives us a better

idea of what this individual section is

a part of, the nature of the surrounding report

or the surrounding document around it. All

right, so next up, in the next cell down, I'm going

to still create my two indexes and the retriever, and

then here's where things start to get interesting. So

again, if we have a really large source document

where we can't fit everything into a single prompt, we might use

this little extra strategy where we include

just some starter chunks and the chunks from right before the

chunk that we're trying to situate. That's

what this code right here does. I've got some configurable

variables right here, so we are going to try to take two chunks

from the very start of the report, and then two chunks from right

before the chunk that we are trying to contextualize. I've

then got some code to make sure we don't get any duplicates or anything like that.

I'm going to get all that context from the report,

join it together, and then pass it off to the add_context

function with the chunk that we're currently operating

on. Once we get back that contextualized

chunk, we will add it into our retriever.

So I'm going to run this. This

will take a while to complete because we are generating context

for every section inside of our report. Well,

once it is done, we can then go down and test it out.

Now, in this case, using the same query right here of what did

the entering team do with Incident 2023, we're

probably still going to get some really good output because we already

had good output. But you can imagine that by including this extra

context, if we add a much more complex document

with individual text chunks or sections that have a lot

more ties between the overall document, well,

then I would expect this contextual retrieval technique to

give me some better accuracy.

---

#### Lesson 55: Quiz on Retrieval Augmented Generation

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289277](https://anthropic.skilljar.com/claude-with-google-vertex/289277)

---

### Features of Claude

#### Lesson 56: Extended thinking

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289197](https://anthropic.skilljar.com/claude-with-google-vertex/289197)

**Video:** 08 - 001 - Extended Thinking.mp4 | **Duration:** 7m 1s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's examine one of Claude's more advanced features

known as extended thinking. Extended thinking

gives Claude time to reason about the user's query before

generating a final response. In many chat

UIs, this will be displayed as a separate thinking

process, which the user can optionally look at to

get better idea of how Claude is approaching their problem.

Now in general, enabling extended thinking will allow

Claude to tackle more complex tasks with greater

accuracy, but there are some big trade-offs here. You

are charged for tokens generated by Claude during

the thinking phase, and the phase itself takes some

amount of time to complete. So with increased

intelligence comes increased cost, and there's

increased latency as well. Now

a common issue around extended thinking is deciding

when to enable it. And the answer to this is really simple.

You're going to rely on your prompt eVals. So

you're going to write out a prompt. You're going to run an

eVal on it. And if the accuracy is not where

you want it to be, and you've already spent some good amount

of effort on improving your prompt in the first place, that

is when you would want to consider enabling extended thinking.

The use of extended thinking is fairly straightforward. Remember,

when we normally use Claude, we send over a user message

that might contain a text block. And then we're going to get back

an assistant message that contains a text block as well. When

we start to enable extended thinking, the response we get

back is going to contain a new block type that we

have not seen before called a thinking block.

Inside of this thinking block is going to be the text that was generated

while Claude was thinking. There's something really

interesting around this thinking block that I want to show you

right away, because you're going to see it really quickly as soon

as you start writing out some code and making requests

with extended thinking turned on. On the right-hand side,

I've got an example of an assistant message that includes a thinking

block and a text block. Inside the thinking

block, you'll notice that there is something called a signature. The

signature is a cryptographic token, and here's what it

does. If you want to take this message and send it back

to Claude as a piece of the conversation in the future,

Claude wants to make sure that you did not modify the text

in the thinking block in any way. The signature is

used to make sure that you did not change the text.

Claude doesn't want you changing that text at all because it is

relied upon very heavily during response generation.

And if developers were allowed to modify that text, they

could possibly steer Claude in an unsafe

direction. There's one other aspect of thinking

related to this idea. In some cases, you

might get back a thinking block that has a field of redacted

content without any thinking text at all. This

occurs whenever Claude generates some thinking text that

gets flagged by some internal safety system.

The redacted content is the actual thinking text,

but in a fully encrypted form. It is provided

to you so you can give this full message back to Claude

in the future as part of a conversation without Claude

losing any context on his previous thinking. To

really understand extended thinking, we need to write out a little bit

of code. So let's go back over to our Jupyter notebooks.

I've made a new notebook called 001 thinking.

Once again, it has a lot of the similar code that we've been working on

throughout the course, but I've added one or two very special

things. So I would encourage you to make sure you download this notebook.

It is attached to this lecture. In order to enable

thinking, we need to find our chat function. We're

going to provide some additional arguments to the chat function

that will eventually be added into this params object. So

I'm going to add in thinking_with_

a default value of false, and then a thinking_budget of

1024. The thinking

budget is the number of tokens that we want to allow Claude

to use in generating a thinking portion of the

response. The minimum value here is 1024,

so we cannot have a thinking budget less than

1024. It's entirely possible that Claude

will not spend 1024 tokens on thinking,

but again, this is the minimum that we can specify as the budget.

There's one other very important fact you need to understand around

the thinking budget. And that is, that max_tokens

must be greater than your thinking budget. So

for example, if we have a thinking budget of 1024, max_tokens

must be at least 1025. And

that's only going to leave one token remaining to

actually apply to generating some text. So usually you're

going to want to have a max_tokens value that is generally

significantly larger than your thinking budget. So

in my case, I'm going to increase my max_tokens here to

4,000. And now I've got a pretty big buffer. This

means that I can generate a response that has

1,000 tokens allocated to thinking, and

then a remaining 3,000 tokens can be allocated

to actually generating some text. Once

we have added in these two keyword arguments, we're then going to

add in some additional parameters to the params

dictionary. So scroll down a little bit and

down here. I'll say if thinking_with_

is enabled, then I want to add in a new key

to my params dictionary, specifically thinking.

This is going to be a nested dictionary with a type

of enabled and a budget_tokens

of whatever we passed in as the thinking budget,

like so. And that's it. So

I'm going to run the cell, I'll then scroll down to

the bottom so we can test this out. I'm going to ask Claude

to write out a one paragraph guide to recursion. I'll

then make sure that I update my chat function call right here to

enable thinking by passing in thinking_with_true. I'll

then run this and let's see how we do. And

here's our response. So in the response, I get

two separate blocks. First, I have my thinking block,

and then a little bit lower down right there is the start of my

text block. Inside the thinking block, I do in fact

have a signature. And along with it, I've got my thinking

text. Remember, the goal of the signature is

to make sure that we don't tap or tamper with the thinking text in

any way. And of course, our text block right here contains

the actual guide that we ask Claude to write. Now

the last thing I want to show you is something that you might use when you

are initially building and testing out your application. As

a reminder, there might be some scenarios where Claude sends

back a redacted thinking block. As

you are building out your application, you might want to make sure that

your code works correctly whenever a redacted thinking

block is sent to you. So we can actually force

Claude to send us back a redacted thinking block.

All we have to do is send in a message that includes

a very, very specially formatted string.

So if you scroll up to the very top of the second cell

inside of here, you'll notice I put in thinking_test

string. And then it has a value of Anthropic,

magic_string_triggered_redacted_thinking, and then a bunch

of special numbers and letters after it. If you

send exactly this string into Claude, you are guaranteed

to get back a redacted thinking block. Again,

we would just do this for testing purposes to make sure that we can

handle that kind of response. So let me just show you this to

you really quickly. I'm going to go back down to the bottom

cell. I'm going to add in a user

message that contains just that thinking_test

string. I'll then send this in. And now

we should be getting back a response that's going to have a redacted

thinking block inside of it. There

we go. So I've got my redacted thinking block and

it has nothing but a data and a type of redacted

thinking. So now, like I said, we could just use

this to make sure that our application doesn't crash when receiving

this kind of unexpected thinking block

in response.

---

#### Lesson 57: Image support

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289203](https://anthropic.skilljar.com/claude-with-google-vertex/289203)

**Video:** 08 - 002 - Image Support.mp4 | **Duration:** 10m 16s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next advanced capability of Claude that we are going to

investigate is Claude's vision capabilities. Whenever

we send a user message off to Claude, we can optionally include

images inside of the message. We can then ask Claude

to do just about anything you can possibly imagine with these images.

So we could ask Claude to tell us what is contained inside them. We

could ask Claude to compare different images. We can ask Claude

to count different objects. Really, there's a lot of

different possibilities here. The first thing I want you to understand

around image handling is some of the different restrictions or requirements.

We can send up to 100 images across all

the messages inside of a single request. There

are some limitations around the size of each image and

the height and width as well. And

finally, you need to understand that whenever you send an image off to

Claude, that is going to count for some number of tokens

that you are going to be charged for. There is an equation you

can use to roughly calculate how many tokens you'll be charged for

based upon the height and the width of the image in pixels.

To send an image off to Claude, we are going to include yet

another type of block inside of a user

message. This is an image block. We can attach

multiple different image blocks inside of one single user

message. Each image block is going to hold a reference

to a single image. Inside this image block, we

can attach either the raw image data, which

is what I showed in this diagram over here on the right-hand side, or

alternatively, we can provide a URL to an image

that is hosted somewhere online. So now that we understand

some of the technical limitations here and how we send

the image off, there's something really important that I want

to address right away. Whenever an engineer

starts making use of images with Claude, well, I

notice very often they start using prompts that are very

simple, even kind of like the prompt I've gotten this example

right here. The number one way to get good

results out of Claude when you are making use of images is

to continue to have a strong focus on prompting

techniques. So if you just throw an image off

to Claude and then put in a very simple prompt, very

often you are not going to get back a good result. For

example, consider the conversation on the right-hand side. I

put in an image with 12 marbles. I actually

tested this by the way and I asked it very simply how

many marbles are in this image. And sure enough, I got back

an incorrect count of 13. We can

dramatically increase Claude's accuracy when

working with images by using the same kind of

prompting techniques that we've already learned earlier on inside

this course. So techniques like providing

guidelines, providing analysis steps, or by using

one shot or even multi-shot examples. So

let me show you two ways in which we could very easily enhance

this prompt and actually get back the correct result. And

again, I actually tested this out and made sure that these examples,

at least for me, worked as expected. So

the first thing we might do is provide a series of steps

for Claude to go through in analyzing the image. Now,

of course, this is only really going to work if we kind of already

understand the content of the image that we're feeding into Claude.

So in this scenario, I might ask Claude to first take

a look and try to identify each individual marble

and just count each of them one by one. and then ask

it to recount a second time to verify

the initial count and provide it a different mechanism

or different strategy for counting the number of marbles.

And then finally at the bottom, I ask, okay, now let's kind of compare

those two different counts and figure out what the correct

answer is. So by providing a more sophisticated

prompt, I was able to get results with a correct count of

12 marbles. Another technique

we might use here is one shot or multi-shot

prompting. So here's how that would work.

Inside of my user message, I can alternate

the presence of an image part and a text part.

So in this scenario, I have an image part up here, a

text part underneath it, and then another image, and

then a text part. In the initial pair,

I provide an image with 11 marbles, and then say very

plainly, the image above has 11 marbles inside

of it. Providing an example like this can easily improve

Claude's accuracy when it goes to tackle your image

later on. As usual, I would like to test

out this feature in Claude inside of a Jupyter notebook. But

this time around, we're going to have a little bit more complicated example.

And I want you to understand the scenario that we're going to walk

through here inside of our notebook ahead of time by showing

you a quick diagram. All right, so here is a

sample use case of how we might use Claude's

image support capability. So in case you're not aware,

in many parts of the United States, we have really

bad wildfire problems, where wildfire

will begin sweeping through an area and burn down a

ton of houses. And because this is a very

common risk, a lot of people want fire insurance to

ensure their home in case it gets burned down. But

these insurers are very much aware that a house

can absolutely be burned down tomorrow or next year

or very shortly. So these insurers

will very often require a homeowner who wants

to insure their home to trim trees or even

cut trees down entirely around their house.

Now the insurer needs to actually verify and make sure

that the homeowner is taking care of the trees appropriately.

But to verify that, they might have to send out a person to inspect

each property and probably do that inspection maybe once

every year or once every two years. That would become expensive

really, really quickly. So one way that we can automate

this process is by getting high resolution up

to date satellite imagery and then feed it into

Claude and ask Claude for a fire risk assessment.

We might ask Claude in particular to try to detect

the main residence on the property. So in other words, inside

of a satellite image of a property, find the main

home that is presumably insured. And then take

a look for maybe tree branches that are overhanging

the residence, which is a very common risk of fire.

Maybe try to gauge how difficult it is for

fire services to actually access the residence.

So make sure in other words, there's kind of a clear path to get to the

home and also take a look at the trees around

the home and make sure that they are not too closely or

tightly packed, which in its own right could be a

fire risk as well. All right, so let's go

over to the notebook and see how we could implement this. I'm

inside of a new notebook called 002 images.

Inside of here, I have already put together a starter prompt for

us. Now notice that this prompt is highly

detailed and walks Claude through different points

or different ideas that I want analyzed inside the image. I

could have written out a very simple prompt of something like provide

a fire score based upon the satellite image of this

property and just left it there. I can almost guarantee

you I would not get a good result. So instead,

I applied some of the different prompt engineering techniques

we've learned about previously, and I provided a series

of different analysis steps for Claude to go through. Step

1. First, find the actual primary residence

inside of the satellite photo. Step 2. Take

a look at the tree density. Then take a look

at the ability for fire services to actually access

the property. Take a look at how many

trees or specifically branches are overhanging the

roof, which is a very common fire risk,

and then finally assign a fire risk rating based

upon all these different qualities. And I provide some criteria

on helping it decide whether it should be a 1, 2, 3,

or 4. And then finally at the very bottom, write

a one-sentence summary for each with a final score.

So that's our prompt. I'm going to make sure I run

that cell. And then let's go down here to the bottom. And

we're going to write out some code to read in a sample

image and feed it into Claude with that prompt and

see what kind of result we get. One other quick item. Attach

to this lecture, you will find a zip archive called images.zip.

Make sure you extract that archive and place the images directory

into the same folder as your notebook. This folder contains

some different satellite imagery of different houses with some number

of trees around it. So for example, Image 1 has a house

with definitely a good amount of tree overhang. Image

2 has definitely a lot less trees,

but there's still a little bit close tree right here to the property. And

you can go through the rest and just verify that, yeah, we've definitely

got some satellite imagery here. So our goal is going to

be to send these different images into Claude and get a fire

score rating for each. Back inside my notebook, I'm

going to first begin by opening up an image file and converting

its contents into base 64. So I'll

do a width open. In the images directory,

I'm going to look for image seven specifically. And

I'm using that image in particular because it is absolutely

surrounded by trees. So here's prop

seven.png. As you can see, definitely a lot of

issues with fire here. I'm

going to get the image bytes as base 64,

standard_b64 and

code. I'm going to pass an F dot

read and I'll decode into

utf-8. I'm then going to

add in an empty list of messages. I'll

add a user message into it. And

this message that I am adding in is going to have two separate blocks.

It is first going to have an image block, exactly with the structure

that you see right here, and it will have a text block.

And a text block is going to contain the actual directions that

I want to feed into Claude. So I'll

add in first a dictionary to represent the image block.

So a type of image with

a nested dictionary assigned to source that has

a type of base 64, a

media_type of image/

png. and data that's going

to be the image bytes encoded as base 64.

Then after that dictionary, I'll add in my actual prompt.

So I'll give this a type of text. And

then the prompt that I want to send in, I assign to the prompt

variable right there. So

I'll do a text of

prompt. All right, finally, I'll

call chat and pass in my list of messages. I'm

going to run this and let's see what we get. Looking

at the response, I'm going to scroll down to the very bottom and I should see

a fire risk rating. In this case, I got a fire

risk of high or a score in particular

of three. So I think Claude did a pretty reasonable job

of evaluating all the trees around the main property and

deciding that, yeah, there's probably going to be an issue here. Before

we move on, there is one last thing I want to remind you around images.

Getting good results out of Claude when feeding images in

all comes down to your prompting technique. Just as we examined

a lot of different ways of improving your prompt when using

plain text, those same techniques apply to the world

of images as well. So I would really encourage you

to always make sure that you put together a very well-developed and

well-evaluated prompt. Because if you rely upon

simple prompts like what I'm putting in right here, it's

probably not going to work quite as well as you might expect.

---

#### Lesson 58: PDF support

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289198](https://anthropic.skilljar.com/claude-with-google-vertex/289198)

**Video:** 08 - 003 - PDF Support.mp4 | **Duration:** 1m 29s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Besides images, Claude can also read content

directly out of a PDF file. I'm going to show you how you

do that in this video. Attached to this video, you will

find a document called earth.pdf.

If you open it up, you'll see that it's just a couple of pages out of

the Wikipedia article on Earth. So make

sure you download this PDF file and place it inside the same

directory as your notebook. To read a PDF

file, we use almost the exact same code that we use for

reading an image and feeding the image into Claude. So

I'm going to find where we are currently opening up an image right

here, and I'm going to change it to earth.pdf.

I'm going to rename this variable from image bytes to

how about file bytes, because no longer are we reading

an image. I'm going to make sure I update the variable down here

as well. I'm going to change the

type right here from image to document, and

then the media type will go from image slash

png to application slash pdf.

And then finally, the question that we're asking of Claude

about this document, rather than feeding in our big

prompt that we have in the previous cell, I'm going to ask Claude to

summarize the document in one

sentence. And let's see what we get out of Claude. So

I'm going to run this. And there's

the summary. It looks like it successfully read the contents of

that PDF file. Now, Claude has the ability to

not only read text out of a PDF, it can also read

images or charts, tables, and so on. So

you should really think of Claude as being like a one stop shop

for extracting just about any kind of information out

of a PDF document.

---

#### Lesson 59: Citations

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289202](https://anthropic.skilljar.com/claude-with-google-vertex/289202)

**Video:** 08 - 004 - Citations.mp4 | **Duration:** 5m 19s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In the PDF file that we were just working with, I'm going to scroll down

to the very bottom page. And done here at the bottom,

you'll notice that it mentions that Earth's atmosphere in oceans

were formed by volcanic activity and outgassing.

Now, as a little exercise, I want to try to ask Claude

a very simple question. I want to ask it how Earth's atmospheres

and oceans were formed. And I would probably expect

to see some kind of answer that says something like volcanic activity

and outgassing. So I'm going to copy this right here and

put it into my prompt, and ask Claude. Power,

Earth's atmosphere and oceans formed. Now,

I'm going to run this really quick. And for me at

least, I'll notice that in the very first sentence here, I'm given

a very appropriate answer. I'm told that these were

formed by volcanic activity and outgassing. So that's

really exactly what I would expect. But I want you to imagine

getting this answer from the perspective of a user. When

a user sees this generated text, they might think that it's just

Claude speaking directly from memory here. And the

user might not really understand that we are actually citing some

kind of source here. In this case, the source is not perfect. It

is Wikipedia, but at least it is something.

So what would be really fantastic is if there was some kind

of way to somehow inform the user or tell them how

we are getting this information. Luckily, Claude has

access to a feature called Citations. Citations

allow Claude to refer to some outside source

of information directly and say that it got its answer

by looking at some other document or some other source of

text. Now, let me show you how citations work

because once you see it in action, I think you'll have a really

good idea of what's going on. I'm going to scroll up to

our prompt right here, and I'm going to make a little modification

to the first block that we're putting into

this message. Right after the source field, I'm going

to add in a title of earth.pdf

because that is the name of the PDF file that we are opening and

a citations field that will be a dictionary with

enabled true, like so.

Now I'm going to send off this request again. And

let's see what we get back now. Now we're going to see that our response

is much more complicated than it was previously. Our

content field right here is a list that has some text

blocks and some of these text block things have a

citations list with something called a citation page

location. So let's focus on exactly what

a citation page location is for just a moment. Let's

show you a diagram. A citation page location

is Claude's way of telling us exactly where it got some

fact or some piece of information from. So

in our case, we got back a structure that has

a cited text, document index, document title,

start page, and end page. The cited text is

the text out of the source document, in our case, earth.pdf,

that is somehow supporting Claude's statement. The

document index and the document title tell us exactly where

this statement was made, and the start and end page

tell us exactly where inside of that document that

statement was made. Now, the real intent behind

giving you these citations is to allow you to build up a user

interface that looks something like this out of Claude's answer.

So I took the response that we just got out of Claude. I

fed it back into Claude and asked it to render

that entire response in a nicely formatted document and

give me some popups to represent all the different citations.

But now if I mouse over the one or the two or the

three, I'll see a nicely formatted popup appear.

This popup contains all the information out of that citation

page location object. It is meant to inform the user

that Claude's response here, specifically this sentence,

really, is being informed by some outside document.

So in this case, this sentence is coming from earth.pdf,

specifically some text on pages four to five,

and the actual text that we're citing is earth's atmosphere was,

et cetera, et cetera. So this entire citations feature

allows you to build up interfaces like this where a user

can be assured that the information being presented by Claude

is coming from some actual outside source. The

user can then go and refer to that source and make sure that Claude

is correctly interpreting the information inside

that outside document. This citations feature is

not restricted to only being used with PDF documents.

You can also use it with plain text as well. So

as a very quick example, in the cell right above, I

manually copy pasted in some text out of the PDF

document, and I signed it to a variable of article text.

Now I can go back down to where I'm making my request down here, and

I'm going to make a big update to this block. I'm

going to leave the type of document. I'm going to leave this

source, but I'm going to change the type to be text.

I'm going to change the media type to be text/plain,

and then the data. to

be article. So that is the text.

That was, oh, sorry, it's article text. There we go. So that's

the text that I signed to that variable up there. I'm

then going to change the title to how about something

like earth article, since it's not really directly

a PDF file anymore. And then I can leave the enabled

true with citations in there. So now if I run

this again, and take a look at the response,

we will see that instead of a citation page location,

now we get a citation chart location. So

this is going to give us a position inside of that big block

of text that Claude is citing from. We can

now use this to build up a very similar interface to the one I just showed

you inside the browser. So again, you can cite from plain

text or PDF documents. Either way,

I really recommend you make use of the citations feature anytime

that it's critical to make sure that users can somehow

investigate how Claude is building up its response and

ensure that Claude is drawing information from some

source documents, either a PDF or plain text.

---

#### Lesson 60: Prompt caching

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289196](https://anthropic.skilljar.com/claude-with-google-vertex/289196)

**Video:** 08 - 005 - Prompt Caching.mp4 | **Duration:** 3m 35s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next feature that we are going to focus on is prompt

caching. Prompt caching is used to speed up

Claude's response and decrease the cost of text

generation. To help you understand how prompt caching

works, we're going to walk through what happens inside of

Claude during a typical request that we make without

any kind of prompt caching enabled at all. So again,

this is just a normal request. And we've already

spoken a little bit about normal requests on the entire flow. But

don't worry, this time, I'm going to add in a little bit of detail on

what happens inside of Claude itself. As usual,

everything begins with us sending a message off to Claude.

And when Claude receives this message, before actually

generating any output text at all, it does a

tremendous amount of work on the input message.

In other words, Claude is going to internally create a tremendous

number of internal data structures and do a tremendous

number of calculations solely on the input

text. It will then eventually generate the output text

using all that earlier work it did, and then send

a response back to us in the form of some assistant message.

After the response is sent off to us, Claude is

going to then take the output text and the result

of all those earlier calculations that were done

on the input message and just throw them all into

the trash. A way it all goes, we see all that work

kind of go up in smoke entirely. Once Claude

has gone through all that cleanup, it declares the world I am

ready to process the next request. Now, let's

imagine for a moment that after making this initial request,

we then make a follow-up request. And in

this follow-up request, let's just imagine that we are continuing

this conversation. So we're going to attach

a list of messages. The first one will be the exact

same message we had sent in a moment ago, and

then the assistant message response we got back, and then some

new user message that we're going to attach just to further

the conversation along. So we're going to take all these

messages and send them into Claude. And internally,

Claude is probably going to be a little bit frustrated when

it sees that first message. Because Claude

is going to see that first message and think to itself, of course,

this isn't quite what happens. We can imagine this is kind

of what's going on behind the scenes. Claude is going to see that first

message and say, I just saw this message.

I just did so much work to process it. And then I threw

away all those calculations. And Claude is

going to think to itself, I really wish I could reuse

all that work that I did just 10 seconds ago

and threw away. If Claude had saved

that work that it threw away just a moment ago, it would probably

be able to send us back a response much more quickly

because it doesn't have to repeat all that work. So

now that we have seen this problem, let's think of some

possible way to solve it. Well, here's one

possible way that we could handle this problem. Maybe

we could say that whenever we make an initial request

off to Claude, and Claude goes through all that initial work

on our user message that we are sending in, rather

than taking the results of all that analysis

and throwing into the trash, maybe we could instead cache

all that work or put it into some temporary data

store. Then if we ever make a follow-up

request and we include the exact same input

user message, Claude could go into its cache

and say, hey, I just saw this exact same

message a moment ago and I saved the work of

all the analysis around that particular message. So

rather than re-analyze the message again, it could reuse

all the work that it did previously. And hopefully this

would dramatically speed up the process of generating some output text

because again, we are reusing some work that we

had already done. This idea of saving

some work from request to be used later on is exactly

what prompt caching is all about. So let's come back

in just a moment and we're going to walk through some of the implementation

details of prompt caching and really understand

how it is implemented by Claude.

---

#### Lesson 61: Rules of prompt caching

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289194](https://anthropic.skilljar.com/claude-with-google-vertex/289194)

**Video:** 08 - 006 - Rules of Prompt Caching.mp4 | **Duration:** 6m 41s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that we understand the theory, we are going to explore how prompt

caching Claude actually works. The core idea of

prompt caching is identical to what we discussed in the last

video. We will make an initial request off

to Claude. Claude is going to do some processing

on that initial message, and then Claude is going to

save all that work into a temporary cache.

Then if we make a fault request at some future point

in time and include the identical exact

same message, rather than processing that message

all over again, Claude is going to instead look into the cache,

find the work that it had already saved, and load

it up. Just to be clear, the work that be saved the

cache does not persist forever. It is only stored

there for five minutes. You're going to find prompt

caching is most useful anytime that you are

repeatedly sending the same content over to Claude again

and again and again, because it really is this kind

of two phase process. We have to make that initial request

to write some data into the cache, and then only the follow

up requests are going to be able to take advantage of that work

that was done ahead of time. This caching system is not

enabled by default with Claude. Instead, to turn

on caching, we have to manually add a cache breakpoint

to a block inside of one of our different messages. And

I've showed an example of that on the right-hand side in this example

user message. So all we have to do to turn on

caching is put in that little cache control field. And

there's a lot of rules around what that cache control thing actually

does. But before we go into those rules and really explain

what's going on, I want to give you a little tip

here, something that's going to make your life a little bit easier.

Throughout this course, we've been making use of a little shorthand

for writing out text blocks very frequently. And I'm

showing that on the left hand side. So this is a user message

that is using the shorthand for defining a text block.

If we have a user message that only has a little bit of

text signed to it, we can assign a string directly

to that content field. There is another way

in which we can write out a text block, and I'm showing this alternative

way of writing out a text block on the right-hand side. So

the alternative method is to write out a content field,

assign a list to it, and then side there put a dictionary

that has a type of text and then a text field that

contains your actual text. Now, we have not really been making

use of that long-hand form. But if you want to use

cache control, we want to turn on this prompt caching feature,

you have to write out these text fields in long form.

So you can actually add on that cache control

field. In other words, we have to write out cache

control somewhere. And over here on the right-hand side, we have some place

to put it. If we use the short form, there's no place for

us to put it. When we add a breakpoint into a block,

All the content in our entire request is going to be cached

up to and including that breakpoint. So

in this scenario, if we send in a request like this where the first

block has a breakpoint, Claude is going to do some amount

of work processing this text right here. And

it's going to result in some amount of work done. Because

this text block has a breakpoint, this work is

going to be stored inside the cache. But this

later work is after the breakpoint, so it's not

going to be cache. If we then send a follow-up request later

on, Claude is going to take a look into the cache and find

that some work was already done for processing this

very first block. So it's going to retrieve that work and

use it to save itself a little bit of effort. One thing to keep

in mind is that our follow-up request must have identical

content inside of it all the way up to that breakpoint.

So for example, if our initial text block right here

that had a breakpoint, if we added in just the word, please

do it. No longer is this content identical. And

so this work would not have been used as out of the cache.

Instead, Claude would reprocess this entire block

and all the content before it. Cache breakpoints can

span across multiple different messages and multiple different

blocks. So for example, if we send in a user

message and then an assistant and then another user,

and the very last message here has a block with a breakpoint,

Everything is going to be cached up to and including

this block right here. So we'd imagine that the

work that is done to process all three of those messages is

going to be stored inside the cache. Then when we make

our follow request later on, as long as everything up

to and including that break point is identical, the

work is going to be retrieved out of the cache. And again, we're

going to save ourselves a little bit of effort. We are not restricted

to adding cache points onto text blocks. We can

also add them onto almost any other type of block, like

an image block or a tool use or a tool result.

We can also add these onto tool schemas and

onto system prompts as well. And I've shown an example

of both those on the right-hand side. You are very often going

to enable caching for your tools and for your system

prompt as well. Because it turns out that for most applications,

not all, but for many applications, your system prompt

and your list of tools don't end up changing. So these

are excellent places to place a cache breakpoint.

In total, we can apply a breakpoint to tool schemas, system

prompts, and message blocks. Now, these are

not three separate cache systems. And

let me show you exactly what I mean by that. Whenever

you add in tools, a system prompt, and messages, behind

the scenes, these all get joined together when they are

fed into Claude, and they get joined together in that particular

order. It is first the tools, then a system prompt,

and then your list of messages. So if you place a

cache breakpoint on your very last tool, everything

up to and including that last tool will

be cached. But the system prompt and your list

of messages will not be cached. So if we then

make a follow request and we change that assistant message

right there, toy fine. We're still

going to save ourselves a little bit of work because the list

of tools was cash ahead of time. Last thing I

want to mention very quickly is that we can add in multiple different

cash breakpoints, up to four in total. So

I might decide to add in a cash breakpoint at the last

tool schema that I pass in, and then maybe I add

in a cash breakpoint on this assistant message down here.

If I then make a follow request and I change the user

message down here, no problem. We're going to save

ourselves the work of having to reprocess the entire

list of tools and assistant prompt and user message as well.

Likewise, if we change the first user message, well,

then we're going to invalidate the cache for everything down here, but

we'll still have the cache work for our list of tools.

So we are very often going to add in multiple different cache

breakpoints if appropriate. We might decide to

cache our entire list of tools and the system prompt

and maybe some number of messages as well. Exactly

where you place these different breakpoints really just comes down to

your particular application. The very last thing I want to share

with you is that there is a minimum content length for caching.

So in order to cache some amount of content, we must cache

at least 1,024 tokens. So

on the top right-hand example, I've got a cache breakpoint

on a message that has only the text high there. This

is definitely not 1,024 tokens long,

so this content would not be written to the cache.

But if I took that text block and duplicated

500 times, now I've

probably got greater than 1,024 tokens, so

this entire list of different blocks would be cash.

---

#### Lesson 62: Prompt caching in action

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289200](https://anthropic.skilljar.com/claude-with-google-vertex/289200)

**Video:** 08 - 007 - Prompt Caching in Action.mp4 | **Duration:** 7m 21s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Time to get our hands dirty with prompt caching. I've

created a new notebook called 003 caching.

You will of course find it attached to this lecture. Inside

here, you'll find a section called prompt with 6K

tokens. So this is meant to serve as a system prompt.

We're going to use it in a little bit. In addition, there is a

tool schema section. It has several different tool schemas to

find inside of it. All these different tool schemas put together

total it to about 1.7K tokens.

We're going to work on updating our chat function,

which is inside the cell up here called helper functions. We're

going to make sure that our chat function always enables prompt

caching for our tool schemas and our system

prompt by default. So let me show you how you would

do that. Inside the helper function cell, I'm

going to scroll down to our chat function. Here it is right

here. I'm going to scroll down a little bit further and you'll notice

I added in two to-do items. First,

if a tools list is provided, I want to always cache

the list of tools. Secondly, if we provide a system

prompt, I want to cache that as well. Remember

that we can have multiple different cache breakpoints inside

of a single request. So if we end up passing both

a system prompt and a list of tools, we're going to set two

different cache breakpots. Let's first take care

of caching our list of tools. Now,

to do so, remember, we need to modify the very

last tool schema that we pass into Claude.

We need to, in particular, add on that cache

control field. But we could do something like

this. We could just say tools, negative

one, and then set a cache control

field on it of type ephemeral.

Like so. As we definitely work, but it's not

the best coding technique. You see, this will

actually modify our tool schema by adding in the cache

control field to it. There might be some scenario in

our application where we later on decide to change

the order of our tool schemas that we're passing in. And if

we did so, we would then end up with multiple different cache

breakpoints being set up inside of our tool schema, which

might not be exactly what we desire. So a little

bit better way of doing this would be to

first create a copy of our tools list.

Then we will clone the last tool scheme inside

there and add the cache control field to it. So

let me see how to do that. I'm going to make a new variable

called tools clone, which will come from calling tools.copy.

So that's going to make a total copy of the list. Next,

I'm going to copy the very last tool inside there. I'm

then going to add on the cache control field to

the last tool schema. So

that will be type ephemeral.

Then I'm going to overwrite the last element inside

tools clone with the tool schema copy that

I just made tools. clone

at negative one will be the last tool. And

I'm going to assign my tools clone to

the tools program. Now, just to repeat here really

quickly, all this copulogic I have inside of here is

not strictly necessary. It's just good practice, again,

in case we ever decide to change our list of tools

at some point in time. Next up, we'll take care of the second

to do. So if we pass in a system prompt, I

want to make sure that we always set a cache breakpoint on it. To

do so, I'm going to remove the comment. I will

replace system with a list. We're going to put

inside of here a text block. So we'll be

a dictionary with a type of text,

text of system, and then finally

a cache control type

ephemeral. And that's it. Alright,

so let's now run the cell. We're going to go down to the very bottom

and test out this caching that we have set up. So

down here at the very bottom, I've already defined a list of tools. These

are tool schemas that are defined inside the cell right above. We've

also got that very large system prompt right here

of code prompt. So let's first try just passing

in nothing at all. So no list of tools, no prompt

whatsoever. We're just going to see the number of tokens that are

used to process the message of was one plus one and

generate a response. So if I run this, I'll

get back in output and we can notice that there is a usage

field inside of here. So it looks like we sent in 14 tokens

and we got 11 out. Let's now try adding

in our list of tools. So

when I add that in and run this, we're now going to

see a very different usage field. Now

our usage has a cache creation input tokens

of 1700. That means that Claude has

seen that we want to do cache our schemas. So

it has written into the cache a total of about 1700

tokens. So now if we make a follow-up request

immediately, without changing anything about it, we'll

see that we are now going to read a certain number of tokens

out of our cache. So now we've got a cache read

of 1700. That means that we have successfully

stored our schemas inside the cache and then retrieve

them at some point in time in the future. Now, if

we change our user message here in any way,

maybe by deleting that question mark at the end,

and then rerun this, we are still going to read out

of the cache because remember the caching order is the list

of tools, then our system prompt, and then our different

messages. So we'll still read out of the cache like

so. However, if we change any

of our tools in any way whatsoever, we're

going to invalidate the cache. So if I go to my

list of tools, I'm going to change the

description on the very first tool. I'm going to remove the

S on the word ads. So now let's just add a specified

duration. Now if I rerun cell,

I've changed my tool schema. And that means that

the cache breakpoint that we have applied to all of our different tools

is no longer going to apply. If I run the very bottom

cell again, we'll see an updated value

of usage. So now we're going to have a cache

write once again. So no longer reading. We're now back to

writing because we have sent in a list of tools that

as far as Claude is concerned is completely different.

All right, so now let's try adding in our system prompt. I'm

going to go to our chat function, and I'll add in system

code prompt. So now when we make

this request, remember the order of caching, it is tools,

then the system prompt, and then our list of messages.

Because we are leaving our list of tools completely identical,

but we are changing the system prompt, I would expect to see

a partial cache read and then a cache

write at the same time. The cache read that we're going

to see is because we are making use of the same list of tools. And

the cache write is going to because we are sending up a new

cache breakpoint by sending in this new prompt.

So I'm going to run this. And now we should see a,

there we go, a cache read of 1700 and a

cache write of 6.3. Now,

just like our list of tools, if we go up to our system

prompt and we change this prompt in any way, maybe

by just removing the word builder at the very end here

and then rerunning that cell. Now, once again, as far

as Claude is concerned, if we send in another request,

this will be a completely different system prompt.

So we are going to lose out on all the cache data we had

previously around the system prompt. So now I'll send

this again, and we will once again see a cache

read of about 1.7, there

we go. And then we are once again writing this brand

new system prompt, so that's another 6.3. All

right, my friends, that is prompt caching. Again, you're

going to very often use prompt caching anytime you are sending

in identical content, either in the form of the same

list of messages, the same tool schemas, or the same

system prompt.

---

#### Lesson 63: Quiz on features of Claude

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289275](https://anthropic.skilljar.com/claude-with-google-vertex/289275)

---

### Model Context Protocol

#### Lesson 64: Introducing MCP

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289201](https://anthropic.skilljar.com/claude-with-google-vertex/289201)

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

#### Lesson 65: MCP clients

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289204](https://anthropic.skilljar.com/claude-with-google-vertex/289204)

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

protocols. A very common way to run a MCP

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

are going to walk through a example call between

a lot of different things. So it's going to be kind of an involved

process. But we're going to imagine the communication that goes on between

a user or a server that we're putting together.

An MCP client, the MCP server, GitHub

as some provider that we're trying to access some data from, and

Claude. So let's get to it. Again, Stephen Grider. First

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

#### Lesson 66: Project setup

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289199](https://anthropic.skilljar.com/claude-with-google-vertex/289199)

**Video:** 09 - 003 - Project Setup.mp4 | **Duration:** 3m 9s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

To better understand some aspects of MCP,

we are going to start to implement our own CLI-based

chatbot. This is going to give us a better idea of

how clients and servers actually work together. In

this video, I want to do a little bit of project setup and just help

you understand exactly what we're going to make. I've got

a lot of project description over here of what we're going to build.

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

a project where we make only an MCP

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

#### Lesson 67: Defining tools with MCP

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289235](https://anthropic.skilljar.com/claude-with-google-vertex/289235)

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

this, behind the scenes, MCP is going to generate

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

then I'm going to raise a value error with

a f-string of doc with id {doc_id} not

found. And

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

Or so we'll be consistent, call it edit_document. And

then we're going to take in a couple of different arguments here. First

is going to be a document ID and then a old

string to find and then a new string to replace

the old string with. So let's write this all

out. We're going to have a doc_id. That

will be a string with a description

of ID of the

document. that will

be edited. old_string will be a string with

a description of the text to replace.

Must match exactly, including

white space. And

then our new_string, the

new text to insert in place of

the old text. So our document editing here is

just a very simple find and replace. That's it. Once

again, inside of here, I'm going to make sure that Claude

is asking for a document that actually exists. So if doc_id not

in docs, raise

value error with an f-string

of doc with id {doc_id} not

found. And then if we do find the correct

document, here's how we will do our edit. We'll say docs

[doc_id] = docs[doc_id].replace(old_string, new_string)

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

#### Lesson 68: The server inspector

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289207](https://anthropic.skilljar.com/claude-with-google-vertex/289207)

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

address to actually access it. I'm

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

#### Lesson 69: Implementing a client

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289206](https://anthropic.skilljar.com/claude-with-google-vertex/289206)

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

right here in case you are not making use of UV. So

if you're not using UV, make sure you take a look at that comment.

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

do a UV run, MCP underscore

client.py. And as usual, if you

are not making use of UV, you'll just do a Python

MCP client.py. Okay, so I'll run

that, and there is our list of tool

definitions. So I can see inside of here that I have the read.contents

tool, which we put together a little bit ago, and our edit

document tool as well. Each one has a description

and a input schema as well.

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

my project with a UV run main.py.

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

#### Lesson 70: Defining resources

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289248](https://anthropic.skilljar.com/claude-with-google-vertex/289248)

**Video:** 09 - 007 - Defining Resources.mp4 | **Duration:** 9m 45s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, we're going to move on to the next major feature inside

of MCP servers, which is Resources. To

help you understand resources, we're going to be implementing another

feature inside of our project. Here's what we're going to add in.

I want to allow a user to mention a document

by putting in an add symbol and then the name of a document.

Whenever they do so, I want to automatically fetch the

contents of that document and insert it into the prompt

that we send off to Claude. So in total, there's kind

of two aspects to this feature. Whenever user types

out the at symbol inside the message, we're going to automatically

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

a user types in the at symbol, we really need

the MCP server to give us a list of all the

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

read the contents of a single document. so we would

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

same thing, such as docs://documents.

A templated resource will have one or more parameters

inside of its URI. So for example, we might have documents

/ and then kind of a wildcard right here. So

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

put in the comment document IDs. Remember

for us, our document IDs are essentially the

name of the document. So for us, we're really just returning

these IDs. They're going to serve the purpose of the name. That

means we can put them directly into that autocomplete element.

All right, so to make our resource, I'm going to delete

that to do. and then I'll add in a MCP.resource.

The first argument is going to be the URI for accessing

this thing. Again, it's kind of equivalent to a route handler.

So I will use docs://documents, and I'm also going

to add in a MIME type of application

/json. A resource can

return any type of data, so it can be plain text,

it can be JSON, it can be binary data, anything.

is up to us to kind of give our client a hint

as to what kind of data we are returning. To do

so, we're going to define this MIME type. A MIME

type of application/json is a hint to

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

resource, docs:

/documents/<doc_id>. And then this time I

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

in this scenario, my MIME type would be text/plain,

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

is asking for actually exists. So if doc

ID not in docs, I'm

going to raise a ValueError with

an F string that says doc with ID {doc_id} not

found. And then if we get past that check, I'll

return docs[doc_id]. And

that's it. Now let's try testing this stuff out inside

of our MCP Inspector once again. So

remember at our terminal, we can run the command UVicorn,

MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPGDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.MCPDev.

---

#### Lesson 71: Accessing resources

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289247](https://anthropic.skilljar.com/claude-with-google-vertex/289247)

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

Then I'll go back down. to

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

#### Lesson 72: Defining prompts

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289249](https://anthropic.skilljar.com/claude-with-google-vertex/289249)

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

This is the real goal of the prompts future inside

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

contents using the read document tool. And then after

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

and hopefully we're going to get back some appropriate kind of response.

So once again, the entire idea here behind these

prompts, we might implement inside of our MCP server, is

that the prompts we are defining are going to be well-tested,

well-evaluated, really specialized to one particular

use case.

---

#### Lesson 73: Prompts in the client

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289209](https://anthropic.skilljar.com/claude-with-google-vertex/289209)

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

result dot prompts. And that's pretty much it.

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

dot messages. So those are the messages coming

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

that single user message, and feeding it directly

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

#### Lesson 74: MCP review

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289205](https://anthropic.skilljar.com/claude-with-google-vertex/289205)

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

to put together a series of different prompts inside of an MCP

server. Likewise, if I go back and

maybe click on this little tab right here, the plus button,

you'll notice that I have an add from Google Drive button.

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

#### Lesson 75: Quiz on Model Context Protocol

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289276](https://anthropic.skilljar.com/claude-with-google-vertex/289276)

---

### Anthropic apps - Claude Code and computer use

#### Lesson 76: Anthropic apps

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289230](https://anthropic.skilljar.com/claude-with-google-vertex/289230)

**Video:** 10 - 001 - Anthropic Apps.mp4 | **Duration:** 0m 43s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this module, we're going to take a look at two applications

that have been built and deployed by Anthropic. They

are Claude code and Computer use. Claude

code is a terminal-based coding assistant. I'm going to help

you go through the setup process and then we're going to use Claude code

on a very small sample project to understand exactly

how it works. After that, we're going to take a look at Computer

use. Computer use is a set of tools that dramatically

expands Claude's capabilities. Both Claude code

and Computer use are extremely useful in their own right, but

there's another reason that we're going to discuss them. You see,

Claude code and Computer use are perfect examples of agents.

And once we understand how they work, we'll be much better prepared

to understand what agents are and how to build an effective

agent. So let's go through the setup process

of Claude code in the next video.

---

#### Lesson 77: Claude Code setup

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289232](https://anthropic.skilljar.com/claude-with-google-vertex/289232)

**Video:** 10 - 002 - Claude Code Setup.mp4 | **Duration:** 1m 31s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's take a look at Claude Code. We'll do some

setup, learn how it works, and see some advanced use

cases. Claude Code is a terminal-based

coding assistant. This is a program running

in your terminal that can help with a wide variety of code-related

tasks. To help you with coding projects, Claude

Code has access to many different tools.

So it has many basic tools like the ability to search, read,

and edit files. But it also has many advanced

tools like web fetching and terminal

access. Finally, Claude Code can act

as an MCP client. And you know what that means. It

means it can consume tools that are provided by MCP

servers. So we can easily expand the capabilities

of Claude Code by adding in some additional MCP

servers. Let's now go through a little bit of setup and

install Claude Code on your machine. Setup

is easy. We're going to first install a copy

of Node.js. You might already have Node installed

on your machine, and to figure out whether or not you do, open up

your terminal and execute the command NPM help. If

you see a result come back, that means you probably already

have Node installed. Once you have node installed,

you'll do a NPM install command that will install

Claude Code itself. Finally, you will need to set up three

different environment variables, and I've listed those out at the bottom

of this diagram. Now a full setup guide can be

found at the official Anthropic documentation at

docs.anthropic.com. Now I'm going

to let you go through this setup process on your own, again, just

these three steps right here. As soon as you are done,

we're going to walk through a little project together and

see what Claude Code can really do for us.

---

#### Lesson 78: Claude Code in action

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289246](https://anthropic.skilljar.com/claude-with-google-vertex/289246)

**Video:** 10 - 003 - Claude Code in Action.mp4 | **Duration:** 10m 29s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

To get you some hands-on experience with Claude Code, I

created a small project for us to work on. You should find

the source for this project in a zip file attached to this lecture.

I would encourage you to download this zip, extract its

contents, and then start up your code editor inside of this

new project directory. I've already opened up the project inside

of my editor. And once you have the project open, you might

be tempted to look through the project contents and maybe go

through a little bit of setup which is described inside the

ReadMe file. But before you do, there's

something important I would like you to understand about

Claude Code. Claude Code is not

a tool that is just going to write code for you.

Naturally, it absolutely can, but that's not the only thing

that Claude Code is about. Instead, you really want to

view Claude Code as another engineer who's

working on this project alongside you. Every

task that you would normally go through on a normal project can

really be fully delegated off to Claude. So

this includes everything from initially setting up a project

to designing new features, to deployment, and to support.

As we go through this project, we're going to leverage

Claude heavily to aid us in various steps. We

will use Claude to set up the project for us, to

plan out a new feature, to write tests and code, and

then later on, on a slightly different project, I'll show you how

we can use Claude Code to automatically discover and

fix errors in a production environment. So

let's get to it. Back inside my editor, I'm going

to open up my terminal and then launch Claude

Code inside there by executing Claude.

Then once I have this open, I'm going to put in my first directive

to Claude. I'm going to ask it to read the contents of

the ReadMe file and go through any

setup directions that are listed inside of here. I

will ask Claude to read the contents of the ReadMe file and

execute these setup directions listed in it. Claude

will then use a variety of different tools to read that file

and then execute a series of different commands. It will create

a new virtual environment, activate the environment, and

install some dependencies. Once that is complete,

we are going to run a command that will help Claude get a better understanding

of our project. We're going to do so by running the init

command. This is a command that we're going to execute inside

of Claude Code itself. When you execute this command,

Claude will automatically scan your code base to understand

your project's general architecture, coding style, and

so on. Once complete, Claude will write

all of its findings into a special file named Claude.MD.

Whenever we run Claude again in the future, this file

will be automatically included as context. And

just so you know, there are three different Claude files, Project

Local and User. We're going to see some references to these

in a minute. So we'll discuss what they're all about then. Whenever

you run this init command, you can also actually add

in some special directions for some areas for Claude

to focus on. So let's try this out right now and

see what is generated for our project. I'm going

to run the init command, and when I do, I'm going to pass in some

special instructions. I'm going to ask Claude to include

some detailed notes on defining MCP tools. Once

it is all done, I'm going to take a look at the newly generated

Claude.MD file. So this is a summary of

what Claude thinks of our codebase. At the top, it will list

out some important commands that it might need to run in the future. We'll

get some listing around our coding style that we've used inside this

project. And then as I specially requested, it

also included some information around defining MCP

tools. As I mentioned a moment ago, this file is going

to be included as context for Claude in any follow-up

request we make in the future. Now, projects

change over time. We might change our coding style

or add in some additional commands. So if that ever happens,

we can very easily manually edit this file, or

we can choose to rerun the init command. If

you rerun this command, Claude will update the contents

of the Claude MD file. Finally, as a very

small shortcut, we can put in a Pound and

then type in some specific note that we want to be appended

into the contents of that file. So we can use this as

a tool to give very specific small directions to Claude

that will be included in all follow-up requests. So

for me, I might add in a direction here that says something

like always apply appropriate

types to function args.

And if I run that, I'll then be asked where I want to add

this little note. This is where we see that project memory,

local memory, and user memory appear. In my case,

this is a note that I want to be shared with everyone who is working

on this project, so I will add it to project memory.

Once I add that in, I can then check the contents of my Claude.md

file, and either somewhere under Code

Style or perhaps at the very bottom, I'll probably see whatever

note I just added in. At this point, we have

added a new file to our project, and this project

is being managed by Git. So normally, we would open

up our terminal, stage this new file that we just

created into Git, and then commit those changes. We

could do all that manually, but it'd be a lot faster if we just

asked Claude to do it for us. So I'll ask Claude

to stage and commit all changes.

Claude will then take a look at all the different changes we have made to

the codebase, write a descriptive commit message,

and commit those files. Next up, I would

like to show you some techniques for increasing Claude's effectiveness

when writing code. We are going to add a new feature into

this project. As a reminder, this project is a very

small, very simple MCP server. We

are going to ask Claude to add in a new tool to the server

that will read a Word document or a PDF file

and convert the contents to Markdown. Now, we

absolutely could just type in directions for

that to Claude, something like make a Word doc plus

PDF file to Markdown conversion tool. But

before doing that, I want you to know that we can dramatically

increase the effectiveness of Claude by putting

in a little bit more effort. So let me show you how.

Think of Claude Code as being an effort multiplier.

If you put a little effort into how you direct Claude,

you will get back significantly better results. I'm

going to show you two different workflows, two different ways

of instructing Claude on how to approach a task. Both

of these workflows require a little bit of effort on your side,

but they allow Claude to tackle much more complex

problems. In this first workflow, we're

going to go through three distinct steps. First, we're

going to identify some areas of our code base that we know are

relevant to a feature that we are trying to work on. We're

then going to ask Claude to specifically read and analyze

those files. Second, we're going to tell

Claude about the feature we want to build and ask it to

plan out a solution. So the steps will actually

go through to implement whatever feature or problem you're

trying to solve. And then finally, after Claude

has gone through that planning step, we will ask Claude to actually

implement these solutions. Let me show you how we would do

this for our particular feature of adding in some

new document conversion tool. So

first, I'm going to go through my codebase and identify some different relevant

files. You'll notice there is a Tools directory,

and inside there is a Math.py file. This

is an example of a tool that has already been put together. So

this might be some file that is relevant for the feature that

we are trying to build, just because it gives Claude a

better idea of how to author a tool.

Second, we might ask Claude to take a look at the document.py

file, which includes a very helpful function,

binary document to markdown. So this will take

in some amount of binary data and convert it to markdown.

So we can tell Claude to take a look at these files, and

Claude will get a better idea of how to write a tool in the first

place, and then how to actually do the conversion. So

I'm going to add in some instructions to Claude and

ask it to just read the contents of those files.

Next, I'm going to ask Claude to plan out the implementation of

a new tool called Document Path to Markdown, which

will take in a path to a PDF or Word document,

read the file, convert the contents to Markdown, and return the

results. I'm also going to tell Claude specifically

to just plan the feature out and not to write any code just

yet. In response, Claude is going to give us a

pretty well detailed plan that's going to go through

a couple of different steps that will be required to implement this entire

thing. Finally, I will ask Claude to implement

this plan. It's first going to update the document.py

file, which is definitely correct. It's then going to

update the main.py file, which is also good.

And then finally, it will author a test around this new tool.

It's then going to run the test suite and make sure that the test actually

passes. You'll notice that in the summary message,

Claude also tells me that added in some error handling for

non-existent or unsupported file types, which was

definitely appropriate, even though it wasn't something

that I actually asked for explicitly inside of my description

of this feature. I'd like to show you another way that

we could have asked Claude to implement this feature. Before

I show you this alternative, I'm going to get Claude to remove

all the code that it just wrote by stashing these

changes. Now I am back to a clean

slate where I don't have anything related to that new feature

that was just implemented. The second technique

that we are going to explore is a test-driven development workflow.

Again, this requires some more effort from you up front,

but it dramatically increases Claude's effectiveness. With

this workflow, we will again ask Claude to take a look at some relevant

context. Then, before writing any code,

we're going to ask Claude to think of some different tests

it could write related to our feature. Next,

we will select the most relevant tests and ask Claude

to implement them. Finally, after we have got

some working tests put together, we will ask Claude

to write out a solution and write code until

the tests actually pass. So let me show

you how this approach would actually look for the same exact

feature, one where we are building a tool that's going

to read a document off of our hard drive and

convert contents into Markdown. First,

I'm going to run the slash clear command. This

is going to clear up my conversation history with Claude, essentially

reset its context. In this case, I'm doing

this just so it doesn't cheat off its previous solution. Then

I will ask Claude to read those two relevant files once again.

Then I'm going to add in some very clear instructions to think

of some tests that it might write to evaluate this new feature

that we want to build. Again, I'm going to ask it specifically

to not write any code just yet. The

suggestions I get back are really solid. Now, I don't

really want to have to worry about tests 6, 7, and 8 because

those are a little bit more specialized beyond what

we're doing right now. So I'm going to ask Claude to just implement

tests one through five. Now

we will move on to the last step, where we will ask Claude to write

out some code to make these tests pass. Very

good, all the tests pass. Now, before we move

on, I just want to remind you one more time that Claude Code

really is an effort multiplier. You can

put in very simple directions, and Claude will do its best. But

you can dramatically increase Claude's effectiveness by putting

in a little bit of effort on your side as well.

---

#### Lesson 79: Enhancements with MCP servers

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289231](https://anthropic.skilljar.com/claude-with-google-vertex/289231)

**Video:** 10 - 004 - Enhancements with MCP Servers.mp4 | **Duration:** 2m 30s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, I want to show you one of the most interesting aspects

of Claude Code. Claude Code has an MCP

client embedded inside of it. That means we can connect

MCP servers to Claude Code and dramatically

expand its functionality. To demonstrate

this, we are going to connect Claude Code to the MCP

server that we have been working on. We just authored

a tool called Document Path to Markdown. We

can now expose this tool to Claude Code, allowing

it to read the contents of PDF and Word documents.

So we are dynamically expanding the capabilities

of Claude Code. Let me show you how to set this up.

Back inside of my terminal, I'm going to end my running session with

a control C. I'm then going to add in

an MCP server to Claude Code by executing Claude,

MCP, add, then we're going to put in

the name for our MCP server. Now the name could be anything

you want it to be. In our case, we are making a server

related to documents, so I'm going to call our server documents.

And then finally, we're going to put in the command that we used to start

up our server, which for us is uvrun main.py.

So uvrun main.py. And

that's it. I'm going to execute that, and I'll

start Claude Code back up with Claude. And

now we can make use of that tool that we just put together to

really test it out inside of our test directory. There

is a fixtures folder inside there are two demo

files, so a Word doc and a PDF doc. Both

contain just a tiny bit of documentation around MCP

itself. So I'm now going to ask Claude to convert

the contents of either one of those files into Markdown.

And my expectation is that Claude will make use of that

tool that we just authored a moment ago. And

if we scroll up just a little bit here, sure enough it worked.

So this actually is the contents of that file. This ability

to consume MCP servers adds an incredible amount

of flexibility to Claude Code, and really opens the door

to some really interesting development opportunities.

For example, you might decide to add in a series of MCP

servers related to your particular development flow.

For example, if you use Sentry for Production Monitoring, you

can add a Sentry MCP server to allow Claude

to fetch details about errors that are occurring in production.

If you make use of JIRA, you can add in an MCP server

that will allow Claude to view the contents of specific tickets. If

you're a Slack user, you can add Slack to message you whenever

Claude is completed working on some particular

problem. These are just a small fraction of

the possible enhancements that you can add into Claude

Code. So it would definitely worth your time to think

about how you can enhance your particular development workflow.

---

#### Lesson 80: Parallelizing Claude Code

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289241](https://anthropic.skilljar.com/claude-with-google-vertex/289241)

**Video:** 10 - 005 - Parallelizing Claude Code.mp4 | **Duration:** 8m 12s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, we are going to explore one of the greatest productivity

gains around Claude Code. Because Claude is a lightweight

process, you can easily run multiple copies of

it. Each instance can then be given a task, and

the separate instances will then work in parallel. This

technique allows a single developer to command their own team

of virtual software engineers. So in the remainder

of this video, I like to show you some of the specifics of implementing

this workflow on a real project. The first big

challenge to address is the fact that two instances

of Claude might want to work with the same file around

the same time. They might end up writing conflicting code

or even invalid code, because they're not aware that

some other process is modifying that same file. To

solve this, we can make sure that each instance gets its own

separate workspace. Each instance can then work

with its own copy of your project, make changes,

and then eventually merge those changes back into your

primary project workspace. A common

way of implementing this is by using a Git work

tree. Git work trees are a feature of

Git, so if your project is already managed by Git,

you can use work trees immediately. Work

trees are like an extension of Git's built-in branching

functionality. A work tree allows you to create

a total copy of your project inside of

a new directory on your development machine. Each

work tree corresponds to a separate branch. So

if we have Feature A on the left and Feature

Branch B on the right, we can easily create two

separate folders, each of which contain a complete

copy of our codebase. Then

we can run separate instances of Claude Code for

each work tree. They will each work in their own

separate environment in total complete isolation.

Once each copy of Claude Code has then finished

some feature, we can then commit the work for each work

tree, and then merge them back into our main

branch, just like we would merge a normal branch. Now,

this might sound like a really complicated workflow

that would be very tough to manage. But remember,

you can delegate an amazing amount of work to Claude Code,

including tasks around Git. So we can

actually get Claude Code itself to manage this entire

workflow. Let me show you how.

First, we can write out a prompt that will ask Claude

to create the work tree for us. We might ask

it to also open up our code editor inside of the

newly created work tree folder. And that's what

I'm asking for inside this prompt. I'm asking Claude

to make a new work tree inside of a directory at

trees slash feature a. I'm then

going to ask it to Simlink in some dependencies because

those are not tracked by Git and so they will not be automatically

copied into the WorkTree directory. And then I'll ask

Claude to also open up my code editor inside

of that new sub directory. Now let me show you how this

would actually all work. So I'm going to take this exact prompt

right here. I'm going to run it inside of Claude Code.

Claude will then create the work tree, create the Simlink

of the virtual environment, and then open up a new code

editor instance inside of this new sub project

folder. Inside of my original editor

window, I'll see that there is a new trees directory.

Inside there is a feature, a folder. Inside

that feature, a folder is a total copy of my project.

And that copy has been opened up automatically inside

of this new editor window. So inside this new

editor window, I can launch Claude Code

and ask it to fulfill some task,

maybe add in some new feature or write tests or do whatever

else I need. And now this instance of Claude Code

is running in total isolation. Before

I ask Claude Code to do anything inside of here, however,

I want to point out that this is a really long

prompt to remember. And it's really tedious to have to copy

paste all over the place anytime that we would want to create a new

work tree. So we're going to do a quick side topic here

really quickly, a little side feature of Claude

Code that makes it really easy to create and merge

in these separate work trees. So we could

automate this entire prompt by making use of another

feature of Claude code. Support for custom

commands. You can add in custom slash

commands to Claude code by creating a markdown

file inside of a special directory inside of your project.

The special directory is dot Claude slash commands.

inside of a file inside that directory, we'll write

out our entire prompt, and then we can easily run

this custom prompt any time we want to. Let

me show you how we can use this feature to easily create a

new work tree. So inside my original

editor window, I'm going to make a new folder

called .Claude, inside there

I'll make another folder called commands, and then

inside that I'm going to make a file called, how

about createWorkTree.md. And

then inside of that, I'm going to paste the prompt that we

saw just a moment ago. Now,

this prompt has a hard coded feature name or hard code

branch of feature underscore a. And I don't always

want to have exactly that string. So I'm going to replace it with

a special string. of

$ARGUMENTS, all capitals.

This allows us to inject some additional argument

when we actually run this custom command. So now if I

save this file and restart Claude

Code very quickly, I

can run /project:

createWorkTree. It's

called specifically createWorkTree because that is the name of the file I

create inside that commands directory. I'll then put in a space

and then the name of this new work tree. And I'm going to call

it feature_B this time around. So

now feature_B is going to be taken and substituted in

for wherever I had placed $ARGUMENTS.

So now if I run this, I should very quickly

see a new work tree created. And

before long, I've got my new code editor instance. So

now this one is open inside of work tree feature

_B. And I can see that the additional work

tree has been created inside that trees directory. Now

that we've seen how we can create multiple different work trees, I want

to give you a full demo here. I'm going to

create four separate work trees. Each one is going

to be designed to complete some different tasks. So I'm going to have four

instances of Claude Code running. The first one

is going to add in some tests around documents. The second

one is going to add in some logging. The third one is going to add in two new

tools, and the fourth one is going to add in a subtract

tool. I'm going to run all these tasks in parallel,

and then I'm going to merge the changes from all of them back into

my main branch. So for step number one, I'm

going to create four separate work trees. I

now have four separate editor instances, one for each feature

that I want to implement. I will start up Claude Code in

each and give each of them some directions on some feature to

add in. When the work tree is complete, I will ask

Claude to commit that code. Then

when they are all complete, it is time to merge all these changes

from these different branches back into my main branch.

We do not have to do this by hand. Instead, we can

ask Claude to do it for us. So I put together another prompt

here, which I'm going to wire up as an additional custom command

inside my project. This prompt is asking Claude

to go into one of our different feature work trees. Take

a look at the most recent commit, just to understand what was done,

and then attempt to merge those changes back into the main branch.

I'm going to add this prompt in as another custom

prompt inside my project. So inside of Claude

commands, I'll make a new file. I'll call this one merge

WorkTree. Paste that in. I'll

then restart Claude Code. I'll

then run the mergeWorkTree command. And

I'm going to first ask it to merge in how about the document

test branch that was just created. I

can then repeat this process for all the other work trees

as well. When

I merge in the Subtract feature, there will be a merge conflict,

but Claude is going to automatically resolve the conflict for me.

When everything is merged in, I can then ask Claude to clean

up all these different work trees that have been created. And

that's it. So I have now implemented four separate features

entirely in parallel through the use of Git work trees.

This is clearly a really big productivity increase. And

it scales up to as many different instances as I feel

like I can manage at a single time as an engineer.

---

#### Lesson 81: Automated debugging

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289238](https://anthropic.skilljar.com/claude-with-google-vertex/289238)

**Video:** 10 - 006 - Automated Debugging.mp4 | **Duration:** 4m 24s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Claude Code is not just about helping you author

some code inside of your editor. It can also help you after

you have deployed your application in monitoring

for errors in helping you fix those errors as they arise.

So in this video, I'm going to walk you through a sample workflow where

we are going to take a look at a production application that is throwing

some errors, but only in a production environment. We're

going to see how we can make use of Claude Code to automatically find

and fix those errors. So first,

let me show you a little sample application I put together. This

is a very simple chatbot, and I'm currently running

it locally on my own computer. You can see the evidence

for that. I'm currently at localhost 3000. If

I ask any question here, let's say maybe what's one

plus one, no problem. I'll get back and answer

rather quickly. This chat application also has the

ability to make simple artifacts. So for example,

it can show a built-in spreadsheet. I'm going to ask

for a spreadsheet with some fake data. And

it appears that everything is working 100% as expected.

Now remember, this application is currently running in my local

development environment. But because everything is working just

fine as I'm testing it right now, I might decide to

go ahead and deploy it into production. So I've

already done that ahead of time. I've already taken this exact app

and deployed it off to AWS Amplify. So

this is a production version of the exact same

app it has hosted at Amplify right now. I'm

going to attribute the exact same test that I showed you a moment ago. I'm

going to first ask what is one plus one. Then

I will follow up with the exact same request that

I made a moment ago in the local application. So make

a spreadsheet with some fake data. And we're going to

see that the request goes through. But

unfortunately, the spreadsheet itself is completely empty.

There's actually no data that has been generated. So

it is now clear that something in this production environment

is not really working as expected. Everything

in development worked just fine. The exact same series

of operations completely fine in development, but specifically

in a production environment, I am running into this error. To

figure out what the issue is, I could take a look at my CloudWatch

logs. I already opened those up, and I've already hunted

through those logs and found the source of this error.

So I've got an error message here. It states the provided model

identifier is invalid. And then I've got a lot of debug

information included in here as well. So I

as an engineer could take this error message, which I

had to hunt down inside of my logs and do

a little bit of local debugging to try to figure out why

this is failing in production, but not locally.

Alternatively, I could delegate this entire

task off to Claude. Let me show you how. Inside

of my GitHub repository for this project, I created a GitHub

Action, which is going to run automatically every day, very

early in the morning. On the screen right now, I have the

results of a sample run from earlier today. I'll

show you some of these logs from the GitHub Action in just a moment.

But first, let me show you a diagram that's going to help you understand what

is going on inside this. OK, so

whenever this GitHub Action runs, it's going to check out my repository,

install some dependencies, and then install and set up

Claude Code. I then also install an AWS

CLI, which allows me to reach out and get some

logs from CloudWatch. I then pass off

some directions to Claude Code. I ask it to

reach out to CloudWatch and find all the errors that have occurred in

the last 24 hours. I also include some logic

in there to remove duplicate errors and reduce the total

number of errors down just to be manageable for Claude's

context window. Once Claude has a list of errors,

it then iterates over them and attempts to fix each one.

And then once Claude hopefully has successfully fixed

these errors, it will commit those changes and automatically

open a pull request where I can view its work. So

in this case, as we just saw, I'm getting an error in

our production environment. And I saw that error inside

the logs. If I now go over to my

list of pull requests right here, I'll say that Claude automatically

ran, it automatically found the issue, applied

a fix, and then created a pull request. So now

I could very easily review this pull request right here.

The entire issue is explained to me in plain detail, and

in this case, it was just a typo on my behalf. I

accidentally put in a invalid model ID that was

only used in a production environment. So Claude,

noticed that. It found the correct model ID and

put the correct one in, committed the changes. So

now I can very easily review the changes and merge the pull

request. This is just one sample workflow

that you might use to automatically monitor and fix your apps

in a production environment. Remember, Claude Code is

very flexible and you can create your own custom workflows

just like this one to aid your own debugging efforts.

---

#### Lesson 82: Computer use

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289233](https://anthropic.skilljar.com/claude-with-google-vertex/289233)

**Video:** 10 - 007 - Computer Use.mp4 | **Duration:** 3m 5s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's take a look at the computer use feature inside

of Claude. We're going to cover this in three different parts. I'm

going to first give you a quick demonstration of computer use and

help you understand why it's useful. We'll then take a look at

some behind the scenes stuff and understand how computer use works,

and then I'll show you how to set up the reference implementation

so you can test out computer use on your own. So let's

get to it. Let's first go over a quick demonstration of

computer use. For this demonstration, I've put together

a very small web application. All it does is

show a text area that supports the ability to

mention a file or some kind of resource using

the at symbol. So if I enter test

and then at, I can scroll through a bunch of different options

and eventually hit enter to select that particular option.

Now, first glance, this thing appears to be working just fine.

I can add in as many different mentions as I

want. But if we use it a little bit more, we'll start

to see a lot of janky behavior. For example,

if I add in two mentions and then press the backspace

key, I'll see that I suddenly get a pop-up on the top

left-hand side of the screen. So it's clear that this thing

doesn't quite work as expected. Now,

I could spend my time as a software engineer to sit

here and figure out all the different cases in which this component

fails. Or, alternatively, I can

delegate this task off to Claude's computer use.

Let me show you how we would do that. Now I have already

set up a computer use environment in this window.

So this is a demo that you and I are going to eventually

set up on your computer a little bit later on inside this section.

On the right hand side is a browser that is running inside

of a Docker container. So this browser is completely

isolated from the rest of my system. And then on

the left hand side, I have a chat interface where I can give direct

instructions to Claude and get Claude to interact

with this browser in some particular way. Inside

of that chat interface, I'm going to enter in a rather large

prompt to Claude. I'm going to tell Claude that it's going

to do some QA testing on a React component

hosted at some particular address. I then

outline some testing process for Claude, and

then some different test cases to go through. And at the very end,

I'm asking Claude to write out a concise report that

summarizes the output of all these different tests. So

again, I'm using Claude computer use here to automate some

QA testing just to save myself some time.

I want to take this big prompt, enter

it into this chat interface, and then Claude

is immediately going to spring into action. Claude

is going to follow us in the instructions I listed inside there, so it's

going to try to navigate to that site where I hosted this

application, and then go through each of those different test cases.

The first test case will just verify that the autocomplete options

appear. The second test case will verify

that pressing Enter will insert a mention. And

the third will make sure that pressing that Backspace key shows

the autocomplete options underneath the mention itself and

not on the top left-hand side. After

all the test cases run, we'll see some output in the chat

window. So it tells me that the first test and the second

test passed, but the third one failed. So again,

this is assigned to me that I probably need to go and investigate

this test case myself and figure out how to fix this. Either

way, Claude's computer use functionality saved me

the developer a lot of time on this QA process.

---

#### Lesson 83: How computer use works

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289234](https://anthropic.skilljar.com/claude-with-google-vertex/289234)

**Video:** 10 - 008 - How Computer Use Works.mp4 | **Duration:** 3m 26s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that we have seen a demonstration of computer use, let's

get a better understanding of how computer use actually works

behind the scenes. To help you understand computer use, we're

going to first get a quick reminder on how tool use works

with Claude. So whenever we want to use a tool, we

will make a request off to Claude, including a user

message and some tool schema. This tool schema

describes some additional functionality that we want to expose

to Claude. So in this example, I might send across

a tool schema of something like GitWeather that

would presumably allow Claude to fetch some weather in a particular

location like Navy San Francisco. Claude

is going to take a look at the user's message and realize that it can't

really answer the question by itself. So it's going to decide

to use that GitWeather tool. To use the tool,

Claude will respond with a tool use part. So

this will have a tool use ID, a name, and some

input that it wants to feed into the tool. In this case,

it would probably be a location of San Francisco.

Then our server is going to have some amount of code written

by you and me that will receive that location and then

return the current weather at that spot. We're

going to take that result and send it back to Claude inside

of a tool result part. So we can summarize

this entire process in a diagram like this.

We initially send Claude some kind of question and a list

of tools, Claude decides to use a tool, we run

some code or do something on Claude's behalf, and then

send the result back to Claude. It turns out that Computer

Use follows the exact same flow, because Computer

Use itself is actually implemented with this exact same tool

system. So here's how a computer use actually

works. We send a request off to Claude that includes a

very special tool schema. The schema we send is

very small. It's exactly what you see on the left hand side. And

it doesn't match the typical structure of a tool schema.

Behind the scenes, this schema will be expanded into a much,

much larger structure, like the one you see on the right. And

this larger structure is what actually gets fed

into Claude. This large schema tells Claude

that it can call an action function. And that

the action function takes arguments like mouse move,

left click, screenshot, and more. Claude

might then decide to make use of that tool in some way. So

it will send a tool use part back to us.

Remember what we saw a moment ago with the git weather function.

Whenever Claude decides to use a tool, it is up to us, the

developers, to actually fulfill Claude's tool use

request in some way. So to simulate a computing

environment for Claude, we can set up a Docker container,

running some program that can programmatically execute key

presses and mouse movements. Once we execute

the requested key press or mouse movement, we then

send a response back to Claude. So to summarize, this

is exactly what's going on behind the scenes with computer use.

Claude isn't actually directly manipulating a computer.

Instead, computer use is implemented using

the tool system. And it is up to us to provide

the actual computing environment. The last thing I'd

like to do is tell you how you can get started with computer use on your

own. Luckily, you do not have to create that

Docker container from scratch on your own. Anthropic

has already implemented a reference implementation. This

is a Docker container that already contains code to receive

tool request from Claude and execute programmatic mouse

movements and key presses inside of the container. I've

provided a link to the reference implementation on the left-hand

side. Setting up this implementation is really

easy. All you need to do is get a Docker implementation.

You might already have one installed. You'll execute a simple

Docker command and that's going to give you access to the same

interface I showed you just a moment ago. You can

then chat directly with Claude on the left hand side of the screen and

test out Claude's computer use functionality.

---

### Agents and workflows

#### Lesson 84: Agents and workflows

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289244](https://anthropic.skilljar.com/claude-with-google-vertex/289244)

**Video:** 11 - 001 - Agents and Workflows.mp4 | **Duration:** 4m 22s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this module, we are going to focus on workflows and

agents. Let's dive in immediately and understand

what these things are. Workflows and agents

are strategies that we use to handle the user tasks that

can't be completed by Claude in a single request. Believe

it or not, you have already been creating workflows and

agents throughout this course. For example, when learning

about tools, we fed tasks into Claude and

relied upon Claude to figure out how to complete them using

some provided tools. That was an example of an agent.

Now here's the rule of thumb that we use whenever we are trying

to decide whether to create a workflow or an agent.

If we have a very precise idea of the task we need to

complete and we know the exact series of steps that are

used to complete it, we'll use a workflow. Otherwise,

if we're not really sure about the details of a task that Claude

needs to solve, we'll use an agent. In this video

and the next couple, we're going to be 100% focused on

workflows. I'm going to show you several examples of

workflows, so let's take a look at our first one right

now. Let's imagine that we are building a small web application.

The goal of this app is to allow a user to drag and drop an image

of some metal part onto the screen. We're

then going to take that image and then somehow build a 3D

model out of it. We're then going to get the user back, something

called a step file. Now, if you're not familiar with a step

file, don't worry, a step file is just an industry

standard way of communicating or sharing 3D models.

So essentially, we're making a 3D model out of an image.

Now, even if you are not very familiar with 3D modeling, with a little

bit of help and a little bit of time, I bet you could figure

out a way to implement this application. Here's

how we might do it. We might take the image that the user

uploaded and feed into Claude and ask Claude to

describe this object in great detail. Then

we could take that description, feed it back into Claude

separately, and ask Claude to use a Python library

called CAD Query to model the object. CAD

Query is a Python library that allows you to do 3D

solid modeling, and you can output a step file

from that process. Now, it's entirely possible

that Claude is not going to get this model entirely

accurate the first time around. So once we build out this

initial model, we might decide to add in a little error

checking step, where we could create a rendering

as a plain image, and then feed that image

back into Claude and ask it how well this

image represents the original image that the user uploaded.

And if Claude decides that there are major issues in our rendering,

we can then go back to the second step and ask Claude to attempt

to render the part again. We can then repeat this

process over and over again until hopefully we eventually end

up with some kind of accurate model of the original part.

Now the important thing to understand here is that this is an

entire flow of steps that we can kind of imagine

ahead of time. We can sit down and design out this

entire process. We could easily write out some code to implement

it. As a matter of fact, I have previously implemented

something almost exactly like this. Because we can explicitly

list out and detail all these steps ahead of time, we

would refer to this as a workflow. Remember, we

define a workflow as a series of calls off

to Claude meant to solve some very specific problem,

where we really know exactly what those steps are supposed to be

ahead of time. This modeling workflow that I've described

is an example of something we call an evaluator

optimizer. The idea behind this workflow is that we

push some input into something called a producer. In

our case, the producer is Claude using the CAD

Query library to model a part and then creating

a rendering out of it. This output, the

rendering, is fed into something called a grader. The

grader will look at the output and decide if it meets some criteria.

If it does, then the workflow ends. Otherwise,

if the output doesn't meet some criteria, feedback

is given back into the producer, which gets an opportunity

to improve the output in some way. This cycle

is then going to keep on repeating until eventually the grader

accepts the output. Now, at this point in time, you've

probably got a somewhat reasonable idea of what this evaluator

optimizer thing is all about. But you're probably wondering, OK,

what exactly is going on with these workflows? So there's

just something I want to clarify here really quickly. Identifying

workflows doesn't really inherently do anything

for us. We still have to write down and write out the actual

code to implement these things. The only reason that we are

discussing workflows and the reason that you're going to see workflows as

a popular discussion topic is that many other

engineers have implemented workflows using these exact

same patterns and found a lot of success. So

the reason I'm showing you these different workflows is so that you can

use these same patterns on your own projects and

hopefully find some success with them because they have worked

well for other engineers.

---

#### Lesson 85: Parallelization workflows

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289236](https://anthropic.skilljar.com/claude-with-google-vertex/289236)

**Video:** 11 - 002 - Parallelization Workflows.mp4 | **Duration:** 3m 44s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Thank you. Let's take a look at another workflow. We're

going to change up our application a little bit this time around.

We're still going to ask the user to drag and drop an image of

a part onto the screen. But this time, we're going to give

the user back an analysis, a report that's

going to tell the user the best material to build their

part out of, depending upon some various criteria.

To implement this feature, we might take the user's supplied

image and send it off to Claude along with a short prompt.

And in the prompt, we might ask Claude to decide whether it would

be best to make this part out of metal, polymer ceramic,

and so on. Now, this would probably work, but

we are really asking a lot out of Claude in this very

simple prompt. For example, we haven't really told Claude

any of the real considerations that it should take into account

when deciding which material to use. So, even

though this might work, we might not get the best results.

So a natural improvement here would be probably to go

back to this prompt and add in a lot more detail. Maybe

tell Claude some of the different scenarios in which it should recommend

metal or polymer and so on. So we might

end up with a really, really large prompt like

this. We might give some criteria for deciding when

to use metal and then some criteria for deciding when

to use polymer and then repeat with ceramic composite

last mere wood and so on. We would end up with a

really, really large prompt that might end

up being a little bit confusing to Claude because it has to do

a lot of analysis and a lot of work inside of one

single step. So this might not lead to the best

results. Let me show you a better way to approach implementing

this feature. We could decide to make a series

of different requests in parallel off to Claude whenever a user

initially submits an image. Each individual request

could then include a specialized prompt asking Claude

if making this given part would be a good idea using

metal or polymer or ceramic or composite

and so on. So in each separate request, we are asking

Claude for the suitability of building this part in one

individual material. With this approach, we

could specialize each individual prompt for the given material.

And now, Claude doesn't have to worry about all these different materials.

It's really just focused on one individual material at a time.

Now, when we eventually get some responses back from Claude, I'm

going to change the structure of this diagram just a little bit so I can fit everything

on one screen. So we're going to get back these individual

analysis results from Claude. Each one is going to tell

us the suitability of building out the given part in, say, metal,

polymer, ceramic, composite, and so on.

We can then take each of these analysis results and

then feed them back into Claude in a follow request and

ask Claude to consider each of the different analysis results

and decide upon a final material to use. Now,

Claude doesn't really have to worry about comparing all these

different materials up front. Instead, it can just take a look at

the analysis results that seem to be the most promising.

This is an example of a parallelization workflow.

The idea behind a parallelization workflow is that we're going to

take one task and break it up into multiple different subtasks.

Each of these subtasks can be ran in parallel, so at

the same time. We will then take the results from all

those different subtasks and then join them all together in

a final aggregator step. In our case,

the aggregator was this final step with Claude right

here. So we fed the results of each parallel

task into the aggregator and Claude gave us this final

recommendation. There are several benefits to this workflow.

First, it allows Claude to focus on one task at a

time. So remember just a moment ago when I told you that we

could feed the original image part into Claude with a

really large prompt that listed out some criteria for

many different material types. In this scenario, Claude

might get a little bit confused or distracted as it tried to consider

all the different pros and cons of each material simultaneously.

The second benefit is that we can very easily improve and

evaluate the prompts that are being used inside of each subtask.

Finally, this flow can generally scale very well.

We can add in additional subtasks at any point if we want

to without really subtracting from the other subtasks

that are being executed.

---

#### Lesson 86: Chaining workflows

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289239](https://anthropic.skilljar.com/claude-with-google-vertex/289239)

**Video:** 11 - 003 - Chaining Workflows.mp4 | **Duration:** 4m 37s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next workflow that we're going to take a look at is going to seem

a little bit obvious and simple, but trust me,

this actually ends up being one of the most useful workflows around,

specifically in one particular situation that you're going to

run into very often. So let's get to it. Let's

change up our application a little bit once again. We'll

imagine that we are building a social media marketing tool. Users

will be asked to enter a topic for when their social

media accounts, kind of what the focus of their account is.

then the goal of our application is to generate

and post some videos to their account. So

here's how we might actually implement this. We

don't really need a fancy agent with a ton of fancy

tools to implement this. We can build out a workflow

that will just go through a series of predefined steps one

by one. So in step one, we might take whatever

topic the user entered into that form and do a search

for trending topics on Twitter. We

could then take the list of topics and feed them all into

Claude and ask Claude to select the most interesting topic.

Then we could do a follow-up request to Claude asking to do some web

research on the topic. Then once the research is

complete, we could ask Claude to write a script for a short

format video. Once we have the script, we could then use

an AI avatar and some text-to-speech program

to create an actual video and finally post that video

off to social media. This is an example of a

chaining workflow. In a chaining workflow, we take

one large task, which was initially to generate

some videos and post them to social media, and we break it up

into a series of distinct steps. In our case,

the subtasks were the individual calls that we sent off to

Claude. We could have attempted to accomplish all three of these

tasks inside of a single call off to Claude. So

we could have just fed in a list of topics to Claude, asked

it to select the most interesting topic, and research

the topic, and write a script inside of a single prompt.

but by breaking this up into three separate calls,

we allow Claude to focus on just one individual task

at a time. Now, like I said, this probably

seems like a kind of simple and obvious workflow,

maybe not even worth discussing because it might be something you've already

implemented in the past. But there's one very

particular reason that I point out this workflow in particular

because it actually ends up being on the most important

workflow to understand to get quality outputs out

of Claude consistently when using rather large

prompts. So let me walk you through a little scenario.

You might not have encountered this before, but I

can almost guarantee that you will at some point in time. Let's

imagine that you are making use of Claude to write an article on

some given topic. You might initially just send

in a very simple prompt to Claude and ask it to write an article,

and then you might get back some results, and although it might be okay,

there might be some aspects to it that you don't like.

So you might initially find that Claude might be mentioning the

fact that it is an AI authoring the article, which you

probably don't want. It might make excessive use of

emojis, which you might not want. And it might use a little

bit cliched language all over the place, which, again,

you might not want. And so over time, as you

start to develop this prompt, you might eventually set

up a big long list of things that you tell Claude

to just not do it all. But inevitably, Claude

might eventually, no matter how many times you repeat these items, Claude

might give you back a response that seems to somehow always

use emojis, mention the fact that it

has been written by an AI, and just generally have

kind of a cringey, non-professional tone to it.

And Claude might persist in writing an article like this, no

matter how many times you repeat these constraints or things

that Claude should not do. So to address this

problem, you can use a very simple prompt-chaining workflow.

Here's what you might do. You might feed in that initial long

prompt that has all these constraints in it, and then just

accept that you are going to get back some initial article that doesn't

really fit the bill of what you're looking for. Claude might

inevitably decide to violate some of the different constraints you

laid out. To fix those issues, you could

then make a follow-up request back to Claude, providing

the article that Claude just wrote. And underneath

the article, you could ask Claude to rewrite the article in some

particular way. So you could say, find any location

where the author identifies as an AI and remove

that mention, find and remove all emojis, and

then write the text in a way that a professional technical

writer would do it. By using this chaining workflow and breaking

the task up into multiple steps, you allow Claude

to focus much more on each individual task

presented to it. So even though it might not really

satisfy all the requirements you put into the long prompt

originally, The follow-up prompt allows Claude to focus

on just the restrictions that you really care about, and

will hopefully rewrite the article in a style that you are

really looking for. So once again, even though prompt

chaining seems like something kind of obvious and simple, this

does end up being something that you're going to use rather often,

anytime that you have a task for Claude with many constraints,

and Claude doesn't seem to be always following those constraints as

much as you might expect.

---

#### Lesson 87: Routing workflows

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289242](https://anthropic.skilljar.com/claude-with-google-vertex/289242)

**Video:** 11 - 004 - Routing Workflows.mp4 | **Duration:** 3m 17s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Our next workflow is going to show us one way of improving this

social media marketing tool. So once again, we'll imagine

that a user is going to enter in a topic, we're then going

to produce some videos somehow, and post them to

a user's social media account. Now, there's

something I really want you to think about about the script generation

process. In other words, the actual tone and language

used in these different videos. Given two different

topics, such as programming on the left hand side, and

maybe surfing on the right hand side, we would really

expect to get video scripts that are very, very different

in nature. So on the left hand side with programming, we

would want to get a lot of information, carefully explain

definitions, and probably just overall a video

that is meant to be educational in nature. And if

user entered in surfing as a topic, we would probably

want to get back a very different video script. Probably something

that is much less educational in nature and doesn't

have a long definition on what surfing is or

anything like that. So let me show you a workflow that

we could use to make sure that a given topic will

result in a video script that fits the nature of that

topic really well. First, we would sit

down and think about all the different possible genres of

videos that users might ask us to create. So

we might decide that the topics that users are going

to give to us are going to fit into one of six different

genres. Entertainment, educational, comedy,

and so on. So in our example back over here, programming

might be educational and surfing might be entertainment.

Then for each of these different genres, we might write out a

script generation prompt. So if someone asks for

a topic that we categorize as being educational

in nature, we would ask Claude to write a script using

this prompt right here. And the prompt is asking Claude to make

a clear, engaging script that has some interesting

examples and interesting questions and so on. If the

user gives us a topic of surfing, we might categorize that

as being entertainment. So then we would take this prompt

right here, put in the topic as surfing and

feed the whole prompt into Claude and ask Claude to write

a script about surfing that maybe has some trendy

language and engaging hooks and so on. So let me show

you what this entire flow would look like in practice.

We would initially send a request off to Claude that contained

just the topic the user had entered, maybe something

like Python functions, and ask Claude to categorize

this topic into one of our different categories that we just

came up with. In this scenario, Python functions

might be most closely related to the category of educational.

So then we would take this response from Claude and then make a follow

up request asking Claude to write a

script that has some clear, engaging information

about Python functions that has thought provoking

examples. And then presumably we would get back some

script with those different qualities and a tone

appropriate for an educational video. This is

an example of a routing workflow. In

a routing workflow, we are going to take the user's original input

and feed it into a routing step. This routing

step will probably be a call to Claude itself, asking

Claude to categorize the user input or task in

some way. Then, depending upon Claude's answer,

we're going to forward the user's input onto some very

particular follow up processing pipeline. So maybe

this one right here, or this one right here, or this one right here, and so

on. But probably only one of these different three.

Each of these different routing options might have a different

workflow implemented inside of it or a customized prompt

or a customized set of tools that are specialized for

handling the exact task that the user is asking for.

---

#### Lesson 88: Agents and tools

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289243](https://anthropic.skilljar.com/claude-with-google-vertex/289243)

**Video:** 11 - 005 - Agents and Tools.mp4 | **Duration:** 5m 2s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that we have taken a look at several different workflows, we are going

to pivot and start to discuss agents. Understanding

agents is easiest if you think back to workflows, specifically

when we would actually use them. Workflows were most

effective when we knew the precise series of steps required

to complete a given task. Agents, on the other

hand, are more effective when we don't really know exactly

what steps are required. So in these scenarios,

we give Claude a task and a set of tools. And

then we rely upon Claude to create a plan to

complete the task using the given tools. This

flexibility around agents is what makes them really attractive

for building. The thought process is that you can make an agent, make

sure it works reasonably well, and then the agent can solve

a wide variety of different tasks. However, there

are some major drawbacks to this approach, which we will discuss

in a little bit. A key aspect of agents

is their ability to make use of tools in different combinations.

So to help you understand this, I want to think back to an earlier example

that we went through earlier on inside this course, where we put

together three different tools. We created tools like

Get Current Date Time, Add Duration to Date Time, and

Set Reminder. Each of these tools were rather simple

in nature, but Claude was able to combine them in different,

kind of surprising ways to achieve a wide variety of

different tasks that we might not really have planned out ahead

of time. Let me show you some examples.

So on the left hand side of this diagram, I've got some example

tasks that we could feed into Claude along with those three

different tools. And then on the right hand portion is

a series of different tool calls that Claude might make to

complete the given task. So for example, if we ask

Claude what's the given time, easy enough, Claude can

just call the Get Current Date Time tool by itself and

answer the question. If we ask Claude what day

of the week is in 11 days, it could first call Get

Current Date Time and then Add Duration to Date Time.

If we ask Claude to say, set a reminder to go

to the gym next Wednesday, Claude could first figure

out the current day of the week, add a duration onto it,

and then Set Reminder for that particular day. Finally,

Claude can also figure out when it needs some extra information in

order to successfully call a tool. So if a user

asks, when does my 90-day warranty expire? Well,

there's really no guarantee that the user got the warranty today.

So Claude might first ask the user for a bit of extra

information, particularly when they actually obtain the

warranty. Once the user gives them that information, then

Claude can call Add Duration to Date Time and figure out when

the warranty will expire. These are all examples

of ways in which Claude can take a set of tools and

combine them together in an interesting fashion in order to solve

a given task. And this is going to lead us into our first

big lesson or understanding around agents. And

that is that the set of tools we provide to an agent

need to be a reasonably abstract. And a great

example of this and to help you understand what I really mean hereby

abstract is to go back and look at Claude code and

specifically some of the tools that are provided to it.

Claude Code gets access to a very small set of

abstract tools. And when I say abstract, I

mean generic or general or kind of vague in

purpose. They are not hyper specialized in any

way. So Claude Code gets access to tools like

Bash in order to run commands, web fetch to

fetch URL, write to create a file, and so

on. And Claude Code can figure out how to modify

and add features to an existing codebase in

really amazing ways by combining together these different tools.

Claude Code does not have access to hyper-specialized

tools that just fulfill one very specific

task in one specific scenario. So for example,

on the right-hand side of this diagram, these are all tools that Claude

Code notably does not have. So there is no refactor

tool that will just magically refactor a file.

Instead, Claude Code should figure out how to make use of

the tools on the left-hand side in order to refactor something.

Likewise, there is no install dependencies tool. Instead,

Claude Code needs to read files to understand the project configuration

and then run the Bash tool to run the appropriate command to install

the dependencies. The lesson that we can take from this

is that whenever we create an agent, we want to make sure that

we provide reasonably abstract tools that

Claude can somehow figure out how to piece together in order

to achieve some goal. So for example,

if we go back to our example of building some kind of social media

video creation agent, we might provide

it for different tools. One might be Bash,

which would give it access to FFmpeg. That's

a commonly used CLI tool that you can use to generate videos,

given some input images or videos or text or

audio and so on. We might also give it a Generate

Image tool, a text to speech tool, just to augment

the video generation process, and then finally, a Post

Media tool so that it can take the generated

content, whatever it made, and post that content

to a social media account. Claude can use

that set of tools in rather unexpected ways. So

for example, it would enable a flow like what you see on the left-hand

side, where a user might chat with our agent and

ask it to create and post a video on Python programming.

But this set of tools might also allow for more dynamic

interactions with the user. For example, on the right-hand side,

a user might ask for a video, but first ask the agent

to generate a sample cover image to use in the

video. Then our agent could first generate an

image, show it to the user, get the user's approval, and

then go into the video generation process.

---

#### Lesson 89: Environment inspection

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289237](https://anthropic.skilljar.com/claude-with-google-vertex/289237)

**Video:** 11 - 006 - Environment Inspection.mp4 | **Duration:** 3m 5s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next idea around agents that we are going to discuss is

environment inspection. When we were taking a

look at computer use previously, you might recall something interesting.

After every single action that we saw logged out on the left

hand side, like typing or moving the mouse, we

always seem to see a screenshot immediately after, and

that's what I'm showing you in this diagram right here. Claude,

attempted to type out some text, and we see that logged in

the first panel up here, and then right after it, we saw a screenshot

appear immediately. I'd like you to look at

computer use from Claude's perspective. Claude

attempts to type or click somewhere and presumably

the page is going to change, but Claude doesn't really understand

how. Clicking on a button might navigate to a new

page or it might open up a menu. In order to understand

the result of any action it took, Claude needed

a screenshot to understand the new state or the

environment that it was in. This same

idea holds for any agent that we assemble. After

taking inaction, and sometimes before taking inaction,

Claude really needs a way of evaluating the result of the

action, often beyond whatever just a tool returns.

By helping Claude understand its environment, it can better

gauge its progress towards completing a task, and

also better deal with unexpected results or errors.

We can see a very similar idea when we make use of Claude

code. So in this screenshot, at the very top, I've

asked Claude to update the main.py file.

Now, the task I've given Claude here of adding in an

additional route is really simple. But before we

can ever modify that file in any way, this is going to

seem really obvious. Well, Claude needs to understand what

the current code is inside the file first. So

Claude needs some way of reading the contents of a file.

Now again, I know it seems really obvious, but I

would encourage you to think about this idea around reading

a file before writing to it anytime you're building an agent

of your own. This idea is even applicable to

our social media video agent. So whenever

we make a request off to Claude, we might give it a task like create

a video on Python and post it to my social media account, along

with our list of tools. Then we might provide some

special instructions inside of a system prompt, helping

Claude understand how can inspect its environment after

generating a video. Personally, if I

was relying upon Claude to use FFmpeg to

generate a video, I would kind of expect it to maybe

sometimes make mistakes around the placement of dialogue.

So specifically, when audio clips would play, that

it generated using some text-to-speech functionality. To

help Claude better understand its progress around completing

a task when making one of these videos, I might

give it some instructions to make use of the BASH tool

specifically to run a program called, specifically Whisper

CPP. This is a program we can use to generate caption

files automatically out of a video. And those caption

files have timestamps inside them, so Claude could

use this program to make sure the dialog was placed

correctly. We might also advise Claude to

use the bash tool to run ffimpeg, which has

the ability to extract screenshots out of a video.

We might tell Claude to extract a screenshot from every

second or every 10 seconds, and take a look at the

screenshots just to make sure that the video looks as

it kind of expects it to look. This allows Claude

to inspect the results of its actions, the actual

video I created, and make sure that it's completing the task

as it should.

---

#### Lesson 90: Workflows vs agents

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289245](https://anthropic.skilljar.com/claude-with-google-vertex/289245)

**Video:** 11 - 007 - Workflows vs Agents.mp4 | **Duration:** 2m 0s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's wrap up by comparing and contrasting some

different aspects of workflows and agents. First,

recall that workflows are a predefined series of calls

to Claude. We often use workflows when we have a good idea

of the exact series of steps that are needed to complete

a task. With agents, on the other hand, we

don't know exactly what task will be provided, so

we instead provide a solid set of basic tools

and expect Claude to combine these tools together to complete

a given task. You might have noticed that a common

theme around workflows is that we take a big task

and we divide it up into much smaller tasks. Each

of these smaller tasks are much more specific in nature, allowing

Claude to focus on a single area at a time. This

increased focus generally leads to higher accuracy

for completing a task compared to agents.

Because we know the exact series of steps that a workflow executes,

they're also far easier to test and evaluate.

With Agents, we aren't constrained to a series of

steps etched in stone. Instead, Claude

can creatively figure out how to handle a wide variety

of challenges. Along with this flexibility, we

also get flexibility in the user experience. While

workflows expect to receive a very particular set of inputs,

Agents can create their own inputs based on queries

received from the user, and Agents can also ask user

for more input when it's needed. The downside

to agents is that they generally have a lower successful

task completion rate compared to workflows because

we are delegating so much work to Claude. In

addition, they're also harder to test and evaluate,

since we often don't have a good idea of what series of steps

an agent will execute to complete a given task.

At the end of the day, agents are really interesting,

but remember, your primary goal as an engineer is

to solve problems reliably. Users

probably don't care that you've made a fancy agent. They

really just want a product that's built to work 100% of

the time. So with this in mind, the general

recommendation is to always focus on implementing workflows

where possible and only resort to agents when

they are truly required.

---

#### Lesson 91: Quiz on agents and workflows

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289274](https://anthropic.skilljar.com/claude-with-google-vertex/289274)

---

### Final assessment

#### Lesson 92: Final assessment quiz

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/290880](https://anthropic.skilljar.com/claude-with-google-vertex/290880)

---

### Wrapping up!

#### Lesson 93: Course Wrap Up

*Source:* [https://anthropic.skilljar.com/claude-with-google-vertex/289240](https://anthropic.skilljar.com/claude-with-google-vertex/289240)

**Video:** 12 - 001 - Course Wrap Up.mp4 | **Duration:** 3m 12s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

If you have made it through this course, you have put in a tremendous

amount of effort, and I congratulate you. Before

we close things out, I want to very quickly recap some of the major

topics we discussed and give you some recommended follow-up

topics to research in the future. First, a

quick recap of what we have covered. We began this course

by discussing some of the different models offered by Anthropic.

Remember, we have access to Haiku for fast, smaller requests,

and Sonnet for greater intelligence. We then spend

a lot of time discussing how to access Claude via the API

and different parameters we could feed into Claude in order

to adjust its response. For example, we discussed

temperature and stop sequences, message prefilling.

All these are parameters we can use to direct Claude in

certain directions, control its creativity, and ensure

that we get the correct format of data or output that we expect.

We then spend a good amount of time talking about prompt evaluations.

I cannot stress it enough. Prompt evaluations is,

by far, the most important practice for you to implement on

your own projects. You might sit down and run

a prompt 10 times on your own and think everything is okay,

but as soon as you deploy it in production, your users might

not get the results that you want them to get. The only

way to make sure that you are writing effective prompts is

by evaluating them. And remember, prompt devals, they

don't have to be hard. You do not have to make use

of a fancy framework or do any kind of a big complicated

setup. You can use Claude to generate

a prompt evaluation framework on your own. And that's

kind of what you saw inside this course. The prompt deval framework

that we made use of, a lot of that code was written directly by

Claude. We then spent some time discussing prompt

engineering. Remember, there's a handful of techniques for

you to keep in mind. Chief among them is just simply being

clear and directly telling Claude what you expect

of it. After that, we spent a lot of effort on

tool use, and that was probably one of the more complicated sections

inside the course. Tool use is extremely important

because it dramatically expands the capabilities of Claude.

We then spent some time with two important applications

that then released by Anthropic Directly, Claude code

and computer use. I hope you enjoyed getting

some hands-on experience with Claude Code. Personally, it is

what I use to help me author code and projects.

I don't actually use a fancy in-editor assistant

that much. I really just run Claude Code at the terminal

in the exact same style that you saw in those videos.

And then finally, we spent a decent amount of time discussing workflows

and agents. Now, remember, agents are

definitely interesting. It's a very exciting topic, but

you very often are going to get better results and higher

accuracy by the use of workflows.

For a lack of time, we were not able to cover every topic

inside of this course. There are some big ticket

items that I recommend you follow up and do some research on your

own. Chief among them is a lot of topics around

agents. Understanding how to get agents to work

together with agent orchestration, understanding

how to evaluate an agent's performance and monitor

it, and a variation on RAG, known as

agentic RAG, are all topics that I recommend you

spend some time to research on your own. I

also recommend you take a look at some different techniques for RAG

evaluation and tool evaluation. Tool

evaluation is similar to prompt eVals. We want to make

sure that our tool descriptions are helping Claude in the

way we really expect. Well, that's it for now. Like

I said, I hope you enjoyed this course and I appreciate your time

in working through this content.

---

*Extracted from Anthropic Academy via authenticated session | Deep Extraction v3 | 2026-04-12*
