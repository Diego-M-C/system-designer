# Claude with Amazon Bedrock

> **Source:** [https://anthropic.skilljar.com/claude-in-amazon-bedrock](https://anthropic.skilljar.com/claude-in-amazon-bedrock)
> **Category:** cloud-integration | **Difficulty:** intermediate-advanced | **Domain:** Cloud Integration
> **Tags:** aws, bedrock, api, rag, tool-use, agents, mcp
> **Extracted:** 2026-04-11 | **Version:** v3 (with YouTube transcripts + quiz content)

---

## Extraction Statistics

| Metric | Value |
|--------|------:|
| Total Lessons | 83 |
| Sections | 11 |
| JW Player Transcripts | 73 |
| YouTube Transcripts | 0 |
| Modular Text Lessons | 0 |
| Quiz Assessments | 0 |
| JW Transcript Chars | 444,608 |
| YouTube Transcript Chars | 0 |
| Modular Text Chars | 0 |
| **Total Content** | **444,608** |

## Curriculum Structure

- **Course introduction** (2 lessons)
- **Working with the API** (12 lessons)
- **Prompt evaluations** (8 lessons)
- **Prompt engineering** (7 lessons)
- **Tool use** (13 lessons)
- **Retrieval Augmented Generation** (10 lessons)
- **Features of Claude** (8 lessons)
- **Model Context Protocol** (12 lessons)
- **Agents** (9 lessons)
- **Final assessment** (1 lessons)
- **Wrap up** (1 lessons)

---

## Complete Lesson Content

### Course introduction

#### Lesson 1: Introduction to the course

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/241929](https://anthropic.skilljar.com/claude-in-amazon-bedrock/241929)

**Video:** 001 - Welcome to the course.mp4 | **Duration:** 1m 4s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Welcome to this course focused on getting started with Claude

on Amazon Bedrock. My name is Stephen Grider and

I'll be guiding you throughout this course. Let's first

begin by understanding exactly what we're going to cover

in the coming videos. We will first take a look

at some of the different models authored by Anthropic and

then quickly learn how to access those models through Amazon

Bedrock. We will then spend some time learning

how to write and evaluate prompts followed

by an in-depth look into tool use.

then it is on to retrieval augmented generation,

which we'll use to provide Claude with knowledge relevant

to the tasks that we give it. We will then

take a look at model context protocol by working on a small

app, and then wrap things up with a look at two

agentic apps authored by Anthropic called

Claude code and computer. There's

a lot of content for us to get through, so there are a couple

of requirements on your side. First, you need to

have some basic Python knowledge. Second, you

will, of course, need to have access to Amazon Bedrock.

So with all this out of the way, let's dive into our first

technical topic in the next video.

---

#### Lesson 2: Overview of Claude Models

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/303332](https://anthropic.skilljar.com/claude-in-amazon-bedrock/303332)

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

### Working with the API

#### Lesson 3: Accessing the API

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276716](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276716)

**Video:** 001 - Accessing the API.mp4 | **Duration:** 2m 31s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this module, we're going to understand how to access

Claude models through AWS Bedrock and use

them to generate some amount of text. To get started,

I want to walk you through a small example app, a

straightforward, standard chatbot application. So

let's imagine that you are making a web app and you want to show

a chat interface to a user, where a user can enter in

some message and then click on send. Whenever they do

so, their expectation is that some response

is going to just magically appear. But let's

examine what's going on behind the scenes to actually make this happen.

Whenever user submits some text, a request containing

that text is going to be made to your server. Your

server is then going to use the Bedrock client to make a request

to the AWS Bedrock service, where the Anthropic

models are actually hosted. In this request

made to the Bedrock service, we'll include something called a

user message, which contains the text the user submitted,

and a model ID, which specifies which model

we want to run. The chosen model

is going to run, it's going to generate some text, and it's going

to be sent back to your server inside of something

called an assistant message. Your

server can then take that generated text and send

it back down to the browser where it can be rendered on the screen

for the user to view. Now, in this section

of the course, we're going to be entirely focused on this communication

layer between this bedrock client and

the bedrock service. We're going to investigate how

to make API requests, how to access generated text,

and discover some common design patterns along

the way. Before we move on, I want

to clarify a common point of confusion, specifically

the difference between the bedrock API

and the Anthropic API. First,

a very quick review. Earlier on inside this course,

we discussed the Claude Sonnet and the Claude High-Q

models. These models are responsible for the actual

computational work that is done to generate some amount

of text. The Claude family of models

are currently hosted through two different services, AWS

Bedrock and the official Anthropic API.

If you're inside this course, you're going to be using the Claude

family models for the AWS Bedrock service.

Now here's the point you really need to be aware of. These

truly are different services. They're accessed

through different SDKs. They have different sources

of documentation. So whenever you are looking up documentation

or trying to understand how to use a model, just be

sure that you're looking at resources specifically for

AWS Bedrock. So now that we've cleared

up that point of confusion, let's move on to making our first

request to Bedrock in the next video.

---

#### Lesson 4: Making a request

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276719](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276719)

**Video:** 05 - 002 - Making a Request.mp4 | **Duration:** 7m 34s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's get our hands dirty and write out a little bit

of code. In this video we're going to focus on making our first

API request off to AWS Bedrock.

We are going to run a model and just generate a very small amount

of text. Now you'll notice that I've already created a Python

notebook. I would encourage you to pause the video right here and

create a notebook of your own so you can code along with

me just to get some experience in making these API requests.

In order to make our first request, we are going to need three

different things. First, we need a client to

actually access Bedrock. We're going to make this client

using the Bodo3 Python module. Second,

we need a model ID. This is going to be the ID

of the exact model that is hosted inside of Bedrock that

we actually want to run. And then finally, we also

need something called a user message. This

is going to be a very specially formatted object that

contains some amount of text that we want to feed into

the model. So back inside of my notebook, let me

show you how we're going to create that client, get the model ID, and

create a user message. First, I'm going to make a client

using the Bodo3 module. I'm going to specifically

connect to the Bedrock runtime and specify a

region name. In my case, I'm going to use US West

2. Next up, we need to designate our model

ID, which is going to be a string. Now, unfortunately,

the model ID is actually going to end up being a little bit

more complex than it might seem at first glance.

So let me show you a couple of diagrams, help you understand what's

going on. Now, as a reminder, whenever we

make a request off to Bedrock, we need to include the ID

of the actual model that we want to run. And we're going to send

that request off to a very specific region. In my case,

I put in US-S2. But there is a really

big gotcha here, something that's not super clearly

outlined in the documentation, but something that you very much

need to be aware of. It turns out that not every

single model is hosted in every region.

So for example, US East 1 is

another region in AWS. And US East 1

might not be actually running the exact model that I want

to execute. So if I were to send this request

into US East 1, I would probably end up getting an air message,

saying something about this model just plain not being available.

To fix that error, I could try to figure out which region actually

is hosting the model that I'm looking for. Or,

alternatively, I could try to keep track of what model

is hosted in which region. But there's an easier

way to solve this problem using something called an inference

profile. Inference profiles are used to route

requests to a different region where your chosen model

is actually hosted. So as an example, we might

have an inference profile that says that this particular

model is guaranteed to be hosted in U.S. West

2 and U.S. East 2. Here's what the inference

profile does behind the scenes. We are still going to make a request

off to some particular region hosted in AWS.

But rather than specifying a specific model ID,

we're going to instead specify the ID of an inference

profile. When we then send that request in, AWS

is going to automatically reroute our request to another

region where the model that we are looking for actually is hosted.

So the reason that I mentioned that this model ID

right here is a little bit tricky to understand is that it is referred

to as a model ID all over the place. But

in reality, we usually don't actually put in a model

ID. Instead, we provide the ID of an inference

profile so that we get that automatic request routing.

Let me very quickly show you an example of this inside of the

bedrock dashboard, just so this idea of an inference profile

is super clear. So inside of my bedrock dashboard,

I've gone to the model catalog on the left-hand side.

I'm then going to take a look at one of the Claude series of models.

Then on this page, if I scroll down a little bit, I

will see right here, yes, I have a model ID.

But again, this model ID is probably not what we actually

want to add into our request. Instead, what we're

probably going to want to use over here on the left hand side, I'll

find cross region inference. And if I click on

that, I'll then find the model that I'm looking for.

Here we go. And then on this page, I'll find

my inference profile ID. And that inference profile

ID is what we want, because that's what's going to automatically

route our request off to some region where our model

is guaranteed to be hosted. So I'm going to take that

inference profile ID, I'm going to copy it, and then

put it back over here inside of my notebook and assign it to

model ID. The last thing that we need to create before

we make a request is our user message. Remember

that this is a very specially formatted object that contains

the text that we want to feed into the model. I'm going

to make a variable down here called user message. It's

going to be a Python dictionary with a role of user

and a content that's going to be a list with another

nested dictionary inside of it with some text. The

text value is going to be whatever I want to feed into my model.

So in my case, I'm going to ask the model, what's

one plus one? Now, I'm going to tell you more about

the structure of the user message in just a moment. But

for right now, let's just focus on making a request to make sure

that we can actually generate some text. To make our actual

request, I'm going to go down a little bit and add in a call

to client.converse. We're going to

feed in our model ID and notice that the keyword argument here

is model ID with a capital I. I'm

also going to add in messages. That's going to be our list of messages.

In this case, we only have one. It's going to be the user message that we just

created. Then I'm going to make sure that I run both

cells. Then I'm going to add in a new cell

underneath this one and print out

response. There's a lot of information

inside this response, but if we look very closely, we can see that

we actually do get a answer to the question that I put in,

which was what is 1 plus 1? So I got an output

of 1 plus 1 equals 2. So if we wanted

to get just the generated text by itself, we would have to

write out something like response and then look up output

message. Content, zero,

text. So that's going to look at the output property,

look at message inside there, look at the content inside

there, look at the first element inside this list, and then get

our text, and that's where our generated text actually

sits. So if I now run this cell again, I'll see just

the generated text of 1 plus 1 equals 2.

Now very quickly, I'm going to make a change to this line. I'm

going to remove the content, the zero in text lookups,

and then run that cell again. Now I'm going to get a dictionary

that has a role of assistant and some content assigned to it.

And if you look at this dictionary, it might actually look a little

bit familiar. It looks rather similar to a structure we

created just a moment ago, specifically the user

message right here. So let me help you understand

what these message things are all about and what they do

for us. Messages contain the text

that we want to feed into our model, and they also contain the

text that eventually gets generated by the model as well. There

are two different types of messages, user messages and assistant

messages. So a user message is always going to

contain the text that we want to feed into the model. And

assistant messages are going to contain the text that was generated

by the model itself. The structure of these two different

message types are always going to be a very similar nature. The

only big difference between them is that a user message will always

have a role of user, and an assistant will always

have a role of assistant. Both message types

will always have a content property that we refer to a list.

And you might be a little bit curious why there's a list there at

all, why isn't it just some simple text property that tells

us whatever we fed into the model or what we got out.

The content property is a list because eventually

we're going to see that a single message can have many different parts

tied to it. For example, we might to send

a message into our model that contains both an image

and some amount of text as well. We would encode

the image and the text as separate parts inside

of this list of content items. We are not going

to worry about messages with multiple content parts inside

them just yet. I only mentioned it to help you understand why

there's that extra little bit of syntax. Okay,

so now we've made our first request successfully. Let's come back

in just a moment and go into a little bit more detail.

---

#### Lesson 5: Multi-Turn conversations

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276722](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276722)

**Video:** 05 - 003 - Multi-Turn Conversations.mp4 | **Duration:** 9m 5s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The code that we've written out so far simulates a very simple exchange

with our model. And we can kind of visualize this conversation

inside of a chat box like this. So we sent

in a request asking in something like, what's 1 plus

1? We got a very simple response back. Something like

the answer is 2. Naturally, we might

want to continue this conversation at some point in time.

So we might want to send in a follow-up asking something

like, and three more. And then we would expect

to get back a response, saying something like adding three to two

would result in five. To have a multi-message

conversation like this, there's something really critical you need

to understand around the Bedrock API and Claude

itself. And that is that Betterock and Claude do

not store any messages. None of the messages

you send to it get stored in any way, and none of the

responses you get back are stored in any way.

So if you ever want to have some kind of conversation going

on, where you have multiple messages that kind of maintain a

context or a flow, then there are two things you

need to do. You need to manually, inside of

your code, maintain a list of all the messages that

you are exchanging. And second, you need to make

sure that you provide that entire list of messages with

every follow-up request that you make. So let's

go into some detail on this entire idea just so it's really

clear that you understand what's going on here. The first

thing I want to do is run just a little bit of sample code. So

I've still got the code we wrote in the last video up here where we asked what's

1 plus 1, and we got back the 1 plus

1 is 2. Now I'm going to paste in Some

additional code snippet here that I wrote ahead of time. So

in this additional code snippet that I just pasted in, I'm making another

call to Bedrock, and this time I'm providing

a message of just and three more. So this kind of simulates

that screenshot I showed you a moment ago. And now if

I run this cell, I will eventually get back

a response that doesn't make any sense whatsoever.

So let me show you a diagram to make sure it's clear why we got

this very strange text. OK. So

on the left hand side, I've got the messages that I'm including in

my request off to Bedrock. I start off with just

a message of what's 1 plus 1. We send that in and we

get back an assistant message of 1 plus 1 is 2,

exactly what we expect. When I then execute

the code that you saw just a moment ago, that extra little code snippet, I

sent in a request that contained just one single message

that said, and three more. Now, when

we send this and three more in, Claude is going

to do its best to give you a response. In our

case, the response we actually got back didn't make a lot of sense, but it's

doing the best job it possibly can, because all

it knows is the fact that we said, and three more.

So to solve this problem, here's what we're going to do. As

I mentioned just a moment ago, we're going to manually maintain a list

of these messages and make sure we provide that list

with every single follow-up request. So

as demonstration of what we're going to do going forward, whenever we want to

have a multi-turn conversation, we're

still going to send in this original user message.

We're going to get back the assistant response, and then we're

going to include that assistant message in

our list of messages. So we're going to kind of move it on over there

to the left-hand side. Then whenever we want to continue

this conversation, we're going to append onto the end

of the list another user message, where we ask,

and three more. And now when we take this full

list of messages and make our request, Claude will have the

full context of the conversation. It will see all

three messages, and we'll know exactly what we are talking about

when we say, and three more. So we'll

get back, hopefully, response is something like 3 plus 2

is 5. Let's go back over to our notebook

and try to simulate a multi-turn conversation

like this. Okay, so back

over here, I'm gonna delete that little code snippet I paste

in very quickly. Then inside this earlier

code cell, I'm gonna write out three helper functions.

These helper functions are just gonna make it a little bit easier for us to maintain

the entire context of this conversation and maintain

that list of messages. So right above user

message, I'm going to put in a function definition of add

user message. I'm going to assume that I'm going

to call this function with a list of messages and

some text. I'm going to indent user

message like so. I'm going to replace

what's one plus one right here with the text

argument that we're going to pass in. And

then right after we define user message, I'm going to add

that into the list of messages. Next

up, I'm going to copy this function entirely. I'm

going to paste it right down here. I

will rename it to add assistant

message. I will change the

name of this variable to be assistant message, change

the role to be assistant,

and then finally update messages dot append right here to be

assistant message instead. So

now we have two helper functions that can very easily make

a message type for us, either a user or an assistant message

and append it into an existing list of messages.

Then one more helper function. Down here,

I'm going to make it just a little bit easier for us to call

our model, get a response, and then get the actual text we

care about out of it. So I'm going to also

define a function right here called

chat. It will take in a list of messages.

I'm going to indent response. I'm

going to pass in the list messages like so.

And I'm going to return from this function, response,

output, message. And

do you remember everything you have to put in there? It's then content.

That's right. We then get a zero and text

like so. So now with these three

functions, we can very easily simulate a full conversation.

Let me show you how we would do it. Down here in this cell, I'm

going to paste in a couple of comments that I wrote ahead of time

just to guide myself and make sure I'm doing this entire conversation

correctly. So here's my list of comments. We're going to put

in one line of code for each comment that I've added in. But

don't worry, each line of code is me very short and simple.

First, I'm going to make a starting list of messages. So initially,

I start off with no communication whatsoever. I'm

then going to add in the initial user question, so that

initial user message of what's one plus one.

To do so, I'll call add user message, pass

the list of messages, and then the second argument is going to

be the actual text I want inside this message. So

in this case, it'll be what's one plus one.

And then immediately after that, I'm just going to print out messages really quickly

to make sure that we are on track. So I'm going to run this.

And it looks like, yep, we added in our user message

correctly. So I've got the role of user, content

as a list, and a Python dictionary inside there. So

I'm going to continue on to the next step. I'm

going to pass the list of messages into that chat function

we made to get back an answer. So when we call

that chat function, it's going to reach out to Bedrock and call our

API. So we'll say answer is

chat and pass on the list of messages. And

once again, just to make sure I'm on track, I'll print out answer.

I'm gonna run that. And after our short pause, I see, yep,

we got it correctly. We got our answer of one plus one equals

two. So now we have this answer back as

a plain string. We need to take that and

add it as an assistant message into our

list. And again, we're gonna do so by using that helper

function we just made. So we'll say add assistant

message pass in our list with

the answer we just got back. And once again, printout

messages just make sure we're doing this correctly. So

now we will see, yes, we are in fact building up our

conversation. We're building up our list of messages. We've

got first user and then assistant. We got what's one

plus one and then the answer we got back. So

now we can follow up with

the user's additional question, which was add

user message. and we'll

say, and three more added

to that. And

we'll skip checking messages again. Let's go ahead and get our follow-up

answer by

calling our API again with a full list of messages.

I'll print out the final answer and let's see what we end up with.

And so sure enough, starting with the result of that, and

we add three more, we end up getting five. So

now it's very clear that we are maintaining the context of

this conversation by including all the previous

messages inside of our follow up request. Now,

this might initially seem a little bit tedious, and

even this code right here might seem a little bit confusing. I

don't blame you if it is confusing. Don't worry, this is the

kind of thing that you're going to get really used to very

quickly. And there's just one last thing I

want to mention around lists of messages, like

the one we have assembled right here. And that is, whenever

we send in a list of messages to the API, we

always need to make sure that we are alternating roles

between each message. So in other words, we should always

have a user and then an assistant, and

then a user, and then an assistant. We should never

have two user messages in a row, and we should also never

have two assistant messages in a row, or any

variation thereof. So we always want to make sure that we are varying

or alternating those roles.

---

#### Lesson 6: Chat bot exercise

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276725](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276725)

**Video:** 05 - 004 - Chat Bot Exercise.mp4 | **Duration:** 5m 13s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's go through a very quick exercise just to make sure everything

 is making sense so

 far.

 Our goal inside this exercise is to make a very simple chatbot using

 those three helper

 functions that we just put together a moment to go.

 Now you can read through the different steps that I think you're

 probably going to have

 to implement right here, but to understand the exercise, it might be

 easiest if I just

 give you a quick demonstration of what I would like you to try to

 build.

 So here's what we're going for.

 Inside of a Jupiter notebook, we're going to make a single cell like

 the one I've got

 right here.

 I've got my solution side of here, but I've collapsed it just so you

 can't see it.

 And now if I run the cell, I want to prompt my user to enter in some

 input.

 So for me, that's appearing up here at the top.

 Then I'm going to enter in some string that I want to send off to my

 model.

 In my case, I'm going to enter in write a one sentence product

 description.

 Now, if I hit enter, I'm going to wait just a second, and I should

 then see a response

 right back here.

 And now I should see my input up here once again, and I should be

 able to enter in a follow

 up message, that's going to still contain these previous messages as

 context.

 So I should be able to say something like make it shorter and see a

 response that's going

 to make it clear that we're still talking about a product description

 because we included

 those previous messages, and I definitely do.

 And then I should be able to repeat this as long as I want.

 So maybe I could say something like make it mention a color and I

 could just keep on

 going and going and going.

 Now you should still be able to complete this exercise, even if you

 are running a Jupiter

 notebook outside of VS code.

 So just as a quick demo, if I flip over, I've got this running inside

 of a browser notebook

 as well.

 And so if I run that cell, I can type in my prompt right here.

 So one sentence product description, and I should still see an output

 in the exact

 same way.

 Now this exercise is just a little bit tricky because it is going to

 require a little bit

 of basic knowledge around Python.

 And if you're not super familiar with Python, that's totally fine.

 I'm going to give you a quick hint right here on the general

 structure of the code you're

 going to write to make this work.

 So as a hint, I'm going to put in a little couple of comments right

 here in just a snippet

 or two of code.

 Here we go.

 This is kind of our starting point.

 So just in case you need a little bit of help in first make that

 initial list messages,

 we can then run our chat bot forever by putting in a while true.

 And then to get our user input, we can call the built in input

 function.

 And then I put in some comments for the other steps you'll have to go

 through, and I bet

 you could figure these out based upon the code that we went over in

 the last video around

 adding user messages, calling chat, and then depending on an

 assistant message.

 So I'd encourage you to give this exercise a shot.

 So pause the video right now and go ahead and give it a chance.

 All right, you've unpause, we'll go our solution right away.

 So I'm going to start from the snippet that I gave you just a moment

 to go.

 All we have to do is fill in a couple of lines of code.

 We've already got our initial list of messages.

 We've got a wild true right here to run this thing forever.

 We've collected some user input as text.

 Now all we have to do is fill in some different tasks right here for

 each of these different

 comments.

 For the first one, we're going to take whatever text a user just

 typed in, and we're going

 to add it into our list of messages.

 And for that, we can use the function we put together a moment ago,

 that add user message

 function.

 So I'll call add user message.

 I'll put in the list of messages I want to add to, and then whatever

 the user just typed

 in.

 Then we're going to take that list of messages and send it off to our

 API and save whatever

 text we got back.

 So I'll say our text that we're generating is going to be chat with

 messages.

 So text right here, that is the response we got back.

 That's the generated text.

 So we'll now add that generated text to our list of messages with a

 add assistant message.

 And we should probably also print that up as well.

 Okay, now depending upon whether you are running your notebook in VS

 code or not, there's one

 other thing you might need to do here.

 If you're running in VS code, you are going to want to print out the

 user input.

 So I'm going to print user input right here.

 I'm going to put a little carrot in the space before it just make it

 look like a nice little

 prompt.

 You only have to do this if you are in VS code.

 If you're not in VS code, if you're running your Jupyter notebook

 inside of a browser,

 you're going to automatically see the user input printed out for you.

 So again, only necessary if you're in VS code.

 I also might want to put in some nice formatting around the text

 right here when I print it

 out.

 But that's totally optional.

 Let's just run this to make sure it actually works.

 So I'll run it and then just as we saw previously, I get this nice

 little prompt up here and

 I'll ask for a one sentence product description.

 And I should see my, yep, there we go.

 Very good.

 That's my response.

 On this conversation, add in additional messages over time.

 So I could say shorten it, add a color, and so on.

 Very good.

 Now, if you had any trouble with this exercise at all, don't sweat it.

 .

 This is our first practice with AI, first time kind of taking a look

 at this stuff.

 So we get a lot more practice throughout this course, a lot more

 opportunities to make

 sure that you're super confident on what's going on.

---

#### Lesson 7: System prompts

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276726](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276726)

**Video:** 05 - 005 - System Prompts.mp4 | **Duration:** 7m 20s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Earlier on inside this module, we discussed making a web-based chat

 interface.

 Now, I want to revisit that example with a little twist.

 I want to imagine how we could take that example and turn it into a

 kind of AWS support specialist chatbot.

 So maybe a user would ask a question like, "How do I host a Postgres

 database?"

 Then our answer that we get back should probably satisfy some

 requirements.

 So for example, our response we get back and show to the user should

 probably directly answer the user's question

 and list out some different ways of hosting Postgres on AWS.

 It might even want to guide the user through some of those different

 initial steps.

 And then finally, it might also want to mention some related AWS

 services that the user might be interested in.

 Now, just as much as we want our response to include some content,

 there's also some kinds of content that our response definitely

 should not include.

 So for example, we would not want to see any kind of answer that

 mentions how to host Postgres with a competitor solution.

 We would also not really want to see any kind of answers related to

 questions

 that are not about cloud services in some way.

 So if a user asks, "How do I fix my car?"

 We would probably want our chatbot to very politely refuse to answer

 that question.

 Now, we're going to take a look at two different possible ways of

 implementing a chatbot like this.

 So a user can ask a question and then get back some answers that

 follow some specific requirements.

 Option number one, which is maybe not the best option, but we'll take

 a look at it anyways,

 we could write out a user message that lists all these different

 requirements.

 So inside of a user message, we could say,

 "Make sure that you mention how to host things on AWS."

 And we could also say, "Do not mention how to host services outside

 of AWS."

 And also don't answer questions that are not related to AWS in any

 way.

 Now, using option number one would just be really tedious,

 because we would have to think up of a very comprehensive list of do's

 and don'ts

 that would address every possible different question a user might

 ever ask us.

 So maybe this isn't the best solution here.

 Maybe there's a better way we could handle this.

 With that in mind, let me show you option number two,

 which is going to be a better way of solving this problem.

 In option number two, we're going to provide a system prompt to that

 converse function call.

 A system prompt is going to provide Claude some guidance on exactly how

 to respond.

 And it does so by assigning a role to Claude.

 By role, I mean to say that we're going to essentially tell Claude to

 pretend

 as though it has an actual real life job.

 So in this case, our system prompt might say,

 "You are an AWS cloud support specialist."

 This is going to force Claude to pretend as though it is a real life

 cloud support specialist.

 And it's going to attempt to respond in the same way that a real life

 support specialist would respond.

 So presumably, a real life specialist would never try to answer with

 competitor solutions

 and would probably refuse very politely to answer questions that are

 not related to cloud services.

 By just assigning this system prompt, Claude is going to try to do the

 same thing.

 It's going to try to respond in the same way that a real life support

 specialist would respond.

 Now, the best way to get a hold of system prompts is to write out

 some code.

 So let's go back over to our Jupiter notebooks and get a little bit

 of experience with system prompts.

 So back over here, I have made a new notebook, but it has pretty much

 the same code we had previously.

 So I'm still making a client, a model ID, and then defining those

 three helper functions.

 I've also put together another cell here where I'm just asking a very

 simple question,

 how do I host a Postgres database?

 Now, at this point in time, I do not have any system message hooked

 up whatsoever.

 So if I run this, I'll expect to see a response come back that's kind

 of like a general purpose Claude answer.

 It's going to respond as Claude normally would by giving a really well

 rounded answer.

 And it's not going to fulfill some of our big requirements for our

 chatbot.

 Namely, if I take a look at the response here, it's probably going to

 end up mentioning some competitors,

 which is not really what we want.

 So one way that we could fix this up is by adding in that system

 message.

 For right now, I'm just going to hard code a system message in.

 And I'll show you how to make this chat function a little bit more

 reusable after that.

 So first, inside the chat function, I'm going to add a system prompt

 right here.

 And I'm going to copy, paste, and a system prompt just to save a

 little bit of time.

 It's just the same thing you saw on that diagram a moment ago.

 So it just says you are a cloud support specialist, and you just have

 to answer questions related to cloud hosting.

 Then to pass this into the converse call, we're going to add in a

 system keyword right here.

 It's going to be a list with a dictionary that has text of that

 system prompt, like so.

 So now I'm going to rerun that cell to redefine the chat function.

 And then I'll try to rerun my conversation right here and we'll see

 how the response gets updated.

 Hopefully, it's going to respond with some AWS particular Postgres

 solutions and not mention any competitors.

 And so that ends up being exactly what we see here.

 We're going to see the different managed solutions, some self-managed

 options, and then some initial setup.

 And then, notably, it's not going to mention anything about any

 competitors or anything like that.

 Likewise, we can also try updating our query to something that is not

 at all about cloud hosting.

 Now, this doesn't always work, but it usually does.

 So I'm going to try to ask something like give me a bread recipe.

 And we'll see what kind of response we get now.

 So naturally, without the system prompt, we'd expect to get back an

 actual recipe.

 But with a system prompt, we get that very polite refusal.

 Says, OK, I understand what you're going for, but I'm really all

 about AWS cloud support.

 So if you have any questions about that, I can help.

 But otherwise, maybe I can't really answer your question about bread.

 Let's go back up to that chat function.

 As I mentioned, I would like to refactor this thing and make it a

 little bit easier to pass in the system prompt

 rather than always having it be hard coded as it currently is.

 Just so you know, if we pass in this system keyword right here, we

 are required to put in a system prompt

 that has at least one character inside of it.

 So if we try to put in an empty string, like so, and then I run this

 cell and the next one down,

 I'll end up getting a big error message.

 It's going to tell me that I provided a system prompt of length zero

 and must have at least one character inside of it.

 So to refactor this thing and just make it a little bit easier for us

 to specify that system prompt,

 I'm going to copy paste a little bit of code in here just to save us

 some time.

 I'm going to replace the chat function like so.

 So now I'm going to expect to receive a system prompt by default.

 It will be none.

 I then make my params object ahead of time.

 And then if a system prompt is passed in, I'm going to add that in to

 the system keyword,

 and I'll pass all those params into the converse function.

 So now as a quick demonstration of how we can use this updated chat

 function,

 I'm going to rerun that cell.

 I'm going to go down here.

 And now when I called chat, I can pass in a system of you are a AWS

 support specialist.

 And of course, we could really flesh that out.

 But for right now, let's try it with that and make sure we still get

 some appropriate output here.

 Namely, should not really give any good output for still the give me

 a bread recipe.

 And it looks like, yep, we definitely get back some good output.

---

#### Lesson 8: System prompt exercise

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276717](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276717)

**Video:** 05 - 006 - System Prompt Exercise.mp4 | **Duration:** 2m 47s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's try going through an exercise around system prompts very

quickly.

So in this exercise, I'd like you to write out some code like what

you see right here.

I've created a list of messages and I added in a user message of

right a function

that checks a string for duplicate characters.

I then get some text out of that and then print the text out.

Now, with this starting prompt, I end up getting a lot of output back.

.

So here's the result that I personally got.

You can see that there is a little bit of preamble up here.

I kind of explained the solution and there's a ton of comments inside

the code.

And then finally, some closing statements around the code that was

written.

Now, this is a lot of response here for a rather simple function.

So I want to somehow get a much more concise answer.

One way that we can get a more concise answer will be to adjust the

user

message and add in a ton of different requirements.

So for example, in the user message, we could say, do not add in any

comments or

anything like that, respond just with some code, et cetera.

Or alternatively, a better way we could get a more concise answer

would be to add

in a very short system prompt that assigns a role to Claude.

So in this exercise, I would like you to take the code you see right

here and then

just add in a system prompt to the chat function and see if you can

get a result

back that has none of the header text or the footer, no comments or

anything like

that, besides maybe a general function comment, like the one right

here, that's

totally fine. But other than that, I want really just the code and

nothing else.

So I would encourage you to pause this video right now and go ahead

and give

this exercise a shot.

Otherwise, if you want to stick around, I'm going to go through a

solution right

away. So here's how you would solve this problem.

Now I'm going to add in a system prompt to our chat function call.

And in this case, I'm going to put in a system prompt, something

really simple,

a role that kind of implies to Claude that it should write some very

concise code.

So I'm going to put in a system prompt of you are a Python engineer

who writes

very concise code.

And that's probably going to be enough to get all those extra

comments removed.

So I'm going to go ahead and run this and we'll see what we get here.

And yeah, I'd say that's probably very much what we're going for here.

.

So it's going to check and see if we have any duplicate characters

inside the string.

That nice function comment right there.

But besides that, we don't get any preamble header or footer

explaining what's

going on and no additional comments.

So I would say that adding in the system prompt was a lot easier than

trying to

adjust our prompt a ton or specifically the user message and add in a

ton of all

those additional requirements.

So let's say this is a pretty good solution.

Now, once again, if you had any trouble with this exercise, do not

sweat it.

We're going to continue to have a lot of exercises throughout this

course.

---

#### Lesson 9: Temperature

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276720](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276720)

**Video:** 05 - 007 - Temperature.mp4 | **Duration:** 7m 55s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Earlier on, inside this course, we spoke very briefly about how

 Claude actually generates

 text.

 Remember, we feed some amount of text into Claude, like the words "

What do you think?"

 Claude is then going to tokenize this text, or break it up into

 smaller chunks.

 Claude is then going to go through a prediction phase, where it

 decides what possible words

 could come next, and assign a probability to each of those different

 options.

 Finally, in the sampling phase, a token is actually chosen based upon

 these probabilities.

 So in this diagram I have on the screen, given inputs of "What do you

 think?"

 Possible next tokens might be about, wood, of, and so on, everything

 you see here on the

 right-hand side.

 Each of these gets assigned a probability, and then maybe, in this

 case, Claude settles

 on "about" as being the best possible next token.

 So we would end up with a phrase "What do you think about?"

 This entire process is then repeated to complete the sentence or

 complete the entire message.

 Now just to make sure things are really clear, the numbers I'm

 showing here are probabilities,

 the percentage chance of each token being selected.

 Just to make things a little bit more clear with these probabilities,

 I'm going to display

 them in a chart for the rest of this video.

 So still the same probability is just in a format that's easier for

 us to understand.

 You also notice I've kind of sorted them from left to right.

 There's no actual internal sorting going on.

 I'm just sorting them greatest to least probability, just to make

 this chart a little bit easier

 to understand.

 So now that we have a reminder on how Claude generates text, I want

 to show you one way

 that we can directly influence these probabilities and control which

 token Claude might actually

 decide to select.

 So we can control these probabilities using a parameter called "tem

perature."

 Temperature is a decimal value between 0 and 1 that we provide when

 we make our model call,

 so whenever we call that "converse" function.

 Temperature is going to influence the exact distribution of

 probabilities.

 This is a little bit tricky to understand, so you can look at the

 plot or these charts

 I've got right here, or alternatively, I put together a quick little

 demo with Claude

 itself just to give you a better idea of what's going on.

 So let me show you that demo.

 Okay, so this is the same chart we were just looking at in that

 diagram a moment ago.

 Whenever we provide a temperature value going down to 0, so you'll

 see I got temperature

 right here, the highest probability becomes more likely to occur.

 So our highest probability was about, and it's going to increase all

 the way up to 100%.

 So at temperatures of 0, we start to get what we call deterministic

 output, where we always

 select the token that has the highest initial probability.

 Then as we start to increase our temperature, it increases the

 chances of us selecting a

 token that has a lower initial probability.

 So we go from maybe having a 0% chance of selecting "we" as the next

 token, all

 the way up to say 9%. So this is the theory behind temperature, but

 what does this actually

 mean in the real world?

 Well, we start to use different values of temperature, given the

 actual task that we're

 trying to complete.

 These are some example ranges and tasks that might fit into each

 sample range.

 For something like, say, data extraction, we really don't want a lot

 of randomness or

 a creativity. If we give Claude a big chunk of text and ask it to

 extract very specific

 pieces of information, no real creativity required there whatsoever.

 We just want Claude

 to look at the exact text we provided and pull out the most relevant

 information.

 And then on the higher temperature side, this is where we start to

 get more creative, and

 we start to see less common tokens being used.

 We probably are going to want to use higher temperatures anytime you

're doing any kind

 of really creative focus task, such as brainstorming, writing, maybe

 doing some really creative

 marketing, or something like a joke where a lot of jokes really

 depend upon using words

 in ways that are not always quite expected.

 Now that we have an idea of what temperature is all about, let's take

 a look at how we

 can play around with it with the bedrock API.

 So the first thing I want to show you is in the bedrock documentation

 or specifically the

 bedrock user guide. Inside of here, on the left hand side, I've navig

ated down to Anthropic

 Claude models, and I'm taking a look at some documentation around

 Claude Sonnet.

 If I do a search on this page for temperature, and then go down a

 little bit, I'll finally

 find temperature right here, so a description of this parameter, and

 you'll see that by

 default, temperature is set to one. So that means that by default,

 whenever we access

 Claude through bedrock, we're going to usually get back some really

 creative responses, which

 may or may not be good. So we might want to control this temperature

 value to sometimes

 make sure that we're getting more deterministic output for tasks like

, say, data extraction,

 and then maybe we could adjust temperature depending upon whether we

 want a more creative

 task, like say, writing a script for a movie or something like that.

 So now back inside of Jupiter, I have the same notebook I was working

 on in the last video.

 I have added in a new cell here, where I've made a new list of

 messages. I'm adding in

 a user message where I'm asking Claude to generate a movie idea in

 one sentence. I then

 call chat, get back some text and print it out. And before running

 this, let's update

 our chat function. So it will take in an optional temperature

 parameter, and we'll pass that

 through to our converse call. So we can adjust the creativity of our

 model a little bit. I'm

 going to go back up to the chat function right here. I'm going to add

 in an additional argument

 of temperature, and I'm going to match the default temperature value

 of the model itself,

 which is 1.0. I'm then going to pass that through this params

 dictionary. So I'm going

 to put in a new key to this of inference config. And notice that this

 is the word inference.

 It is not interface. So make sure you get the spelling there correct.

 I'll then put in

 a temperature of whatever temperature was passed in. And that's it.

 So now if I rerun

 that cell just to redefine chat, I'll then go back down to the cell I

 had added down

 here to generate movie ideas. And remember, now we have a default

 temperature of one,

 I'm going to leave it like that for right now. And if I run this once

, I should get back

 a movie idea that it is at least somewhat creative. And if I read

 this over a reclusive

 origami master, this is a very creative movie idea, you can tell

 right away, I'll run it

 again. And we're definitely going to expect to get back another movie

 idea that is really

 creative. Okay, that also looks reasonable just one more. And yeah,

 reasonably creative.

 So now I'm going to add in the temperature and set it to flat zero.

 Now in theory, we're

 going to get back some ideas for movies that are a little bit less

 creative in nature perhaps.

 So if I run this, I'll see a time traveling archaeologist. Now it's

 kind of hard for you

 and I to just run this prompt a couple times and decide whether or

 not it is creative.

 But let's run this one or two more times. And I think you're going to

 notice a theme

 really quickly. Notice how this is a time traveling archaeologist. So

 if I run this

 again myself, I'm probably going to see another response here about

 yeah, there we go, a time

 traveling something related to history. I'll do it again. And I'll

 probably see again,

 a time traveling historian. So you can start to see right away that

 we start to get responses

 that are a little bit less creative and they tend to be rather

 similar to all other responses

 that we get when we feed in this identical initial prompt of generate

 a movie idea in

 one sentence. Okay, so that's temperature. Now remember, there's some

 general guidance

 here. Whenever we are doing tasks that require less creativity or

 where we want to have very

 deterministic output, we're going to use that lower temperature. And

 then whenever we have

 a task that requires a little bit more creativity, that's when we

 start to start to want to

 think about dialing up the creativity a little bit.

---

#### Lesson 10: Streaming

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276721](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276721)

**Video:** 05 - 008 - Streaming.mp4 | **Duration:** 9m 5s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

I want to think back to our original chat interface example

just one more time.

So remember, we've got a chat interface

running on a website or maybe a mobile app.

A user is gonna submit a question,

or they're then going to take that text in our server,

put it inside of a user message, send it off to bedrock,

that's gonna give us back an assistant message,

we'll extract some text from that,

and then potentially send it down to the browser

where the actual generated text can be displayed to the user.

Now, this would all work,

but there's one big downside to it.

And that is that the time between sending that initial request

with the user message and get a response

can sometimes take a really long time,

depending upon the length of the response

that is being generated.

So it can take anywhere from maybe three seconds,

but it could also take maybe 30 seconds.

Most users' expectations are that whenever they enter

in some kind of initial message,

like how do I host a Postgres database,

they want to immediately start seeing some content

being generated on screen right away.

But they don't want to wait 30 seconds.

So to implement this kind of immediate feedback,

we can use a function that's kind of like converse,

it just works a little bit differently.

And that is the converse stream function.

Converse stream allows us to stream back a response.

It streams back some generated text

as it is being produced by our model.

Let me show you a couple diagrams

to make sure it's really clear how this thing works.

So once again, we're gonna have a user

submitting an initial question to our server.

We're then going to send a request off to bedrock,

this time using the converse stream function.

Then the response we get back

is gonna be a little bit different in nature.

Right away, we're going to immediately get back

an initial response.

There's not gonna be any generated text

inside this initial response.

It's really just gonna be a message from bedrock

that says, "Hey, we received your request,

"we are now generating some text."

We're then going to start to receive a stream of events.

We're gonna go into more detail

around exactly what these events are.

But for right now, just understand

that they contain pieces of the generated response

that we want to send back eventually to our user.

We're going to get a number of different events.

The number that we get depends upon

how much text we are generating.

Each event is gonna contain just a little bit

of the overall message that is being generated.

So maybe this first event has the text, "You can,"

and then the next one, "Host A,"

and then the next one, "Postgres."

In theory, we would probably have some

additional events after that to really flush the message out.

As we receive each event, we would take this generated text,

send it down to the browser,

and then hopefully our browser or mobile app

would display that part of the generated message on the screen.

And then we would repeat this process

for each additional event.

So we'd take the text, send it down to the browser,

and show that on the screen.

And eventually, we would stream in each chunk,

and so the user can start to read the response

right away as soon as possible.

Now, I wanna spend a lot of time

discussing the exact nature of these events,

because that's really the kind of challenging part

of understanding how a converse stream works.

But first, let's write out a little bit of code

just to get our hands on Converse Stream

and really understand it.

So back inside of a notebook,

I've once again got an initial set of messages

right here that starts off empty.

I've added in one message that just says,

write a one sentence description of a fake database.

Now I'm going to get a response

by calling clientConverseStream.

I'm gonna pass in my list of messages.

And of course, I still need to pass in my model ID.

And remember, our model ID keyword

is actually model capital ID,

but our model ID that we specified earlier

is model_id.

I'm then going to print out just the response for right now.

And when I run this cell,

you'll notice that it only takes about a second

for me to get the initial response back.

So again, this is the initial response

we saw in the diagram.

It's this thing or right here.

Inside of this initial response,

there's not actually any generated text.

Instead, we get this new key added inside of it of stream.

Stream is an event stream object.

Essentially, it's a generator that we can iterate over.

And each value that gets emitted

or yielded by that generator

is going to be one of these different event objects.

So let's update our code here a little bit.

I'm gonna change it to for event in response.

And remember that thing is specifically

at the stream key inside the response object.

I'm then going to print out that event.

I'll then run this again.

Let's see what we end up getting.

So now we start to get a stream

of different events being printed out.

And even though it's a little bit hard to see,

you might notice that when you run the cell,

you first see the first print or two,

like the first event print.

And then you start to see the other start to trickle in

with a little delay in between each one.

So let me show you a diagram that's gonna help you

understand what these event things are all about.

So again, whenever we make our request off to bedrock,

we're gonna get back a series of these different events.

There are several different kinds of events

that are going to be yielded by that generator.

And we can see these all being printed out

when we run that cell.

So we might see an event of type message start.

We then might see an event of type content block start

and then content block delta and so on.

If I go back over to Jupiter, I'll see those right here.

So here's message start.

I've then got some content block deltas.

And if I scroll down, I eventually get a message stop

and a metadata event.

Now, each of these different events

has a different meaning in the context of our response.

For right now, the only event that we're really

gonna be focused on is the content block delta.

Each content block delta event contains a little piece

of text that was generated by our model.

And this is the actual text that we eventually want

to probably show to a user or make use of in some way.

So if I again, look at my log right here,

I'll see that each of these content block deltas

have nested inside them a delta and then a text.

And then that is the actual text I care about.

So for me, I would end up with a generated message here

of the Xenonlin Q7 database is a revolutionary

yet entirely blah, blah, you see, so on and so on.

You are always gonna see these different events

listed out in the same order.

So we're always gonna end up seeing

a message start event first.

We'll then see some number of content block delta events,

then a content block stop, message stop and metadata.

Now, as we start to take a look

at some more advanced features of our model,

we might eventually see multiple content block start

and stops.

But for right now, when we're only generating text,

we're only going to get back a single set

of content block deltas and a single content block stop.

We're not even going to actually see a content block start,

even though that is an event.

So that is an event, but we're not actually gonna see it

if we're only generating text.

It's only gonna be relevant once we start

to go into tool use, which we're gonna cover

a little bit later on.

So again, for right now, the only event

that we really care about when we only care about text

is content block delta.

So with that in mind, let's update our for loop

back inside of our code.

I want to collect all the different content block

delta events.

Whenever we get one of these,

I want to try to print out the text inside of that event.

So here's how we would do it.

I'm going to update the contents of the for loop

and I'll say if content block delta in event.

So I'm just checking for the presence of that string

inside of this event dictionary.

Then I want to get the chunk text, which I'll call chunk

and that's going to be event at content block delta,

delta text.

And then I'll print out just that chunk.

Whenever we print out a chunk using the print function

of Python, it's gonna automatically append a new line

to the end of the print statement.

So it ends up being a little bit challenging

to read like this.

So I might recommend adding in the end keyword

---

#### Lesson 11: Controlling model output

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276723](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276723)

**Video:** 05 - 009 - Controlling Model Output.mp4 | **Duration:** 6m 44s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Besides just changing our prompts that we send into Claude,

 there are two other ways we could strongly influence the output that

 we get out of it.

 So in this video, we're going to discuss two techniques.

 One is pre-filling assistant messages, and second is stop sequences.

 Let's first take a look at pre-filling assistant messages.

 Okay, let's imagine that we send Claude some kind of really tough to

 answer question,

 something like is tea or coffee better at breakfast.

 I have absolutely no idea what kind of response Claude would give me.

 As a matter of fact, let's go over to our Jupyter notebook really

 quickly

 and see what kind of response we get in the first place.

 So back over here, I have created a new notebook,

 still has all the same code we had previously though,

 so I'm still making a client, assigning my model ID,

 and then I define those three helper functions.

 In the next cell down, I'm going to make a list of messages.

 I'm going to add in a user message of is coffee or tea better for

 breakfast.

 And then let's see what we get with that.

 So after a brief pause, we're going to get back probably a rather

 long message

 because I think Claude has a lot of input on this topic,

 but you can see right away that it's just not really taking a

 position per se.

 So there might be some scenarios where we want to strongly influence

 Claude one way or another,

 where we want to kind of direct its output or direct its response in

 some particular fashion.

 So one way we could do this is by pre-filling and assistant response.

 With message pre-filling, we're still going to assemble a list of

 messages.

 We're going to put our user prompt inside there,

 but there's going to be one extra little difference.

 You and I are going to manually put on an assistant message at the

 very end,

 and you and I are going to author the content inside of that

 assistant message.

 We're then going to take this list and send it into bedrock.

 And then in Claude, we can kind of imagine this is what goes on behind

 the scenes.

 We can imagine that Claude is going to see that first message and say

 to itself,

 "Okay, the user wants to know what I think about coffee versus tea."

 It's then going to take a look at the second message, which is an

 assistant message.

 And because it is an assistant message, Claude is going to say to

 itself,

 "Oh, it looks like I already have some thoughts on the situation."

 So I better continue my final response.

 I'm going to send back using this as a starter.

 So Claude is going to essentially use this as the start of its

 response.

 Because Claude sees the sentence, "Coffee is better because,"

 that's going to very strongly steer it in the direction of supporting

 coffee

 as being better at breakfast.

 So chances are, Claude is going to give us back a final assistant

 message

 that says something like, "It has higher caffeine,"

 which implies talking about coffee.

 Now, the one very important thing here to distinguish

 is that whenever we put in this final assistant message right here,

 Claude is going to assume that that is kind of content that has

 already been

 authored, and it's going to continue its response from the very end

 of the sentence.

 So you would kind of expect Claude to give you back a full response

 like this,

 where it says, "Coffee is better because it has a higher caffeine,"

 that is not the case.

 It's going to continue the response from the very end of whatever you

 pre-filled with.

 So in other words, this is not really a complete sentence.

 And if you want to use this, you're probably going to have to go back

 and kind of stitch together that text right there and that text right

 there.

 Okay. This is when you explain it, something is kind of hard to

 understand,

 but in practice, it ends up being really easy once you see a demo or

 two.

 So let's just go right out some more code and see how this actually

 works.

 So back over here, message pre-filling, super simple.

 All we have to do is say, "Add assistant message,"

 and we'll say, "Coffee is better because,"

 and now when we send this off, Claude is hopefully going to give us

 something that supports coffee much more strongly than it did

 previously.

 So before, it was kind of even on the fence.

 It said, "Oh yeah, either tea or coffee is fine,"

 but now with message pre-filling,

 we have very strongly steered it towards preferring coffee.

 And of course, we could say, "Tea is better because,"

 okay, that works.

 And then, of course, we could just give it a neutral position.

 And we could say, "They are the same because,"

 and then we get back the more neutral response that doesn't favor

 either of them.

 Now once again, I want you to notice that when we use this message

 pre-filling,

 we get back kind of a partial response right here.

 So it just says, "Both drinks don't have any nutrients."

 So like I mentioned, when we were looking at the diagram,

 it's kind of up to you to take whatever your pre-filled response

 right here was

 and join it onto the end of the actual response when you're using

 this technique.

 So now that we have seen message pre-filling,

 let's take a look at our other topic for this video,

 which is stop sequences.

 Stop sequences are going to force Claude to stop generating a

 response

 as soon as it generates some particular string that you provide.

 So let's imagine that we provide a prompt of count from 1 to 10.

 And naturally, our expectation would be that we get back 1, 2, 3, 4,

 5,

 all the way up to 10.

 We could stop the generation early by providing a stop sequence of

 the string 5.

 Then internally, whenever Claude generates the string 5,

 it's going to immediately stop the response

 and send whatever it has generated already back to us.

 Again, let's take a look at a quick example of this.

 Stop sequences are provided as an additional parameter to our con

verse function.

 So I'm going to scroll up a little bit, find where we define chat

 right here,

 because that's where we actually call it converse.

 I'm going to add in an additional optional keyword argument to the

 chat function itself.

 I'll call it stop, sequences, and I'll default it to be an empty list
.

 Then inside the inference config dictionary,

 I will pass in stop sequences like so.

 I'm then going to make sure that I rerun that cell.

 Now let's test this out.

 I'm going to go down to the very bottom of my notebook and make a new

 cell.

 I'm going to copy everything out of the previous one just to save a

 little bit of typing.

 I'll remove the pre-filled message and then update the user message

 to say

 count from 1 to 10.

 And if I run this as is, I'll expect to get back the full list of,

 well, 1 to 10.

 So if we wanted to truncate the response or stop it at a certain

 point,

 we could now add in to our chat function a stop sequences keyword

 argument.

 That's going to be a list.

 And inside there, we're going to put in all the different characters

 that we might want to stop at.

 They don't have to be individual characters.

 They could be full words.

 So I might say stop whenever you print out the character five.

 And if I now run this, we'll see only one, two, three, four.

 And you'll notice that it does not include the character five.

 So five is removed entirely.

 We can put in as many stop sequences as we want.

 So I could also put in say three, four, like so.

 And the response will just be stopped as soon as it sees any of these

 different sequences.

---

#### Lesson 12: Structured data

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276724](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276724)

**Video:** 05 - 010 - Structured Data.mp4 | **Duration:** 6m 1s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

stop sequences, and Assistant message prefilling can be combined

 together in a really powerful way,

 something that you're probably going to end up doing rather

 frequently anytime you need to generate

 some kind of structured data. So to help you understand how these

 things work together,

 let me walk you through a really quick example. Let's imagine that

 we are building a web app

 like the one you see on the screen. This is a web app that's going to

 generate event bridge

 rules based upon some user input. If you're not familiar with them,

 event bridge rules are used

 in AWS, they're essentially little JSON snippets. So user is going to

 enter in some prompt like this

 and then click on generate. And chances are the user is going to want

 to see some generated rule

 just appear that they can very easily select right away or click on

 this little copy button

 and go use somewhere else. The point there is that part of the

 critical user experience here is

 that we want to show just the JSON for the generated rule and nothing

 else. So if we instead displayed

 a response that looks like this, it would definitely not be as

 helpful for our users.

 We're still generating the rule, but now it also has this header up

 top and this commentary

 footer down at the bottom. So now a user can't really use this copy

 all button. They would have

 to go in and manually select that JSON right there. So this is an

 example where we really don't want

 Claude to be that helpful and explain its work. We want just some very

 particular data and nothing

 else. Now to be clear, this is not a problem that is just limited to

 generating JSON. It turns out

 that anytime you are using Claude to generate any kind of structured

 data. So it could be JSON

 or it could be Python or even just a bulleted list of text items.

 Claude is very often going to try

 to insert a header or a footer or some additional kind of commentary.

 And in many of these scenarios,

 you don't want that additional commentary. You just want the raw

 content that you asked Claude to

 create. So to help keep Claude on track here and only give us the raw

 content that we're asking for

 and no additional header or footer or commentary or anything like

 that, we can use our stop sequence

 in combination with a pre-filled assistant message. Let me show you

 how. I'm going to go back over to

 my notebook. I'm going to continue on by making a new cell down here.

 I'm going to again make a

 list of messages. I'll add in a user message and I'll say something

 like generate a very short

 event bridge rule as JSON. I'll then pass that off like so. And then

 let's just see what we get

 with this kind of initial take. So right away, we can see that we do

 get back some JSON, but it has

 unfortunately that little back tick back tick back tick back tick

 JSON right there and then a matching

 closing one over there. And just to make sure it's super clear, these

 back ticks are in place to

 format this all as markdown. So it gets formatted very nicely if you

 were to render it as markdown

 text. But in our case, we don't want any of those additional

 characters. We want just the raw

 JSON by itself. So to do so, we can do two things. We're going to use

 both an assistant message and

 a stop sequence. For right now, we're just going to write out the

 code to do so. And then I'll show

 you a diagram that explains how it all works. First, I'm going to pre

-fill an assistant message.

 So let's say add assistant message. And my pre-filled message will be

 back tick back tick back tick

 JSON. And then on my chat call, I'll add in stop sequences. And

 anytime we see a back tick back tick

 back tick, I want to immediately stop generation. So let's now run

 the cell and see what we get back.

 Okay, so now we get just the JSON by itself. You will notice that

 there are some new line

 characters in here, but that's totally fine. We can very easily

 remove those extra new lines

 by just parsing the response as JSON, or by doing a strip call. So I

 could say text is chat,

 I'll print out text. And then on the next cell down, I might import

 JSON. And do a JSON loads

 with text and strip on text as well. And if I run that, yes, we

 definitely get back some

 very well formatted JSON here that we can access in any way that we

 expect. All right, so what

 exactly is going on with the assistant message and the stop sequence?

 Well, let me show you a

 diagram just to break it all down and make sure it is super clear. So

 once again, we are doing

 our user message, we're providing a pre-filled assistant and a stop

 sequence. So when you send

 this all into bedrock, Claude is going to take a look at all the

 different parts of this request.

 It's going to initially take a look at that user message content and

 say, all right, it's very clear

 that I need to write a full rule. And I should probably also describe

 it. So maybe put on a header

 and a footer. Because that's kind of what Claude naturally wants to

 do. It wants to explain the

 work that is doing. But then it's going to encounter that assistant

 message. And just as we learned in

 the last video, Claude is going to assume that it already wrote that

 out in its response. So it's

 going to say, Oh, I've already started the JSON part. So now all I

 have to do is write out the actual

 JSON. It's then going to write out all of this JSON in the response.

 And then as it gets to the

 very end, it's going to naturally want to close off that markdown

 code block that it thought it

 created earlier. So Claude is going to want to put in a closing, back

 tick, back tick, back tick.

 As soon as it does so, however, it's going to encounter the stop

 sequence, which stops the

 generation entirely and immediately sends us back the response. So

 you can really imagine that what's

 really going on here is we're kind of saying start with this and with

 that and just give us

 everything in between. And that results in us just getting back the

 part we really care about,

 just the JSON by itself. And like I mentioned, this is a really

 powerful technique that we're

 going to use very often anytime we want to generate some kind of

 structured data and get just that

 data with nothing else besides it. And remember, this technique can

 be used for any kind of structured

 data. It is not limited just being used on JSON. So anytime we have

 any kind of very specific

 content we want to generate and get just that content with no

 additional commentary on it,

 we're going to take a look at using assistant message pre-filling

 along with stop sequences.

---

#### Lesson 13: Structured data exercise

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276718](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276718)

**Video:** 05 - 011 - Structured Data Exercise.mp4 | **Duration:** 4m 57s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's go through a very quick exercise,

just make sure the idea of stop sequences

and message pre-filling are super clear.

So in this exercise,

I'd like you to write out the exact code

I've got right here on the screen.

All this code should be really familiar.

If you take a look at the prompt,

it says generate three different sample AWS CLI commands.

Now when you run this code,

you're probably gonna get back some output

that looks vaguely like this right here.

Just make it a little bit easier to read.

I rendered it as markdown down here.

So here's the sample starting output that I get.

You'll notice that it does give us three different sample

commands, but it has a lot of commentary around them.

So I've got a header and then some numbers

listing out each individual command.

For this exercise, I would like you to take this code

and using all new message pre-filling and stop sequences,

I want you to get all three different commands

in a single response,

all right next to each other

without any additional comments or explanation

or anything like that.

I don't like you to do this using only message pre-filling

and stop sequences.

So no adjusting this prompt at all.

So go ahead and give this a shot.

I did put a little hint on here, just as a reminder,

with message pre-filling, it's not limited

just to using characters like the Bactik, Bactik, Bactik.

You can put any kind of pre-filling response you want.

I would encourage you to pause this video now

and give this an exercise a shot.

Otherwise, I'll go over a solution right away.

So here we go. Here's how we're gonna solve this.

To solve this, the first thing I recommend you do

is take a look at the output

without any kind of pre-filling or stop sequences

or anything like that.

So if we take a look at what we have right here,

we'll notice that each of our three commands

are wrapped in a series of three Bactics.

So a good place to get started

would probably be to put in a pre-filled assistant message

of three Bactics to kind of tell Claude,

just go right into the command writing right away

and skip any initial commentary.

And then we might also decide to put in

a stop sequence of three Bactics as well.

Let's see how far that gets us.

So I'll put in a add assistant message

and I'll start everything off with three Bactics

and I'll put in a stop sequences

of closing three Bactics.

Let's run this and see how far it gets us.

My initial output looks kind of reasonable,

but it's not perfect just yet.

I do get three commands.

There's one, two, and three.

But you'll notice that I also get the word bash

added at the very start.

So where's that word coming from exactly?

Well, let me show you what Claude is really trying to do here.

We provided the initial assistant message

of those three Bactics.

Whenever you put down three Bactics,

it's kind of indicating that you are writing out some

Markdown and when you are writing a Markdown code block

with Bactics, you can optionally put in

a language identifier right here.

If you choose to put one in,

that whenever you render this as Markdown,

the content inside of those Bactics,

we rendered using that language's syntax highlighting.

So in this case, Claude decided to put in a bash right here

just to say, hey, we should use bash style syntax highlighting

when we render this stuff out.

Now for us, we don't want that at all.

So one way we could address this

would be to adjust our pre-filled message right here

and just include bash ourselves.

So that's now gonna make it super clear to Claude itself

that yes, you are inside of a Markdown code block

and inside this code block,

you should be writing out bash formatted commands.

So let me try run this again and see how I do now.

Okay, so that looks better.

Now I will tell you that from this point,

there are probably two additional errors

that you might want to address.

The first is sometimes you will get back a single command,

which is kind of an indication that Claude might want

to write out three separate Markdown code blocks.

The other problem that you might run into

because we are now using a bash code block,

Claude might try to insert some bash formatted comments

in there as well.

So it might be something like this command does xyz

and you might see that repeated.

And so we definitely don't want those comments

really just because that was one of the requirements

of this exercise.

So to get rid of those comments

and to also make sure that we get all three commands

more reliably, we can use that hint I gave you.

Remember the hint was message prefilling

isn't just limited to designating characters

like back ticks or stuff like that.

We can also use the message prefill

to dramatically guide Claude

in how it's going to answer us.

So in this case, we could add in something like

here are all three commands in a single block

without any comments.

And then I'll put in a colon right there

and then a new line.

Just so it starts all the Markdown stuff

on the next line down.

So I'm going to try running this

and we should now get some much more reliable output.

Okay, that looks good.

And of course I can keep running all day

and we're probably going to see exactly the result we want.

Okay, this looks good.

---

#### Lesson 14: Quiz on working with the API

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/289293](https://anthropic.skilljar.com/claude-in-amazon-bedrock/289293)

---

### Prompt evaluations

#### Lesson 15: Prompt evaluation

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276731](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276731)

**Video:** 06 - 001 - Prompt Evaluation.mp4 | **Duration:** 1m 48s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that we understand how to access Claude, we're going to shift our

 focus a little bit

 and look at two new topics, prompt engineering and prompt evaluation.

 These two topics are all about making sure that we are writing

 prompts that will get

 us the best possible output from Claude.

 Prompt engineering is a series of techniques that will use any time

 that we want to write

 or edit a prompt.

 These techniques will aid Claude in understanding what we're asking

 of it and how we want it

 to respond.

 Prompt evaluation, on the other hand, is where we do some automated

 testing of a prompt,

 with a goal of getting some kind of objective metric that tells us if

 our prompt is effective

 or not.

 In this section, we're going to be mostly focused on prompt

 evaluation.

 After we understand how to measure the effectiveness of a prompt, we

'll then take a look at some

 prompt engineering techniques, so let's get to it.

 The first thing I want to do is help you understand where prompt

 evaluation fits in to the prompt

 writing process in general.

 After you first write a prompt, you generally have three different

 paths ahead of you, three

 different ways you can go from there.

 With option number one, you might take that prompt you put together,

 maybe test it once

 or twice and decide it is good enough to use in production.

 With option number two, you might test the prompt a couple of times

 with your own custom

 inputs and maybe tweak it a little bit to handle a corner case or two

 that you notice.

 Now right away, I want you to understand that options number one and

 number two are kind

 of traps that all engineers fall into, myself included.

 It happens to everybody.

 We all start writing out prompts that are going to eventually be used

 in serious applications

 and we don't really test them enough to make sure that they are

 working as expected.

 So whenever you write a prompt, I highly recommend going with option

 number three.

 Run your prompt through an evaluation pipeline to get an objective

 score that will tell you

 how well your prompt is performing.

 You can then try to iterate on your prompt a little bit and make sure

 that it's performing

 as well as it possibly can.

---

#### Lesson 16: A typical eval workflow

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276732](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276732)

**Video:** 06 - 002 - A Typical Eval Workflow.mp4 | **Duration:** 4m 36s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, we're going to walk through all these steps

implemented by a typical prompt evaluation workflow before you go

through any of these steps. However, I just want you to understand

two important things.

First is there are many different ways you can assemble a workflow.

There's no one set methodology set in stone that is standard across

the industry.

The second thing to understand is that there are many different open

source packages and even paid options online that will help you

implement your own workflows.

Now, in this video and this module, we're going to start to implement

our own custom workflow from scratch inside of a Jupyter notebook.

The reason we're doing this is to, of course, just help you

understand how these workflows behave, but also to help you

understand that you don't have to get a really heavyweight solution

to do prompt evals.

You can start small, just to get started and get a sense of how

everything works and then scale up from there.

All right, so let's get to it. Step one of a typical prompt eval.

Step one, we're going to write out a initial prompt draft so you and

I will sit down and just write out some kind of prompt that we want

to improve in some way.

For this example, we're going to have a very simple prompt that just

says, please answer the user's question and then we're going to

interpolate in some user input. So some question provided by user.

In step two, we're going to create an evaluation data set. This data

set is going to contain some number of possible inputs that we might

want to put into our prompt.

So for us, our prompt only has one input, a question provided by user.

So for our eval data set, we'll have a list of different possible

questions that we might want to put into our prompt.

My data set is only going to have three different questions inside of

it, but in real world evals, you might have tens, hundreds, even

thousands of different records in your data set.

Now you can assemble these data sets by hand, or you can, of course,

also use Claude to generate them for you.

Once we have our eval data set, we're then going to feed each of

these different questions into our prompt. So we get a fully fleshed

out prompt that we can then feed into Claude.

So we might have prompt one right here, where we have please answer

the user's question and then a sample question out of our data set,

like what's two plus two and then we will repeat for all the other

records inside of our data set. So here is two and three.

We'll then feed each of these into Claude and get an actual response

out of Claude. So for the first one, we might get back a response of

something like two plus two is four and then something about how to

make oatmeal and then something about the distance to the moon.

Once we have these actual answers coming out of Claude, we're then

going to grade them in some way.

During this grading step, we're going to take each of the questions

out of our data set and the answers we got out of Claude.

We'll pair them all off together and we'll feed them into a grader

one by one. There are many different ways we can implement this

grader. We'll take a look at some of the different methodologies a

little bit later.

The grader will then give us a score, maybe from one up to 10 based

upon the quality of the answer that was produced by Claude. So a 10

would mean we got a perfect answer and there's really no possible way

we could improve it.

It may be something like a four indicates that there's definitely

room for improvement there. Now, as you can guess, there's kind of a

lot of hidden complexity here with a grader because you're probably

curious or wondering, well, how do we actually get these scores at

all. Again, don't worry, we're going to cover these grader things in

much greater detail in a little bit.

After we get these scores, we're then going to average them all

together. So in this case, I would add the scores together, divide by

three and get an average score of 7.66.

So I now have some kind of objective way of describing how well our

original prompt performed.

Now that we have this score, we can then change our prompt in some

way and iterate or repeat this entire process.

So if I want to improve my score, I might try adding in a little bit

more detail to the prompt to hopefully guide Claude a little bit more

and help understand what kind of output we want.

So maybe I would add on to the end of the prompt, something like

answer the question with ample detail.

Once I have the second version of my prompt, I would then run it

through this entire pipeline again.

I would then have a score for prompt version 1 in prompt version 2. I

could then compare these two scores in whichever score is greater or

higher.

It's kind of a objective sign better than nothing that tells me that

prompt V2 in this case is perhaps the better version of our prompt.

So now that we have a high level overview of this entire process, as

I mentioned, we're going to start to implement our own custom eval

framework inside of a Jupyter notebook.

So let's get started on an implementation in the next video.

---

#### Lesson 17: Generating test datasets

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276733](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276733)

**Video:** 06 - 003 - Generating Test Datasets.mp4 | **Duration:** 6m 37s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's get started on building our own custom prompt evaluation

 workflow.

 We're going to be writing out a prompt and then writing out some code

 to evaluate how well it performs.

 So let's first focus on making a prompt.

 The goal of our prompt is to help users in writing out some code

 specific for AWS use cases.

 So we're going to allow user to enter in some kind of task that they

 need help with.

 And then we're going to respond with one of three types of output.

 We're either going to output Python, JSON configuration, or a raw

 just plain regular expression.

 Those are our three possible outputs.

 So we need to make sure that whenever a user asks for us to complete

 some kind of task,

 we give them some output in one of these three particular outputs

 without any other kind of explanation or header or footer or anything

 like that.

 So that's the overall goal.

 Now, the first step of our goal is, of course, to write out a draft

 prompt.

 Now, I've kind of already done that for us on the right hand side

 here.

 I've got V one of our prompt, where it just says, please provide a

 solution to the following task,

 and we'll put the user's task in there.

 Step two is to assemble a data set.

 Remember that a data set is going to contain some number of inputs

 that we're going to feed into our prompt.

 And then we're going to run our prompt for every combination of

 prompt and input.

 For our particular case, we're going to have an array of JSON objects

,

 where every object has a task property.

 These tasks are going to describe something that we want to be done

 by Claude.

 So we're going to take each of these tasks, put them into our prompt,

 and then feed the result into Claude.

 Remember that when we make a data set, we can either assemble it by

 hand,

 or we can generate it automatically with Claude.

 Now, as a side note, if you're using Claude for something like this,

 this would be a really good opportunity to use a faster model like Haiku.

iku.

 And that's what we're going to be doing here.

 Let's go back over to Jupiter.

 We're going to open up our notebook,

 and we're going to write out a little bit of code that's going to

 generate a sample data set,

 like the one you see on the left hand side, using Haiku.

 Okay, so back over here, I'm inside of a new notebook,

 and once again, very similar setup to all the others we have worked

 on.

 I'm creating a client.

 I have updated my model ID to use a inference profile

 that's referring to a Haiku series model, just so I get that

 additional speed.

 I've then got those three helper functions put together.

 I'm going to scroll down and make a new cell.

 And inside of here, I'm going to make a helper function called

 generate data set.

 And then inside, I'm going to write out a rather lengthy prompt

 that's going to ask Claude to generate this kind of evaluation test

 set for us.

 Just to save some time, I'm going to copy paste the completed prompt

 in here,

 rather than asking you to sit around and watch me type it out.

 Remember, if you want to just copy paste a prompt,

 you can always open up the completed version of this notebook

 and copy paste the prompt yourself as well.

 So I'm going to paste this thing in.

 So here's my prompt.

 You'll notice that I am asking it to generate some tasks related to

 AWS.

 And I'm giving it some example output here.

 And notice that the example output I'm asking for specifically an

 array of objects,

 each of which has a task.

 And then at the bottom, I'm also clarifying asking it to generate

 just three separate objects.

 So essentially three different tasks here.

 Remember that in a real world scenario, we would want to have way

 more than

 just three different test cases.

 But right now, this is enough.

 Do note that we are going to eventually come back and change the

 structure of this object.

 So for right now, it's going to be just a very plain, flat, simple

 object,

 but we will come back later and change it up a little bit.

 And the only reason I mentioned that is that if you go and look at

 the completed code,

 you might notice that this prompt looks a little bit different.

 All right.

 So now that we have this prompt put together at the bottom of the

 function,

 I'm going to make sure I indent because we are still inside of a

 function here.

 I'm then going to send this prompt off to Claude and ask it to

 generate some different tasks for us.

 So we'll add a user message.

 And then when we get our response back, we are expecting to receive

 some JSON.

 And to extract that JSON, we can use the same technique we covered in

 the last module,

 which is to use a combination of a pre-filled assistant module,

 or some assistant message, and a stop sequence.

 So we'll do a add assistant message.

 And I want to pre-fill message with Backtix 123 JSON.

 I'm going to call chat with messages.

 And I want to provide that stop sequence of three backticks as well.

 And now when we get this response back right here of text,

 this is really supposed to be some JSON.

 So I'm going to immediately try to parse that JSON using the JSON

 module

 and then return it from this function.

 So I will do a return JSON dot loads with text.

 I'm going to make sure that I imported that JSON module up here at

 the top.

 I did already.

 You might need to add in that import statement and rerun that cell.

 All right, then let's test this out really quickly.

 So back down here, I'm going to run that cell.

 And in the next down, I will call generate data set.

 And we'll see how we are doing.

 Because I'm using Haiku and I'm only generating three records,

 this should generate pretty quickly.

 And there we go.

 So it looks like these tasks are actually pretty reasonable.

 Once again, just reminding you that we would definitely want to have

 more than three here.

 And we would also want to have a lot more variety and kind of the

 structure of these requests.

 But again, for right now, this is definitely appropriate.

 I have a sample task to generate a Python function to write out a

 JSON schema

 and one regular expression as well.

 So this is overall looking pretty solid.

 The next thing I'm going to do is save this data set into a JSON file

,

 just so I don't have to constantly regenerate the data set.

 So I'm going to say data set, it's going to be the result of that

 generation.

 I'm then going to open up a file called data set dot JSON in right

 mode.

 And I'll do a JSON dot dump data set.

 And I'll format it really nicely just in case we ever want to open up

 that file

 and see what it looks like.

 So I'll write that file.

 It's going to take a moment just because I'm regenerating the data

 set again through Haiku.

 And that should be it.

 So now if I open up that data set dot JSON, here is my data.

 Okay, this is a good start.

 We've got our eval data set put together.

---

#### Lesson 18: Running the eval

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276736](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276736)

**Video:** 06 - 004 - Running the Eval.mp4 | **Duration:** 6m 42s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

With our data set generation complete, we now need to take every

 record in that data set, which we're going to refer to as a test case

, so we're going to take each test case and merge it with the prompt,

 where they're going to take the result and feed it into Claude.

 And then once we have all these different outputs, we're going to

 feed them through our grader.

 Remember, we have not discussed graders just yet.

 Don't worry, that's going to come up very quickly.

 Now, once again, just to save a little bit of time, I've written out

 a little bit of code here just to help guide this next phase of our

 workflow.

 I put together three separate functions with a very clear comment on

 what each one does.

 The first one that's easiest to understand is the run prompt function

.

 This is going to be called with a test case.

 And those JSON objects that we generated just a moment ago, each of

 these is a test case.

 So you can imagine that each of these one by one are going to flow

 into the run prompt function.

 So inside of here, our goal is to merge that task that we generated

 with our prompt, generate some text with Claude, and then return the

 result.

 So let's do that right away.

 I'm going to put in my V1 prompt right here, which is very simple.

 Remember, we are starting off as simple as possible here, so it'll

 just say something like, please solve the following task.

 And I want this to be a F string, and I'm going to put in test case

 task.

 Next up, we want to send this off to Claude, so I'll make a list of

 messages.

 I'll add in a user message.

 I'm then going to pass this off to Claude by calling chat.

 And we're going to get back some resulting text, some result, or

 maybe we'll call it output this time around.

 And then for right now, I'll just return the output.

 Now, remember, we don't have any kind of formatting included or any

 formatting instructions inside the prompt right now.

 So we're going to probably get back a lot more output than we ever

 asked for.

 The real goal of our prompt is to make sure that we get just Python

 or JSON or that regular expression, and we don't have anything for

 that right now.

 So we'll almost definitely have to come back and make some

 improvements.

 But for right now, we at least have a start to run prompt.

 The next thing we're going to work on is run test case.

 The goal of this function is to take in one of those individual cases

,

 call the run prompt function we just put together, get some output

 from Claude,

 and then grade the result and return a dictionary describing the, and

 everything that happened there.

 Now, that sounds really complicated, but in reality, it's going to be

 surprisingly simple.

 So let me show you all we have to do here.

 We're going to put in output that's going to come from calling the

 function that we were just working on a moment ago.

 So this run prompt function put in our test case and then we're going

 to do some grading right here.

 That's going to be a to do.

 For right now, I'll just say that we have a hard coded score of 10.

 So we definitely have to come back and do a lot of heavy lifting

 right there.

 And then at the bottom, we're just going to return some information

 that summarizes everything about running this test case.

 So I will return a dictionary with some output.

 Whatever we got back from Claude, I'll include the test case and then

 our score.

 And then one final step here, we have to implement run eval.

 So this function is going to load up our data set or receive it as an

 argument.

 Either one is fine.

 And then we're going to loop through that data set.

 And for every test case, we will call run test case and then just

 assemble all the results together.

 So for implementation here, I'll say results is going to start off as

 an empty list.

 And for every test case in data set, I'm going to get our result from

 calling run test case and pass in the test case to it.

 And then add that into our list of results.

 And then down here, I'm just going to print up all of our results.

 Actually, you know what, let's actually just go ahead and return

 results.

 I mean, that's a little bit better.

 Okay, so there's the outline for our three major functions.

 Now, believe it or not, this is like a vast majority of what a eval

 pipeline is.

 We just put together the vast majority with the obvious exception of

 grading.

 So as you can see, there's not a whole lot of code that goes into

 this.

 Let's now test this out.

 So down here in the next cell down, I'm going to go into open up our

 data set JSON file.

 And parse it as JSON.

 And then call the run eval function.

 That's the one that we were just putting together right here with the

 entire data set.

 Finally, I'm going to assign the results to that to results.

 I'm going to rerun all the cells above, just to make sure that I

 executed all of them.

 And then I'm going to run the cell and we'll see what happens.

 And just so you know, the first time you run this, it is going to

 take a pretty good amount of time, even if you are using Haiku.

 It's going to end up taking me about 31 seconds to complete this with

 Haiku.

 I'm going to show you some techniques for speeding up our eval

 runtime.

 But right now, we're just going to have it take a little bit longer,

 but don't worry if we will speed it up.

 So now let's take a look at results and see what we have.

 Results is going to be a rather large JSON object.

 So I'm going to print it out really nicely with a print JSON dumps

 with results and an indent of two.

 There we go.

 So now we get an array of objects.

 Every object represents the output from one of our individual test

 cases.

 I've got the output right here. That's the output coming from Claude.

 And we can see there is a lot of stuff generated here.

 And if I scroll down a little bit, I'll see the definition of the

 test case that this was based upon.

 And then the score, which again right now is just hard coded at 10.

 And then that's just going to repeat over and over again.

 All right.

 So at this point in time, we have successfully gone through this step

 right here.

 We merged together our data set with our test prompt and we got some

 output from Claude and we kind of collated all this stuff together.

 So now the last thing we really have to do here is take the input and

 the result that we got out of Claude and feed it into one of these

 different graders.

 So this finally is the time where we're going to start to learn about

 graders.

 We're going to start to discuss them in the next video.

---

#### Lesson 19: Model based grading

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276738](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276738)

**Video:** 06 - 005 - Model Based Grading.mp4 | **Duration:** 10m 1s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next thing we're going to implement inside of our prompt

 evaluation workflow is a grading

 system. And as a reminder, a grader is going to take in some output

 coming from our model.

 And then our hope is that the grader is going to give us some kind

 of objective signal. It might

 be a number or a true or false value. It could be really anything,

 but very commonly, very frequently

 you're going to see a number output between one and 10, where 10

 means that we got a very high

 quality output. And one means we got a very low quality output. Again

, that's not a requirement.

 We don't have to get numbers out of these graders, but it's a very

 common practice you're going to

 see very often. There's three different kinds of graders that we're

 going to discuss in this video,

 code, model, and human. Let's first figure out what code base graders

 are all about.

 With a code base grader, we're going to take the output from our

 model and feed it into a

 snippet of code that you and I author. Inside this code, we can do

 just about any kind of

 programmatic check you can imagine. So we might verify to make sure

 that the output from the model

 was not too long or too short. We might make sure that the output

 does have or doesn't have certain

 words. If we are returning JSON or code, we can do syntax validation

 programmatically. And we can

 even do more complex checks like implement a readability score, where

 we make sure that the

 generated text is at an appropriate reading level for our particular

 use case. The only requirement

 here is that when we run this code, we return some kind of actual

 signal we can use. And again,

 usually that's going to be a number between one and 10, but that is

 not a hybrid requirement.

 The next kind of grader that you're going to see very often is a

 model based grader.

 This is where we take the output from our original model call, so the

 one that we already made,

 and we feed it into an additional model. So this is another API

 request. When we use a model

 grader, we get a tremendous amount of flexibility. We can ask a model

 to evaluate a response based

 upon its general quality, maybe how well it followed prompt

 instructions, maybe the completeness of

 the response, really just about anything you can imagine. Once again,

 the only real requirement

 here is that the model gives us back some kind of hard objective

 signal, usually as a number

 between one and 10. And then finally, human based grading. With human

 based grading, we're

 going to take all the outputs from our model and then put them in

 front of an actual person.

 This person is then going to be in charge of evaluating these

 responses in some particular way.

 As you can imagine, humans are very flexible, so we can ask them to

 evaluate responses in

 just about any fashion or for any metric you can possibly imagine.

 The one big downside to human based grading is that it generally does

 take a lot of time,

 and it's certainly very tedious work. Now, no matter what style of

 grading you are using,

 you need to decide up front what your evaluation criteria is going to

 be.

 So in other words, exactly what aspects of these responses are you

 going to be focusing on?

 For our particular use case, I've centered on three different

 evaluation criteria.

 I think first off, we should evaluate the responses to make sure that

 we're only getting back

 Python, JSON, or regular expression without any additional

 explanation being provided by Claude.

 Secondly, whenever we get that Python JSON or Reg Reg X, we should

 make sure that has some valid

 syntax so that there should be no typos in there or anything like

 that. And then finally,

 we should probably do some general task following and make sure that

 the model clearly address the

 user's task and answered it with some generally accurate code that

 doesn't contain any major

 errors or logic mistakes. So for these three different evaluation

 criteria,

 I think we can evaluate the first two with a code grader. So we can

 evaluate the format and

 make sure we got actual Python, JSON, or Reg X with code. And we can

 also validate the syntax

 of that code using, well, additional code. And then finally, the

 general response and making

 sure that the user's question was clearly addressed, that would be

 more appropriate to

 address through a model grader, given its flexibility. All right,

 let's start to implement

 first the model grader, because that's believe or not going to be

 the easiest one to put together.

 I'm going to first begin by going back over to my notebook.

 I'm going to find that to do we had put together right here inside of

 our run test case function.

 And then right above that cell, I'm going to add a new cell with a

 function that I'm going to call

 grade by model. And I'm going to assume that I'm going to pass in my

 test case dictionary.

 Remember, the test case dictionary is essentially these objects right

 here, each of these data set

 values, these are our test cases. I'm also going to pass in the

 output from our original model call.

 And then inside of here, we're going to essentially make a call off

 to a model and ask it to grade

 the output. So for this, we usually end up writing a fairly long

 prompt. And again, just to save

 us a little bit of time, I'm going to copy paste a prompt in. So here

 we go. I'm going to paste this

 in. And yes, it is a little bit long, but this is kind of the bare

 minimum of what we want.

 So this prompt is going to set a role. It's then going to ask very

 clearly for the model to evaluate

 a AI generated solution. We're then going to print out the task. We

 're then going to

 list out the solution that was generated by the model. And then we're

 going to provide some

 directions on exactly how to respond. In this particular case, I'm

 asking the model to give me

 a list of strengths and weaknesses of the AI generated solution,

 along with some reasoning

 behind that and an actual score. Now we could just ask for a score by

 itself. But if you do so,

 you're going to see very often you tend to get scores of just six. So

 if you don't ask for any

 additional strengths or weaknesses or reasoning, you're going to very

 often just get very middling

 scores because the model kind of assumes, well, could be better,

 could be worse, we'll give it a six.

 By asking the model to provide some reasoning, strengths and

 weaknesses, you really make it

 hone in and decide upon a more concrete score. So now we have that

 prompt in here. I'm going to

 call our additional grading model. So right underneath it, I'll again

 make a messages list.

 I'll add in a user message. And then because we are getting back some

 JSON here,

 we need to once again make sure we extract that cleanly by using a

 pre-filled assistant message

 and a stop sequence. So we'll add a assistant message with back ticks

 JSON. And then I'll get

 back some eval text. And we'll call chat with messages and a stop

 sequence or stop sequences

 of once again, closing back ticks. Now this eval text should be a

 JSON object with this kind of

 structure right here. So I'm going to parse that and just return it.

 So I'll return a JSON.loads

 with eval text. Okay, so that is our model grader. That's really all

 it takes to at least get started.

 So now we need to make sure we actually call this grader. To call

 the grader, I'll go down to our

 to do right here. I'm going to replace score with model grade. And

 that's going to be coming

 from our grade by model function. And remember, we have to pass in

 the test case along with the

 output from actually running the prompt. And then from this, we're

 going to get a score

 from model grade. And I'm also going to extract from that dictionary

 that gets returned

 the reasoning behind the score. Inside of this model grade dictionary

 that we are returning,

 there is also going to be the strengths and weaknesses list. You

 could definitely extract

 those as well as you want, but it's going to keep our example a

 little bit more concise.

 I'm going to take the score and reasoning and put them into this

 final output dictionary.

 So I will add in some additional keys here of score. Oh, I already

 have score right there. My

 mistakes. I don't need that. But I do need reasoning. And that will

 be reasoning.

 Okay, so that looks good. I'm now going to make sure I run these

 cells.

 It's going to run that one update run test case. And then I'm going

 to rerun my actual evaluation.

 That is going to take a while to complete. For me, it takes about 22

 seconds this time around.

 And now if I print out those results, let's see what we get. So I've

 now got the generated

 output here. And if I scroll down a little bit, I can take a look at

 the score that was

 generated by the model and some reasoning behind that score. So in

 this case, I got an eight and

 it's not bad. And that's why I got the eight. And if I keep going

 down, the next one got a seven.

 And then finally, I got a six. So last thing we would probably want

 to do here is take all these

 scores, add them together, get an average and print that out. So we

 get a final, very objective

 score to tell us how well our prompt is currently functioning. So to

 average all these scores out

 and print results, I

---

#### Lesson 20: Code based grading

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276735](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276735)

**Video:** 06 - 006 - Code Based Grading.mp4 | **Duration:** 7m 26s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Next up we need to implement our code grader.

 So our code grader is gonna take in some output

 from the model and make sure that we get back

 just plain Python, JSON or regular expression

 without any kind of explanation.

 In addition, we should also make sure

 that we have valid syntax for whatever type of code

 we actually got.

 You might be kind of curious,

 how are we going to validate the syntax

 of say, Python at all?

 Well, we use a little trick for this.

 We're going to define three helper functions.

 One would be called validate JSON, another validate Python,

 and another validate RegEx.

 Then inside of each of those,

 we're gonna take whatever output we got from the model

 and try to either parse it as JSON,

 we'll try to parse it as a Python abstract syntax tree

 or AST, or we'll try to compile it as a regular expression.

 And then for each of these,

 if we successfully parse or load or whatever else,

 we'll return a full score of 10.

 Otherwise, if we get an error during this parsing operation,

 we'll assume that we completely failed the syntax check

 and return a zero.

 There is one other thing to be aware of here.

 In order to know which of these different validators

 or these kind of grading functions to run,

 we need our test case data set

 to include the expected format

 that we're going to get back for each output.

 So in other words, back here inside of our data set,

 on our first task, for me at least,

 I was expecting to get back a Python function

 and then JSON and then a RegEx.

 So we need to update our data set

 to include something like a format key

 that will say, hey, this output should probably be Python.

 This one should be JSON and this one a RegEx.

 Now, of course, I could just edit this file manually,

 but instead we will update our prompt

 that is generating our data set

 so that we can eventually generate

 really large data sets for testing purposes.

 Now in total, to do all this stuff,

 couple of different steps we have to go through.

 So just to help you understand the code side of it

 and keep everything in line,

 I came up with this quick checklist

 of items that we're going to go through.

 So our first item,

 add in functions to validate JSON, Python,

 and regular expressions.

 For this, I'm going to flip back over to my notebook.

 I'm going to find the run test case cell.

 I'm going to add a new cell right above it.

 And then inside there,

 I'm going to add those three functions

 that you just saw inside that diagram.

 Once again, to save a little bit of time,

 I'm going to paste them in here.

 You can always copy the completed code

 out of the finished version of this notebook.

 So at the top of the cell,

 I'm importing these two helper modules.

 I've then got the three different validator functions

 that we just saw.

 And then at the bottom,

 I have kind of a general purpose function

 to figure out which these different validators to use.

 So I've got grades syntax right here.

 That's going to take a look at the test case.

 It's going to look at the format in particular.

 So we need to make sure our test cases

 have that format property

 that I just mentioned a moment ago.

 And then depending upon that,

 we're going to call the appropriate format function.

 Okay, that is step one.

 So step two, we need to update our data set

 to make sure we include that format key.

 So for that, we'll scroll up a little bit

 and find our data set.

 Here it is right here.

 So generate data set.

 And I'm going to add onto the example output.

 On task, I'm going to add a comma at the very end,

 and I'll add in a format key.

 And inside of here, we'll say simply JSON or Python.

 Or regex.

 That's really all we have to do.

 So now if I rerun that cell

 and rerun the cell underneath it,

 that actually generates the data set.

 There we go.

 Now I'll go back over to my data set file.

 And I'll see, yes,

 I did in fact get the format inside there.

 And it looks like it matches up with the task perfectly.

 So the first task is create a JSON configuration.

 Got JSON, write Python, got Python,

 and then write a regular expression, and I got regex.

 Okay, onto step number three.

 Now this, we're going to update our draft prompt template,

 just to make sure that it's really clear

 that we only want JSON, Python, or regular expression.

 'Cause right now our draft prompt just kind of says,

 "Yeah, try to solve the task."

 So inevitably, we're going to get back some non-JSON

 or non-Python content,

 and we'll always be failing the actual validation check.

 So we're just going to give our prompt a little help here,

 give it some work that we know that it needs.

 So for step three, we'll go back down to our run prompt,

 which is where our draft prompt is,

 and I'm going to update the prompt just a little bit.

 I'm going to add in some notes,

 and I'll ask it to respond only with Python, JSON,

 or a plain regex.

 And do not add any comments or commentary or explanation.

 Next up, I'm going to make sure that we get back

 just that raw content that we really care about.

 And once again, to do so,

 we'll use a pre-filled Assistant message

 along with a stop sequence.

 So I'll add in a Assistant message right here.

 In my Assistant message, in this case,

 I'm going to put in three back ticks,

 and then usually, as we saw previously,

 we might put in something like JSON, or Bash,

 or Python right here.

 But in this particular case,

 we don't really know ahead of time

 the exact format that we expect to get back.

 We don't know if we're going to get back Python,

 or JSON, or regex.

 So one little cheat code here, one will work around,

 we could just put in code,

 and that kind of pre-filled Assistant message

 and tells Claude, hey,

 you're going to put some code inside of here

 without us having to specifically say

 this is going to be Python, or JSON, or regex.

 I'm then going to add on the closing stop sequence

 with back ticks like so.

 Lastly, we need to actually merge the scores

 from our model grader and the code grader together.

 So for that, back over here,

 I'm going to scroll down once again,

 and we will find our run test case function.

 So this is where we are running our model grader.

 Right underneath it,

 I'm going to put together the syntax grader for code grader,

 whichever you want to call it.

 So I'll say my syntax score,

 it's grade syntax.

 We need to pass in the output and our test case.

 And then finally,

 we're going to merge the syntax score together

 with the model score.

 I'm going to first rename score right here

 to model score just to be clear.

 And I'm going to take the average of these two scores.

 So I'll say score is going to be model score plus syntax score

 divided by two.

 And that should be it.

 So that's all it took to add in a little bit of code grading.

 So last thing to do is test this all out.

 To do so, we'll go down just a little bit here.

 So right underneath the run eval function

 is where we actually call run eval

 and calculate our overall average score.

 So I'm going to rerun this

 and remember it usually takes a decent number of seconds

 to complete.

 And after a short pause, I get a final score of 8.166.

 So now the question is, is this good or not?

 Well, the real answer to that is that we just don't know.

 The only way we're going to know

 is if we now try to change our prompt in some way

 and hopefully get a better score.

 So let's try out an exercise in the next video

 where we will try to change our prompt a little bit

 and hopefully improve our score.

---

#### Lesson 21: Exercise on prompt evals

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276734](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276734)

**Video:** 06 - 007 - Exercise on Prompt Evals.mp4 | **Duration:** 4m 44s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's try out an exercise to improve our prompt evaluation workflow.

So here's the task I'm going to give you.

I want to improve our model grader a little bit by providing it with

more

context on what a good solution should actually look like.

Now, at first glance, that might sound a little bit challenging, but

it turns out

you only really have to go through two steps to add in this

additional context.

So in step one, I would encourage you to go back to the prompt where

we generate

our data set and inside that prompt, try asking it for some solution

criteria

to be included in every test case.

So ideally, our test cases that could output should now have some

additional

solution criteria key, which might look like what you see right here.

So it might say something about what a good solution would look like.

Maybe you say, well, a good solution would include this

characteristic

and this characteristic and this characteristic.

Once we have this additional solution criteria, we can then insert

that

into our grade by model prompt.

So you might find the existing area of that prompt where we put in

our

solution to evaluate and then right after it, you might add in that

newly

generated solution criteria.

And that's all it would really take to give our model grader, a

little bit

better idea of what a good solution would actually look like.

As usual, I would encourage you to pause the video right now and give

this exercise a shot.

Otherwise, we're going to go through a solution right now.

So the solution really is just going to be these two separate steps.

Should be pretty straightforward to get started.

Back inside my notebook, I'm going to find our generate data set

function.

And inside there, I'll find the really big prompt we put in.

And then when we ask for each of these different test cases, I'm

going to say,

in addition to a task and the output format, I also want to get some

solution

criteria and then I'll put in a string right here just to give our

model an

indication of what this key should actually be.

So I'm going to ask for some key criteria for evaluating the solution.

And that's pretty much it.

So I'm going to rerun the cell.

I'm going to go to the cell underneath it and regenerate the data set.

Okay, just a couple of seconds.

It should be done.

There we go.

So now we should have an updated data set dot JSON file.

I'm going to open that file up and I should now see some updated

tasks in here,

still with the format, but now I've also got some solution criteria.

So the solution criteria, we can read over.

Of course, yours is going to look different than mine, but it's going

to get

going to give some idea on again, what a good solution will actually

look like.

Next up is step number two, we're going to find our grade by model

function

and specifically the prompt inside there.

And we're going to include this newly generated solution criteria,

again,

just to tell the model grader, what a good solution looks like.

So for that, I will go back to the notebook.

I will scroll down and find that grade by model function.

Here it is right here.

So I'm going to find the prompt.

We are already putting in the original task, the output that was

generated.

And then right after that, I'm going to put in some note to the model

and just

say, here's some criteria that you should use to evaluate the

solution.

So criteria, you should use to evaluate the solution.

I'm going to put in some tags.

And I'll tell you why we were adding in these tags very shortly as we

start to

discuss prompt engineering.

And then I'm going to interpolate in from the test case, our solution

criteria.

And that key right there, remember, our test case is really these

objects, each

these objects, one by one, so we know because we see it right here

inside this

file, there is a key inside that dictionary of solution criteria.

So we're taking that sentence right there and putting it right here.

All right, so now time to run the cell.

And we're going to rerun our pipeline and see how everything is

working.

So I'll go down to the run eval function.

And then right after that is where we actually execute everything.

So I'm going to run that and then we get our updated score back.

Now I want to print out the results really quickly.

Just so we can see how this is going to affect the actual output.

So we'll do another print of JSON dumps results with an indent of two.

So now we can see the output from our model.

So that's the actual produced output.

Here's our test case.

So we can take a look at the task and the solution criteria.

Here's the score in this case, it was nine.

And now hopefully our reasoning section, which is produced by the

model

grader, is going to be a little bit more fleshed out than it was

before

because we are including that solution criteria.

---

#### Lesson 22: Quiz on prompt evaluations

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/289297](https://anthropic.skilljar.com/claude-in-amazon-bedrock/289297)

---

### Prompt engineering

#### Lesson 23: Prompt engineering

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276749](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276749)

**Video:** 07 - 001 - Prompt Engineering.mp4 | **Duration:** 10m 50s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that we've got a handle on prompt evaluation, we're going to move

 on to the world of prompt

 engineering. Remember, prompt engineering is all about taking a

 prompt we've written and

 improving it in some way to get more reliable outputs and higher

 quality outputs. To understand

 prompt engineering, we're going to go through a series of videos in

 this module. And I want to

 very quickly help you understand how the module is set up. In this

 video and the next, we're going

 to write out an initial prompt. And then in the coming videos, we're

 going to try to improve it

 step by step by implementing new prompt engineering techniques on

 that original prompt. So in short,

 in this video, we're going to set a goal. So something we want our

 prompt to do, we're then

 going to write an initial version of that prompt. So kind of like a

 really poor first attempt,

 we will then eval the prompt. And then we're going to see right away,

 we get a very poor

 evaluation score. And then as I mentioned in the coming videos, we're

 going to learn about and

 apply some different prompt engineering techniques. And as we apply

 each of these, we're going to

 run our evaluation again, and see that we are getting better

 performance with every single

 improvement we make. Now to run these emails, we're going to use that

 same kind of eval pipeline

 that we put together in the previous module. Just one little twist

 here, something you really

 need to be aware of if you want to follow along and code with me. I

 took our original eval pipeline

 we put together in the last module, and I made a couple of different

 improvements to it to make

 sure that it can work with just about any prompt, as opposed to the

 very specific prompt we were

 working on previously. So to get this updated notebook that has this

 more flexible evaluation

 pipeline, make sure you download the accompanying notebook named 001

 underscore prompting.

 Before you open up that notebook, however, I want to very quickly

 tell you about the goal of our

 prompt. So this initial prompt that we're going to write and exactly

 what it is intended to do.

 All right, so we're going to make a prompt that's going to hopefully

 generate a one day meal plan

 for an athlete based upon their height, weight, some kind of physical

 goal that they might have,

 and any dietary restrictions they might have. So you can imagine that

 we are going to take in

 some kind of sample input that describes an athlete, maybe their

 height, weight, goal,

 and dietary restrictions. We're then going to interpolate all those

 inputs into our prompt,

 and then we're going to send that off to our model, and hopefully we

'll get back some kind of output,

 like what you see on the right hand side. This is what we're really

 going for. This is our ideal

 output. In the first version of our prompt, we're going to get some

 output that looks nothing like

 what you see here on the right hand side, but through a variety of

 different prompt

 engineering techniques, we're going to eventually refine the prompt

 and eventually hopefully get

 something that looks almost exactly like this. All right, so now that

 we understand our goal,

 let's open up that new notebook. So remember 001 prompting, I can

 give you a very quick tour of

 it because there are a couple of things have changed compared to the

 last module, and just

 make sure everything inside there is super clear. We'll then use the

 notebook to generate our initial

 data set. All right, so I've opened up that notebook. Right away, you

'll notice there are a couple of

 collapsed cells at the top. So this is a lot of different setup code.

 Just make sure you execute

 those cells at least one time. So I can do so right away. Next up,

 you'll see that I'm creating

 an instance of something called a prompt evaluator. Prompt evaluator

 is a class I created that wraps

 up all the data set generation, all the model grading, just about

 everything is wrapped up inside

 of this class. The class takes one argument, max concurrent tasks. So

 this class supports concurrency,

 we can make multiple API calls at the same time. The upside to this

 is that it's going to dramatically

 speed up our eval process and the data set generation process as well

. But I do need you to be aware

 that depending upon your service quota, you may or may not very

 quickly start to run into some

 rate limit errors. So if you see any rate limit errors at all, as you

 go through this module,

 I would highly encourage you to change this value right here all the

 way down to the default of

 one, which means no concurrency at all. For me personally, I have

 super high rate limits. So I'm

 going to dial this all the way up to a concurrency of 50. Chances are

 you are not going to be able

 to use 50. So don't try 50. I would really recommend maybe starting

 off at three. And then if you

 see any rate limit errors, start to go down to two or one. Again, I'm

 going to use 50 just so you

 can see some immediate feedback on my screen as I run all these

 different steps. I'm going to make

 sure I run that cell. And then let's get started on generating our

 actual data set. So to generate

 the data set, I've added this new generate data set method for us. To

 use this method,

 we're going to describe the overall purpose of our prompt. So kind of

 what our prompt is supposed

 to do. For you and I, we're trying to work on a prompt that is going

 to write a compact, concise,

 one day meal plan for a single athlete. And then inside of this

 prompt input spec, we're going to

 have a dictionary that's going to list out all the different inputs

 that our prompt requires.

 As we saw just a moment ago, our prompt is going to require a height,

 a weight, a goal, and some

 dietary restrictions. So these are some extra properties that are

 being generated as a part of

 the data set. And eventually, we're going to take them test case by

 test case and interpolate them

 into our prompt. So I'm going to fill out all four of these different

 properties. My height is going

 to be the height in cm. And just be clear, I'll put in athletes

 height. And I'm going to duplicate

 that because it's going to be just about the same, we're going to do

 our weight in kilograms.

 My goal is going to be the goal of the athlete. And my restrictions

 will be a dietary

 restrictions of the athlete.

 And the last input for you to be aware of is number of test cases to

 generate. I would really

 recommend that you just leave this at three, because it's going to

 allow you to get through

 this module way faster, because the emails are going to run much more

 quickly. Just remember,

 as I mentioned, many times whenever we do an eval in reality, we want

 to have a really solid,

 really large number of test cases. So I'm going to dial mine

 personally way up. I do not recommend

 you do this. I recommend you leave it at like two or three, just to

 make sure all your emails run

 very quickly. But again, I'm going to dial mine all the way up to 50.

 Once I put this all together,

 I'm going to run the cell, and that's going to generate my data set.

 Once I have generated

 my data set, I can open up the data set dot JSON file, which should

 be created in the same directory.

 And we're going to see all these different individual data sets have

 been generated. So

 they have a pretty similar structure to what we were doing on our

 previous module, when we were

 talking about prompt emails, I'm going to go back over to my notebook

, and then scroll down a little

 bit to the run prompt function. This is where we are going to write

 out our prompt, and then

 eventually improve it over time. This function gets called one time

 for every test case that

 you generated. Whenever this function is called, it's going to

 receive your test cases prompt

 inputs as its only argument. So in other words, prompt inputs right

 there is going to be that

 dictionary. And then that function is going to be called again, and

 it will be that dictionary,

 and then again, and it will be that dictionary and so on. So we're

 going to take this dictionary,

 and we're going to interpolate those inputs into this prompt that we

're going to write out right

 here. Let's immediately write out a first version of our prompt. And

 it's going to be very simple,

 very naive. We're going to get a very bad eval score, but it will at

 least get us started.

 So I'm going to write in my initial starting prompt here. And I'm

 going to use a very bad

 prompt. I'll say, what should this person eat? And then I'm going to

 list out their height,

 their weight, their goal, and dietary restrictions. And then for each

 of these, I'm going to interpolate

 in a value from prompt inputs. So the first one will be the height.

 And I'm going to copy paste that

 just to save a little bit of time and update the keys on each one. So

 make sure you have first

 height. And then we want the weight, and then our goal. And then

 restrictions.

 All right, once we have our starter prompt in here, I'm going to run

 that cell.

 And then let's do our eval. So we can run our eval down here at the

 very bottom. Now,

 before we run our eval, I want to know that this function that's

 going to actually kick off the

 evaluation process, it takes in one additional keyword argument that

 I'm not showing here.

 It's called extra criteria. It's going to be a string.

---

#### Lesson 24: Being clear and direct

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276743](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276743)

**Video:** 07 - 002 - Being Clear and Direct.mp4 | **Duration:** 2m 5s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

With a starting grade of 2.32, we can definitely only go up.

 So with that in mind, let's take a look at our first prompt

 engineering technique that we're

 going to use to improve our prompt. All right, so we're going to be

 discussing the idea of being

 clear and direct. These two rules are really talking about the very

 first line of your prompt.

 The first line of your prompt tends to be the most important. In that

 first line,

 you want to use simple and direct language and tell Claude, with a

 kind of action verb,

 exactly what its task is. So for example, we might want to have a

 first line of a prompt be

 something like write three paragraphs about how solar panels work.

 That tells Claude that it's

 going to have a job and needs to write or generate or create

 something. It also clarifies a little

 bit of information about the expected output and exactly what that

 output should contain.

 So we're really setting an action and providing a task in that very

 first line.

 Another great example would be identify three countries that use ge-

 othermal energy and for each

 include generation stats. Again, we are telling Claude to do

 something or giving it an immediate

 task and a little bit of information about the expected output. Let's

 take this idea of being

 clear and direct in the very first line of our prompt and see if we

 can't use it to improve the

 outcomes of our prompt that we're currently working on. Using that

 rule that we just learned,

 I might update this line to say something like generate a one day

 meal plan for an athlete

 that meets their dietary restrictions. So again, I'm being direct by

 making use of

 a action verb at the very start and then in very simple language, I'm

 providing a direct task for

 Claude to fulfill. Now, let's rerun the cell to get our updated

 prompt and then rerun the eval

 itself and see if this does anything to improve our score. And I bet

 as you can guess, yeah, we're

 probably going to do a little bit better than we did previously. So I

 think before I had a 2.32.

 Now I'm up to a 3.92, definitely an improvement, but still not great.

 So let's move on to the next

 video and take a look at our next prompt engineering topic in order

 to improve our prompt a little bit

---

#### Lesson 25: Being specific

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276745](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276745)

**Video:** 07 - 003 - Being Specific.mp4 | **Duration:** 5m 14s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next topic we're going to discuss in the world of prompt

engineering is the idea of being specific.

To be specific, we want our prompts to list out some sort of

guidelines or steps to somehow direct our model in a particular

direction.

For example, consider the prompt I have on the left-hand side of the

screen.

In this prompt, I'm asking Claude to write out a short story about a

character who discovers a hidden talent.

If I just put that prompt by itself into Claude, Claude can go any of

an infinite number of directions.

It can decide to vary the story length significantly. It can decide

to add in extra elements or remove elements from the story.

It might have just one character. It might introduce five different

characters.

If I want to ensure that I'm going to get a particular kind of output

, I might decide to put in a list of guidelines, as you see on the

right-hand side.

These guidelines will provide some high-level guidance or kind of

direct Claude in a specific way when it starts generating the

response.

So for example, I might decide to add in some guidelines of keeping

the story under a thousand words, add in some rising actions, and

including at least one supporting character.

Now I've provided a little bit of guidance to direct Claude towards

writing a particular kind of short story.

Now, there are two kinds of guidelines you're going to see very often

in prompts.

Type A on the left-hand side, it's kind of like what I just showed

you in the previous diagram.

You might decide to put in a list of guidelines and those are going

to list out some qualities that you want your output to have.

So you might try to control maybe the length of the output or the

structure of the output or maybe list out some different attributes

that the output should have.

On the right-hand side, the second type of guidelines that we can

provide are to provide some actual steps that the model should follow

, with the intent of making the model think about specific things or

choose between different directions that would hopefully increase the

quality of our output.

So for example, we might instruct Claude to maybe first brainstorm

three special talents that would be really interesting and then pick

the most interesting one.

We might then ask Claude to try to outline or think about some kind

of interesting scene that would reveal that talent and then think

about different kinds of supporting characters that could make the

story a little bit more interesting.

So on the left-hand side, we're really guiding attributes in the

output. On the right-hand side, we're trying to be a little bit more

specific in how Claude arrives at the final product.

You can absolutely, and you're going to see this very often in

professional prompts, you'll absolutely very often see these two

techniques mixed together.

So you might have a list of guidelines that intend to control some

attributes of the output and then a list of steps that the model

should follow as well.

Both of these are examples of being specific in your prompting.

So now we've seen some idea around what it means to be specific. Let

's go back over to our prompt in progress and see if we can

incorporate this idea of being specific.

All right, so back over here, I'm taking a look at my run prompt

function.

Now just to save a little bit of time, I'm going to first paste in a

list of guidelines.

So this is kind of like that first type of being specific, where I

include a list of attributes that I really want to see inside of the

output.

I'm going to run that cell and then go down and run the eval again.

And let's see what we get here. So after a quick pause, I'm going to

get back a final score of 7.86.

That is an incredible improvement over our previous 3.92, just by

adding in a little bit of guidance and telling Claude precisely what

things we want to see inside of the output.

Now I'm going to try to put in a little variant of this, where I use

that second variation of being specific.

So I'm going to provide some steps that Claude should follow when

deciding exactly how to build up this meal plan.

So now in this scenario, I'm telling Claude to first do a calculation

and then think about this and then do a bit of planning.

You kind of get the idea. I'm providing some steps that Claude should

go through.

I'm going to run the cell again and then run down here and I'm going

to remember that score of 7.86. That is really, really high, might be

a little bit of a statistical anomaly.

And now we get 7.3. So still a dramatic improvement, but not quite as

good as listing out some attributes that we'd want to see inside the

output.

So for me, I'm going to revert and go back to listing out some

guidelines.

So when would you want to use one technique versus the other?

Well, I would generally recommend almost always listing out qualities

that the output should have, as I'm showing on the left hand side, on

just about any prompt you ever work on.

And you will usually want to provide steps that the model should

follow, as shown on the right hand side. Anytime you're asking Claude

to work on a more complex problem where you want to kind of force

Claude to consider a wider view or some extra topics beyond what it

naturally might want to consider.

For example, consider the prompt on the right hand side of the screen

where I ask Claude to figure out why a sales team's numbers have

dropped in the last quarter.

In this scenario, we might want to force Claude to consider some

extra viewpoints or extra pieces of data that it might not otherwise

immediately consider.

All right, so now that we've got a better idea of what it really

means to be specific and this idea of adding guidelines or steps as

the situation warrants,

let's take another break right here and then move on to our next

prompt engineering topic in just a moment.

---

#### Lesson 26: Structure with XML tags

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276744](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276744)

**Video:** 07 - 004 - Structure with XML Tags.mp4 | **Duration:** 4m 0s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next topic we are going to examine is the idea of providing

 structure in your prompt

 by using XML tags.

 Now, let me give you a little bit of backstory on this.

 Very often, whenever we write out a prompt, we're going to interpol

ate some amount of

 content into it, and we've been doing that already.

 Inside of our example, we have been interpolating some height, weight

, goal, and restrictions.

 Now, each of these values are rather small, but it's entirely

 possible that we might

 eventually write a prompt where we need to put in a lot of content

 into a prompt.

 For example, examine the prompt on the right hand side.

 We might decide to paste in 20 pages of sales records and try to get

 Claude to analyze

 them in some way.

 Whenever we dump a lot of content into a prompt, it can be a little

 bit challenging for Claude

 to figure out exactly what text really means what or how text is

 actually grouped together.

 One way that we can make the structure of our prompt a little bit

 more obvious is by

 wrapping different pieces of content in XML tags.

 For example, I might provide a little bit more structure to this

 prompt on the right by wrapping

 the sales records right here with an XML tag of sales records, like

 so.

 Now there is no official XML tag called specifically sales records.

 This is a name of a tag that I just made up that will probably give

 Claude a little bit

 of insight into the nature of the content that exists inside these

 tags.

 I could have just as well called this records or perhaps even data.

 But of course, being a little bit more specific here is definitely

 better.

 So providing a tag of something like sales records would probably get

 us the best output.

 I want to make sure it's really clear why XML tags like this are

 necessary.

 So let me show you a little exaggerated example.

 In the prompt on the left hand side, I have a leading line of debug

 my code below using

 the provided documentation.

 So this kind of implies two things.

 It implies that underneath this header statement right here, I have

 some amount of code that

 was written by me that is buggy and some amount of documentation as

 well.

 And if you just look at the code that's listed out here, it's

 absolutely not very clear what

 content is the code and what content is the actual documentation.

 One way that we could clarify this to Claude would be to wrap each

 chunk of code with appropriate

 XML tags.

 For example, on the right hand side, I might wrap my code with some

 XML tags that simply

 say my code being very direct and obvious, and then the code that

 represents some amount

 of documentation in a docs tag, again, being very clear and obvious.

 Now it is much easier for Claude to understand what code it is trying

 to debug and which

 code provides some source of documentation.

 Let's take this idea of providing structure via XML tags and try to

 use it to improve

 our prompt that we are working on back inside of our notebook.

 Now unfortunately in this particular scenario, we don't really have a

 big blob of content

 that we really need to delineate in any way.

 All of our interpolated content, like the height, weight, goal, and

 restrictions are sufficiently

 short that Claude is probably not going to be confused by them in any

 way.

 Regardless, we can still use some XML tags to make it really clear

 that this is some kind

 of external input or maybe some information about the athlete that

 should be considered

 when generating the meal plan.

 So we might decide to wrap this entire block right here with some XML

 tags that just make

 it really clear that this is information about the athlete.

 So I might put in tags like athlete information and then a closing

 tag on the other side.

 Now let's try to measure and see whether or not this has any kind of

 impact on the quality

 of output.

 So I'm going to rerun the cell, I'll go down to my eval cell and run

 this one, and then

 you might recall that before adding in those XML tags, I had a score

 of 7.3.

 So let's see if we go up or down.

 And I end up going up quite a bit.

 Now you probably are not going to see an improvement quite this large

.

 As a reminder, I'm using a little bit more simple and basic model

 just so I get some exaggerated

 returns in these improvements to the prompt.

 So if you do not see quite a big a jump in quality, that is totally

 fine.

---

#### Lesson 27: Providing examples

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276747](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276747)

**Video:** 07 - 005 - Providing Examples.mp4 | **Duration:** 6m 44s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

I'm really excited about this next prompt engineering technique we're

 going to discuss

 because it is probably one of the most effective that you're going to

 find.

 It's the idea of providing examples inside of your prompt.

 This is often referred to as one-shot or multi-shot prompting,

 depending upon whether or not you

 are providing just one example or multiple examples.

 Understanding this concept is definitely easiest if you take a look

 at an example, so let's

 do that right away.

 Consider the prompt on the right-hand side.

 I'm asking Claude to categorize the sentiment of a tweet.

 Let's be clear.

 When we say sentiment, we mean kind of does this tweet seem kind of

 happy or positive in

 nature or unhappy or negative.

 In this particular instance, I provided a input tweet of, "Yeah, sure

.

 That was the best movie I've ever seen since Plan 9 from outer space

."

 Now if you're not aware, Plan 9 from outer space is a famously bad

 movie.

 So if someone were to tweet something like this, they're actually

 probably being sarcastic

 and they probably did not like the movie they just watched at all.

 So we would probably want to classify the tweet as being negative,

 but Claude could potentially

 have some issue categorizing this.

 One way to solve the problem would be by using multi-shot prompting.

 So here's how we would fix this.

 We would take our starting prompt we have on the left-hand side and

 add in some examples,

 which I've added in on the bottom half of the prompt right here.

 To add in an example, we will very directly tell Claude that we are

 about to give it some

 example input and an ideal perfect world kind of response.

 So almost always wrap these inputs and outputs inside of some XML

 tags just to better structure

 our prompt and make it super clear to Claude what the purpose of the

 input and output are.

 So in this particular example, I have given a sample input of great

 game tonight, which

 I would say is definitely positive in nature.

 So right after that, I would then put in an ideal output of simply

 positive.

 This gives Claude a concrete objective example of how to deal with

 some kind of input.

 Now Claude knows that if it ever sees some kind of input like this

 again in the future,

 well, it should probably label it as positive, because that's how it

 was done in the past.

 We can make use of multi-shot prompting, that's where we provide

 multiple different examples

 whenever we want to handle corner cases.

 And dealing with sarcastic tweets like this is definitely a corner

 case that we kind of

 want to highlight to Claude.

 When adding examples that highlight corner cases, add in some context

 to Claude and tell

 it that it should be especially aware of certain scenarios.

 So for example, we might say be especially careful with tweets that

 contain some sarcasm

 and then provide an immediate example of that.

 So now in this case, I've got a example tweet or a sample input of,

 oh, yeah, I really needed

 a flight delayed tonight.

 Excellent.

 If you didn't understand the concept of sarcasm, this would seem like

 a positive sentiment

 tweet.

 But of course, we can probably understand that this is sarcasm.

 And so probably is actually negative.

 Once again, Claude can take a look at this example when grading our

 provided input up

 here, the original input.

 And Claude will have a better chance of recognizing that, oh, yeah,

 this looks like it's sarcasm

 too.

 This is also probably negative in nature.

 Now multi-shot prompting like this can be used not only for capturing

 corner cases or giving

 a little bit more clarity to Claude, but also helping Claude

 understand more complex

 output formats.

 So if you ever need to generate a JSON object that is rather complex

 in nature, you might

 provide a sample input and an example output and show that kind of

 complex JSON structure

 to Claude.

 And now it will have a better idea of the exact structure of output

 that it is going

 for providing examples is especially effective whenever you are doing

 prompt evals as we

 currently are.

 Remember, whenever you run a prompt develop using our little

 framework inside the notebook,

 it creates an HTML file inside the same directory.

 So we can hunt through this file until we find a perfect 10 or

 hopefully just a test case

 with a rather high score.

 If I scroll through, I will find a 10 right here.

 Now you might not have any tens inside of your output.

 If you don't, that's totally fine.

 Just try to find the record with the highest score.

 So this is an example of where we had some input and output that was

 gauged to be pretty

 much as good as we're going to get by our model greater.

 So we might decide to provide this as an example inside of our prompt

.

 And hopefully that will guide Claude to producing output that looks

 like this a little

 bit more often.

 So let's try this out.

 I'm going to copy this input right here, go back over to my prompt, I

'm going to scroll

 underneath the guidelines section and I'm going to explicitly tell

 Claude that I'm about

 to provide an example that's going to contain a sample input and an

 ideal output.

 So I'll say here is a or an example with a sample input and an ideal

 output.

 I'll then put in my sample input inside of XML tags and a ideal

 output.

 And inside those tags, I'm going to go back over and copy paste the

 output from right

 here.

 I'll then paste it in like so and fix some indentation.

 Before we rerun our eval, there's one last thing I want to show you.

 This last step is completely optional, but I personally have had

 great success with it.

 It's often very beneficial to help Claude understand exactly why this

 is ideal output.

 If we go back over to our report, remember, we have this last column

 over here that explains

 exactly why the greater thought that this was some ideal output.

 So we can copy just the kind of first half of some message over here,

 where it says or

 lists out why this is a good response.

 Take that back over and then underneath the closing ideal output tag,

 we could paste in

 that reasoning and then maybe update the grammar just a little bit to

 say, this example meal

 plan is well-structured, blah, blah.

 So now Claude has a better idea of exactly why this is considered to

 be ideal output.

 And it's going to better reinforce the idea that Claude needs to

 return a well-structured

 output that contains some detailed information on the food choices

 and quantities and most

 importantly, matches the athlete's goals and restrictions.

 Okay, so let's now run that cell and then rerun our eval and see how

 we are doing.

 So I'm going to rerun this and are we going to go up or down?

 We end up going up just a little bit to 7.96.

 Well, let's wrap things up.

 As a reminder, this technique is often referred to as one-shot or

 multi-shot prompting.

 One-shot is where you provide a single example, multi-shot is where

 you provide multiple examples.

 And this is a technique you're going to very often use anytime you

 want to make sure Claude

 handles corner cases or especially when you want Claude to make sure

 it matches some kind

 of complex output format.

---

#### Lesson 28: Exercise on prompting

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276746](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276746)

**Video:** 07 - 006 - Exercise on Prompting.mp4 | **Duration:** 5m 22s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's test your knowledge of prompt engineering by going through a

 quick exercise now for this exercise

 I made a new notebook called zero zero three underscore exercise

 You do not have to download this one all I did was replace the task

 description the prompt input spec and

 Then I just did some of the extra criteria down here

 so if you want to you could manually change all the stuff in the

 notebook you're working out of or

 I'll generally just download this zero zero three exercise and get

 caught up with exactly where I am

 Your goal in this exercise is to improve an existing prompt using all

 the prompt engineering topics

 We've learned about inside this module the data set you're going to

 be working with is going to create a series of

 passages of text from a scholarly article

 The goal of your prompt is to take in that passage of text and

 extract all the topics from it into a JSON array of strings

 And when I say topic, I really just mean well

 What does this article talk about so if it's our article about say

 solar panels?

 I would want to get back a JSON ray strings that contains solar

 panels inside of it only with any other topics mentioned inside that

 text

 The only input to the prompt is going to be a content property. So

 that's going to be one paragraph of text

 Now in my notebook that I've opened right now

 I have already executed the cell and generated a data set I have

 already put together a

 Starter prompt for you and right now, it's a very poor prompt that

 can definitely be improved quite a bit

 So go ahead and play around with this prompt and use some of the

 different techniques

 We have learned about in order to evaluate your progress go ahead and

 run the cell down here

 I've already included a couple of extra criteria to make sure that

 you're kind of achieving the correct result

 Remember whenever you run the evaluation you can always open up that

 report.html file and get a better understanding of what's going on

 By default with that really simple prompt. I've got a average score

 of 2.8

 And so I'm hoping we can at least get that average score over maybe

 seven or so as

 Usual I would encourage you to pause the video right here and go

 ahead and give this exercise a shot

 Otherwise if you want to stick around I'm going to go over a solution

 right away

 Alright, so to solve this we know without a doubt all the work we're

 going to be doing is focused on this variable right here

 We need to improve this prompt in some way to get back some better

 output

 The first thing we might do here is make sure you run the evaluation

 at least one time to generate that output.html file

 And then once you have created that file

 I would encourage you to open it up and take a look at some of the

 reasoning on why the output has been graded so poorly

 You'll notice a common theme between each of these a real common

 theme right away that we can see is that well

 It doesn't like the fact that we are not returning a JSON array of

 strings

 To solve this problem

 Let's make use of that technique of being simple and direct inside of

 our prompt

 If we expect to get back a JSON array of strings that contains all

 the topics out of this content

 Well, we need to be very simple and direct with Claude and tell it

 exactly what we want

 So I'm going to update the first line of the prompt right here

 And I'll say extract key topics mentioned from a passage of text from

 a scholarly

 Journal into a JSON array of strings

 as simple as I can phrase it and as direct as I can possibly make it

 and right away if I rerun the prompt with the evaluation

 I will see that I get up to a kind of shocking 9.5 almost immediately

 So I kind of didn't really expect it to go that well because there

 are still some other techniques

 We might want to try out here

 But if we take a look at the report now, I'm definitely getting back

 this JSON

 containing all the different topics mentioned and it looks like the

 model grader is extremely happy with this output

 Now, I don't really want to leave it here

 So obviously there are some other techniques we can add in to make

 sure that we get the correct kind of output

 So the next technique we might add in is structuring our prompt a

 little bit better by using some XML tags

 Before and after the content that we're going to interpolate in right

 here

 I'm going to add in some XML tags and I'm going to give them the name

 of simply text

 Now in this case

 I'm choosing to call these tags text because I earlier referred to

 some text inside of the first line of the prompt

 So now we have just a little bit more clear connection between us

 talking about a passage of text right here and us providing the text

 right here

 Another improvement that we might add in is to be very specific in

 what we want Claude to do

 So I could put in a series of steps for Claude to follow. Let's try

 that out

 I might say follow these steps and then list out exactly what I want

 Claude to do step by step

 so we might say

 closely examine the

 provided text

 Identify each topic mentioned

 add each topic to a JSON array and then finally respond with the JSON

 array

 Do not provide any other text or commentary

 Now if you wanted to also add in an example using one shot or multi

 shot prompting

 Absolutely feel free to do so, but we already have some pretty good

 scores

 So I think this is probably enough. I'm going to rerun this prompt

 I'll then run the evaluation again and I end up getting a 9.5 again

 So I would say this is a pretty strong prompt and I would definitely

 trust it to extract a list of topics from an article

---

#### Lesson 29: Quiz on prompt engineering

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/289298](https://anthropic.skilljar.com/claude-in-amazon-bedrock/289298)

---

### Tool use

#### Lesson 30: Introducing tool use

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276756](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276756)

**Video:** 08 - 001 - Introducing Tool Use.mp4 | **Duration:** 4m 14s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this module we are going to discuss tool use. Tools allow Claude

 to access information from the outside world.

 Understanding tool use can be a little bit challenging, so in this

 video I'm going to give you a really soft introduction.

 We are going to walk through the entire flow of tool use and

 understand what it's all about.

 I want to first begin by giving you an example of where Claude can,

 unfortunately, sometimes hit its limits.

 Remember, by default Claude only has access to information that was

 actually trained on.

 So, in general, it doesn't really have any information about very

 recent current events.

 As an example of this, if we had a user making use of our chatbot,

 ask a question of something like,

 "What's the weather in San Francisco, California right now?" and sent

 that off to Claude,

 we would probably get a response back of something like, "I'm sorry,

 but I don't have access to up-to-date weather information like that."

 To fix this and give the user a better response, we can make use of

 tools.

 Let me show you a diagram that's going to break down tools with

 really simple terminology.

 And then I'll show you another one that's going to give you an

 example of how we would solve this specific weather problem.

 Okay, so here's the entire flow that we're going to eventually

 implement when we start to make use of tools.

 We're going to send off an initial request to Claude.

 We're going to ask a question or maybe give Claude a task.

 And along with that, we're going to include instructions on how

 Claude can get some extra data from the outside world.

 Claude will then take a look at whatever question it was asked or

 whatever task it was given,

 and it might decide that it needs to ask for some extra data.

 So it'll send a response back to us where it asks for some extra data

 and it's going to give us some details on exactly what information it

 needs.

 Then on our server, we are going to run a little bit of code that

 will go and get the information that Claude asked for,

 and then respond with that on a follow-up request back to Claude.

 Now Claude has all the information it needs, in theory, to give us a

 response.

 So it will generate a final response that will be hopefully augmented

 or improved by that extra data.

 Now I'm going to show you the same exact flow, but I'm going to

 customize each of these little steps for this scenario

 where a user asks us for some current weather in a particular

 location.

 So here's what happened.

 We would send an initial query off to Claude, and it would include a

 prompt where the user asks about the weather.

 And inside of that initial request, we're going to include details on

 specifically how to retrieve current weather data.

 Claude would take a look at the prompt and decide, "Hey, to answer

 this question, I need to get some current weather data."

 It sends a response back to us where we would then run some code that

 would reach out to some maybe third-party weather API

 and actually get some live details on what the current weather is for

 a particular location.

 Once we have those details from that outside API, we would then make

 a follow-up request to Claude with that current weather data.

 And now Claude has all the information it needs. It has the original

 prompt along with the up-to-date weather data

 so it can generate a final response and send it back to us.

 Now, this entire process seems really simple. That's fantastic. And

 if it seems really confusing, that's totally fine as well.

 As I mentioned earlier, understanding tool use can be a little bit

 challenging.

 And I think one of the reasons for that is that there's a really big

 disconnect between the order in which things actually occur,

 so like this diagram you see right here, and the actual code that we

 write to implement this process.

 You see, each of these different steps needs to be implemented with

 some actual code that you and I write.

 And it turns out that the way we actually often structure our code

 inside of real projects doesn't quite match this flow.

 So we end up kind of jumping all over the place. We very often start

 off by first writing a tool function

 and then we go up to writing out the JSON schema spec, and then we

 might actually handle the actual tool use part in a tool result,

 and then actually go back and make sure that we include the original

 JSON schema spec with request.

 So very often we end up jumping all around as we implement this stuff

, and that tends to be a big reason on why this ends up being

 complicated.

 So in the coming videos, when we start to implement tool use

 ourselves in a Jupyter notebook,

 I'm going to do my best to come back to this diagram rather

 frequently and make sure it's really clear what piece of the puzzle

 we are currently implementing. All right, so with that in mind, let's

 come back in the next video

 and we're going to start to implement our own tool use pipeline.

---

#### Lesson 31: Tool functions

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276757](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276757)

**Video:** 08 - 002 - Tool Functions.mp4 | **Duration:** 5m 48s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

To learn more about tools, we are going to set ourselves a little

 goal.

 This is going to be a small project that we implement inside of a Jup

yter Notebook.

 We are going to try to teach Claude how to set reminders that occur

 at some point in time in the future.

 This is going to require us to implement several different tools.

 And for right now, we're just going to focus on one tool at a time,

 but just know that we're going to eventually have to deal with

 multiple tools.

 So I want to eventually be able to send a message to Claude of

 something like

 "set a reminder for my doctor's appointment, it's a week from

 Thursday."

 And I want Claude to respond to something like,

 "Okay, I will remind you at that point in time."

 When you first look at this task, you might think it seems really

 easy,

 but it turns out that there are actually several different challenges

 that we're going to need to tackle, and we're going to solve all of

 them through the use of tools.

 So in particular, Claude does know the current date.

 In other words, if you open up a prompt right now, you could ask it

 what the current date is,

 and it will give you an exactly correct answer.

 However, Claude doesn't always know the exact time of day.

 So if we were to ask Claude to do something like,

 "set a reminder for 24 hours from now, expecting it to be exactly 24

 hours,"

 Claude doesn't really know what 24 hours from now actually is because

 it doesn't know the current time.

 Secondly, Claude does not always perfectly handle time-based addition

.

 So if I were to ask it, what is 379 days from January 13th, 1973,

 Claude will very often give you the correct answer, but sometimes it

 will get that addition incorrect.

 And finally, Claude just doesn't know what it means to set a reminder

.

 It has no concept of it.

 It does know conceptually what setting a reminder is,

 but there's no mechanism inside of Claude whatsoever for setting

 reminders in the future.

 To solve each of these issues, we are going to make a dedicated tool.

 So we have three issues right here.

 We are going to make three separate tools, one at a time.

 Here's what each tool is going to do.

 We're going to have a very simple tool that we're going to get

 started with.

 Its only job is to get the current date time.

 So that means the current date plus the time.

 The second tool we will make will add a duration to a date time.

 So this will allow us to say something like,

 take the current date and add 20 days to it and what would the

 resulting day be.

 And then finally, we will make a reminder setting tool as well.

 And then finally, we will make a reminder setting tool as well.

 The first tool that we are going to create and test is the get

 current date time tool.

 There are several different steps that go into making one of these

 tools

 and I've listed them all out at the very top of this diagram.

 So one step one right now, writing out a tool function.

 If we go back over to this diagram we had looked at previously.

 We are currently in this step over here where we are going to write

 out a function

 that will eventually be called on our server at some point in time.

 So for these tool functions, we're going to write out a plain Python

 function

 and it will be called automatically at some point in time.

 There are several best practices around these functions

 that we will go into very shortly.

 But for right now, let's go over to our Jupyter notebook

 and get started on this get current date time function.

 And again, it's going to be really easy for us to put together.

 All right, so back over here.

 I am inside of a new notebook and I've called it 001 tools.

 It has a lot of very familiar code.

 I would really recommend you download this copy or that kind of the

 starter version

 of this notebook regardless because I have added in a rather long

 function down here

 just to save us a whole lot of time.

 It's called add duration to date.

 This is going to be one of our critical functions later on.

 But as you can see, it has a lot of code for it.

 So I did not want you to have to write it all out yourself.

 So make sure you download this kind of starter version of the

 notebook.

 I'm going to add in a new cell and we are going to immediately start

 to implement our tool function.

 So this is a function that will be called automatically at some point

 in time.

 I'm going to call it get current date time.

 I'm going to take in an argument of date format

 and I will give this a default value of percent capital Y percent

 lowercase M percent D.

 And then just a little bit more percent capital H percent capital M

 percent capital S.

 Then inside of here, I'm going to return date time dot now SDRF time.

 And I will put in that date format string.

 I'm then going to test this out very quickly by calling it current

 date time.

 And sure enough, there we go.

 There is my date time.

 Whenever we write out these tool functions, there are a couple of

 best practices.

 I really recommend you follow first off and by far the most important

.

 I really recommend you use well named and descriptive arguments.

 You're going to see later on that this step is really important.

 Secondly, if possible, validate the inputs that are passed into the

 function

 and raise an error if they fail validation.

 So in the case of this get weather example on the right hand side,

 if we get a empty location, so just an empty string,

 well, that's probably a mistake.

 We can't really get weather for a unknown location.

 So we might want to immediately raise an error and just say,

 sorry, but the location can't be empty in our particular case

 with the get current date time function.

 We could just validate the date format input to make sure that it is

 a string.

 But beyond that, technically we could put in any string here

 and everything is going to work out OK.

 And there are scenarios where you would want to allow strings like

 this.

 So I would be a little bit hesitant to try to strictly validate the

 input string

 in this particular case.

 Well, we've got our first tool function put together.

 Let's come back in just a moment and understand how to write out

 a JSON schema spec to describe this tool function.

---

#### Lesson 32: JSON Schema for tools

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276758](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276758)

**Video:** 08 - 003 - JSON Schema for Tools.mp4 | **Duration:** 5m 17s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Once we have created our tool function, we're going to move on to the

 next step, which is to

 write a JSON schema. This JSON schema is going to be used to describe

 our tool function, or more

 specifically, the arguments that the function expects to receive. Now

, the JSON schema is going

 to eventually be sent in our request off to Claude, and it's going to

 help Claude understand

 how to make use of the function we just wrote. Now, I know that when

 you look at all this

 configuration on the right hand side, it looks really intimidating.

 And this probably is one of

 the most challenging aspects in general of tool use, because this

 just looks like a huge blob of

 configuration that you have to write out. So let me give you a couple

 of notes here to help you

 understand what this is really doing for us. The first thing to

 understand is that JSON schema is

 not just specific to tool use or LLMs. In other words, this was not

 something that was just invented

 yesterday, just to facilitate tool use. JSON schema has been around

 for a very long time. It is a

 general purpose technique for data validation. There are two main

 areas to this big configuration

 object that I want to draw your attention to. At the top, there's the

 name and the description.

 We're going to come back to those in just a moment. For right now, I

 think the more confusing part

 is this JSON object right here. So I want to focus on this thing for

 just a little bit and make

 sure it's super clear how you put this thing together. The easiest

 way to understand this is to go

 through a example with a rather complex function. So let's imagine

 that we need to make one of these

 JSON schema specs for a function like this, process data. Now process

 data takes in four different

 arguments, ID is profile, primary ID and value. And based upon the

 example call, each one is going

 to take in a different type of data. So to turn this into a JSON

 schema that we can use back inside

 this larger structure, so basically whatever we want to put right

 here, here's exactly what we're

 going to do. I'm going to show you the simplest way of doing this.

 Step one, we're going to take

 our function and specifically the arguments. And we're going to write

 out a dictionary of all the

 keyword arguments with sample data for each one. So in this case,

 process data is going to take an

 ID's profile, primary ID and value. So I want to make a dictionary

 with exactly those keys. And I

 will provide some expected sample data for each of those different

 arguments. So IDs would presumably

 be listed numbers. I have a dictionary here, a string and a number.

 In step two, we're going to

 take that dictionary and convert it to JSON. Now I know it already

 looks like JSON, but there's one

 very important distinction. This is a capital T true, which is used

 in Python and JSON, it would

 be a lowercase T. So that's really the only conversion step you have

 to do, but it is important for

 the next step. So in step three, go off to Google, I'm not kidding

 here, go off to Google and search

 for JSON to JSON schema converter. There's a ton of different tools

 out there like this.

 These different tools allow you to paste in some JSON data. And based

 upon the values in that data,

 it will automatically generate a schema for you. So I'm going to

 paste in that dictionary that we

 just created and turned into JSON. Then I'm going to convert this

 thing. And now I've got exactly

 what I need to put into my tool schema. So this is the exact object I

 would want to use right here

 with one exception, we do not need that dollar sign schema statement.

 So I would delete that right

 there. Finally, step four, we're going to take that output, and we're

 going to add a description

 to each property. So inside of this properties object right here, I

've got a property of ID,

 primary ID, and the other two that I'm just not listing on this

 particular diagram.

 For each of these, I'm going to add in a description to describe

 exactly what this property or this

 argument into the function is supposed to do. So for example, if we

 go back to the example of the

 get weather spec that I had over here, you'll notice that the JSON

 schema, which is that section

 right there, the function get weather is expected to receive a

 location argument. It has to be a

 string. And then we provide a very descriptive or very detailed

 description of exactly what this

 argument does, and exactly how it fits into the overall tool use.

 When you are writing out these

 individual property descriptions, and the overall description for the

 tool itself, there's a couple

 of best practices that you really should follow. First, in the

 overall tool description at the very

 top, be sure to explain exactly what the tool does, when Claude

 should use it, and what kind of data

 it returns. We want our tool descriptions to be three to four

 sentences long, ideally. If you can't

 think of enough text to write out, remember, you can always just take

 your function. So for example,

 this right here, copy paste it directly into Claude, and ask it to

 write out a description for each

 the arguments to the function for you. Now, if you want to, go ahead

 and try to write out your own

 JSON schema for the get current date time function. If you don't want

 to put this together, that's

 totally fine. I've already written out a schema for you in the cell

 right above. So if you expand

 that one and scroll down a little bit, you will see that there is a

 get current date time schema.

 And if you want to take a look at it to get a better idea of how I

 structure this thing and the

 description of the overall tool, and some of the different arguments.

 All right, so that is our

 second step. We wrote out a JSON schema. So now the next thing we

 need to do is call Claude and

 include the schema with it. So Claude understands that this tool is

 available for use.

---

#### Lesson 33: Handling tool use responses

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276764](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276764)

**Video:** 08 - 004 - Handling Tool Use Responses.mp4 | **Duration:** 11m 45s | **Platform:** jwplayer

---

#### Lesson 34: Running tool functions

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276762](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276762)

**Video:** 08 - 005 - Running Tool Functions.mp4 | **Duration:** 11m 23s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

On to the next step where we are going to actually run a tool using a

tool use part that was sent back to us.

So in other words, when we get that initial response back that

contains a list of parts,

we're going to find all the different tool use parts based upon this

criteria right here.

We're going to run one of our different tool functions.

Now there is just one little gotcha here that I want you to be aware

of.

You see, whenever Claude decides to respond back to us and send back

a tool use part,

there is a potential that Claude might decide to use multiple tools

in parallel.

So we need to write our code to be a little bit defensive here

and assume that when Claude sends us back this tool use part, there

might be more than one.

So when we get that assistant message back, we might have a leading

text part

and then there might be maybe one or two or potentially even more

tool use parts in there as well.

So again, we just want to make sure we write code to handle this case

as well.

All right, let's go back over to our Jupyter notebook.

We're going to write out some code that's going to extract all these

different tool use parts

and then run the appropriate tool for each one.

Okay, so back over here, I'm going to make a new cell

and I'll write out a new function called run tools

and that's going to receive all the different parts that we get back

from a chat request.

So remember whenever we call chat now, we're going to get back text

and parts.

All we have to do is take parts right there and feed it into this

function.

Then inside this function, we're going to iterate over that parts

list

and find all the different tool use requests inside there.

So in other words, we want to extract this part and this part

and not extract the text part.

To do so, I will say tool request is going to be a comprehension

with part for part in parts if tool use in part.

So in other words, if the part object of that dictionary has the key

tool use inside of it,

that is a part that we care about.

So we are grabbing all the objects that have that key right there

specifically.

Then after that, I'm going to make a list that we're going to build

up over time.

Of all the different results, we'll use that in a little bit.

And then I will start to iterate over all these different tool

requests

for tool request in tool request.

I'm going to extract out the tool use ID, the name and the input to

send into the tool.

So I will get tool use ID from tool request tool use ID.

And to save a little time, I'm going to paste that down twice.

The next one, I'm going to extract out the tool name.

Then update the key on the right hand side.

It's not tool name. That's not the key that we need to extract.

So it's actually name. That's what the key is right there that we

need to get out.

So I will make sure I get name.

And then finally, the last one we care about is the input.

So the tool input and the key is simply input.

Now, just to make sure that we are going down the right path,

I'm going to add in a little print statement here really quickly.

So I'm going to print out. I need to run this given tool name with

these given arguments.

Then I'm going to test this by calling down here run tools with parts
.

.

I'll make sure I rerun the cell above to get a list of parts and then

test this out.

And I get, all right, I need to run the tool get current day time.

And here are the arguments I want to pass into it.

Well, that definitely looks good.

Next up, I'm going to make a helper function, which is going to be

responsible for actually running the tool.

So right above run tools, I'm going to make a separate function

called run tool.

This will take in the name, the tool to run and the arguments to it

as well.

And then inside of here, I'll put in a very simple series of if

statements,

many different ways we can do this, but we'll keep it simple.

I'll say if tool name is equal to our get current date time function.

So if that is the function that Claude wants to run, then I will

return get current date time.

And I will pass in tool input with star star tool input.

So little gotcha here, just something to be aware of,

you're always going to get back an object containing all the

different arguments that Claude wants to shove into your function.

So you're going to take that dictionary and you're going to splat it

in with star star into your tool function as I'm showing right here.

I'm going to also handle the case where Claude might mistakenly try

to ask for a tool that doesn't exist.

Now Claude is probably not going to make a mistake here.

It's actually much more likely that you are going to make a typo

somewhere.

For example, I might leave off the word time on here and put in just

get current date.

And this name needs to match up with our actual tool schema.

So entirely possible that we're going to make a typo ourselves.

And to handle that case, I'm just going to put in an else here.

So if I fall into the else case and I don't find the tool to run,

I will raise an exception with unknown tool name and then print out

the tool name and make sure that I make that a f string.

Okay, so now down here inside of our run tools function, I will

replace the print statement and I'll say tool output is run tool with

tool name and the input to it.

And now once again, let's try to run the cell.

We need to do a print first.

Let's make sure we actually see the output.

There we go.

So now run that.

And all right, that looks good.

So we got the current time right now in real life.

For me, it is 1224 roughly in fact.

So at this point, we have achieved this step right here.

We have written out some code to call a tool function.

So now we need to take the result of that function, whatever the

output was in our case, the current time.

And we need to send it back to Claude inside of something called a

tool result part.

So let me show you how we create these tool result parts.

Okay, the tool result part looks a little bit like the tool use parts

we looked at previously.

So these are dictionaries.

They're going to have a tool result key and inside a couple of

different properties.

The first is the tool use ID.

And I'm going to tell you about that in just a moment.

The second is content that's going to be simply the output that we

got from running our tool and we're going to serialize it as a string

just in case our tool function end up returning something like a list

or a dictionary.

So we're going to make sure we turn that into a string and put it

right there.

Then we're going to also provide a status flag of either success or

air.

Now it really is important to do air handling here because Claude is

rather intelligent when it comes to calling tools.

If Claude tries to call the tool and we end up returning an air to it

, Claude might try to figure out what's going wrong and maybe it'll

adjust the argument that it is providing and eventually figure out

how to correctly use your tool.

So we do want to make sure that we put in some reasonable air

handling here and add in that status of either success or air.

So now let me very briefly describe what this tool use ID is all

about because we saw this previously when we are looking at the tool

use parts.

So remember, these are kind of like our inputs, they had a tool use

ID and now the outputs, the tool results have an ID as well.

So here's what they are all about.

Remember what I told you at the start of this video.

Claude can potentially give us multiple tool use requests inside of a

single message.

So let's imagine a scenario in which we define a tool called

calculator.

Claude might decide that it needs to run that calculator twice in

parallel to execute two different operations.

Maybe one is evaluating 10 plus 10 and the second is 30 plus 30.

So when we receive these two tool use requests, we're going to

eventually have to send back to tool results.

And on this scenario, it would be kind of hard for Claude to figure

out which of these two results match up with the two original

requests.

And that's where the ID comes in.

So we need to make sure that the result of this operation of 10 plus

10, which might have an ID of 83,

has that same ID in the output as well with the appropriate output of

, in this case, 20.

And then the result of 30 plus 30 with an ID of P09 might be right

here, P09 with an output of 60.

So in short, the entire goal of this tool use ID key inside of here

is just to help Claude identify which result is which.

All right, let's go back over to our notebook and for every tool use

part we got,

we are going to generate one of these different tool request parts

that will eventually be sent back over to Claude.

Back inside of my notebook, I'm going to remove the print statement

and make a tool result part that will be a dictionary that has a tool

result key.

And inside of here, we will add in tool use ID content.

That will be a list with a dictionary in there with a text of JSON

dump string with the tool output.

00:09:03,000 --> 09:09:930
And I need to make sure I import JSON really quickly, which I will do

at the top of this cell.

And then finally, we need our status flag of success.

Now, this is assuming that everything always goes perfectly, but it's

entirely possible that one of our tool functions might fail in some

way.

So to really handle things

---

#### Lesson 35: Sending tool results

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276760](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276760)

**Video:** 08 - 006 - Sending Tool Results.mp4 | **Duration:** 3m 4s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

On to the very last step.

 We are going to take that list of tool result parts

 that we just generated, add them all into a user message,

 and then take the entire conversation history

 and send it all off to Claude.

 So let's go back over to our notebooks

 and test this out really quickly.

 First, I'm going to scroll up to the cell right above.

 Now right up here, we called chat,

 and we got our list of parts,

00:00:21,800 --> 0 প্রে0:00:24,920
 but we never actually added them into our message history.

 So in other words, right now,

 we do not have this part of the conversation

 inside of our list of messages.

 So I'm going to fix that really quickly.

 I will add in a add assistant message

 and put in the big list of parts.

 I'm then going to rerun that cell.

 Okay, next up, I'm going to go down.

 In the cell that we were just working in a moment ago,

 we had a call to run tools.

 Now it's totally fine to leave that in there,

 but I only have it in there for debug purposes.

 So I'm going to remove that call

 just to clean up my code in here.

 And then underneath, I'm going to take a look at messages

 and just to verify that I do in fact,

 have the original user message

 along with the follow-up assistant

 that has the tool use request.

 And there it is right there.

 So that definitely looks good.

 Next up, I'm going to add in a new code cell

 and call add user message.

 And to my list of messages,

 I'm going to pass in run tools

 with all the parts we got out of our initial response.

 So this is where we are going

 to run all those individual tools.

 And it's going to generate our list of tool result parts.

 And we're going to add those all into our conversation history

 inside of a user message.

 So once again, I'm going to run the cell

 and print out messages.

 So now I should see I've got my user,

 the assistant and user.

 And inside the assistant,

 I have my tool use requests.

 And inside the user message,

 I have my tool result responses.

 So now the very last thing we have to do is

 just take this list of messages

 and send it all off to Claude.

 So I'm going to add one more cell down here.

 And I'll get text and parts from calling chat with messages.

 And when we do this follow-up,

 we do have to include all the original tool schemas as well.

 If we don't include those tool schemas,

 Claude will end up being really confused and say,

 hey, wait a minute,

 I tried to call some tool named getCurrentDateTime,

 but where's the actual definition for that?

 So we need to make sure that we include

 that same list of schemas.

 So in other words, this right here.

 I'm going to copy that

 and just make sure that I added in.

 And then finally, I will print out text and run this

 and we'll see what we get.

 And hey, it worked.

 So I was able to print out the current date and time.

 Now, as we said at the very start of the series of videos,

 well, Claude already knows the current date,

 but it doesn't know the time.

 And so this is evidence that our tool is working

 absolutely correctly.

 We are 100% getting our time in there.

---

#### Lesson 36: Multi-Turn conversations with tools

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276759](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276759)

**Video:** 08 - 007 - Multi-Turn Conversations with Tools.mp4 | **Duration:** 6m 35s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next thing I want to show you is how to have a long running

 conversation that includes tool use you'll notice that I collapsed

 the cell that has our run tools implementation just make things a

 little bit easier to read.

 Now as we saw at the end of last video right now everything works

 just fine, but I want you to notice what happens if I change the

 original query right here and if I instead say something like what is

 one plus one.

 So if I run that I will get back it responds really quickly. I'll

 then add in the result of running tools to messages and print out

 messages and let's see what happens.

 So in this scenario we got back a response from the assistant that

 did not include any tool use requests. So we kind of erroneously

 added in this completely empty message right here.

 In order to have a long running conversation that includes tools what

 we should really do is take a look at the stop reason that comes back

 inside response.

 Remember whenever we get a response back from Claude it's going to

 include a stop reason we should really consider the stop reason in

 deciding whether or not we need to process any tool use requests.

 So let's do a little refactor here back inside of my notebook. I'm

 going to first do a little bit of code cleanup. I'm going to find the

 example conversation we had right here. I'm going to delete that cell

.

 I'm going to delete this example one right here and this one right

 here.

 Next up I'm going to go up to the very top where we have our helper

 functions defined inside of here we can find the chat function.

 Now remember we did refactor here just a little bit ago to always

 return text in parts but now I also want to return the stop reason.

 We could add in another multiple return element right here so I could

 just put in stop reason if we wanted to but that's starting to get a

 little bit challenging to work with.

 So I'm going to change the return structure of this chat function

 just a little bit.

 First I'm going to delete text right there. I'm still going to keep

 parts and now I'm going to return a dictionary that is going to have

 the list of parts.

 I'm going to return a stop reason which will come from response stop

 reason with a capital R and then I will still return text and I'm

 going to do a little fix here on text at the same time.

 You see what we had previously we always tried to access the first

 part of a message and we always assumed it was a text part.

 That's not necessarily always going to be true. So to fix things up

 just a little bit I'm going to scan through the list of parts.

 I'm going to find all the text parts and just join all the text

 together.

 So I'll put in a new line and I'm going to join on a comprehension

 with P text for P in parts if text in P like so.

 All right so now we are getting a list of parts we got the text and

 our stop reason.

 We could at this point kind of just return the entire response object

 but doing this pre processing just kind of a nice little thing to add

 in.

 Now I'm going to rerun that cell and now let me show you how we are

 going to use that improved chat function.

 I'm going to add a new code block here at the bottom and inside of

 here we are going to make a new function that's going to handle a

 multi turn conversation for us that involves tool use.

 So I'm going to make a new function called run conversation.

 It's going to take in a list of messages and inside of here I'll do a

 while true and I'll say result will come from calling chat with the

 list of messages and my list of tools.

 Right now we only have one tool schema which is get current date time

 schema.

 Then I'm going to add assistant message to messages with result parts

.

 So that's where we are taking all those tool use parts and

 potentially text parts and adding them into our message history as an

 assistant message.

 I'm then going to print out whatever result text we got back just so

 we can kind of monitor the conversation.

 If the results stop reason is not equal to tool use.

 Then I'm going to break out of the while loop.

 So in other words if we're not asking for a tool that means we must

 have hit some other reason to stop the conversation and we don't need

 to continue inside this while loop anymore.

 Otherwise if we continue that means that we must have a need to run

 some tools.

 So I'm going to get my tool result parts by calling run tools and

 pass in those parts and add that as a user message to messages.

 And that's it. So now whenever we run this function we'll pass in a

 list of messages. We're going to get back a result.

 If we have need of calling any tools we will do so and continue

 inside of the while loop again until we finally get a response back

 that does not ask us to do any kind of tool use.

 At the very bottom here outside of the while loop I will return

 messages.

 So I'm going to run this and let's do a test down here.

 I'll ask what we need to make our list of messages first my mistake.

 I'll add a user message of what time is it and call run conversation

 with the messages.

 So now let's test this and see how we're doing and we should see the

 conversation kind of progress as Claude figures out what is going on.

 Okay so there we go we've got first I can help you figure out the

 current time let me use a tool to figure out the current time for you

.

 I then get the current time and then I see my entire log of messages

 right here and you can absolutely go through this and just verify

 that we have the correct ordering of messages.

 We've got our original user we've got the tool use request we've got

 the tool result being sent back to Claude and then a final assistant

 message coming back that does not ask for any tools.

 So the nice thing about this approach is it should very easily also

 support questions that don't require required tool use at all.

 So if I ask what is one plus one we should just about immediately see

 a response back and yes there we go.

 Alright so this is excellent the last thing we really have to do to

 finish up this section is go through adding in multiple tools because

 right now we just have one just adds in the current time not super

 useful so we're going to add in those last little pieces in just a

 moment.

---

#### Lesson 37: Adding multiple tools

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276761](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276761)

**Video:** 08 - 008 - Adding Multiple Tools.mp4 | **Duration:** 3m 36s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

You might recall that the original goal of this project was to add in

 three separate tools,

 and right now we have only done one, just the get current date time.

 So now in this video,

 we're going to add in those two remaining tools, add duration to date

 time and set a reminder.

 Now I have already provided implementations of these other two

 functions for you,

 along with JSON schema specs, just to save us a lot of time with a

 lot of typing that we would

 need. So let's take a look at how we would wire up these additional

 functions along with their

 accompanying JSON schema specs. Now as a reminder, I've already got

 these implemented inside of

 one of the earlier code cells. So right here is add duration to date

 time. And then if you scroll

 down a little bit, there is set reminder. All it does is print out

 the timestamp and some content.

 So there's not an actual reminder system here, but you can kind of

 imagine a couple of different

 ways in which we might implement that. And then underneath that, the

 existing schema,

 here is the add duration to date time schema. And then finally, the

 set reminders schema.

 So again, all we really have to do is touch a couple of places to add

 in these schemas

 and wire the actual tool functions up to our run tools function. So

 let's get to it.

 Step one, I'm going to find the run conversation function. Here it is

 right here,

 and I'm going to add in those two additional schema that we just saw.

 So I have add duration

 to date time schema and set reminder schema.

 Then in the cell right above it, which is where we have all the tool

 running code,

 I will find the run tool function. And we need to add in two

 additional cases to this if statement

 to handle the case where Claude asked to use those two additional

 functions that we were just

 looking at. So one will be L if tool name is set reminder. And if

 that's the case,

 then I'm going to return a call to set reminder. And then L if tool

 name, add duration to date

 time. And if that's the case, we will call the appropriate function.

 And that should be it. So now I'm going to make sure I rerun the cell

. I will scroll down.

 I'll make sure I run run conversation. And now we should be able to

 test out the entire process

 of setting a reminder. So I'm going to say set a reminder to go to

 the doctor. The appointment

 is in 100 days. And run it. Now I might run into a rate limit here

 rather quickly,

 because at present, I have a rather low service quota. But I should

 at least be able to see a

 couple of steps here. Notice how right away Claude is giving us a

 great plan of what it needs to do.

 So it's going to try to get today's date. And that kind of like

 happens in between these two

 messages. We don't see it printed, but it does happen. Then Claude

 says, I need to add 100 days.

 So it's going to use the add duration to date time. And then finally,

 it calls the set reminder

 function as well. And so we see correctly right here, setting the

 following reminder for 100 days

 from my current date. Go to the doctor appointment. And that's it. So

 as you can see, once we write

 out all that kind of base code for implementing tool use, adding

 additional tools is really,

 really easy and straightforward. It's just that first little bit is a

 little bit challenging.

 And I hope you didn't lose your patience with me earlier on inside this

 module when we had to go

 over all that different message and part handling stuff.

---

#### Lesson 38: Batch tool use

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276766](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276766)

**Video:** 08 - 009 - Batch Tool Use.mp4 | **Duration:** 7m 15s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, we're going to take a look at how we can parallelize

 tool calls by implementing

 something called a batch tool.

 Now, I first want to begin by reminding you something I told you

 about earlier on inside

 this module.

 Whenever Claude sends us back some tool use parts inside of a message

, so essentially

 tool requests, there can potentially be more than one tool use part

 inside of one single

 message.

 So take this example I have on the right hand side really quickly.

 If I sent in an initial query of something like what is March 12 plus

 50 days, also

 what is March 12 plus 100 days, then Claude in theory could send us

 back two separate

 tool use parts inside of one single message.

 The first one might try to calculate March 12 plus 50 days and the

 second one March 12

 plus 100.

 These are two operations or two tool calls that are absolutely

 parallelizable.

 They can be executed at the same time without any issue whatsoever.

 Now Claude, sometimes we'll try to do this in parallel, but it turns

 out that some versions

 of Claude don't try to call tools in parallel quite as much as you

 might wish.

 So there's a way that we can kind of trick Claude and that is by

 implementing another

 tool called the batch tool.

 This is another tool that we implemented in the exact same way as the

 others.

 That means that we still have to write out a tool spec and we also

 have to make some kind

 of function to handle whenever that tool gets called.

 Now the easiest way to understand the batch tool is to just walk

 through the implementation.

 So let's do that right away.

 The first thing I want to do is show you what happens if we put in

 that exact query that

 I just wrote out inside of that diagram.

 So what happens if we put in that March 12 plus 50 and plus 100.

 If I run this, I sometimes might see two parallel calls, but almost

 always I'm going

 to see two separate calls.

 So when I get some output back, if I scroll down a little bit and

 look at the message

 log, I will see in fact that I've got roll of assistant right here.

 So this contains one tool use request where it put in March 12 plus

 50 days, I then sent

 back a tool result and then right underneath that is a separate

 second call for the same

 tool this time with a hundred days.

 So very clear that Claude did not try to parallelize these calls,

 even though it absolutely

 could.

 All right, so now that we've seen that, yeah, doesn't always work

 quite as expected.

 Let's take a look at how we implement that batch tool.

 So first thing we would need is a spec.

 Once again, I have provided a spec for you inside of an earlier code

 cell.

 So if you scroll way up to that code cell that starts off with the

 date time imports,

 expand that thing and then go all the way down to the bottom.

 And here's the spec for the batch tool.

 And I'm providing these for you because it would just be a ton of

 typing if we were to

 walk through it together.

 So this tool is super simple in nature.

 It just tells Claude that it can run other tool calls simultaneously.

 And the input arguments to it is a list called invocations.

 Inside this list, there will be a variety of different objects and

 each object is going

 to have the name of some other tool to invoke and the arguments to

 pass to it.

 So we need to take each of these different invocation objects.

 We need to loop through it.

 We need to find each of the listed tools and call each one with the

 provided arguments.

 One other thing to notice here, the arguments are encoded as a JSON

 string.

 So we will have to do a little bit of JSON parsing as well.

 Once we call each of these different tools, we'll then assemble all

 the results and pass

 it back as though it were a single call to a single tool called the

 batch tool.

 Let me show you how we implement that.

 All right.

 So to get started, I'm going to go to the very bottom of the notebook

 once again and

 scroll up a little bit and find where we put together all the run

 tools code.

 At the top of the cell, I'm going to find the run tool function and I

'm going to add

 in another case here, I'll say if tool name is batch tool, then I

 want to return the result

 of calling run batch and I'm going to pass in the tool input and this

 time I'm not going

 to use the splat.

 So I'm not going to put in the star star, I'm just going to pass in

 the tool input directly.

 I'm then going to define this new run batch function right above run

 tool.

 And this will receive that tool input argument.

 Then inside of here, we're going to loop over all the different inv

 ocations.

 So for invocation in tool input invocations, remember invocation, we

 just saw the structure

 of this object or what this thing should really be inside of our tool

 spec.

 So inside of there, we should have a tool name, which will be the

 name property and some

 list of arguments, which should be invocation arguments.

 Remember what I told you just a moment ago, arguments is designated

 inside of that JSON

 spec as being a JSON encoded string.

 So we need to parse that with a JSON load string.

 So now we have everything we need to run the correct tool with the

 appropriate arguments.

 And we can do so by just reusing the run tool function.

 So watch how we're going to do this going to be going to be

 surprisingly simple, we'll

 say tool output and that will be run tool and we will pass in the

 tool name that we want

 to run and the arguments for it.

 And then finally, we need to collect all these different tool outputs

.

 So I'm going to make a list up here, I'll call it batch output.

 And I'm going to append into that.

 Then we will add in tool name with the tool name and the output that

 we got from it.

 And then finally down here at the bottom, I will return batch output

 like so.

 Okay, so that should be it.

 We've now got a function to run a bunch of other tools by just deleg

ating to the function

 we already had.

 So it was not that hard to implement.

00:鋃06:11,920 --> 00:06:16,620
 And now I'm going to rerun the cell and let's go back down to our

 test function.

 So run conversation right here.

 We just need to make sure that we add in the run batch schema.

 So it was actually called batch tool schema, I believe.

 There we go.

 And now it's time for us to do a test.

 And now if we take a look at the message log output, hopefully we're

 going to see one

 single tool request.

 And in fact, we do.

 So take a look at this.

 It really is quite interesting.

 We've got the initial user message.

 We then have our assistant message where it asked to use a tool.

 And in this case, it asked to use the batch tool and the invocations

 that it wants to

 run.

 So kind of the sub tools is going to be a call to ad duration to date

 time and ad duration

 to date time.

 The first one has the duration of 50 second has a hundred.

 So by just adding in this tool, we've kind of trick Claude into

 calling multiple tools

 in parallel.

 So this is a technique that I highly recommend you keep in mind

 anytime that you need to run

 multiple tools at the same time.

---

#### Lesson 39: Structured data with tools

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276765](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276765)

**Video:** 08 - 010 - Structured Data with Tools.mp4 | **Duration:** 9m 13s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Earlier on inside this course, we spoke about how to get structured

output from Claude by using

some clever techniques. In particular, we discussed using a message

pre-fill and stop sequences,

along with a carefully structured prompt in order to get some JSON

out of Claude.

Now this definitely worked well and it was very easy to set up, but

we can get some more reliable

output by a very clever use of tools. So we're going to take a look

at how we can implement

structured output using tools alone without having to worry about any

message pre-filling

or stop sequences. Now I anticipate one of your very first questions

is going to be,

why did we learn about this style of structured output when we could

have just used tools all along?

Well, the answer is very simple. Using tools for structured output is

a lot more set up,

there's a lot more complexity. So having both these abilities of

getting structured data at your

disposal is really valuable because in some scenarios, you might want

to just make use of this prompt-based

structured output. In other scenarios, you might want to make use of

tools. All right,

so let's take a look at how we can make use of tools to generate

structured data. Now as I just

mentioned, this is a alternate method of extracting structured data,

primarily JSON out of some data

source. This is more reliable than past techniques we took a look at,

but again, much more complex

to set up. The general idea here is that we are going to write out a

JSON schema spec for a tool

whose inputs are going to be the structure of data that we are

looking for. So back over here a

moment ago, when we looked at this prompt, we can imagine that we

were asking Claude to take a look

at a financial statement and extract a balance that was an integer

and a list of key insights that

was going to be a list of strings. So if we wanted to approach this

using tool-based structured output,

we would write out a JSON schema spec where the inputs would be a

balance that's going to be an

integer and key insights that's going to be a list of strings. Then

we're going to feed this

JSON schema spec into Claude along with the financial data that we

might want to get some

information out of. Now at this point, let me show you a diagram of

the flow because it's a lot

easier to understand in diagram format. Okay, so just as before, we

are going to write out a

reasonable prompt for Claude. So we might say analyze a filing

financial statement and then call

some provided tool. Along with this prompt with all the statement

data inside of it, we'll also

provide that schema. So that's going to go off to Claude. Claude is

going to take a look at the

prompt. It's going to see the tool that is available to it. And it's

going to say,

Oh, fantastic. I will call this financial analysis tool. And I'll

make sure that I provide arguments

that match this structure right here. So Claude is then going to

respond back to us

with a assistant message that presumably will have just one tool use

part. And then we'll say,

I want to call the financial analysis tool. And here is the input to

it. And the input will be

the extracted JSON that we are looking for. So it's going to be

exactly these arguments right

here. Our balance that's a number and the key insights that is a

string. So once we get that

assistant message, this part is the worst part because I honestly

feel bad for Claude.

We basically take that JSON data right there. And we just said,

Claude, Hey, thanks for the data.

We're out. We got what we were looking for. And we don't continue the

message from beyond that

point. Because at this point, we got the data we were looking for. We

got those arguments. We got

that extracted data. And so there's no need for us to do any follow

up in this conversation at all.

We can just take the data and use it for whatever purpose we have. So

that is the general idea

behind using tools for generating structured data. Now again, best

way to really understand

this is to take a look at an example. So I would encourage you to

download another notebook here.

Its name is 003 structure data in the current module. I've got a lot

of setup code in here,

some example tool schemas. And I've got a little example of a very

simple data generation.

So I'm asking Claude right now to write out a one paragraph article

about computer science.

And I ask it to include a title and an author name. So this is some

data. Now let's just imagine

that this data was not generated by Claude. Let's imagine that maybe

we have this article from some

other source and we want to extract information from it. Maybe we

want to extract specifically

the title right here, the author, and then maybe some primary topics

that are mentioned inside of

the article. And we want to extract all this as JSON. So we could use

the old technique we saw,

where we write out a prompt, we do the message prefilling and some

stop sequences and we write

out the structure of JSON that we are looking for. But another way we

could do this is by making

use of tool based data extraction. So let me show you how we would do

that.

Step one, we would write out our tool schema. Now again, just to save

us a whole bunch of time,

I have already authored a tool schema for you. It's inside of this

tool schema section. So it's

called article details schema. And you can take a look at the

description. But the primary part that

we really care about here is the fact that we are asking for input to

this kind of fake tool here

of a title, an author, and a list of topics. So now that we have this

tool schema, we're going to make

a request to Claude, we are going to ask it to take this text right

here, extract the key data,

and call that tool that you just saw with all the data that has been

extracted. So let me show you

how we'd write out the code for that. First, I'm going to make a new

list of messages. I'm going to

add in a user message. And I'm going to make it a multi line f string

. There we go. And I'm going

to ask Claude to analyze the article below and extract key data, then

call the article details

tool. And I'll use some XML tags, and I'll put in my article text.

And that's going to come from

our variable up here, result text. So I'm going to assume you ran the

cell result text should contain

all the article text that was generated. So I'm going to refer to

result text right there.

All right, so that is our user message as a part of a brand new

conversation that we are starting.

So now we are going to call chat, pass in our messages, and list out

the different tools we

want to include. And in this case, we want to include that article

details schema.

Now when Claude sees this, we really want to make sure that Claude

makes use of this tool.

So this would be a really good place to make use of that setting that

we discussed a little bit

ago, specifically the tool choice setting. Remember, by default,

Claude is going to decide if it needs

to use a tool or not. But if we want to, we can force Claude to make

use of a specific tool

by adding in something like this inside of our request parameters. So

we'll put in tool choice

inside their dictionary with tool name, and then the name of the tool

to call. So this would be a

perfect scenario of making use of this option, because we're going to

force Claude to make use of

this provided tool. Now to add in this option, I have already done a

little bit of work on the

chat function for us. Let me show you what I did. If we scroll up the

implementation of the chat

function, here it is right here. So I added in a new keyword argument

of tool underscore choice.

And by default, it is set to auto. Then down here, you will find some

code that makes use of that

argument. Now I would encourage you to read over this code closely.

Essentially, the way it works is

if you pass in a string of auto, it will set the appropriate auto

option. If you pass in any,

it will set the any option. And if you pass in as tool choice right

here, the name of a specific

tool, it will go to this style of input right here. So it will

automatically make this little

dictionary and put in your provided tool name as the name. So in

short, to make use of this thing,

let me show you how. Back down here at the very bottom chat call that

we just added in,

I'm going to put in a tool choice. And I'm going to set that to our

article details tool.

All right, so let's test this out. I'm going to assign the result to

this to JSON result.

And print that thing out afterwards. I'll run this and let's see how

we do. All right, very good.

There is my JSON output. Now very quickly, if you saw a result of

something like unknown or

something like that, make sure that you ran the cell above that

actually generates some text to

use because result text might be empty if you just open up the

notebook and you did not run that cell.

So now we can take a look at this output right here. So we can see

that we have an input to this

tool that's going to be this JSON object that has the exact

properties that we were looking for.

It has the author of the article, the title, and then a list of

mentioned topics. And that's the

entire process. So once we have this input right here, really, for us

, its output, so to speak,

---

#### Lesson 40: Flexible tool extraction

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276763](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276763)

**Video:** 08 - 011 - Flexible Tool Extraction.mp4 | **Duration:** 4m 40s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Without a doubt, the number one downside to making use of tools for

 structured data extraction

 is having to write and manage these really big JSON schemas. So in

 this video, I'm going to show

 you a little trick to alleviate that pain. So here's what we're going

 to do. We are going to make one

 single schema with a name of something like to JSON. And then we

 will tell Claude that the inputs

 to it is going to be an object that has as many properties as Claude

 wants to add. Then inside

 of our prompt, we will write out the actual structure that we want.

 So the actual listing of different

 properties that we expect and the different types. And then we will

 tell Claude to call this tool

 and pass in some argument that follows the structure that we listed

 out in our prompt. Now yet again,

 this is another scenario we're taking a look at an example is the

 easiest way to understand what's

 going on. So let's go through a quick example. All right, so back

 over here, I want to again

 scroll up a little bit and find that section with tool schemas.

 Inside of here is the article

 detail schema, which we already used. And if you scroll down, you

 will find to JSON schema, which

 has all the same properties and description as what you just saw in

 that diagram a moment to go.

 So we're going to make use of this schema as a flexible way of

 getting any kind of structure of

 data out of Claude. All right, so I will once again go down to the

 very bottom of the file and we're

 going to start in a brand new cell. I will then make my list of

 messages, add a user message.

 And to save time as usual, I'm going to do a little bit of copy past

ing from the cell above.

 So I'll go just right here and take that F string, go back down and

 put it right there.

 I'm then going to update the prompt to tell Claude to call the to

 JSON tool. And then underneath

 article text, I'm going to be very clear with Claude and tell it

 exactly how to call that tool.

 So I'll say something to the effect of when you call to JSON, pass in

 the following structure.

 And then I will list out all the different properties that we need.

 Now notice we are in

 an F string here, so we need to use escape curly braces, which means

 we just need to double them up.

 And then I will list out the title. And I'll put in a little comment

 here. So I'll say it should

 be a string. And this is going to be the title of the article. I'll

 copy that

 and replace with author. And then topics will be a list of strings

 and say a list of topics

 mentioned in the article. Okay, so there is our user message.

 So now we are going to call Claude, we will get some flexible result.

 Just to distinguish from our earlier result variables, we declared

 early inside of this file.

 We'll call chat, pass in our messages. And then we do need to provide

 our list of tools. Don't

 forget about that. So we want to use our to JSON schema. And we want

 to force a tool use here.

 So we'll pass in a tool choice. And we want to use the tool that is

 named to JSON.

 All right, let's run this and see how we do.

 So I'll print out flexible results. And now once again, there's our

 results. So we've got our input

 with a title, author, and then our list of topics. And so you can see

 right away that life is a lot

 easier when we are making use of this style of tool based extraction,

 because now if we need to

 change the structure of data coming out, all we have to do is make a

 very simple edit inside of

 this prompt. So if I also want to get maybe the number topics about

 just numb topics,

 let's make that an integer and say number of topics mentioned. And

 that's all we have to do.

 So I'd rerun that. Once it's done, we can print out flexible results

 again. And now we should see

 number of topics listed as well. All right, so again, this is a much,

 much more easy way of

 specifying the exact structure of the data that you want when you're

 making use of tool based

 extraction. The one downside here is that your results in general are

 not going to be quite as

 good as writing out a dedicated schema. But you're still going to get

 JSON. And it's still

 going to be high quality JSON. Just at some extreme levels, you might

 notice that you're not getting

 quite as nice a structure as you might expect. So if you are writing

 a very critical data extraction

 task, you might want to go with the more hard coded structure, which

 we saw back over here,

 where you specifically list out all the different properties you

 expect to see inside of a schema like

 this.

---

#### Lesson 41: The text editor tool

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276767](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276767)

**Video:** 08 - 012 - The Text Editor Tool.mp4 | **Duration:** 11m 23s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

As we saw earlier on inside this module,

 usually, you and I, as developers,

 author all the different tools that we want to pass off to Claude.

 But there is one tool that Claude has access to by default.

 This is called the text editor tool,

 and it is built directly into Claude.

 This tool gives Claude a wide variety of abilities

 related to just about everything you can do inside of a standard text

 editor.

 So for example, this tool gives Claude the ability to open up files

 or

 directories and read the contents. It can take a look at specific

 ranges of text inside of a file.

 It can add or replace text inside of a file. It can make new files.

 It can do undo.

 Essentially, everything you would do inside of a normal text editor.

 So this dramatically expands Claude's abilities and almost right out

 of the gate

 kind of gives Claude the ability to act as a software engineer.

 Now, understanding the text editor tool is just a little bit

 confusing.

 So I want to walk you through a couple of different diagrams and

 clarify

 what this tool does for you and what you and I have to do

 to actually make use of it inside of a project.

 So the first thing to understand here is that only the JSON schema

 part

 is actually built into Claude. And let me clarify what I mean by that.

 Remember that when we want to make use of tools,

 we really have to author two separate things.

 First, on the left-hand side, we have to write out that JSON schema

 spec.

 This gets provided off to Claude and tells Claude about some tool

 that it can make use of

 and all the different arguments that the tool requires.

 And then on the right-hand side, you and I had to write out a tool

 function

 implementation to pair up with that JSON schema.

 These were actual functions implemented inside of our codebase

 that would be called at some point in time when Claude wanted to use

 our tool.

 So we really had to write both sides here.

 We had to do both the JSON schema and the tool function

 implementation.

 So when we make use of the text editor tool,

 the only thing that is actually kind of provided for us or built into

 Claude

 is the JSON schema, that set of instructions that tells Claude how to

 make use of this tool.

 You and I have to provide an actual implementation

 to handle all of Claude's requests to use the text editor tool.

 That does not exist. It is something that you and I have to write out

 inside of our codebase.

 So in other words, whenever Claude decides to say, maybe create a new

 file,

 and it sends back a tool use part to us that says, I want to create a

 new file,

 we have to provide an actual function that will actually make a new

 file somewhere on our hard drive.

 So using the text editor tool is not free, so to speak.

 It requires a little bit of effort on our side,

 because we have to write out a couple of different functions.

 Now, let's go over to a Jupyter notebook,

 and we're going to demo the use of this tool and take a look at

 how we would write out some of these different functions.

 All right, so back inside of my editor, I have opened up a new

 notebook.

 This one is called 005 text editor tool.

 Inside of the first cell, I have some of our usual setup code.

 Now, to use the text editor tool, there is just a little bit of

 tricky setup here.

 Remember, we need to eventually provide the name of some different

 tools that we want to

 allow Claude to use. In order to use the text editor tool, we must

 provide very specific string

 IDs when we make our request off to AWS bedrock.

 So there are different tool names for this text editor,

 depending upon the exact model version you are using.

 So if you are using Claude 3 Sonnet, you want the text editor variable to

 be set to exactly

 that string right there. If you're using Claude 3 Haiku,

 then you're going to comment that line out and uncomment the other

 one.

 If you are using a newer version of Claude than the two that I am

 showing right here,

 that's totally fine. Hopefully, I will be able to update this

 notebook for you.

 Otherwise, you can do a quick search in the AWS bedrock documentation

 to find this new string

 that you should be using here. Now, for me, I'm using Claude 3 Sonnet,

 so I'm going to comment out that one and uncomment that one like so,

 and then I will run the cell.

 In the next cell down are some of the same helper functions we've

 been working with

 throughout this entire course. So stuff like add user message, add

 assistant message.

 I have modified the chat function just a little bit to accept in a

 new text editor keyword.

 So that's going to be the name or that idea of the text editor that

 we're just looking at a moment

 to go. If one is provided, then some extra configuration is included

 inside of a additional

 model request fields inside of the params that we're sending off to

 the converse method.

 In the next cell down, there is a class called text editor tool.

 This class includes all the different methods that are required to

 use the text editor tool.

 So in other words, this class provides this piece of the puzzle over

 here. So remember,

 I just told you usually we have to write out some code to handle all

 of Claude's requests

 to actually use the text editor tool. I wrote out that code for you

 inside of this notebook.

 So there are methods inside this class to do things like, if I scroll

 down a little bit,

 view the contents of a file or a directory. There are methods inside

 of here to

 replace a string inside of a file to create a file and so on. So

 everything has already been

 put together for you inside of this cell. Now, without further ado, I

 would like to give you

 a demonstration of how this tool works. So I'm going to open up my

 folder explorer on the left

 hand side. I'm going to find the directory that my current notebook

 is in. And then inside that

 same directory, I'm going to make a new file called main.py. And

 inside there, I'm going to

 write out a very simple function. I'll say def, hello, and inside

 there, print out, hi there.

 I'm then going to save that file. I'll go back over to my notebook.

 And in the final

 cell down here, I'm going to add in a starting user message. Inside

 of that, I'm going to add

 a prompt of write a one sentence description of the code in the dot

 slash main.py file.

 And I'm going to run the cell. And let's see what kind of response we

 now get out of Claude.

 In this response, it is very clear that it successfully opened up the

 contents of that file

 and read the code that was inside of there. Because it says very

 plainly, I opened up that file.

 And it looks like there is a function called hello, the prints are

 greeting high there.

 Now, to really understand what's going on behind the scenes, I would

 encourage you to read

 the message log down here. So the back and forth between Claude and

 our notebook.

 Let's take a look at a diagram to better understand what is really

 being exchanged here.

 So we send off that initial prompt, Claude asking it to write a one

 sentence description

 of the code inside that file. Claude is then going to immediately

 realize that it needs to

 read the contents of the file. Claude is then going to respond with

 an assistant message that has a

 tool use part with this kind of structure inside of it. So it will be

 a dictionary that has a command

 of view and a path of dot slash main dot pie. The code running inside

 of our notebook is going to

 automatically take that little structure right there and realize that

 Claude wants to view the

 contents of the main dot pie file. So the code inside of our notebook

 is going to use that class

 that I just showed you the text editor tool class and a specific

 method in there called the view

 method to open up that file and read its contents. Once it reads the

 contents, we're then going to

 send back a user message that includes a tool result part that looks

 like this. So it'll have some

 text that includes the exact text out of that file that could sent

 off to Claude. And now Claude

 has everything it needs in order to answer our original prompt, which

 was write a one sentence

 description of the code inside that file. So Claude will then send

 back some follow-up assistant

 message like this with a single text part inside of it. Now we can

 very easily verify this is what

 happens while taking a look at the message log. So right here, there

's the immediate follow-up

 assistant message with the tool use asking for a command of view and

 a path of dot slash main dot

 pie. We then respond with the tool result part that contains the

 contents of that file. And then

 here's the final assistant message that says based upon this file,

 here's what the contents does.

 Now the thing that I really want to focus on here is this command

 structure. So what exactly is

 command? Well, as a part of implementing this function right here to

 implement everything that

 is required by the text editor tool, there are a series of different

 commands that we need to

 be able to respond to. So in total, there are five different commands

 that the text editor tool

 might send back to our application. So again, we need to write out

 code to handle each of these

 different cases. And you can very easily find the code that I wrote

 for that in an earlier cell here

---

#### Lesson 42: Quiz on tool use

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/289296](https://anthropic.skilljar.com/claude-in-amazon-bedrock/289296)

---

### Retrieval Augmented Generation

#### Lesson 43: Introducing Retrieval Augmented Generation

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276780](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276780)

**Video:** 09 - 001 - Introducing Retrieval Agumented Generation.mp4 | **Duration:** 5m 51s | **Platform:** jwplayer

---

#### Lesson 44: Text chunking strategies

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276782](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276782)

**Video:** 09 - 002 - Text Chunking Strategies.mp4 | **Duration:** 13m 7s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Inside of this video and the next couple of videos,

 we're gonna start to implement our own custom rag workflow

 inside of a series of different notebooks.

 We're gonna first focus on just making

 the most simple basic rag setup we can possibly make,

 and then we're going to add in

 some additional steps over time.

 Now, as a reminder, a typical rag pipeline

 looks a little bit like this to really simplify things.

 We're gonna take a source document,

 break it up into chunks of text,

 then whenever user asks us a question,

 we're gonna find some relevant chunk of text,

 put it into a prompt,

 and that's pretty much the entire thing.

 So step one of this entire flow

 is to take a source document

 and break it up into chunks of text.

 Now, believe it or not,

 this process of taking a document

 and breaking it up into separate chunks

 is one of the more complex steps of the entire rag pipeline,

 simply because how we chunk our document up

 has a huge output on the quality of our rag pipeline.

 And I wanna give you an example right away

 to help you understand why that's the case.

 So take a look at this source document.

 It's just a couple of little lines,

 and it's supposed to kind of represent some kind of report

 from a company or something like that.

 And just reading through it really quickly,

 we can see there's really three general areas.

 We have a header,

 we have a section about medical research,

 and then a section about software engineering.

 Now, there are many ways

 in which we could divide this thing up into separate chunks,

 but I'm just gonna suggest one way.

 I'm gonna say for every kind of distinct line

 inside this document, we're gonna make a separate chunk.

 So we'd end up with about five separate chunks

 like the ones you see right here.

 If you consider each of these different chunks now,

 you'll notice something really interesting.

 The third chunk of text right here

 is all about medical research.

 That's what this text is about.

 It was inside of the medical research section,

 but it contains the word bug.

 So at kind of a high level,

 if you just glanced at this paragraph alone,

 it is almost like it's kind of about software engineering,

 just because it contains the word bug.

 And then likewise, down here,

 we have the software engineering section,

 and inside of it is the word infection vectors.

 Infection vectors is a little bit more of a medical term.

 So once again, we have a section

 that is about software engineering,

 but the language inside of it is kind of about medical research.

 So now we want you to think about what would happen

 if we took these chunks and we add them into our rag pipeline.

 Let's imagine that a user asked a question

 of something like how many bugs did engineers fix this year?

 So now our job as a part of the rag pipeline

 would be to find the chunks of texts we have

 that are most relevant for the user's question.

 Well, the user said something about bugs.

 So, well, at first glance,

 this chunk of text right here seems relevant,

 just because it contains the word bug.

 So we might decide to take this chunk of text

 and add it as context into the overall prompt.

 And as you can tell right away, this is a huge error.

 The user wants to understand something

 about software engineering from the report.

 So we definitely wanted this section,

 but we erroneously got something

 about medical research instead.

 So this is an example where a chunking strategy

 can easily introduce huge errors

 and very bad context inserts into your prompt.

 So to solve this problem, we're gonna spend a lot of time

 thinking about how we're going to take

 our original source document

 and break it up into different chunks of text.

 In this video, we're going to cover

 three different chunking strategies

 or methods to divide our document

 into separate chunks of text,

 each of which have some feature or some technique

 meant to address the problem that we just saw.

 So we are going to discuss size-based chunking,

 structure-based, and semantic-based.

 The first one we're going to cover is size-based chunking.

 This is where we take our big old document,

 so a big chunk of text,

 and we just divide it into a number of strings of equal length.

 This is by far the easiest technique to implement,

 and it's also probably the one you're gonna see

 most often in production implementations.

 So let's take a look at how size-based chunking is done.

 With size-based chunking,

 we're going to take our original document

 and divide it into some number of strings

 of more or less equal length.

 In our particular case,

 we have a source document with about 325 characters.

 So we could decide just completely arbitrarily

 to divide that into three separate chunks,

 and that means each chunk would have

 about 108 characters or so.

 So we might take the first 108 characters,

 put them in the chunk one,

 the next 108, put them in the chunk two,

 and just repeat for the entire document.

 Now, very simple technique,

 but right away, it has a big downside,

 and that is that each chunk is probably gonna end up

 with some number of cut-off words inside of it.

 You could see right away, the first chunk

 has the word significant cut-off.

 So it's just significant key in the first chunk,

 and then it ends the word in the next one.

 In addition, each chunk ends up lacking context.

 So for example, the third chunk down here,

 unfortunately does not really include the section header

 that was right above it,

 and this section header would have provided a lot of context

 on what this text right here is really talking about.

 So to solve this problem that starts to come up right away

 if you use size-based chunking,

 we can implement a overlap strategy.

 An overlap strategy is where we are still going

 to do size-based chunking,

 but we're also going to include a little bit

 of overlap from the neighboring chunks.

 So for example, we have the original chunk one right here,

 but we might decide to include just a number of characters

 from the next chunk down.

 So in this case, we might include the rest

 of the word significant plus the end of that entire sentence.

 So we would end up with a chunk that looks like this

 that just has a little bit more meaning to it.

 And then for chunk two, we would still have the body

 be this area right here,

 but we'd include an overlap of some number of characters

 from before the chunk and after the chunk.

 So with the strategy, we are going to end up

 with a decent amount of duplicated text.

 For example, in this case,

 we have section one medical research inside the second chunk,

 and that was also included inside the first one as well.

 So there is duplication of text,

 but the upside here is that each chunk of text

 has in general a little bit more context provided for it.

 The next kind of strategy that you're going to see

 is structure-based chunking.

 This is where we are going to divide up the text

 based upon the overall structure of our document.

 So we might try to find headers, or paragraphs,

 or general sections and use those as our dividing lines

 for each chunk.

 Implementing this strategy of chunking with our document

 would be really easy because our document

 is written with markdown syntax.

 We know that because it has the little pounds right here,

 the double hashes for each section.

 So we might look for these little pound symbols

 and then say that every time we see this kind of symbol,

 that means we must be starting a brand new section.

 So we could very easily write out some code

 to programmatically split on the double hash characters,

 and we would end up with some pretty well-formed sections,

 like what you see right here.

 Now this might sound like a fantastic strategy,

 but unfortunately, reality just doesn't favor it

 quite so often.

 In many cases, you are going to be trying to ingest documents

 that are not formatted with markdown syntax at all.

 They might be plain PDF documents that just contain plain text,

 in which case you will not get these very clearly

 delineated sections.

 So again, even though this seems like a great technique,

 implementing it can be really challenging,

 especially if you do not have any guarantees

 around the structure of your different documents.

 The last chunking strategy that we are going to discuss

 is semantic-based chunking.

 This is where you might take all of your text,

 divide it up into sentences or sections,

 and then use some kind of natural language processing technique

 to figure out how related each consecutive sentence is.

 You'll then build up your chunks out of groups

 of these somehow related sentences or sections.

 Now, as you can tell just by the description,

 this is by far definitely more advanced technique,

 so we're not going to look too closely

 into the actual implementation.

 The only reason I mention it at all is just to make it clear

 that there's really no set finite

---

#### Lesson 45: Text embeddings

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276777](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276777)

**Video:** 09 - 003 - Text Embeddings.mp4 | **Duration:** 4m 53s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

After extracting some number of text chunks

 out of a source document,

 the next step inside of our rag pipeline

 is to wait for a user to submit a question

 or a query or something like that.

 And whenever that occurs,

 we need to take a look at all of our different text chunks

 and find some number that seem to be somehow

 related to the user's question,

 so that we can add them as context into our prompt.

 Now, this process of finding some number of text chunks

 that are related to the user's question,

 oh, there's a lot of complexity hidden there.

 But when we really think about it,

 this truly is a search problem.

 We want to take the user's question

 and search through all of our different chunks

 until we find some related content

 and then surface those in some way.

 The most common way of implementing this

 inside of a rag pipeline

 is by implementing a system known as semantic search.

 Semantic search utilizes something called text embeddings

 to better understand what each chunk of text is all about

 and somehow find the chunk of text

 most related to the user's question.

 Now, we're gonna spend a decent amount of time now

 to focus on text embeddings

 and really understand what they are doing for us.

 So let's take a look at a couple of diagrams.

 A text embedding is a numerical representation

 of the meaning contained in some text.

 These text embeddings are generated by something called

 an embedding model.

 We feed text into an embedding model,

 such as I'm very happy today

 and the embedding model is going to spit out

 a long list of numbers.

 That long list of numbers is our actual embedding.

 The numbers inside the embedding

 can range from negative one up to positive one.

 So now the question is,

 what do these numbers really mean?

 Each number inside of an embedding

 represents a score of some quality of the input text.

 Now, this is where things get a little confusing

 because I'm showing two conflicting ideas in this diagram.

 Let me break this down for you and just be super clear.

 In reality, we do not know what quality

 each number inside the embedding is actually tied to.

 So when I label that first number and say,

 "This is a score of how happy the text is,"

 that's not entirely accurate.

 We simply don't know what that first number

 truly represents.

 Nonetheless, it is very helpful

 to think of these numbers in that way.

 It is helpful to imagine that the first number

 might be one score of how happy the text is

 and the second is how much the text

 is talking about fruit, et cetera.

 Again, these labels are completely made up by me

 and we don't actually know what each number represents,

 but it's extremely helpful to think about embeddings

 in this way.

 So that's how you really want to picture each of these numbers.

 They are kind of like scores

 of some different qualities of the input text.

 Now that we have a vague idea

 of what embeddings are all about,

 let's go back over to our notebook.

 We're gonna try to create an embedding

 and get a better handle on what they are going to do for us.

 All right, so back over here,

 I've opened up a new notebook called 002 underscore embeddings.

 Make sure you open up that notebook as well.

 Inside of here, at the very top,

 I am creating a bedrock client,

 just as we've done many times previously.

 And then a little bit further down,

 I've made a function called generate embedding.

 So this is a function that we can call,

 we'll pass in a bit of text,

 it's gonna reach out to AWS bedrock

 and generate embedding for us.

 To use it, I'm gonna go down to the bottom.

 And down here, the first thing I want to point out

 is that you do need to specify a embedding model ID.

 As I mentioned a moment ago,

 there are different embedding models out there.

 So we want to use a very particular one in this case.

 It is Titan embed text V2.

 Now, you might not have default access to this model.

 If you don't, that's totally fine.

 You can hop onto the bedrock console

 and request access for it.

 And if you still can't even do that,

 you can always use version one,

 that is totally fine as well.

 For our purposes, it will work just as well as version two.

 Then inside the rest of the notebook,

 I'm gonna open up the file, report.md once again.

 I'm going to chunk it by section,

 and then I'm going to pass in the first chunk

 to the generate embedding function.

 Let's run that and see what we get back.

 So we get back a huge list of numbers.

 So these are our individual embedding values.

 If you scroll down a little bit,

 you can see the list goes on for quite a while.

 By default, you're going to get back a list of embeddings

 that is 1024 elements long.

 So as you can see, generating embeddings

 is super easy and straightforward.

 There's truly not a lot of complexity here.

 So the real question that we need to understand

 is not really so much how do we generate an embedding,

 so much as it is, what do embeddings do for us?

 And how are they useful during the rag pipeline?

 Remember, we got into this entire topic

 when we started talking about semantic search.

 So we're gonna take a quick pause right here.

 We're gonna come back in just a moment,

 and we're going to outline the entire rag pipeline

 in greater detail.

 And I'm going to show you where embeddings

 really fit into the entire process

 and why this idea of having a mathematical

 or numerical representation of some chunk of text

 is useful at all.

---

#### Lesson 46: The full RAG flow

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276774](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276774)

**Video:** 09 - 004 - The Full RAG Flow.mp4 | **Duration:** 8m 0s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

At this point in the module, I've given you a high level overview of

how that rag pipeline works.

We've spoken a little bit about text chunking and we've got just a

taste of text embeddings.

So now we're going to take these three different topics, our high

level overview of the rag process,

text embeddings and text chunking, and we're going to merge them all

together and really understand

the entire rag pipeline. So we're going to go through a complete rag

example and go through a

lot of detail and really understand everything step by step. So let's

get to it. Step number one,

just as before, we're going to take some source document and chunk it

into separate pieces of

text. So for this example, I'm going to assume I just have two pieces

of text here, just section

one, medical research and section two, software engineering. Step two

, we're going to generate

embeddings for each of these different chunks of text. Now in this

example, we're going to pretend

that we have this imaginary super perfect embedding model. And this

embedding model has two very

important characteristics. First, we're going to assume that it

always returns embeddings of length

two, so just two separate numbers. And we're going to also assume

that we know exactly what each

number is really scoring about the source text. Remember, in reality,

that is not the case. But

in this scenario, we're going to imagine we know exactly what each

number is really talking about.

So we're going to say that the first number is how much the text is

talking about the medical

field. And the second is how much the text is talking about software

engineering. So for the

first chunk of text, when we embed it, this thing is definitely

talking about medical research.

So I would give it maybe a score of 0.97 to say, yes, absolutely,

this is very much talking about

the medical field. And then it also uses the term bug, which has a

slight software engineering

connotation. In addition, medical itself is pretty heavy on software

engineering. So I'm going to

give it a score of three, four, four software engineering. Then for

the second piece of text here,

well, it's definitely talking about software engineering. So I'm

going to give it a score of 0.97 for that.

And then it also mentions infection vectors, which has that con

notation of medicine. So I'll give it

a slightly higher medicine score as well of 0.3. Now that we have

generated these embeddings,

we're going to go through an extra little step of mathematics here,

something referred to as

normalization. Now you do not really have to understand normalization

that much. This is

already going to be done for you in the vast majority of cases by the

embedding API that you

are using. This normalization step is going to scale the magnitude of

each of these pairs of

vectors to 1.0. And if you don't understand that terminology, totally

fine. Don't sweat it too much.

Just understand that we're going to do a slight little adjustment to

the actual magnitude of each

number. Once we have generated these embeddings and normalized them,

we can kind of visualize them

on a plot like this. So on this plot, I've drawn a unit circle and

each of our points representing

both those embeddings will lie exactly on the circle because we have

normalized their lengths

to exactly 1. So we've got the software engineering section up here,

and here's medical research over

here. So now that we have these embeddings, we're going to move on to

the next step. In this step,

we are going to take these embeddings and store them inside of

something called a vector database.

This is a database that has been optimized for storing, comparing,

and looking up long lists of

numbers exactly like what our embeddings are. Now at this point in

time, we kind of pause, we take a

break because this has all been pre-processing work that we did ahead

of time. So at this point,

we kind of just sit around and wait for a user to actually submit a

query to our application.

So we will imagine that at some point in time, finally, a user will

come to our app and maybe

type into a chatbot or something like that, either a question or

their query. Maybe in this case,

their question is going to be something like, I'm curious about the

company, in particular,

what did the software engineering department do this year? Now at

this point in time,

we're going to take that user's question and we're going to run it

through the exact same

imaginary embedding model. In this scenario, because the user's

question is asking specifically

about software engineering, I'll give it a score of 0.89. And then

because it's also talking about

company and again, software engineering is kind of tied up in the

medical field, I'll give it a

very slight medical score as well of 0.1. Now that we have this embed

ding, we're going to go and go

through that normalization step again. And then finally, we're going

to make use of our vector

database. We're going to take the user's query, we're going to feed

it into the vector database

and say, please search through all the vectors we have stored inside

of you and give us the vector

that is closest in nature to this one. So in our case, I would kind

of expect to get back

section to software engineering, because that's kind of what the user

asked about over here.

But let me tell you exactly what is happening inside of the vector

database that is able to

give us this very closely related result. Okay, so a little bit of

math here, don't worry,

won't be too much. So when we take the user's query and add it onto

this chart, we can see

right away that visually the user's query is just really close to

software engineering.

So you and I as humans, we could look at this chart and say, oh yeah,

clearly these two things

are very close. The user's query is very similar to software

engineering. So obviously, if we want

to find some chunks inside the vector database related to the user

query, this would be the one

that we want. But of course, we are using computers here. And our

computer doesn't actually just

make a chart like this and then look at it, there's some actual

calculation going on behind the scenes.

So let's examine exactly what that calculation is. And it's kind of

important for you to

know it because eventually when you start using vector databases,

they're going to use a lot of

terminology that's related to this kind of math going on behind the

scenes. And to actually interface

well with the vector database, you kind of need to have at least a

very basic understanding of the

math. So that's why I want you to understand it. All right, here's a

high level look at the map

that is being done inside of your vector database. To find which

embeddings are most similar to the

user's query, we want to calculate something called the cosine

similarity. This is the cosine of the

angle between the user's query and each of the other embedding stored

in the database. So we'd

want to find the angle A right here and take the cosine of it and

angle B right here and take the

cosine of it. The math for this is shown on the right hand side. The

result of this calculation

will be a number between negative one and one. If we get a result

close to one, as we did right

here, then that means that we have found an embedding very similar to

the user's query.

Results closer to negative one mean we have found an embedding that

are not at all similar to the

user's query. In our case, the cosine similarity between our user

query and the software engineering

chunk is 0.983, meaning that these two embeddings are very similar.

So this is a sign to us that we

would want to take the software engineering chunk of text and include

it in our prompt with the

user's question. Now, before we move on, one other quick thing that's

going to be a little confusing

right now, but it's going to be very, very helpful to know later on

when you start working with vector

databases. In a lot of vector database documentation, you're going to

see something referred to as

a cosine distance. This is different than the cosine similarity. It

is calculated as one minus

the cosine similarity as adjustment is often done just to give us an

easier to interpret number.

With a cosine distance, values close to zero mean you have a large

similarity and larger values

than that mean we have less similarity. Again, this is going

something you're going to see

very often in vector database documentation. So just be aware of it

whenever you see the term

cosine distance and cosine similarity. So now that we understand some

of this math at a very high

level, let's get back on track. Once we have found a text chunk with

a high similarity to the user's

question, we're going to take the user's question, add it into our

prompt and the text chunk that we

found that's most relevant and put that into our prompt as well. We

then take that prompt and send

it off to Claude. And that's the entire process in great, great

detail. So now that we understand

everything from start to finish with all the kind of tech behind the

scenes going on and even

some of the math, let's start to implement this inside of a notebook

in just a moment.

---

#### Lesson 47: Implementing the RAG flow

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276781](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276781)

**Video:** 09 - 005 - Implementing the Rag Flow.mp4 | **Duration:** 5m 39s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that we understand the entire rag flow, we're going to walk

 through an example inside

 of another notebook called 003 vector DB.

 So in this notebook, I've provided a sample implementation of a

 vector database, and I've

 called it class vector index right here.

 If you want to, feel free to take a glance at it, but I'll walk

 through everything you

 need to understand about it.

 Now, in this notebook, we're going to walk through the entire rag

 flow by implementing

 five different steps, the same five steps we just spoke about in the

 last video.

 So let's get to it.

 Step number one, I have already opened up the file and read the text

 from it specifically

 our report.MD file, which should be in the same directory as this

 notebook.

 So in step one, we're going to chunk the text by section.

 I've already added in a function to help with that.

 So the same chunk by section function we had previously.

 So to do our chunking process, I'll say chunks is chunk by section

 and pass in all that text.

 And now just to test things out and make sure I've got everything

 working correctly, I'll

 try printing out chunks at about two, and I should see a printout of

 the table of contents.

 And then if I go to three, I should see the next section down and

 then the next section

 and so on.

 Next up, let's take care of step two.

 So in step two, we're going to loop through all the different chunks

 that we just created

 and generate an embedding for each one.

 So for that, I'll say embeddings is generate embedding and I'll pass

 in the chunk for chunk

 in chunks.

 We already saw the generate embedding function a moment ago.

 All that function is going to do is take in a little bit of text and

 generate embedding

 for it.

 So if I run this, it's going to take a little bit to actually execute

 because we are making

 a API request for each chunk of text.

 And if I wanted to, I could of course also print out embeddings at

 zero just to verify

 that yes, we did in fact get the embeddings.

 Yep, there they are right there.

 Now in step three, we're going to create our vector store and store

 all these different

 embeddings inside of it.

 So I'm going to make an instance of the vector index, like so.

 And that I'm going to loop through all the embeddings that we just

 created and add each

 them one by one to this store.

 So we'll say for embedding and chunk, and I'm going to zip together

 embeddings and chunks.

 And then for each those, I'm going to add a vector of the embedding

 and then a dictionary

 with content of chunk.

 So let me explain why I'm doing this exactly.

 Why are we doing the zip operation, why are we including this extra

 dictionary on here?

 As we just discussed, eventually at some point in time, we're going

 to reach out to our vector

 database and give back a list of all the different related embeddings

 to the input.

 Now when we get back this list right here, just getting the number by

 itself, just getting

 the embedding is not really useful to us because the embedding, it

 doesn't really have a lot

 of meaning to you and I as developers.

 What we really care about is the text associated with that embedding.

 So usually whenever you store these different embeddings inside of

 your vector database,

 you're also going to include either the text from the chunk that the

 embedding was generated

 from, or at least the ID of the chunk.

 Something to at least point you back to the original chunk text.

 So in this case, I'm going to include the original chunk text along

 with each embedding.

 Again, just so when we do the lookup later on, and I get back the

 most similar chunks,

 I've got the actual text that I'm looking for.

 All right, I'm going to run that and it should take just a moment.

 And now step four, so this will be some time later, eventually a user

 is going to ask a

 question.

 So now we want to generate an embedding for it.

 So we'll say user embedding will be generate embedding.

 And my question here, I'm going to pass in as a plain string.

 I'll say something like, what did the software engineering dept do last

 year?

 So run that get the embedding.

 And now finally, here's what we go and find our relevant documents.

 So I want to search the store with the embedding.

 And I want to find the two most relevant chunks, not just the most

 relevant.

 I want to get the two chunks that seem to be most relevant to this

 question right here.

 So for that, I'll do a results store dot search, I'm going to pass in

 the user embedding.

 And I'm going to pass in another argument here of two, because I want

 to find the two

 most relevant chunks.

 And then I will print out for doc and distance in results, I'm going

 to print out the distance,

 a new line, and then the documents content, and because each chunk

 here is really, really

 large, I'm going to print out just the first 200 characters, and then

 another new line

 like so.

 And I'll run this, and there's our result.

 So we get back section two as our best result.

 We also see the cosine distance here.

 So it's 0.71.

 And the next closest chunk is at 0.72, and that was the methodology

 section.

 So these were the two chunks that were found most relevant for the

 user query that we just

 submitted.

 All right, so that is our entire rag workflow.

 Now all this works, but there is one or two scenarios where

 everything doesn't quite work

 as expected.

 So there are still a couple of improvements that we could add into

 our workflow, and

 let's start to discuss those in just a moment.

---

#### Lesson 48: BM25 lexical search

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276776](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276776)

**Video:** 09 - 006 - BM25 Lexical Search.mp4 | **Duration:** 10m 0s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

We've got the first iteration of our rag pipeline put together.

 Everything looks good right now, but we're going to very quickly

 realize that, well,

 maybe we are not getting the best search results.

 Let me show you an example.

 If you open up the report.md file and scroll down just a little bit

 to the software engineering

 section, here it is right here, you'll notice that it has the

 statement of INC, which is short

 for incident 2023 Q4 011, and it looks like that search term occurs

 three times inside of this

 paragraph. So here's one right here, two right there, three right

 here. And if I continue

 searching throughout the document, I'll see that it is also mentioned

 down here inside of section 10,

 cyber security and analysis. It's mentioned inside the header and

 then one time inside the

 actual paragraph itself right there. Now I want to try searching for

 this term, this incident 2023

 Q4 011 and we're just going to see what happens. In other words, what

 search results do we actually

 get back using semantic search? So back inside of my notebook, I'm

 going to update the user query

 right here to be what happened with incident 2023. Then I'm going to

 rerun all cells and we'll see

 what result we get. All right, so take a look at this. It's a little

 bit surprising result.

 We get section 10, which is good. That's definitely the result we

 would want to see

 first in the list, because section 10 is all about this incident. But

 then very surprisingly,

 the next result is section three, financial analysis. Well, if you

 open up section three,

 right here, you'll notice that nowhere inside of section three is

 that incident ever mentioned.

 So we are getting some output from our semantic search that is a

 little bit surprising here.

 What we really want to get back was section 10, and then section two.

 But what we got was

 section 10, and then unfortunately, section three. And section three

 appears to be completely irrelevant

 when it comes to investigating this incident. So even though the

 semantic search technique we put

 together is really fantastic, and it's going to work well a lot of

 the time, there are these

 corner cases where it really just doesn't quite work as expected. So

 let's take a look at a technique

 we can use to improve our search results and hopefully get the

 results we want, which is

 section 10, and then section two. All right, so here's the general

 strategy we are going to use.

 Whenever a user asks a question, we're going to feed that question

 into our semantic search side

 of the equation, which is generating those embeddings and using the

 vector database. But then in parallel,

 at the same time, we're also going to implement a separate lexical

 search system. Now lexical

 search is more like classic text search, where we are going to break

 down the user's question

 into individual words, and then trying to find chunks of text that

 seem to include those words.

 Once we go through the search process in both different systems, we

'll get two sets of results,

 and then we will merge the results together. And the hope here is

 that we'll get a little bit

 better balance of search results, where we get both the kind of

 semantic aspect and the plain

 text search aspect included in one result set. So hopefully we will

 eventually get a result that

 looks like this over here. Now to implement this lexical search,

 there are a tremendous number of

 methods for implementing text search. But a very common method that

 you're going to see used in

 rag pipelines, like the one we are building right now, is a technique

 referred to as BM 25. Now this

 is short for best match 25. In the rest of this video, I'm going to

 give you a high level overview

 of how this algorithm works. And we're going to take a look at a

 notebook that actually implements

 BM 25. So we'll be able to play around with it directly and see what

 kind of search results we

 get. So here's the general idea behind the BM 25 algorithm. Now again

, I'm going to give you a high

 level overview, and I'm going to leave out a couple of smaller steps

 just to simplify things and make

 it easier to understand. Everything is going to begin with us

 receiving a user's query. And let's

 imagine this case, they put in a search string like this right here,

 just a so the word a,

 and then incident 2023 key for 011. In step one, we're going to token

ize the user's query. And that

 means we're going to break it up into separate chunks. There are

 different ways in which we can

 tokenize a user's query. But right now we're going to use a very

 simple method, which is to just

 remove punctuation and break up the term all terms based upon spaces.

 So in this case, I would end

 up with separate search query terms of a and an incident 2023. Next,

 we're going to see how often

 each of these different search terms occurs across all of our

 different documents,

 or in our case, really text chunks. So let's imagine that we only

 have two text chunks in this

 scenario. So we're going to see how often the word a and the word

 incident blah, blah, blah,

 occurs across each of these chunks. And it looks like this first

 chunk right here has a right there,

 a right there. And then the second one has a a. So in total, I would

 count all those up,

 and I would have five a's. And then I would see how often I have

 incident 2023. It looks like

 there's only one right here. So I'd end up with a frequency of one.

 Next up, we're going to assign

 a relative importance to each term based upon its usage frequency. So

 in the case of the word a,

 it was used five times. And because it was used rather often, we're

 going to say this term is

 not super important because it is used all the place across all of

 our different documents,

 or an again, our case are text chunks. But incident 2023, that was

 used very infrequently,

 which means it is probably going to be of greater search importance.

 Then finally,

 in the last step, we're going to find the text chunk that uses the

 higher weighted terms more

 often. So in this case, the first text chunk right here, it only has

 two a's, whereas the

 second one has three a's. But a's are not super important because

 they're used rather frequently

 across all of our different chunks. However, text chunk one uses

 incident 2023 one time,

 and that is a highly weighted term. It's a really important term. So

 in this case, we would say,

 this is probably our best text chunk. And we would want to return

 this as a prime search result.

 Now again, to see all this in action, let's take a look at a quick J

upyter notebook.

 So back inside of my editor, I'm going to find a new notebook. This

 one is called 004

 underscore BM25. Again, at the top, I've got some code relating to

 chunking by section.

 I then got a basic implementation of BM25 in the form of this class

 called BM25 index.

 So I'm going to collapse that cell, make sure I run it. I'm going to

 read the contents of our

 report file. And then we're going to go through three separate steps

 here. We're going to first

 chunk the text by section. We're going to create a BM25 index store,

 and we're going to add each

 text chunk to it. And then we're going to attempt to search the store

. And once again, our hope here

 is that we're going to maybe get some search results that look a

 little bit closer to this,

 maybe not exactly these results. But I definitely want to see the

 sections that use incident 2023

 before I ever see some results that don't include that search term at

 all. So let's see how we do.

 Okay, let's take care of step one here. We need to chunk the text by

 section.

 So we've gone over this a couple times now, we'll say chunks is chunk

 by section with text.

 Next up, I'm going to create a store.

 And I'm going to loop over all my chunks and add them in as documents

 to the store.

 So I'll say for chunk in chunks, store, add document.

 And I'll pass in the dictionary with a content of chunk. I'm going to

 run that.

 And now finally, I'm going to search over the store. I'll say store

 search. And I'll use that

 same term that I used in the previous notebook that did not give us

 the very good results. So I'll

 ask what happened with incident 2023 Q 4011. And I'm going to ask for

 the first three search results.

 And then I'm going to print up the results very nicely just so we can

 interpret them really well.

 We'll say for doc distance in results, and I'll print out the

 distance, a new line,

 doc with content. And again, I'm only going to print out the first

 200 lines.

 And then how about a new line, a couple of separators and another new

 line.

 I'm going to run this and we'll see what we get. All right, so that's

 a much better search

 result than what we had before. Now I'm going to see software

 engineering first,

 and then cybersecurity after that, and then methodology down here. So

 now I am actually

 prioritizing the sections that use the most important search term

 inside my query, which was the

 incident 2023. And you'll notice that I don't really have quite as

 much importance around the

 other terms like what happened with those aren't quite as

---

#### Lesson 49: A multi-search RAG pipeline

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276779](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276779)

**Video:** 09 - 007 - A Multi-Search RAG Pipeline.mp4 | **Duration:** 6m 45s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

We now have an implementation for semantic search

and an implementation for lexical search.

So now we need to wire these things up together.

Let me show you how we're going to do that.

The first thing to notice is that the implementation

for both these searching functionalities

have the almost exact same public API.

So we have a vector index class on the left hand side

that has methods like add document and search.

And we have almost identical methods inside

of our BM25 index as well.

So to connect these two things together

into a single search pipeline,

we're going to wrap them up inside of a new class

that we will call Retriever.

This Retriever is going to receive a user's question

and then forward it on to the search methods

of vector index and BM25 index.

The Retriever will then receive the results from both them

and figure out some way of actually

merging the results together.

Now it turns out that the merge operation

is actually a little bit tricky.

So I want to go into a little bit of detail

on how you can merge the results

that are coming out of these different search methodologies

to combine the results together.

We're going to use a technique known as reciprocal rank fusion.

The easiest way to understand this technique

is to go through an example.

So let's do that right now.

Let's imagine that we run a search on the vector index

and we get outputs of section two, seven, and then six.

And then we do the same exact search on BM25

and we get six, two, and seven.

So now we need to take these two lists of results

and combine them together in some way.

To do so, I'm going to take all the search results

and put them together on a single table, like so.

So now I've got text chunk two, seven, and six

and I've recorded the rank from the vector index output

and the rank from the BM25 index output.

And to be clear, when I'm talking about rank,

I just mean kind of search output position.

So rank one, two, three, rank one, two, three,

I'm just kind of putting those same exact numbers

on this chart down here.

Once I have all those ranks in place,

I'm then going to apply a formula.

Here's the exact formula right here

and I know it looks really terrible,

but don't worry, it's not as complicated as it looks.

Here's how it works.

For every rank column we have,

so like that column right there and that column right there,

we're going to write out a separate term.

So here's the term for the first column,

here's the term for the second column.

In the first term, we're going to write out one over one plus

whatever number is right there.

So we end up with one over one plus one.

And then the second term will be one over one plus

whatever number is right there.

So one over one plus two.

Once we have calculated the score for each text chunk,

we're then going to sort the table based upon score

from greatest to least.

So we'd end up with something like this.

So we'd end up with text chunk for section two

as being the most relevant search result.

Section six would be the second most

and section seven would be the least relevant.

And this kind of makes sense.

We can kind of visually confirm

that these outputs make sense

if you just look at the individual rank outputs

from each search methodology.

So section two was rank one and two.

That means, hey, in general, it's trending up towards the top.

Section six is one and three.

That's kind of like in the middle.

It has a good score and a bad score.

And then section seven is two and three.

And so it trends down towards the bottom.

So with a visual inspection,

the results I think do make a decent amount of sense.

All right, so now that we understand

how we're going to combine the results together,

let's go back over to our Jupiter notebook.

And we're going to take a look at a sample implementation

of a retriever class and a sample implementation

of merging the results.

Okay, so back over here, I move on to the next notebook,

which is 005 hybrid.

Once again, there's a lot of setup up here.

So I've got the vector database implementation,

the BM25 implementation.

And now I've added in a implementation

for the retriever class as well.

The retriever has method of add document.

And if you call add document,

it's just going to take whatever document you pass in

and pass it off to each of the different indexes

that are contained inside the retriever.

So in our case, our indexes are the vector index

and the BM25 index.

Then the retriever also has a search function.

If you pass in some query text to it,

that query text will be passed off

to each of the different indexes

that are contained inside the retriever.

We then take all the results that come back

and combine them together.

So here's the merge logic that implements

that reciprocal rank fusion.

All right, so time to do a little test here.

Now I want to recall what led us down this entire path

was back on our vector database implementation.

So this notebook over here,

we found that if we search for something like,

what happened with incident 2023,

we got back some unexpected results

where we had section 10, which was good as the first result.

And then section three was the second result.

And that was really unexpected.

We want that second result to be software engineering.

So when we now run this hybrid approach

that combines together multiple different indexes,

my hope is that we're going to get first section 10

and then whatever section the software engineering one is.

I think it's section two.

So let's test this out inside of our new notebook.

I'm going to go down to the bottom

and I'll do a results is retriever,

search what happened with incident 2023, Q4011.

And I'm going to get the first three search results.

And then once again, I'm going to print them all out,

like so.

And I'll do the score, a new line,

the content of the document with just the first 200 lines.

And then just a little separator between each chunk.

So I'm going to run this.

And now we get a some much better search results

than what we have before. So I've got section 10,

and then section two, exactly what we wanted.

And then section five, but that one's not super relevant here.

So we now have a much better output

by combining together these two different search techniques.

And the nice thing about this is we were able to author

each of these indexes kind of in isolation.

They're their own separate classes.

And because we made each implementation

have the same exact API with that search function

and the add document function,

we were able to easily wrap them up

into this larger retriever class.

So if you wanted to, we could absolutely add in

some additional search index here

that maybe implements some other

completely different searching functionality.

And as long as it has that search function

and the add document function,

we can very easily add it,

have it generate some results

and then merge the results along with the results

coming from the other search methodologies as well.

Okay, so let's say this is a good success,

but we're not quite done yet.

There's still some other techniques

we're gonna go over to improve the accuracy

of our rag pipeline.

---

#### Lesson 50: Reranking results

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276775](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276775)

**Video:** 09 - 008 - Reranking Results.mp4 | **Duration:** 6m 9s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The hybrid based retrieval approach that we have implemented is

working pretty well.

So as we saw at the end of the last video, if we search for what

happened with this incident,

we're going to get first the cybersecurity and then software

engineering.

However, there are still some weak points inside our retrieval

process.

Let me show you an example.

I'm going to update the query here to be, "What did the engineering

team?"

And notice I put in not engineering, but just in abbreviation of ENG.

What do the engineering team do with incident 2023?

So now that I am asking specifically about the engineering team

and the incident, I would kind of expect to see section two pop up a

little bit.

Because remember, section two is about software engineering

and the software engineering team.

And inside of the body of this section, there is mention of this

incident.

So now this query in my mind personally, I think this really is the

most relevant section.

But if I rerun this, we're going to see that we still end up getting

section 10 and then section two.

So it's clear that even though we have added in a lot of complexity,

well, again, still a couple of rough edges.

So in this video, we're going to take a look at yet another technique

that we can add in to improve our retrieval accuracy.

This technique is referred to as re-ranking.

And the idea behind this is super simple.

After going through everything that we just covered in the last video

,

so we're going to still run our vector index and the BM25 index

and merge the results, we're then going to add in another post

processing step,

something called a re-ranker.

The re-ranker is going to take some number of our search results

and pass them off to Claude inside of a prompt.

So here's a sample prompt that we might use for a re-ranker.

We are going to ask Claude to take a look at the user's question,

specifically what happened with incident so and so,

and then we're going to provide all the different documents that we

have currently found

that seem to be somehow related to the user's question.

And then we're going to give Claude a very simple task.

We're going to ask Claude to return the three most relevant.

And it doesn't have to be three, just some number of the most

relevant documents

in order of decreasing relevance.

So in other words, go through all the supposedly relevant documents

and just reorder them or re-rank them

so that the most relevant document is at the top.

So Claude is going to take in the instructions and of course,

it's going to execute the task perfectly and send us back a reorder

list of relevant documents.

To understand how this really works,

let's take a look at a notebook where I have implemented this re-

ranking strategy.

So back over here, I've opened up a new notebook called 006

underscore re-ranking.

There is a ton of setup code inside of here,

and then eventually we get to the implementation of a function called

re-ranker fn.

This function is going to be called automatically by the retriever

after we have ran the initial search process with the vector index

and the bm25 index.

So we've already gotten back the initial results.

We've already merged them and now we're going to take these merge

results

and pass them into this re-ranker function.

So we are going to iterate over all those documents we found.

We're going to print them up in a nicely formatted XML structure.

We're then going to insert that list into a larger prompt, the one

you see right here.

This prompt is asking Claude to take a look at the user's question

and take a look at the documents that we have found already.

We are then going to ask Claude to return a list of documents in

order of decreasing relevance.

So the first documents that we get back should be the most relevant

results.

Then as usual, we're going to go ahead and use a assistant message

pre-fill and a stop sequence

just to ensure that we get back some well formatted JSON.

Remember, we could use tools here to ensure that we get back well-

structured JSON,

but in this case, it would be a lot of extra work just to get some

structured data back.

And I think using this pre-fill with the stop sequence is definitely

appropriate.

Now, before I say anything else, there is something I want to clarify

that might be a little confusing.

You'll notice that in this prompt, I'm referring to some document IDs

all over the place.

But in the diagram, I showed you just a moment ago,

there is no mention of any IDs whatsoever.

So what are these document IDs exactly?

Well, it really comes down to efficiency.

If we use the prompt, I showed you that diagram just a moment ago,

and asked Claude to just give us back the most relevant documents or

text chunks,

we're essentially asking Claude to send us back the full text of

every single text chunk.

This would be extremely inefficient because we would just be sitting

around and waiting for Claude

to copy the text out of each individual chunk.

So a better solution would be to generate some random IDs ahead of

time

and assign them to each document or essentially text chunk.

And then ask Claude to just return those IDs.

This will be significantly more efficient because Claude can return

just a very simple little bit of text

that's going to tell us the exact order of chunks that we should be

making use of.

Well, now that we understand how everything is working,

let's actually run the notebook and see if we get some reasonable

results.

Now, I've already ran all the different cells inside of here.

Make sure you run all the cells as well.

I'll go down a little bit and get down to the very bottom here.

We're going to ask that same question as before.

What happened with incident 2023?

So I'll run that and I'll get back same results we had previously

back when we had the just hybrid approach.

So I got section 10 and then section two, so nothing bad.

But now I'm going to update the query to the one that gave us just a

little bit of trouble

a moment ago with the hybrid approach.

So what did the engineering team do with incident 2023?

And again, my expectation here, my real hope is to see section two

pop up to the top.

There's no guarantee that's going to happen.

You might get different results than I, but that's personally what I

'm going to hope for.

So I'm going to run this and then sure enough, we do in fact get

software engineering popped up to the top.

So that's definitely a good result.

Claude has noticed that the user query here really cared about

specifically the software engineering team

and their relationship to this incident.

While adding in this re-ranker was definitely a success.

On the downside, it increases the latency of our search pipeline

because now we have to wait for a call to Claude to resolve.

But on the plus side, it also without a doubt increases the accuracy

of our search pipeline.

---

#### Lesson 51: Contextual retrieval

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276778](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276778)

**Video:** 09 - 009 - Contextual Retrieval.mp4 | **Duration:** 6m 27s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, we're gonna take a look at another technique

 for improving the accuracy of our rag pipeline.

 This technique is known as contextual retrieval.

 The idea here is that whenever we take our original source

 document and split it up into chunks,

 each individual chunk no longer contains context

 of the original document.

 Contextual retrieval aims to fix this

 by adding in a pre-processing step

 before we insert each text chunk into our retriever database.

 So we're going to take each individual chunk

 that we have produced and our original source document

 and place it into this prompt and then send it off to Claude.

 This prompt, as you can read, is gonna ask Claude

 to take a look at this individual text chunk

 and the contents of the overall source document.

 We then ask Claude to write out a little bit of text

 to situate or kind of place or add some context

 to the individual text chunk.

 We're then going to repeat this process

 for each text chunk we have over here on the left-hand side.

 So as an example of the output we might get from this,

 let's imagine that we put in section one,

 software engineering right here,

 which includes a mention to that 2023 incident.

 And there's also a similar mention

 down inside of section two, cybersecurity analysis.

 The added context that Claude might generate

 could look like this.

 Might say something like this is a section

 from a larger report and this section

 includes a mention of this incident

 and that incident is also mentioned in this other section.

 So now we're taking this input chunk

 and adding some additional ties to the larger document.

 Once Claude generates this extra little bit of context,

 we're then going to join together that context

 with this input text into something

 that we're referred to as our contextualized chunk.

 So right here is the extra context that Claude generated

 and out here is the original chunk text.

 We will then use this contextualized chunk

 as the input to our vector index

 and our BM25 index as well.

 Now right away a very common problem

 that you're probably going to run into,

 your original source document right here,

 we're saying that we want to take all the text

 out of that original document

 and put it into a single prompt

 and then send that off to Claude.

 In many cases, this original source document

 might be simply too large to fit into Claude by itself.

 If you're in that scenario,

 don't worry, there's still a way we can make use

 of contextual retrieval.

 If our source document is too large

 to fit into a single prompt, here's what we might do.

 Let's imagine that we are trying

 to contextualize chunk nine down here.

 So this is the one that we really want to feed into Claude

 and ideally we would provide the original source document

 in its entirety.

 But instead we might decide to include some of the chunks

 from the very start of the document.

 So maybe chunks one, two, and three right here.

 And then some of the chunks right before chunk nine.

 The idea here is that the starter chunks

 at the very top of the document provide

 possibly a summary or an abstract

 or something to kind of explain

 what the entire document is about.

 And then the chunks right before chunk nine

 are going to provide some context for chunk nine itself.

 And chunk four, five, and six,

 while they might be important,

 they're probably not going to provide

 quite as much context as all the others

 that we might include for chunk nine.

 So this is how we can significantly

 pair down the amount of text we're going to push into Claude

 to provide this context when trying to contextualize chunk nine.

 Now once again,

 let's take a look at a Jupyter notebook

 to get a better idea of how this stuff works.

 All right, so back over here,

 I've opened up a new notebook called 007_contextual.

 We still have a ton of helper code.

 And then I've added in a new cell

 with a function named add context.

 This function is going to take in a single text chunk

 that we're trying to generate some context for

 and some source text.

 So that would be the text from the original source document.

 We're then going to ask Claude

 to write out some succinct context to kind of place

 or give us a better idea

 of what this particular text chunk is really all about

 in the context of the larger document.

 We're then going to get back our response.

 We're going to add together whatever response we got

 with the original text chunk and return it.

 So I'm going to run that cell

 and I've already ran all the cells above it.

 Now let's test this out really quickly.

 So I'm going to chunk the source document like so.

 I'm going to add in a new cell right here

 and I'm going to call add context with chunks at five

 and the report text.

 And let's see what we get out.

 All right, here's my output.

 Now this might look like a lot,

 but remember this is both the added context,

 which is really just that part right there,

 plus the text from the original chunk.

 So section two software engineering right there.

 So in this case, our added context says,

 this is a chunk of section two from this larger report

 and it is following the methodology

 and it's before financial analysis

 and it is a part of a larger report

 that covers 10 separate research domains.

 So I would say this is some pretty effective context.

 It really gives us a better idea

 of what this individual section is a part of,

 kind of the nature of the surrounding report

 or the surrounding document around it.

 All right, so next up in the next cell down,

 I'm going to still create my two indexes and the retriever.

 And then here's where things start to get interesting.

 So again, if we have a really large source document

 where we can't fit everything into a single prompt,

 we might use this little extra strategy

 where we include just some starter chunks

 and then chunks from right before the chunk

 that we're trying to situate.

 That's what this code right here does.

 I've got some configurable variables right here.

 So we are going to try to take two chunks

 from the very start of the report

 and then two chunks from right before the chunk

 that we are trying to contextualize.

 I've then got some code to make sure

 we don't get any duplicates or anything like that.

 I'm going to get all that context from the report,

 join it together and then pass it off

 to the add context function with the chunk

 that we're currently operating on.

 Once we get back that contextualized chunk,

 we will add it into our retriever.

 So I'm going to run this.

 This will take a while to complete

 because we are generating context

 for every section inside of our report.

 But once it is done, we can then go down and test it out.

 Now in this case, using the same query right here

 of what did the engineering team do with incident 2023,

 we're probably still going to get some really good output

 because we already had good output.

 But you can imagine that by including this extra context,

 if we add a much more complex document

 with individual text chunks or sections

 that have a lot more ties between the overall document,

 well, then I would expect this contextual retrieval technique

 to give me some better accuracy.

---

#### Lesson 52: Quiz on Retrieval Augmented Generation

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/289295](https://anthropic.skilljar.com/claude-in-amazon-bedrock/289295)

---

### Features of Claude

#### Lesson 53: Extended thinking

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276788](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276788)

**Video:** 10 - 001 - Extended Thinking.mp4 | **Duration:** 8m 50s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's examine one of Claude's more advanced features known as

 extended thinking.

 Extended thinking gives Claude time to reason about the user's query

 before generating

 a final response.

 In many chat UIs, this will be displayed as a separate thinking

 process, which the user

 can optionally look at to get a better idea of how Claude is

 approaching their problem.

 In general, enabling extended thinking will allow Claude to tackle

 more complex tasks

 with greater accuracy, but there are some big trade-offs here.

 You are charged for tokens generated by Claude during the thinking

 phase, and the phase itself

 takes some amount of time to complete.

 So with increased intelligence comes increased cost and there's

 increased latency as well.

 Now, a common issue around extended thinking is deciding when to

 enable it, and the answer

 to this is really simple.

 You're going to rely on your prompt evals.

 So you're going to write out a prompt, you're going to run an eval on

 it, and if the accuracy

 is not where you want it to be, and you've already spent some good

 amount of effort on

 improving your prompt in the first place, that is when you would want

 to consider enabling

 extended thinking.

 Now, the use of extended thinking is really straightforward.

 Remember, when we normally use Claude, we send over a user message

 that might contain

 a text part, and then we're going to get back an assistant message

 that contains a text

 part as well.

 When we start to enable extended thinking, the response we get back

 is going to contain

 a new part type.

 And we have not seen before.

 It's called the reasoning content part.

 Inside of this part is going to be the text that was generated while

 Claude was thinking.

 There's something really interesting about this reasoning content

 part that I want to

 show you right away, because you're going to see it really quickly as

 soon as you start

 writing out some code and making requests with extended thinking.

 So this kind of interesting thing is the signature.

 So on the right hand side, I've got an example of an assistant

 message that includes a reasoning

 content part and a text part as well.

 Inside the reasoning content part, you'll notice that there is

 something called a signature.

 The signature is a cryptographic token.

 Here's what the signature does.

 If you want to take this message and send it back to Claude as part

 of the conversation

 in the future, Claude wants to make sure that you did not modify the

 text in the reasoning

 content block in any way.

 The signature is used to make sure that you did not change that text.

 That doesn't want you changing that text at all, because it is used

 very heavily during

 response generation.

 And if developers were allowed to modify that text, they could

 possibly steer Claude in a

 unsafe direction.

 There's one other aspect of reasoning content parts kind of related

 to this idea.

 So in some cases, you might get back a reasoning content part that

 only has a field of redacted

 content.

 This occurs whenever Claude generates some thinking text that gets

 flagged by some internal

 safety system.

 The redacted content is the actual thinking text, but in a fully

 encrypted form.

 It is provided to you so you can give this full message back to

 Claude in the future as

 part of a conversation without Claude losing any context on its

 previous thinking.

 To really understand extended thinking, we need to write out a little

 bit of code.

 So let's go back over to a Jupyter notebook.

 I've made a new notebook called 001 thinking.

 Inside of here, the first thing we need to do is update our chat

 helper function that

 we have put together previously.

 So I'm going to find the chat function right here.

 And I'm going to begin by updating it to add in some additional

 keyword arguments.

 I'm going to pass in a thinking argument and by default, it will be

 false and a thinking

 underscore budget of 1024.

 This thinking budget is the number of tokens that we want to allow

 Claude to spend on generating

 its thinking portion of the response.

 So 1024 means Claude can spend at most 1024 tokens on generating some

 thinking thoughts

 ahead of time before it will be forced to finally respond to us in

 some way.

 1024 is the minimum.

 So this will serve as our default.

 And if we ever want to give Claude a little bit more allowance and

 allow it to think longer,

 we might bump this value up a little bit.

 The optimal value right here, again, it comes down to your emails.

 There's really no rule of thumb where I can just say to you, oh, yeah

, 1024 is perfect.

 You have to rely upon your emails to decide upon a budget that is

 right for your particular

 application.

 So now we have added in these keyword arguments.

 We're going to do a little bit more refactoring, a little bit lower.

 I'm going to find the if statement of if text editor, so you might

 recall previously,

 we added in the ability for Claude to use that text editor tool.

 And to enable it, we had to create this additional parameter of

 additional model request fields.

 To enable thinking, we have to place an additional parameter on this

 dictionary.

 So we're going to do a little bit of a refactor here, just so it's

 easier to use the text

 editor and thinking separately.

 Here's what we're going to do.

 Right above the if statement, I'll make a new dictionary called

 additional model fields,

 and we'll start off as empty.

 Then inside the if statement, I'm going to delete everything from the

 colon right there

 of tools to the start of the line.

 And I'll say additional model request or just no request fields.

 There we go.

 And then I will index into this with tools.

 And I'll set that to the list, like so, so we should have additional

 model fields.

 We're looking up tools inside there, and we're going to set that to

 be this whole list.

 Then underneath that, I'm going to place a new if statement, and I'll

 say, if we are

 enabling thinking, then I want to add into the additional model

 fields.

 A thinking property, that's going to be a dictionary with a type of

 enabled and budget

 tokens of our thinking budget.

 And then finally, I'm going to add into this params that we're going

 to send off to a

 converse function.

 I'll say params, additional model request fields.

 And that's going to be the additional model fields dictionary that we

 just created a

 moment ago, and that should do it.

 So now I'm going to make sure I run that cell.

 And then if we scroll down a little bit, I already put together a

 cell for us a little

 template here, where you can very easily test out thinking, I'm going

 to add in a query

 to Claude, and I'll ask it to maybe write a one paragraph guide to rec

ursion.

 And I want to enable thinking.

 So I'll put in a thinking of true, I'll then run this, print out all

 the parts, and we'll

 see what we end up getting.

 Well, before long, I get my response.

 And we can very easily see that it does in fact have two separate

 parts.

 So here's part one right here.

 That is our reasoning content part inside of it is going to be the

 thinking text.

 So that is giving us a clue as to what Claude is thinking about here.

 And then we've got our signature, which is going to make sure that we

 never try to tamper

 with or change this text right here, in case we ever decide to send

 this part of the message

 back to Claude to follow up our conversation.

 And then we've got the final text or the real guide that was

 generated down here a little

 bit lower.

 Now in some cases, you might want to test out your application and

 make sure that the

 code you wrote to handle these responses can handle a reasoning

 content that has the actual

 text.

 And you also want to make sure that it can handle getting a response

 that has the redacted

 content as well.

 So there actually is a way that we can force Claude to give us back a

 redacted content

 field just if we want to test out our application and make sure that

 we can handle this redacted

 content stuff.

 To force Claude to give us back some redacted content, we can update

 our prompt that we're

 sending in right here to include a very special string, one that I

 have already written out

 ahead of time inside of this notebook.

 So if you scroll up to the very top inside of client setup, you'll

 notice I put in their

 thinking test string right here.

 So that is the magic string.

 It's even labeled as magic string.

 If you include this exact string right here inside of your user

 message, Claude is guaranteed

---

#### Lesson 54: Image support

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276789](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276789)

**Video:** 10 - 002 - Image Support.mp4 | **Duration:** 10m 45s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next advanced capability of Claude that we are going to investigate

 is Claude's vision capabilities.

 Whenever we send a user message off to Claude, we can optionally

 include images inside of the message.

0আমর0:10:320 --> 00:00:13,390
 We can then ask Claude to do just about anything you can possibly

 imagine with those images,

 so we can ask Claude to tell us what is contained inside the image.

 We can ask Claude to compare different images. We can ask Claude to count

 different objects.

 Really, there's a lot of different possibilities here.

 The first thing I want you to understand around image handling is

 some of the different restrictions

 or requirements, so we can send up to 20 images across all the

 messages inside of a single request.

 There are some limitations around the size of each image and the

 height and width of each as well.

 And then finally, you need to understand that whenever we send an

 image off to Claude,

 that is going to count as some number of tokens that we are going to

 be charged for.

 And there is an equation you can use to roughly calculate how many

 tokens you'll be charged for

 based upon the height and the width of your image in pixels.

 Now to include an image itself, this is just yet another type of

 message part.

 So inside of our list of parts, we might add into a user message,

 we're going to add in a new type of image. We are going to include

 one image part for every image

 that we want to send to Claude inside of a message. So let me show you

 what I mean by that.

 If we want to include just one single image, that means we'll send a

 user message with

 one image part. And if we want to send a message off that has two

 separate images,

 those will be two separate image parts. We're just going to keep

 adding them to that list of parts

 inside of the user message. So now that we understand some of the

 technical limitations here and how

 we send an image off, there's something really important that I want

 to address right away.

 Whenever a engineer starts making use of images with Claude, well, I

 noticed very often they start

 using prompts that are very simple, even kind of like the prompt I've

 got in this example right here.

 The number one way to get a good results out of Claude when you are

 making use of images is to

 continue to have a strong focus on prompting techniques. So if you

 just throw a image off

 to Claude and then put in a very simple prompt, very often you are not

 going to get back a good

 result. For example, consider the conversation on the right hand side

. I put in an image with

 12 marbles. I actually tested this by the way, and I asked it very

 simply how many marbles are

 in this image. And sure enough, I got back an incorrect count of 13.

 We can dramatically increase

 Claude's accuracy when working with images by using the same kind of

 prompting techniques

 that we've already learned earlier on inside this course. So

 techniques like providing guidelines,

 providing analysis steps, or by using one shot or even multi shot

 examples. So let me show you

 two ways in which we could very easily enhance this prompt and

 actually get back the correct

 result. And again, I actually tested this out and made sure that

 these examples at least for me

 worked as expected. So the first thing we might do is provide a

 series of steps for Claude to go

 through in analyzing the image. Now, of course, this is only really

 going to work if we kind of

 already understand the content of the image that we're feeding into

 Claude. So in this scenario,

 I might ask Claude to first take a look and try to identify each

 individual marble and just count

 each of them one by one, and then ask it to recount a second time to

 verify the initial account and

 provide it a different mechanism or different strategy for counting

 the number of marbles.

 And then finally, at the bottom, I ask, okay, now let's kind of

 compare those two different counts

 and figure out what the correct answer is. So by providing a more

 sophisticated prompt,

 I was able to get results with a correct count of 12 marbles. Another

 technique we might use here

 is one shot or multi shot prompting. So here's how that would work.

 Inside of my user message,

 I can alternate the presence of a image part and a text part. So in

 this scenario, I have a image

 part up here, a text part underneath it, and then another image, and

 then a text part. In the initial

 pair, I provide a image with 11 marbles and then say very plainly,

 the image above has 11 marbles

 inside of it. Providing an example like this can easily improve Claude

's accuracy when it goes to

 tackle your image later on. As usual, I would like to test out this

 feature in Claude inside of a

 Jupiter notebook. But this time around, we're going to have a little

 bit more complicated example.

 And I want you to understand the scenario that we're going to walk

 through here inside of our

 notebook ahead of time by showing you a quick diagram. All right, so

 here is a sample use case

 of how we might use Claude's image support capability. So in case you

're not aware, in many parts of

 the United States, we have really bad wildfire problems where

 wildfire fire will begin,

 sweet through an area, and burn down a ton of houses. And because

 this is a very common risk,

 a lot of people want fire insurance to ensure their home in a case it

 gets burned down. But these

 insurers are very much aware that a house can absolutely be burned

 down tomorrow or next year or

 very shortly. So these insurers will very often require a homeowner

 who wants to ensure their home

 to trim trees or even cut trees down entirely around their house. Now

, the insurer needs to

 actually verify and make sure that the homeowner is taking care of

 the trees appropriately.

 But to verify that, they might have to send out a person to inspect

 each property and probably

 do that inspection maybe once every year or once every two years.

 That would become expensive

 really, really quickly. So one way that we can automate this process

 is by getting high resolution

 up to date satellite imagery, and then feed it into Claude and ask Claude

 for a fire risk assessment.

 We might ask Claude in particular to try to detect the main residence

 on the property. So in other

 words, inside of a satellite image of a property, find the main home

 that is presumably insured.

 And then take a look for maybe tree branches that are overhanging the

 residence, which is a very

 common risk of fire. Maybe try to gauge how difficult it is for fire

 services to actually

 access the residence. So make sure in other words, there's kind of a

 clear path to get to the home.

 And also take a look at the trees around the home and make sure that

 they are not too

 closely or tightly packed, which in its own right could be a fire

 risk as well.

 All right, so let's go over to notebook and see how we could

 implement this.

 I'm inside of a new notebook called 002 images. Inside of here, I

 have already put together a

 starter prompt for us. Now notice that this prompt is highly detailed

 and walks Claude through

 different points or different ideas that I want analyzed inside the

 image. I could have written

 out a very simple prompt of something like provide a fire risk score

 based upon the satellite image

 of this property and just left it there. I can almost guarantee you I

 would not get a good result.

 So instead, I applied some of the different prompt engineering

 techniques we have learned

 about previously, and I provided a series of different analysis steps

 for Claude to go through.

 Step one, first find the actual primary residence inside of the

 satellite photo.

 Step two, take a look at the tree density, then take a look at the

 ability for fire services to

 actually access the property. Take a look at how many trees or

 specifically branches are

 overhanging the roof, which is a very common fire risk, and then

 finally assign a fire risk

 rating based upon all these different qualities. And I provide some

 criteria on helping it decide

 whether it should be a one, two, three, or four. And then finally at

 the very bottom,

 write a one sentence summary for each with a final score. So that's

 our prompt. I'm going to

 make sure I run that cell, and then let's go down here to the bottom,

 and we're going to write out

 some code to read in a sample image and feed it into Claude with that

 prompt and see what kind of

 result we get. One other quick item in the same directory as this 002

 images notebook,

 you should find a images directory. And inside there, I have seven

 different PNG files that are

 each a satellite photo image of a house that has some trees around it

. So we should have one,

 two has very low fire risk here, and then three, very, very low fire

 risk. And then we could go

 through and see some different examples. I think seven is pretty bad.

 So I would expect to see a

 very poor fire rating score on number seven, but let's test

 everything out and see if it works or

 not. All right, so inside of our cell down here, I'm going to first

 open up one of those image files

 and read it as a series of bytes. So I'm going to get the raw image

 data. I'll say with open images,

 and I'll start off with property seven, just because as we saw that

 one is particularly egregious,

 I'm going to read the contents of that file into a image bytes

 variable. I'll then make my list of

 messages. I'll add a user message. And in this case, I'm going to add

 in one single image. So

00:08:31,2

---

#### Lesson 55: PDF support

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/308839](https://anthropic.skilljar.com/claude-in-amazon-bedrock/308839)

**Video:** 10 - 002.1 - PDF Support.mp4 | **Duration:** 2m 2s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Besides reading images, Claude can also very easily read

the contents of a PDF document as well. Let me

show you a quick example of this. First, attach

this lecture. You'll find a PDF file named earth.pdf.

This is a printout of the first three pages of

the Wikipedia article on earth. So it just has a couple

of different facts around earth and our entire planet

and whatnot. Make sure you download this attachment

and put it in the same directory as your notebook. So

if my notebook is inside this directory right here, I should

see earth.pdf right next to it. Then

to read the contents of that PDF and chat with it,

all we do is change a couple of different properties in

this exact same code that we have right here. So

first, rather than opening up that image, I'm going to

instead open up .slash.earth.pdf.

Then just to kind of do things right here, we shouldn't

really call this image bytes anymore, I'm going to rename it to

be file bytes. And I'll make sure that

I update the name down here as well. Now

here's the only tricky part. We need to make a couple

of updates to the structure right here, specifically the

image part. So I'm going to first change image

to document. I'm going

to change the format to PDF. And

then right after the format PDF, I'm going to add

in another key value pair with a name

of Earth. So

the idea here is that this is supposed to be the name of the

file that you are attaching, but without any extension.

So there should not be a earth.pdf. It's just

earth by itself. Then we

can update our prompt. I'm going to put in a hard code string

right here. I'll ask Claude to summarize this document

in one sentence. Then

I'm going to run this and we'll see what we get.

All right, so clearly, Claude was able to read that PDF,

take a look at all the content inside of it, and give us some reasonable

response. Reading the contents of a PDF

can be incredibly useful, especially when you combine

it with another feature that we'll take a look at in just

a moment called citations.

---

#### Lesson 56: Citations

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/308840](https://anthropic.skilljar.com/claude-in-amazon-bedrock/308840)

**Video:** 10 - 002.2 - Citations.mp4 | **Duration:** 2m 37s | **Platform:** jwplayer | **Captions:** English, French, German, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that we've got a simple example of Claude's PDF reading

ability, let me show you one additional feature that's

going to give you a better understanding of why giving

Claude PDF is really useful. You

see a common problem around consuming information

from a PDF is that users often have to

take it on faith that the model is correctly interpreting

the contents of the document. Now, Claude has

a feature known as citations that directly addresses

this issue. So let me show you how it works. We're

going to first go through just a little bit of setup.

So the first thing I want to do is open up our earth.pdf

document again. I'm going to go down to the very bottom

page. And the last page here, you'll

notice is all about the formation of the earth. So

the formation of the earth itself and its atmosphere.

Next, I'm going to go back over to my editor. I'm going to update the text

on sending off to Claude. I'm going to change my query to how

earth's atmosphere and oceans formed. Then

on the document dictionary, I'm going to add in an additional field

of citations enabled

true. And finally,

down at the very bottom, rather than just printing out the response

text, I'm going to print out the entire response. I'm

going to run this, and let's see what we get back. The response

we get back is going to have many different parts inside of it. The

first part that we see is one that we've seen many times before. It

is a text part that contains plain text.

But after that, we get a part that we haven't seen

previously called citations content. Let

me help you understand what this new part is all about. The

best way to understand this is to look at a quick demonstration.

So I took that response you saw inside of my editor just a moment ago,

and I reformatted it using Claude into this

nicely formatted document. All the plain text

you see in here is all coming from the different text

parts inside the response I just got back. But

in addition, you'll also have little numbers scattered

throughout. These are serving as citations, and

they are represented inside the response by those citation

parts we just saw. If I mouse over one, I'll

get some information about why Claude decided to make

this statement. So specifically, why it decided

to say that statement right there. In short,

Claude is citing a source and telling us exactly

where from the source PDF, it is pulling the information

that is supporting that statement. So in this case, Claude

is saying that it looked into the earth.pdf file. and

on page four in particular, it found

some text to support this statement.

We have many different citations inside of this example, so

in my case I got seven in total. The reason

that this citations feature is so useful is that it gives

your users confidence in the answers that Claude is generating.

If a user wants to, they can go back to the source PDF

and verify the information that led Claude to making

particular statements.

---

#### Lesson 57: Prompt caching

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276786](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276786)

**Video:** 10 - 003 - Prompt Caching.mp4 | **Duration:** 3m 36s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next feature that we are going to focus on is prompt caching.

 Prompt caching is used to speed up Claude's response and decrease the

 cost of text generation.

 To help you understand how prompt caching works,

 we're going to walk through what happens inside of Claude during a

 typical request

 that we make without any kind of prompt caching enabled at all.

 So again, this is just a normal request.

 Now, we've already spoken a little bit about normal requests in the

 entire flow,

 but don't worry, this time I'm going to add in a little bit of detail

 on what happens inside of Claude itself.

 As usual, everything begins with us sending a message off to Claude.

 And when Claude receives this message, before actually generating any

 output text at all,

 it does a tremendous amount of work on the input message.

 In other words, Claude is going to internally create a tremendous

 number of internal data structures

 and do a tremendous number of calculations solely on the input text.

 It will then eventually generate the output text using all that

 earlier work it did

 and then send a response back to us in the form of some assistant

 message.

 After the response is sent off to us,

 Claude is going to then take the output text and the result of all

 those earlier calculations

 that were done on the input message and just throw them all into the

 trash.

 Away it all goes, we see all that work kind of go up in smoke

 entirely.

 Once Claude has gone through all that cleanup, it declares to the world

 "I am ready to process the next request."

 Now, let's imagine for a moment that after making this initial

 request,

 we then make a follow-up request.

 And in this follow-up request, let's just imagine that we are

 continuing this conversation.

 So we're going to attach a list of messages.

 The first one will be the exact same message we had sent in a moment

 ago,

 and then the assistant message response we got back,

 and then some new user message that we're going to attach just to

 further the conversation along.

 So we're going to take all these messages and send them into Claude.

 And internally, Claude is probably going to be a little bit

 frustrated when it sees that first message

 because Claude is going to see that first message and think to itself.

 

 Of course, this isn't quite what happens.

 We can imagine this is kind of what's going on behind the scenes.

 Claude is going to see that first message and say,

 "I just saw this message. I just did so much work to process it, and

 then I threw away all those calculations."

 And Claude is going to think to itself,

 "I really wish I could reuse all that work that I did just 10 seconds

 ago and threw away."

 If Claude had saved that work that it threw away just a moment ago,

 it would probably be able to send us back a response much more

 quickly

 because it doesn't have to repeat all that work.

 So now that we have seen this problem,

 let's think of some possible way to solve it.

 Well, here's one possible way that we could handle this problem.

 Maybe we could say that whenever we make an initial request off to

 Claude,

 and Claude goes through all that initial work on our user message

 that we are sending in,

 rather than taking the result of all that analysis and throwing into

 the trash,

 maybe we could instead cache all that work or put it into some

 temporary data store.

 Then if we ever make a follow-up request and we include the exact

 same input user message,

 Claude could go into its cache and say,

 "Hey, I just saw this exact same message a moment ago,

 and I saved the work of all the analysis around that particular

 message."

 So rather than reanalyze the message again,

 it could reuse all the work that it did previously.

 And hopefully this would dramatically speed up the process of

 generating some output text

 because again, we are reusing some work that we had already done.

 This idea of saving some work from a request to be used later on is

 exactly what prompt caching is all about.

 So let's come back in just a moment and we're going to walk through

 some of the implementation details of prompt caching

 and really understand how it is implemented by Anthropic.

---

#### Lesson 58: Rules of prompt caching

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276785](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276785)

**Video:** 10 - 004 - Rules of Prompt Caching.mp4 | **Duration:** 6m 19s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that we understand the theory, we are going to explore how prompt

caching with Claude actually works.

The core idea of prompt caching is identical to what we discussed in

the last video.

We will make an initial request off to Claude.

Claude is going to do some processing on that initial message,

and then Claude is going to save all that work into a temporary cache.

Then if we make a follow-up request at some future point in time,

and include the identical exact same message, rather than processing

that message all over again,

Claude is going to instead look into the cache, find the work that it

had already saved,

and load it up. Just to be clear, the work that we saved the cache

does not persist forever.

It is only stored there for five minutes. You're going to find prompt

caching is most useful

anytime that you are repeatedly sending the same content over to

Claude again and again and again,

because it really is this kind of two-phase process. We have to make

that initial request

to write some data into the cache, and then only the follow-up

requests are going to be able to

take advantage of that work that was done ahead of time. To enable

and control prompt caching,

we are going to make use of a new type of message part called a cache

point.

So by default, there is no prompt caching enabled with Claude. We have

to add in these additional

new types of parts into our different messages. You might recall that

we have other types of

parts we've already discussed, like a text part and an image part and

so on. So this is just yet

another type of message part that we're going to need to understand.

When we include a cache

point inside of a message, we are telling Claude that we want to cache

all the work that is done

for all the text up to that point inside of our message. Now that's

really confusing to hear in

just plain words. So let me as usual show you a quick diagram here.

All right, so let's imagine

we have an initial request we send off to Claude. We have a text part,

then a cache point, and then

another text part. As usual, because this is an initial request,

Claude is going to go through

some amount of work that is done to process the first text part and

the second text part.

And we're going to visualize that with this box right here and this

box right here. Because

we put the cache point in between these two parts, everything before

this cache point is going to be

cached. So in other words, this work right here, it's going to be

cached. But everything after the

cache point, in other words, this right here is not going to be

stored in cache. If we then make a

follow up request where that initial text part is identical to the

one we had sent previously.

So here's that same exact text part right here that is above the

cache point, rather than trying

to process that chunk of text again, Claude is going to see if it

already has something stored

inside the cache. In this case, it does. So it's going to reuse this

bit right here.

Claude is not going to look into the cache to see if it has already

processed these other

text parts previously, because they are all listed after this cache

point. Now a key point to understand

here is that the caching system is only going to work if everything

before the cache point is

identical. So in this case, before the cache point, I have one text

part that says exactly

summarize this long text and then whatever text we want to summarize.

If we instead made a follow

up request, where the text part was slightly different, if it said

something like, please

summarize this long text. Well, this text part is now different. So

Claude would not attempt to use

this cached work that it had previously generated. Instead, Claude is

going to ignore the cache

and generate a new analysis or go through all the work once again on

this brand new text part

that it has not seen previously. The next thing to understand is that

cache points are not limited

to just one single message or one single text part. They can use to

store work that is done on

multiple different messages, multiple different parts, even assistant

messages. For example,

if we make an initial request like the one you see right here, where

we have our cache

point all the way down here at the bottom, Claude is going to process

all the different

text parts across all the messages before it. We're going to get some

intermediate work like

what you see. And then Claude is going to cache all that over here.

Then if we make another follow

up message with the exact same text parts across all the different

user message, assistant message,

user message, we're going to reuse this cache. So here's our follow

request. Again, we have

everything identical before the cache point. We're going to reuse all

that work we had done

ahead of time. Before we move on, there are two other very quick

ideas I want to share with you

around prompt caching. First, there is a minimum amount of content

required for Claude to cache

its work. There must be at least 1024 tokens worth of content before

a cache point in order for Claude

to actually cache its work. So in the first example up here, the only

content we have before the

cache point is a single text message of Haiku. That is definitely

not 1024 tokens long.

So in this case, that we are not going to write anything to cache.

But down here, if I've got

Haiku, Haiku, Haiku repeated 500 times or so, that is

probably going to be

greater than 1024 tokens worth of content. So all the different text

parts right here,

the result of processing all them is going to be cached, and we can

make use of that cache on

follow-up requests. The other big item that I want you to be aware of

around prompt caching

is that we are not limited to just caching message parts. We can also

put in cache points on tool

definition lists, so the actual list of schemas we pass in, and we

can also provide cache points

on system prompts as well. So for example, when we pass in a list of

tools, the actual tool specs

where we write out all that JSON can end up being rather long, and

they count towards our token

budget for any given request. So when we pass in our list of tools,

we might put in all of our

different JSON schema specs, and then a cache point right after it.

The same thing can be done

for a system message as well. We can pass in a text part that

includes the actual system prompt

that we want to cache, and then right after that a cache point. Now

even though I'm tossing this idea

of caching the tool schemas and system prompts towards the end of

this video, this actually ends

up being one of the more common locations where you are going to

implement prompt caching. Because

in reality, it's rather rare that we are going to change our list of

tools or even the system prompt

between requests. So because we are going to very often make the same

request with the same exact

list of tools and system prompt, you're very often going to want to

put in cache points.

All right, so now that we understand all this theory around prompt

caching, it's time to actually

get our hands dirty by writing out some code. Let's come back in the

next video and test out

prompt caching inside of a Jupyter notebook.

---

#### Lesson 59: Prompt caching in action

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276787](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276787)

**Video:** 10 - 005 - Prompt Caching in Action.mp4 | **Duration:** 7m 8s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's get our hands dirty with prompt caching

 and just write out a little bit of code to play around with it

 and understand how it works.

 I'm inside of a new notebook called 003_caching.

 I have a lot of the very same setup code

 that we've used several times before,

 but I've added in two new sections here.

 First, I've added in a cell with a rather long prompt.

 It's got about 6,000 tokens inside of it.

 I've also got a set of tool schemas.

 These are the same schemas we worked on earlier

 on inside the course.

 So I've got add duration to date time,

 the set reminder schema,

 and the get current date time schema as well.

 In total, all of those schemas put together

 are about 1,200 tokens.

 So both the prompt and the schemas,

 total up to definitely being above

 the minimum threshold for prompt caching,

 which again is 1,024.

 The first thing I wanna do to change this notebook

 is open up our helper functions.

 And I want to make a change to our chat function.

 In particular, I want to enable caching by default

 for our system prompt.

 So if we ever pass in a system prompt,

 I just wanna cache it no matter what,

 because again, we usually don't change

 the system prompt too often,

 and it's usually consistent between requests.

 And then for a similar reason,

 I always want to cache the list of tools as well,

 or specifically the tool schemas.

 And then finally, on our return statement down here,

 I want to include the usage field

 from the response object that we get back

 whenever we make our request.

 This usage object that we're going to include in here

 returns some information related to prompt caching.

 So we can use it to inspect and figure out

 whether or not we are successfully caching input

 that we're feeding into Claude or not.

 All right, so let's get to it.

 We'll start off first by making sure

 that we always cache our system prompt.

 So to do so, all we have to do is expand this list of parts,

 and we're going to add in a new part here,

 our cache point part.

 And that's going to have a type of default.

 And that's pretty much it for the first to do.

 So I'm going to mark that one as complete.

 Second, for caching our list of tools,

 I'm going to make a new variable here,

 tools with cache.

 And that's going to be our list of tools,

 and I'm going to concatenate in a new part

 of cache point type default.

 And then I'll make sure that I pass off tools with cache

 as our list of tools.

 So make sure we update that right there.

 Okay, that's all we have to do to enable caching

 for our tool list.

 And then finally down here at the bottom with my response,

 I'm going to add in a new usage.

 That'll be just this plain exact usage property

 from the response.

 So we're just going to essentially pass that right through.

 Okay, so that's really it for enabling prompt caching

 across a huge part of our application.

 So now both our system prompt and our list of tools

 are going to be cached.

 So I'm going to rerun that cell,

 and then we'll go down here to the bottom.

 And then after I get back a response,

 I'm going to print out the responses usage.

 Next up, I'm going to provide a system prompt right here.

 I'm going to use the prompt that I had included

 on that earlier cell, so code prompt.

 I want to include that as my system prompt.

 So I'll pass that in like so.

 And then I will put in a very simple text message here.

 So I'm just going to say something like

 summarize the design spec in one sentence.

 So the intent here is to just pretty much summarize

 everything that's inside of that giant code prompt.

 I don't really care about the text prompt here at all.

 All I really care about right now

 is demonstrating prompt caching to you.

 So again, I just really care about the usage field here.

 Okay, I'm going to run this,

 and I'm going to see something interesting.

 The usage field is going to have a cache read input tokens

 and a cache write input tokens.

 Because this is our very first request

 where we have never submitted

 this particular system message before,

 we are going to write some information to the cache.

 So Claude did a lot of work to analyze all the text

 inside this giant system prompt right here

 that we are providing, and then it stored the result

 of all that work into the cache,

 and it took up 6,322 tokens.

 So if we now make a followup request,

 within the next five minutes,

 my expectation would be that we're not going to see

 a cache write, and instead we're going to see a cache read,

 because now we're going to try to use all that work

 that we already did ahead of time

 in analyzing that system message.

 Okay, so I'm going to run this,

 and again, hopefully we're going to see a cache read,

 because we are consuming something out of the cache,

 and sure enough, there we go.

 And we're going to continue to see

 something from cache read right here,

 as long as we do not change our system message,

 so the content before our cache point,

 and as long as we don't go for a gap of five minutes,

 because as soon as we go over five minutes

 without making a request,

 that cache entry is going to be automatically cleared.

 So now the next thing I would like to do

 is just try changing our input text right here really quick.

 So I'm going to say, summarize the design spec

 in one sentence, period, it's only change I'm going to make.

 Now at this point in time, the system message

 occurs semantically above this text part right here.

 So even though I changed the text part,

 the cache point that we have for our system message

 is above this piece of text.

 So I should continue to see a cache read,

 even though I changed part of this user message,

 'cause I am reading the cache version

 of the system prompt, and there we go.

 Next up, if we go and change our system prompt in some way,

 so maybe I count this very first line right here,

 and just put a period at the end.

 Now I have a very different system prompt

 in the eyes of Claude.

 So if I run this, and then run the bottom cell again,

 now that I am feeding in different content

 for the system prompt, no more cache read.

 Instead, it turns into a cache right

 because that content has changed.

 If I run it again, now we're going to have a cache read

 because we cached the change version of that prompt.

 Now I know this is going really quickly,

 and I'm using a lot of terms here

 of in very quick succession, but I think if you personally

 play around with the caching system a little bit,

 you're going to get a sense of what's going on really quickly.

 Now the last thing I want to show you is caching tool use.

 So with the change we made to our chat function,

 all we really have to do is add in a list of tools,

 and remember we have some of those different schemas

 like add duration to date time schema.

 We have set reminder schema

 and get current date time schema.

 So once again, if we send this off,

 now we're going to see an even larger cache write

 because now we are caching both our schemas

 and the system prompt as well.

 All right, so that is prompt caching.

 Again, we are going to very often want to cache

 our system prompt and our tool schemas

 because they are very often going to be longer

 than that 1024 token cutoff.

 And by enabling prompt caching,

 we're going to pay less for our generation

 and the text generation is most often going to run

 a little bit faster.

---

#### Lesson 60: Quiz on features of Claude

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/289300](https://anthropic.skilljar.com/claude-in-amazon-bedrock/289300)

---

### Model Context Protocol

#### Lesson 61: Introducing MCP

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276798](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276798)

**Video:** 11 - 001 - Introducing MCP.mp4 | **Duration:** 4m 40s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this module we are going to focus on model context protocol. MCP

 is a communication layer

 designed to provide Claude with context and tools without requiring

 you, the developer,

 to write a bunch of tedious code. When you first get started with MCP

,

 you will see diagrams that look like this very often. It shows two

 major elements of MCP,

 namely the client and the server. The server often contains a number

 of internal components

 named tools, resources, and prompts. Now there's a lot of terminology

 here, so to help you understand

 all of this, we're going to imagine that we are building a small app

 and see how MCP fits into it.

 Our sample app is going to be another chat interface. It's going to

 allow a user to chat with Claude

 about their GitHub data. So if a user asks a question like what open

 pull request do I have

 across all my different repositories, the expectation is that Claude

 is probably going to make use of a

 tool to reach out to GitHub, access the user's account, and see what

 open pull requests they

 have, maybe open repositories or whatever else. The point here is

 that we would implement this

 probably by using a set of tools. Now one thing I want to mention

 really quickly is that GitHub

 has a tremendous amount of functionality. There are repositories,

 pull requests, issues, projects,

 and tons of other things. So to have a complete GitHub chatbot, we

 would really have to author

 a tremendous number of tools. If we wanted to build that sample app,

 we would be on the hook

 for authoring all these schemas and all these functions. And this is

 all code that you and I,

 as developers, would have to write, test, and maintain. That's a lot

 of effort, a lot of burden

 being placed on us. This challenge of making developers maintain a

 big set of integrations

 is one of the primary difficulties that model context aims to solve.

 MCP shifts the burden of

 defining and running tools from your server to something else called

 an MCP server. So no longer

 would you and I have to author this tool right here. Instead, it

 would be authored and executed

 somewhere else inside of this MCP server. These MCP servers can

 really be thought of as like

 an interface to some outside service. So I might have a GitHub MCP

 server that provides access to

 data and functionality provided by specifically GitHub, where

 essentially wrapping up a ton of

 functionality around GitHub and placing it into this MCP server in

 the form of a set of tools.

 So at this point, we have a very basic understanding of what a MCP

 server is. It gives us access to

 a set of tools that exposes functionality related to some outside

 service. And the benefit here is

 that you and I do not have to author all these different tool schemas

 and functions and so on.

 Now that we have this basic understanding, I want to address some

 very common questions that a lot

 of people have when they first learn about MCP servers. So three

 common questions that seem

 to always come up. The first common question is who authors these MCP

 servers? And the answer is

 anyone. Anyone can make an MCP server implementation. But very often,

 you will find that service

 providers make their own official implementation. So for example, AWS

 might decide to release their

 own official MCP server implementation and inside of it, it might

 have a wide variety of different

 tools available for you to use. The second common question is how is

 using a MCP server different

 than just calling a services API directly? Well, as we just saw, if

 we wanted to call a API directly

 such as GitHub, then we would have to author this tool ourselves. And

 now we can call GitHub

 directly. So what did we gain here? Well, all that really changed was

 we are now having to

 author the schema ourselves and the function implementation ourselves

. So simply by adding in

 the MCP server, we are saving ourselves a little bit of time. The

 final common question is more of a

 common criticism that you're going to see people have around MCP. And

 this criticism is most often

 coming from people who don't quite understand what MCP is all about.

 So very often, you will see

 people saying MCP and tool use are the same thing. Well, as I have

 just laid out to you, MCP servers

 and tool use, they are complimentary. They are different things, but

 they are complimentary.

 The idea behind MCP is that you do not have to author the tool

 function and the tool schema.

 That is something that is done for you by someone else and is being

 wrapped up inside of this MCP

 server. So at some level, yeah, they're kind of similar because we

 are talking about tool use in

 both cases. But MCP servers are really talking about who is doing the

 actual work. So if you ever

 see this criticism, again, it's usually because people don't quite

 understand what MCP is all about.

---

#### Lesson 62: MCP clients

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276793](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276793)

**Video:** 11 - 002 - MCP Clients.mp4 | **Duration:** 4m 56s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

The next portion of model context protocol that we're going to

investigate is the client.

The purpose of the client is to provide a means of communication

between your server and a MCP server.

This client is going to be your access point to all the tools

implemented by that server.

Now MCP is transport agnostic. This is a fancy term that just says

that the client and the

server can communicate over a variety of different protocols. A very

common way to run a MCP server

right now is on the same physical machine as the MCP client and if

these two things are running on

the same machine then they can communicate over standard input output

and that's what we are

going to be setting up later on inside this section. There are

however other ways we can connect the

MCP client with the MCP server so they can also connect over HTTP or

WebSockets or any of a number

of other varieties or techniques. Once a connection has been formed

between the client and the server

they communicate by exchanging messages. The exact messages that are

allowed are all defined

inside of the MCP spec. Some of the message types that you and I are

going to be focusing are the

list tools request and the list tools result. As you guessed list

tools request is sent from the

client to the server and it asks the server to list out all the

different tools that it provides.

The server will then respond with a list tools result message which

contains a list of all the

different tools that it can provide. Two other common message types

that you and I are going to see

are the call tool request and call tool result. The first will ask

the server to run a tool with

some particular arguments and the second will contain the result of

the tool run. Now at this

point in time we've got this idea of a server and a client but I

suspect it's probably not really

clear how all this stuff really works together. So here's what we're

going to do in the remainder

of this video. We are going to walk through an example call between a

lot of different things.

So this will be kind of an involved process but we're going to

imagine the communication that goes

on between a user, our server that we're putting together, a MCP

client, the MCP server, GitHub as

some provider that we're trying to access some data from, and Claude.

So let's get to it again step

by step. First thing we would expect to happen is a user to submit

some kind of query or question

to our server, like what repositories do I have? At this point it

would be up to our server to

make a request off to Claude, but in that request we want to list out

all the different tools that

Claude has access to. So before our server can make the request off to

Claude, it's first going to go

through a little side detour through the MCP client and the server.

So here's what happens.

The server is going to realize that it needs to see a list of tools

to send off to Claude,

along with the user's query. So it's going to ask the MCP client to

get a list of tools.

The MCP client in turn is going to send a list tools request off to

the server,

and the server will respond with a list tools result. Now that our M

CP client has a list of the

tools, it will give that list of tools back to the server. And now

our server has everything it

needs to make an initial request off to Claude. It has both the

original message from the user

and a list of tools to include. So our server can make request off to

Claude with that query

and the set of tools. Claude is going to take a look at the tools and

realize, you know what,

in order to answer the user's original question right here, I really

want to call a tool.

So Claude would respond with some tool use message part. At this

point, our server is going to

realize that Claude wants to run a tool, but our server is no longer

really in charge of executing

any tools. Instead, our tools are going to be executed by the MCP

server. So in order to run

the tool that Claude is asking for, our server is going to ask the M

CP client to run a tool

with some particular arguments that were provided by Claude. The MCP

client, however, doesn't actually

run the tool is going to send a call tool request off to the MCP

server. The MCP server will receive

that request and make a follow request off to GitHub. So this is

where we would actually be getting

a list of repositories that belong to this particular user. GitHub

would respond with that

list of repositories. Then the MCP server would wrap up that data

inside of a call tool result

and send that back to the MCP client. Then the MCP client, in turn,

would hand the result off to

our server. Now our server has the list of repositories, and it can

make a follow up request to Claude

with the tool result part inside of a user message. So this tool

result would include the

list of repositories that Claude was asking for. And now Claude has

all the information it needs

to formulate a final response. So it'll write out some text of

something like your repositories are,

and then send that back to our server. And our server would send it

on back to our user.

All right, so this flow, yes, it is rather complicated. The reason I

want to show you this is that we

are going to see all these different pieces as you and I start to

implement our own custom MCP client

and MCP server a little bit later on.

---

#### Lesson 63: Project setup

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276792](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276792)

**Video:** 11 - 003 - Project Setup.mp4 | **Duration:** 3m 23s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

To better understand some aspects of MCP, we are going to start to

 implement our own CLI-based chatbot.

 This is going to give us a better idea of how clients and servers

 actually work together.

 In this video, I want to do a little bit of project setup and just

 help you understand

 exactly what we're going to make. I've got a lot of product

 description over here of what we're

 going to build. We're going to go through all this over time. Right

 now, I just want you to get

 a high level understanding. So as I mentioned, it's going to be a CLI

-based chatbot. We're going to

 allow users to work with a collection of documents. These are going

 to be fake documents. They're

 just going to be stored in memory. We're going to build out a small M

CP client that is going to

 connect to our own custom MCP server. For right now, the server is

 going to have two tools implemented

 inside of it. One tool to read the contents of a document and one

 tool to update the contents of

 a document. Again, these documents are here on the right hand side.

 They're all fake, so they are

 going to be persisted only in memory. That's it. Now, before we go

 any further, there is a very

 important note, something I really want you to understand around this

 entire process. And that is

 that on a normal project, typically, we would be implementing either

 a client or an MCP server.

 So on a real project, we might be authoring just an MCP server to

 distribute to the world and allow

 developers to access some service that we have built up.

 Alternatively, we might be building a

 project where we make only a MCP client. And the intent here would be

 that we would be connecting

 to some outside MCP servers that have already been implemented by

 some other engineers.

 So in this project, we are making both a client and a server. And we

're just doing that in one

 project. So you get a better understanding of how this stuff actually

 works together. All right,

 now that we have this disclaimer out of the way, let's go through

 just a little bit of setup.

 Attached to this video, you should find a file named CLI project.zip.

 Inside there is some starter

 code for our project. Make sure you download that zip file, extract

 it, and then open up your code

 editor inside of that project directory. Just to save a little bit of

 time, I have already done

 so. So I've already got my code editor open inside of that smaller

 project. Inside this project,

 I would encourage you to take a look at the read me document. I put

 in some setup directions

 inside of here. And it's really critical that you go through these

 setup. You're going to do a little

 bit of environment variable configuration by specifying the bedrock

 region and a model ID.

 The region and the model ID can be the exact same one that used

 previously inside of all of our

 different Jupyter notebooks. And then after that, you're going to go

 through a little bit of dependency

 installation. So all you have to do is set up a Python environment,

 install a couple of packages,

 and that's it. Once you have gone through all this setup, you can

 then run the starter project

 right away. To do so inside of your terminal, make sure sure that you

 are inside of your project

 directory. So I called my project mcp. And inside there, I've got all

 my different project files and

 folders. To run the project, we will run uv run main.py if you're

 making use of uv. If you are not

 making use of uv, then it'll be just python main.py. Now I'm making

 use of uv. So I'm going to do a

 uv run main.py. And then when I run that, I should see a chat prompt

 appear. And if I ask what's one

 plus one, I should see a response rather quickly. That is it for our

 setup. So now we can start

 to focus on adding in some new features to this application.

---

#### Lesson 64: Defining tools with MCP

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276800](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276800)

**Video:** 11 - 004 - Defining Tools with MCP.mp4 | **Duration:** 7m 3s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's start to make an MCP server for our CLI chatbot.

 As you saw, the CLI itself already works,

 and we can already chat with Claude,

 but there's no additional functionality

 around the MCP server tied to it just yet.

 So we're gonna work on adding in this MCP server

 that is gonna have two tools in it for right now.

 It is gonna have one tool to read a document

 and one tool to update the contents of a document.

 The implementation of the server

 is gonna be placed into the MCP server.py file

 inside of the root project directory.

 Inside of here, I've already gone through

 a little bit of work to set up a basic MCP server.

 And then I defined a collection of documents

 that are going to exist only in memory.

 And then finally, I put together some different to-do items.

 So these are different tasks that you and I

 are gonna complete inside of this file.

 For right now, as I just mentioned,

 we're gonna be working only on these first two items,

 writing out two tools.

 Now we have authored tools in the past,

 and we saw that, well, there's a lot of syntax there.

 There's those big JSON schemas,

 but I got good news for you here.

 In this project, we're making use

 of the official MCP Python SDK.

 So that's what this MCP packages

 that we're making use inside of here.

 This MCP package is going to create our MCP server for us

 with just one line of code, like what you see right there.

 This SDK also makes it really easy to define tools.

 To define a tool, all we have to do is write out

 what you see on the right-hand side over here.

 This will make a tool named Add integers

 with this description and two arguments

 that are going to be required to be passed into it.

 Once we write out a tool definition like this,

 behind the scenes, MCP is gonna generate a tool

 JSON schema for us, which we can then take

 and then pass off to bedrock.

 So right away, as you can see,

 it starts to get a lot easier to do

 some basic things like define tools.

 Now, as I mentioned, our first task is going to be

 to implement these two different tools.

 So let's go back over to our MCP server.py file right away,

 and we're gonna start to implement the first tool

 of reading a document.

 So the only goal here is to take in the name

 of some document and return the contents of it.

 All of our documents are already placed

 inside of this docs dictionary.

 The keys are the IDs or essentially names of a document

 and the value is a document's contents.

 So our tool is really simple.

 We're gonna take in one of these strings,

 look at the appropriate value inside this docs dictionary

 and then return it.

 That's all we need to do.

 So to implement this, I'm gonna find the first to do

 and right underneath it, I'm going to define a new tool

 by writing out @mcp.tool.

 I'm going to give this tool a name of read doc contents

 and a description of read the contents of a document

 and return it as a string.

 And remember, in a perfect world,

 we put in a really fleshed out description right here

 to make sure it's super clear to Claude

 exactly when to use this tool.

 But right now, just as usual to save a little bit of time

 and keep you from having to type out a bunch of text here,

 I'm just gonna leave in a very simple description.

 Then I will define my actual tool function.

 So this is the function to run

 whenever we decide to run this tool.

 I will call it read document.

 It's going to take in a argument of doc ID

 that is going to be a string.

 I'm going to set that to a field with a description

 of ID of the document to read.

 And then we need to make sure

 that we import this field class at the top.

 So I'm going to go up to the top

 and add an import from pydantic import field.

 Then back down here, inside of the function body,

 I'm gonna put in my actual implementation.

 So the first thing I'm going to do

 is just make sure I handle the case

 in which Claude asks for a document

 that doesn't actually exist.

 So I'll say if doc ID not in docs,

 so in other words, if the provided document ID

 is not found as a key inside of this dictionary,

 then I'm going to raise a value error

 with a F string of doc with ID, doc ID not found.

 And then if we get past that check,

 I'll go ahead and return the actual document.

 So I'll return docs at doc ID.

 And that's it, that's all it takes to define a tool.

 So we've specified the name of the tool,

 its description, the argument that is expected,

 its type and a description for that argument as well.

 All these different decorators and field types and whatnot

 are all gonna be taken together by this Python MCP SDK

 and it's going to generate a JSON schema for us.

 Now that we've implemented this first tool,

 I'm going to remove the to-do right there

 and then we will implement our other tool,

 the one to edit a document.

 So we're going to repeat the exact same process.

 I'll say MCP.tool, I'll give it a name of edit document

 with a description of edit a document

 by replacing a string in the document's context

 or semi-content with a new string.

 Then for the implementation, I'll call this function edit doc,

 actually we'll be consistent called edit document.

 And then we're going to take in a couple of different arguments

 here, first is going to be a document ID

 and then a old string to find

 and then a new string to replace the old string with.

 So let's write this all out, we're going to have a doc ID

 that will be a string with a description of ID

 of the document that will be edited.

 Old string will be a string

 with a description of the text to replace,

 must match exactly including white space.

 And then our new string,

 the new text to insert in place of the old text.

 So our document editing here is just a very simple find

 and replace, that's it.

 Once again inside of here, I'm going to make sure

 that Claude is asking for a document that actually exists.

 So if doc ID not in docs, raise value error

 with a f string of doc with ID not found.

 And then if we do find the correct document,

 here's how we will do our edit, we'll say docs at doc ID

 is docs at doc ID, replace old string with the new string.

 And that's it.

 All right, so just like that, we have put together

 two tool implementations really, really quickly.

 I can't repeat it enough.

 The finding tools with this MCP Python SDK

 is a lot easier than writing out

 the schema definition manually.

 Now that we've got both tools put together,

 I'm going to delete the to-do right there.

 Okay, so this is a good start.

 We have put together our MCP server

 and we've implemented two tools inside of it.

---

#### Lesson 65: The server inspector

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276796](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276796)

**Video:** 11 - 005 - The Server Inspector.mp4 | **Duration:** 3m 52s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

We have put together some functionality inside of our MCP server, but

 we have no idea if it works.

 So it'd be really great if we could test this out somehow.

 It turns out that by using this Python SDK, we automatically get

 access to an in browser debugger

 so we can make sure that this server is working as expected. Let me

 show you how to use it really

 quickly. Back inside my terminal, I want to make sure that I have my

 Python environment activated.

 Remember the read me document goes into detail on the exact command

 to run to make sure that you

 have activated that environment. Once you are sure that it is

 activated, we'll run MCP,

 dev, and then the name of the file that contains our server. In this

 case, it is MCP server.py.

 Once I run that, I'll then be told that I have a server listening on

 port 6277

 and I'll be given a direct address to actually access it. I'm

 going to open up that address

 inside my browser. And once you go there, you'll see something that

 looks like this.

 This is the MCP inspector. Now, right away, there's something

 important I want you to understand here.

 This inspector is in active development. So by the time you are

 watching this video,

 what you see on the screen right now might be very, very different

 than what I am showing.

 Nonetheless, it's probably still going to have some very similar

 functionality.

 On the left hand side, you'll see a connect button that is going to

 start up your MCP

 server. So that file that we just edited, I'm going to click on

 connect, and then right away,

 we'll see a couple of different things on the screen up here. I first

 want you to notice the

 top menu bar up here. It lists out resources, prompts, tools, and

 some other stuff. Again,

 the UI might change by the time you watch this video. So if you do

 not see this menu bar up here,

 all we are really looking for here is some tools section. Once I

 click on tools, I will click on

 list tools, and we'll see the name of the tools that we just put

 together. If I click on one,

 the right hand panel is then going to change. And I can use this

 panel over here to manually

 invoke one of my tools to make sure that it is working as expected.

 So this is how we can do some

 live development on our MCP server without actually having to wire it

 up to a real application.

 In order to use the read dot contents tool, all we have to do is put

 in a document ID.

 If I go back over to my editor and go up to the docs dictionary right

 here, I can copy one of

 these document IDs. So I will take out deposition.md. I will put it

 in as the doc ID and then click on

 run tool. I should then see run tool of success with the contents of

 the document. That is it right

 there. I can verify it. It's the same exact string as what I see

 right there. We can use this same

 exact technique to test out the other tool as well. So I will change

 over to the edit document tool.

 Now I'll put in my document ID, my old string that I want to replace.

 How about we replace the

 word deposition actually about an easier word to type out about just

 this. That'll be a little bit

 easier. So my old string is this member that is going to be capital

 sensitive. And I'm going to

 replace it with a report. And if I run the tool, I'll then be given a

 success. Remember that tool

 does not actually return the document's contents. It just edits the

 document. So now to verify

 that the edit was done correctly, I can go back over to the read doc

 contents tool, run that one

 again with the same document ID. And I should see a report deposition

 and then blah, blah, blah.

 All right, so as you can see, this MCP inspector allows us to very

 easily debug a MCP server that

 we are implementing without actually having to wire the server up to

 an actual application.

 As you start building your own MCP servers, I expect you will be

 using this inspector tool

 quite a bit. And we'll probably use it a little bit more inside of

 this module,

 just to make sure that our server development is going along pretty

 well.

---

#### Lesson 66: Implementing a client

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276802](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276802)

**Video:** 11 - 006 - Implementing a Client.mp4 | **Duration:** 8m 56s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that our server is in a good place, we're going to shift gears a

 little bit and start

 working on our MCP client.

 The client can be found inside the MCP client, the .py file inside

 the root project directory.

 Now before we do anything inside this file, I just want to give you a

 very quick reminder

 here.

 Remember what I told you about earlier.

 Usually in a typical project, we are either making use of a client or

 we are implementing

 a server.

 It's just in this one particular project that we are working on that

 we are doing both.

 Again, just you can see both sides of the puzzle.

 The MCP client itself inside of this file is consisting of a single

 class.

 You'll notice there is a lot of code inside of here and it doesn't

 look quite as pretty

 as some of the code we just wrote out inside of the server.

 Let me tell you exactly what's going on inside this file and exactly

 why it is so large.

 Okay.

 So inside this file, we are making the MCP client class.

 This class is going to wrap up something called a client session.

 The client session is the actual connection to our MCP server.

 This client session is a part of the MCP Python SDK.

 So again, this session is what gives us this connection to the

 outside server.

 The session itself requires a little bit of resource cleanup.

 In other words, whenever we close down our program or decide that we

 don't need the

 server anymore, we have to go through a little bit of a cleanup

 process.

 And I have already written out a lot of that cleanup code inside of

 the MCP client class.

 So that's really why this class exists at all.

 Just to make that cleanup a little bit easier.

 You can see some of that cleanup code inside the connect function and

 down a little bit

 lower at the cleanup, async enter and async exit functions as well.

 So it's very common practice to not just make use of this client

 session directly.

 Instead, very common to a rapid up inside of a larger class that's

 going to manage some

 of this different resource stuff for you.

 The next thing I want to clarify is why this client exists at all.

 So in other words, what is the client really doing for us here?

 Well, remember this full that we looked at a little bit ago.

 So we had our code right here and at certain points in time, we

 needed, say, a list of

 tools to send off to Claude.

 And then later on after that, we also needed to run a tool that was

 requested by Claude.

 In order to reach out to our MCP server and get this list of tools or

 to run a tool,

 that's where we are making use of the MCP client.

 So we can imagine that this client is exposing some functionality

 that belongs to the server

 to the rest of our code base.

 So inside of our code base, inside this project, specifically inside

 of the core directory,

 there is a lot of code already inside there that I put together that

 is making use of

 this class.

 So there's some other code that's going to call some of the different

 functions you see

 inside of here, like list tools, call tool, list prompts, get prompt

 and so on.

 For right now in this video, we're going to focus on implementing two

 functions, list

 tools and call tool.

 So as you just saw in the diagram, we looked at a moment ago, these

 two functions are going

 to be used in different parts of our code base to get a list of tools

 to provide off

 to Claude, and eventually call a tool whenever Claude requests to

 call a tool.

 Implementing these two functions is going to be really simple and

 straightforward.

 So let me show you how we're going to do it.

 We'll first begin with list tools.

 I'm going to remove the to do inside there and replace it with result

 is await self dot

 session.

 I'm going to call that like a function list underscore tools.

 And then I will return result dot tools.

 And that's it.

 So this is going to get access to our session, which is our actual

 connection to the MCP server.

 It's going to call a built-in function to get a definition or a list

 of all the different

 tools that are implemented by that server, I'm going to get back

 result and then just

 return the tools and that's it.

 Then we can implement call tool right here in a very similar fashion.

 So this will be return await self dot session, call tool, tool name

 and tool input.

 Once again, getting access to the session, that is our connection to

 the server.

 And I'm going to attempt to call a very specific tool.

 The name, the tool will be passed in along with the input parameters

 or input arguments

 to it that were provided by Claude.

 Now at this point in time, I would like to test out these two

 functions really quickly.

 To do so, we're going to go down to the bottom of this file where I

 put together a very small

 testing harness for us.

 So down here, you'll notice I put together this testing block.

 So we can run this MCP client.py file directly.

 And if we do so, we're going to form a connection to our MCP server

 and then we can just run

 some commands against it and just see what we get back.

 Notice that in your version of the code, there's a comment in there

 about changing the command

 in ARGS right here in case you are not making use of UV.

 So if you're not using UV, make sure you take a look at that comment.

 Inside of this with block, I'm going to add in a little bit of

 testing code.

 So I'll say result is await underscore client list tools.

 And then I'm going to just print out the result that we get back.

 So this should start up a copy of our MCP server, then attempt to get

 a list of all the different

 tools that are defined by it and then just print out the result.

 To test this out, I will flip back over to my terminal and do a UV

 run MCP underscore

 client.py.

 And as usual, if you are not making use of UV, you'll just do a

 Python MCP client.py.

 Okay, so I'll run that.

 And there is our list of tool definitions.

 So I can see inside of here that I have the read it doc contents tool

, which we put together

 a little bit ago, and our edit document tool as well.

 Each one has a description and a input schema as well.

 So this is our tool definition, which will eventually be passed off

 to Claude.

 Now there's one very small gotcha here that you're probably going to

 run into when you

 start working on your own project.

 When you take a look at input schema, you might notice that the

 structure of it, if you've

 got a really careful eye, it doesn't really look exactly like what a

 bedrock Jason schema

 is expected to look like.

 In other words, the structure here is just a little bit different.

 So again, this is a gotcha.

 It's some little bit of a trap that you just need to be aware of.

 The MCP spec has its own definition of what a tool looks like.

 And that is slightly different than what bedrock considers a tool

 definition to look like.

 So somewhere inside of our code, we really have to take this tool

 definition right here

 and convert it into the exact structure that is expected by bedrock.

 I have already written out the code to do that for us.

 So back inside of our editor, if you open up the core directory and

 then bedrock.py inside

 of here, this is all of our code related to running bedrock and

 communicating with messages

 and so on.

 And if you scroll down towards the bottom, you will notice that there

 is a function

 side here called two bedrock tools.

 So this will take in that list of tools that we just saw printed out.

 And then for each tool, it's going to convert it into the structure

 that is expected by

 bedrock.

 Once again, this is just a little bit of a gotcha.

 Just something you need to be aware of.

 This conversion process is already being done automatically somewhere

 else in the code

 based for us.

 So we don't have to worry about calling to bedrock tools inside of

 the code that you and

 I are writing right now.

 I just want you to be aware that yes, we do have to go through this

 little bit of a translation

 step.

 Now, before we move on, there's one other thing I want to test.

 Remember, we just implemented the function that's going to allow us

 to list out some

 tools and pass them off to Claude and the function that's going to

 allow us to call

 a tool that is implemented by the MCP server and then pass the result

 off to Claude as

 well.

 I've already implemented the code that is going to call list tools

 and call tool for

 us somewhere else inside this project.

 So now that we have added in this functionality, now that we have

 defined these tools and the

 ability to call a particular tool, we can now run our CLI again and

 attempt to get Claude

 to make use of these tools.

 In other words, we can ask Claude to inspect the contents of some

 particular document and

 even edit a document.

 So let me show you how we do that.

---

#### Lesson 67: Defining resources

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276799](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276799)

**Video:** 11 - 007 - Defining Resources.mp4 | **Duration:** 9m 45s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, we're going to move on to the next major feature

 inside of MCP servers,

 which is resources. To help you understand resources, we're going to

 be implementing

 another feature inside of our project. Here's what we're going to add

 in. I want to allow a user to

 mention a document by putting in an @ symbol and then the name of a

 document. Whenever they do so,

 I want to automatically fetch the contents of that document and

 insert it into the prompt that

 we send off to Claude. So in total, there's going to be kind of two

 aspects to this feature.

 Whenever a user types out the @ symbol inside of a message, we're

 going to automatically show

 a list of all the different documents that they can mention inside of

 a little autocomplete window.

 Then whenever a user submits a message with a mention inside of it,

 we're going to automatically

 get the contents of that document and insert it into the prompt that

 we send off to Claude.

 So for example, if a user says something like what's in the @report.

pdf file,

 I would want to assemble a prompt like this and send it to Claude. So

 we're going to have the

 query inside there from the user and then we're also going to tell

 Claude that the user might

 have referenced some document and here is the contents of the

 document. So the approach here,

 or the idea here, is that we will not have to rely upon Claude to go

 and make use of some tool

 to figure out what is inside of the @report.pdf file. Instead, the

 user can just preemptively

 mention the file and we're going to automatically insert some context

 ahead of time. Now one thing

 I want to clarify here is that we're kind of talking about two

 separate features. The first

 feature is that whenever a user types in the @ symbol, we really need

 the MCP server to give

 us a list of all the different documents that the user can possibly

 mention. And then the second

 aspect here is that whenever a user submits a message that contains a

 mention, then we need the

 MCP server to give us the contents of a single document. To get this

 information out of our MCP

 server, we are going to be making use of resources. Resources allow

 our MCP server to expose some

 amount of data to the client. We usually define one resource for each

 distinct read operation.

 So in our example, we need to get a list of documents and read the

 contents of a single document.

 So we would probably end up making two separate resources. One

 resource would be responsible for

 returning just a list of document names so we can put them inside the

 autocomplete. And then we

 would probably make another resource that will expose the contents of

 a single document based

 upon its document ID. When we define these resources, they're going

 to be accessed through our MCP client.

 So the entire flow that we're going to eventually put together here

 whenever user types in something

 like what's in the @ and then presumably they're going to put in

 something right there. As soon as

 they type in that @ character, we need to display a list of document

 names to put in the autocomplete.

 So our code is going to reach out to the MCP client, which in turn is

 going to send a read

 resource request off to the MCP server. Inside of that read resource

 request, we're going to include

 something called the URI. That is essentially the address of the

 resource we want to read.

 This URI gets defined whenever we put together our resource initially

. So the URI is that right there.

 When we send off this read resource request, the MCP server is going

 to look at the exact

 URI that we put inside of here and then run the function we put

 together right there. Take the

 result and send it back to us inside of a read resource result

 message. We can then take the data

 inside there and display it inside of our autocomplete or do whatever

 else we need to do with it.

 There are two different types of resources, direct and templated. You

'll also sometimes see

 direct resources referred to as static resources. A direct resource

 just has a static URI. So it's

 always going to be the exact same thing, such as docs colon slash

 documents.

 A templated resource will have one or more parameters inside of its

 URI. So for example,

 we might have documents slash and then kind of a wild card right here

. So we can put in any document

 ID we want to. And whenever we ask for this resource, that document

 ID right there inside the URI

 will be automatically parsed by the Python MCP SDK and provided as a

 keyword argument to our function.

 The keyword argument will have the exact same name of whatever string

 you put in right there.

 So doc ID right there will be doc ID right there. As you can probably

 guess, we'll make use of

 templated resources anytime that we want to allow a little bit more

 selection or variety or customization

 in what someone is asking for out of our MCP server. Implementing

 resources is pretty straightforward.

 So let's go back over to our editor and we're going to add in some

 resources to our server right away.

 All right, so back over inside my editor, I will find the MCP server.

py file. I'm then going to

 scroll down a little bit and I'm going to find some comments for

 writing resource to return all

 document IDs and writing resource to return the contents of a

 particular document. Now for this

 first one right here, I put in the comment document IDs. Remember,

 for us, our document IDs are

 essentially the name of the document. So for us, we're really just

 returning these IDs. They're

 going to serve the purpose of the name. That means we can put them

 directly into that auto

 complete element. All right, so to make our resource, I'm going to

 delete that to do.

 And then I'll add in a MCP resource. The first argument is going to

 be the URI for accessing this

 thing. Again, it's kind of equivalent to a route handler. So I will

 use docs colon slash slash

 documents. And I'm also going to add in a MIME type of application

 slash JSON. A resource can

 return any type of data. So it can be plain text. It can be JSON. It

 can be binary data, anything.

 It's up to us to kind of give our client a hint as to what kind of

 data we are returning.

 To do so, we're going to define this MIME type. A MIME type of

 application slash JSON is a hint

 to our client who's eventually going to ask for this resource right

 here, that we're going to be

 sending back a string that contains some structured JSON data. And so

 it would be up to our client to

 deserialize that data, or essentially turning into some usable data

 structure.

 Underneath that decorator, I'll write out my function of list docs.

 And I'm going to return a

 list of strings. And then inside there, I will return list docs keys.

 So just take all the keys

 out of that dictionary and turn it into a list. And I'm going to

 return it. Now you'll notice that

 we are not returning distinct JSON here. In other words, we're not

 actually returning a string.

 The MCP Python SDK is going to automatically take whatever we return

 and turn it into a string for us.

 All right, let's take care of our second resource. So I'm going to

 delete that comment and then

 replace it with MCP resource docs colon slash documents. And then

 this time I want a templated

 resource because I'm putting in this wild card right here. And then

 my MIME type this time around,

 just for a little bit of variety, I'm going to be returning plain

 text because it's going to be

 just the contents of the document. And I'm not going to wrap it up in

 any kind of structure.

 Now just so you know, in a real application, something like read a

 document, I would probably

 return an entire document record. So some kind of dictionary that

 contains maybe the ID, the content,

 the author name, the author ID and stuff like that. But just for the

 sake of an example,

 I'm going to return just the text of the document to show you how we

 would normally return plain

 text. So in this scenario, my MIME type would be text plain.

 And then I will make fetch doc, I'm going to take doc ID, which is

 going to be a string.

 And I'm going to return a string. Once again, whatever word you put

 right there, it's going to

 show up as a keyword argument inside of your function. If we added in

 some additional parameters

 inside of here, such as maybe doc type or something like that, it

 would just show up as an additional

 keyword argument like so. Then inside of here, I'm going to first

 make sure that the ID that

 this person is asking for actually exists. So if doc ID, not in docs,

 I'm going to raise a value

 error with a F string that says doc with ID, not found. And then if

 we get past that check,

 I'll return docs doc ID. And that's it. Now let's try testing this

 stuff out inside of our MCP

 inspector once again. So remember, at our terminal, we can run the

 command uv run MCP dev MCP server

 dot pi. That's going to start up a web server at port six two seven

 seven or see me six two seven

 four is the default. So I can make sure I open that up inside my

 browser. Here we go. I'll click

 connect, I'll then find resources. And then I should be able to list

 out all the different

 resources that are available. Now when I list out resources, this is

 going to be specifically

 static or direct resources. So I'll see only doc slash documents. And

 then I can separately list

 out all my different resource templates. And so we'll see that I have

 one resource template

---

#### Lesson 68: Accessing resources

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276797](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276797)

**Video:** 11 - 008 - Accessing Resources.mp4 | **Duration:** 4m 38s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

We have defined two separate resources inside of our mcp server.

 So now our client needs the ability to request these resources.

 To do so, we're going to add in a single function inside of our mcp

 client.

 And remember, this mcp client is going to have some functionality

 that we're putting together

 that is going to be used by the rest of our application.

 And I've already put together that code already.

 So somewhere else inside this project, something is going to try to

 make use of this

 function that we're about to add into the mcp client.

 To get started, I'm going to open up the mcp client file again.

 I'm going to scroll down and find read resource right here.

 So our goal inside of here is to read a particular resource by making

 a request

 off to our mcp server, and then parse the contents that come back,

 depending upon its mine type, and then just return whatever data we

 get.

 So you'll notice that a argument to it is the URI.

 This is going to be the URI of the resource that we want to fetch

 from the server.

 In order to make request, just to get all of our types nicely,

 we're going to add two imports at the very top of the file.

 I'm going to add in an import for the JSON module and from pydantic,

 I will import AnyUrl.

 Then I'll go back down to our read resource function.

 I'm going to clear out the comment in the return statement.

 Then I'll get a result from calling await self session, I want to

 read resource.

 And then again, this is really just to get the types to work out.

 We're going to put in a AnyUrl with the input URI.

 Then I'm going to take from that result,

 response or to excuse me, result contents at zero.

 And I want to make this clear right here why we were adding this in.

 So just a moment ago inside of our inspector,

 we saw the response we get back.

 So this is essentially that result variable.

 Result has a contents list and there's going to be a list of elements

 inside there.

 We really only care about the very first one.

 So I want to get the first dictionary.

 I want to access the type property and the mine type.

 I want specifically the mine type because it's going to help me

 understand

 what kind of data we got back.

 If it is JSON, then I want to make sure I parse the text as JSON and

 return that result.

 So let me show you how we're going to do that.

 I'm going to add in a if is instance of resource types, text,

 resource contents.

 And inside there, if resource, mine type is equal to application JSON

.

 So this is our hint in use.

 If the server told us that it's giving us back some JSON,

 we need to make sure that we parse the text content as JSON.

 So I will return in that case a JSON loads of resource dot text.

 And then otherwise, if we don't fall into that if statement and

 return early,

 I want to just return resource dot text.

 So in this scenario would be returning the text as just plain text.

 We're not parsing anything.

 So this would really be the case in which we get back the contents of

 a single document.

 All right.

 So that should really be it.

 We've got our read resource put together.

 Now, again, I want to remind you, I know I've said this several times

,

 but I just want to remind you because I think it might be a little

 bit unclear.

 The code that we're writing inside of the MCP client is being used

 from several other places

 inside of this code base.

 So somewhere else in this code base, we're going to be calling that

 function that we just

 put together to get the list of document names and then eventually

 get the contents of a document

 to put into a prompt.

 So at this point, everything should essentially work because the rest

 of the work

 has already been done for us.

 So with that in mind, let's go back over to our terminal and we're

 going to test out

 our CLI application again and see if this mention feature works.

 Okay.

 So back over here, I'll do a uv run main dot pi.

 And now I should be able to say something like what's in the at.

 And there we go.

 I see my list of resources and I can use the arrow key to scroll

 through.

 Once I am at a resource I like, I'll just hit space and we'll insert

 that resource.

 So what's in the report dot PDF document and now I can tell you that

 everything is working

 as expected here.

 In other words, the contents of this document is being sent off to

 Claude inside of prompt.

 So if I submit this, I should see an immediate response and it's

 going to tell me what is inside

 of report PDF.

 So this time around, Claude did not have to use a tool to read the

 contents of the document.

 All right.

 So that is resources.

 Again, we make use of resources to expose some amount of information

 from our MCP server.

---

#### Lesson 69: Defining prompts

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276801](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276801)

**Video:** 11 - 009 - Defining Prompts.mp4 | **Duration:** 7m 45s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Last major focus we're gonna have inside of our MCP server

 is going to be on prompts.

 Once again, just like we did with resources,

 we're going to implement a small feature inside of our project

 and we're going to use this feature

 to understand what prompts are all about,

 just like we did with resources a moment ago.

 Let me tell you about the feature

 we're gonna add into our program.

 We're going to add in support for slash commands.

 So for example, I want to have a format command.

 I've got some screenshots over here

 of how it's going to work.

 Whenever a user types in a slash,

 we're going to list out some number of commands

 that are supported by our application.

 For right now, we're gonna have just one command

 called format.

 So if I type in just slash,

 I should see a little autocomplete right here

 and the only autocomplete option should be format.

 If I then select format,

 I should be prompted to add in some document ID after it.

 So one of our different document names

 like report.pdf or whatever else.

 Then whenever user runs this command,

 the goal is to get Claude to reformat this document

 using a markdown syntax.

 So in other words, take the plain string that we have

 without any special formatting tied to it

 inside of each of our documents right now.

 Remember inside of our MCP server,

 our current document content is just plain text.

 We want to feed this into Claude

 and somehow get Claude to rewrite it

 using markdown syntax.

 So I would expect to see some output like this,

 something that says I'll help you reformat the document.

 Claude is then going to use a tool

 to read the contents of the document

 and then finally inside the final response,

 I want to see the content of that document

 rewritten down here in markdown syntax.

 Now, there is something interesting

 about this feature that I want to point out.

 The real core of this feature,

 like the real goal here,

 is to allow a user to reformat a document

 into markdown syntax.

 And that is an operation

 that actually doesn't require you and I,

 the developers, to write out any code to implement.

 What do I mean by that?

 Well, a user can already launch our CLI

 and say something like reformat

 the report.media file in markdown syntax.

 A user can already do this, no issue whatsoever.

 And Claude is going to do a reasonable job of it.

 It's going to take the contents of our document

 and reformat it into markdown.

 As you can see right here,

 it worked entirely perfectly.

 So what are we really doing with this feature?

 Well, the thought process here

 is that if we just left this up to users

 and allowed them to manually type in something

 like convert this to markdown,

 they might get a okay result,

 but they might get much better result

 if they had a really strong prompt

 that is custom tailored for this particular scenario

 of converting a document into markdown.

 So a user might be a lot happier

 if you and I sat down as the MCP server authors

 and wrote out and tested and emailed

 and went through the entire process

 of developing a really thorough, fantastic prompt,

 like the one you see on the right hand side.

 So again, just repeat.

 Yes, a user can execute this entire workflow on their own,

 but if they use this fancy prompt over here, instead,

 well, I think they would be all the better.

 This is the real goal of the prompts feature

 inside of MCP servers.

 The thought here is that ahead of time,

 we can define a set of prompts inside of our server

 that are custom tailored to whatever our server

 is really specialized to do.

 In our case, our server is all about managing documents,

 reading documents, editing documents, and so on.

 So we might decide to add in a set of prompts

 that are very high quality, that have been evaled and tested,

 and we know that they work in a wide variety

 of different scenarios.

 We can then expose these prompts for use

 inside of any client application,

 like the CLI app that we are putting together right now.

 Now, one thing I want to point out here

 is that we could develop this prompt

 and just put it directly into our CLI code base.

 That is totally possible.

 We could do that, obviously.

 But again, the thought here is that your MCP server

 that might specialize in some particular task

 might expose some number of prompts

 so that people can just come and use

 without having to worry about developing them ahead of time.

 To define a prompt inside of our MCP server,

 we're going to write out a little bit of syntax,

 very similar to the tools and resources

 we have already put together.

 We will use the prompt decorator.

 We will add a name to the prompt,

 and optionally a description as well.

 Then, whenever the client asks for this prompt,

 we'll send back a list of messages.

 These are actual user and assistant messages.

 So we can take the messages

 and send them off to Claude directly.

 All right, so let's go over to our server,

 and we're going to try putting together our own prompt.

 And just like you see right here,

 it's going to be all about taking the contents of a document

 and somehow rewriting it in Markdown format.

 Okay, so back inside my editor,

 I'm going to find my MCP server file.

 I'm going to go down a little bit

 to the comment about rewriting a document

 in Markdown format.

 I'll delete that to do,

 and then I'll add in a MCP prompt,

 the name of format,

 and a description of rewrites

 the contents of the document in Markdown format.

 I'll then add in an actual implementation.

 So format document.

 I'm going to receive as an argument a doc ID,

 and then optionally we can add in a field description here

 as well, just like we did with our tool earlier on.

 So I can optionally add in a field

 with a description of ID of the document to format.

 And I'm also going to add in a type annotation of string,

 just to make sure that's really clear as well.

 From this function,

 we are going to return a list of messages.

 I'm going to make sure I add in an import

 for this base thing at the top right away.

 So right underneath the existing MCP server import,

 I will add in from MCP server fast MCP prompts import base.

 Then back down at the bottom.

 Inside of here, we're going to define

 our very well tested, very well-evalmed prompt.

 I wrote a prompt out ahead of time.

 I'm going to paste it in like so.

 So this prompt is just asking Claude

 to take in a document ID.

 Implicitly, we are kind of asking Claude

 to fetch the document ID's contents

 using the read document tool.

 And then after getting that document,

 just go ahead and rewrite it with Markdown syntax.

 And finally, after rewriting it,

 edit the document as well to save those updates

 inside of our server.

 Now, after defining this prompt,

 we're then going to return a list of messages.

 So down here, I'm going to return a list

 with base user message.

 And I'm going to feed in our prompt

 that we just wrote out to it like so.

 Now I'm going to save this file.

 And then let's go start up our MCP development inspector

 and test out this prompt from that interface.

 So at my terminal, I'll run that same command again

 and then navigate to that address inside of my browser.

 I'll make sure I connect to my server.

 I'll then find the prompts section.

 I'm going to list out all the different prompts

 that are available to us.

 And at this point in time, we have one prompt, just format.

 So I'll click on format and then I have to enter

 in a document ID right here.

 Let's, this time around, maybe we'll put in a document ID

 of how about Outlook.pdf.

 So I'll put that in and then get prompt.

 And then here is our list of messages.

 So these have been put together ahead of time.

 I've got one message part here.

 So a text part with our full prompt right there.

 We could see that the document ID was interpolated into it.

 So now that we have these messages,

 we can take them and send them off to bedrock.

 And hopefully we're going to get back

 some appropriate kind of response.

 So once again, the entire idea here behind these prompts

 we might implement inside of our MCP server

 is that the prompts we are defining

 are going to be well tested, well evaled,

 really specialized to one particular use case.

---

#### Lesson 70: Prompts in the client

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276795](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276795)

**Video:** 11 - 010 - Prompts in the Client.mp4 | **Duration:** 3m 1s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Our last major task is to implement some functionality inside of our

 MCP client and allow us to list out all the different prompts that

 are defined inside the MCP server and also get a particular prompt

 with some variables interpolated into it.

 So let's first implement list prompts.

 I will delete the comment and replace it with a result is await self

 session list prompts and then I will return result.props and that's

 pretty much it.

 And then get prompt. Now, to be clear, when we get an individual

 prompt, we're going to be given some number of arguments. These

 arguments will eventually show up inside of our prompt function.

 So for example, inside a format document right here, we expect to

 receive a document ID.

 Inside of this our dictionary, the expectation is that there will be

 a document ID key and that will be passed in to the appropriate

 function over here and then we will get that value interpolated into

 the prompt itself.

 So inside of the get prompt function, I will get a result from self

 session, get prompt.

 I'm going to pass in the prompt name.

 That's the name of the prompt I want to retrieve and then I'll pass

 in the arguments and then I will return result.messages.

 So those are the messages coming back.

 They form some kind of conversation that we want to feed directly

 into Claude.

 And that's it.

 That's all we have to do for our client.

 So now we can test this out inside of the CLI itself.

 I'll flip back over, run the project again.

 And now if I put in a slash right here, I'll see that I can access

 this format command.

 Now format is really just the name of the prompt that we're going to

 invoke.

 So if I select that and then hit space, I'll then be asked to select

 one of the different documents.

 You'll go with plan.MD, I'll hit enter and then we're taking that

 entire prompt, really just that single user message and feeding it

 directly into Claude.

 So Claude now has the instructions to go and reformat a document into

 Markdown syntax.

 And it has also been given the ID of the document that we want to

 reformat.

 So the first thing it needs to do here is go and fetch that document

's contents.

 And it will do so by using the get document tool.

 And then finally, Claude is going to respond with the Markdown

 version of this document.

 So here is the document with a bunch of Markdown syntax inside of it.

 All right, since it looked like this worked as fine, let's do a quick

 recap on prompts and make sure we understand

 what they are all about.

 We begin by writing out and evaluating a prompt that has some relevancy

 to our MCP server's purpose.

 In our case, we were making a document server.

 So having some functionality or something about rewriting a document

 in a different style, I think it kind of makes sense.

 Once we have put our prompt together, we'll define a Sonnet inside

 the MCP server and then our client can ask for that prompt at any

 point in time.

 When we ask for the prompt, we will put in some number of arguments

 that will be provided to this prompting function right here as

 keyword arguments.

 And then our function can make use of those keyword arguments inside

 the prompt itself.

---

#### Lesson 71: MCP review

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276794](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276794)

**Video:** 11 - 011 - MCP Review.mp4 | **Duration:** 4m 12s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

We are all done with our project, but before we move on, I want to do

 a quick recap on the three server primitives that we learned about,

 so tools, resources, and props.

 In particular, I want to highlight something interesting about each

 of these, namely, what part of an app is really responsible for

 running each?

 In other words, in a typical application, who is really running each

 of these things and who benefits from them?

 Well, we would say that tools are model-controlled.

 This means that Claude alone is really responsible for deciding when

 to run a given tool.

 Resources are app-controlled, in other words, some code running

 inside of your app is going to decide that it needs some data

 provided by a resource.

 It will be your app's code that decides to execute a resource and use

 the return data in some way, maybe by using that data in the UI or

 something like that.

 In our case, we fetched a resource and then used that data inside the

 UI to provide a list of auto-complete options.

 We also fetched a resource to augment a prompt, both those things

 were really application-related code that was authored by you and I

 to put together.

 And finally, prompts are really user-controlled, so a user decides

 when a prompt is going to run.

 A user might start the invocation of a prompt by clicking on some UI

 element, like a button or a menu option, or they might make use of a

 slash command, which is what we did.

 The reason I highlight what is controlling each of these is to give

 you some idea of their purpose.

 So if you ever need to add capabilities to Claude, you're probably

 going to want to look at implementing some tools inside of your MCP

 server or consuming some server's tools through your MCP client.

 If you ever want to get some data into your app for the purposes of

 showing content in the UI or something similar, then you probably

 want to use a resource.

 And if you ever want to implement some kind of predefined workflow,

 you probably want to look at prompts.

 Now, you can see examples of all these ideas inside of the official

 Claude interface at Claude.ai.

 So here's what it currently looks like for me.

 You'll notice that underneath the main chat input are some buttons

 right here.

 If I click on one and then click on one of these examples, you'll see

 that I immediately dive into a chat.

 So this was a user controlled action. I, as the user, decided to

 start up this particular workflow and I'm making use of a prompt that

 was probably already written ahead of time and probably has been

 optimized in some way.

 So to implement that list of buttons right there, we would probably

 want to put together a series of different prompts inside of a MCP

 server.

 Likewise, if I go back and maybe click on this little tab right here,

 the plus button, you'll notice that I have a add from Google Drive

 button.

 Now, I'm not going to click on it because it's going to show some of

 my internal documents.

 But if I click on that button, I'm going to see some documents that I

 can add into this chat as some context knowing what documents to

 actually render in that list.

 And then whenever I click on one, automatically injecting its

 contents into the context of this chat, that is all application

 related code.

 So it is solely the application that needs to know the list of

 documents to render here. And that's, again, specifically UI related

 elements.

 So to implement that listing of documents from Google Drive, I would

 probably look at implementing a resource inside of a MCP server.

 And then finally, if I enter in a message to this chat of something

 like what is square root three, use JavaScript to calculate the value

 and send it off.

 I'm clearly expecting Claude to somehow execute some JavaScript code,

 which would likely be done through the use of a tool.

 In this case, the decision to use a tool was 100% model controlled.

 It is the model that decided to use some JavaScript tool execution.

 To implement something like this inside of a MCP server, we'd likely

 want to, you guessed it, provide a tool.

 So in total, that's our three different server primitives. And each

 one is really intended to be used by a different portion of your

 overall application.

 So we got tools which are generally going to serve your model,

 resources, which are generally going to serve your app and prompts,

 which are going to serve your users.

 And once again, these are high level guidelines.

 And the only reason I mention them is to just give you a sense of

 when you should use each of these primitives, depending upon what you

 are trying to put together.

---

#### Lesson 72: Quiz on Model Context Protocol

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/289299](https://anthropic.skilljar.com/claude-in-amazon-bedrock/289299)

---

### Agents

#### Lesson 73: Agents overview

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276804](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276804)

**Video:** 12 - 001 - Agents Overview.mp4 | **Duration:** 1m 4s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

This is going to be an exciting module.

 We are going to learn about building agents,

 which are one of the most interesting use cases

 of language models.

 However, as exciting as agents are,

 we really have our work cut out for us.

 You see, the field of agents is still being explored.

 There are a variety of different open questions

 about absolutely foundational aspects of agents.

 For example, there isn't even a single agreed upon definition

 of what an agent is.

 So with this difficulty in mind,

 let me show you how we are going to cover agents

 inside this module.

 Here's our plan.

 We are going to kick off this section

 by examining two agents that have been authored

 and released by Anthropic.

 They are Claude Code and Computer Use.

 If we can understand how these agents were designed

 and how they work, we can extract some insight

 into what agents really are

 and what makes an effective agent.

 We are going to start with Claude Code.

 I'll walk you through the setup process.

 We'll understand its use cases

 and get some hands-on experience with it.

 We will then repeat that process with Computer Use

 and then circle back and analyze

 what makes these agents so successful.

---

#### Lesson 74: Claude Code setup

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276809](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276809)

**Video:** 12 - 002 - Claude Code Setup.mp4 | **Duration:** 1m 49s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's take a look at Claude Code.

 We'll do some setup, learn how it works, and see some advanced use

 cases.

 Claude Code is a terminal-based coding assistant.

 This is a program running in your terminal that can help with a wide

 variety of code-related tasks.

 To help you with coding projects,

 Claude Code has access to many different tools,

 so it has many basic tools like the ability to search, read, and edit

 files.

 But it also has many advanced tools, like web fetching and terminal

 access.

 Finally, Claude Code can act as an MCP client.

 And you know what that means?

 It means it can consume tools that are provided by MCP servers,

 so we can easily expand the capabilities of Claude Code

 by adding in some additional MCP servers.

 Let's now go through a little bit of setup and install Claude Code on

 your machine.

 Setup is easy.

 We're going to first install a copy of Node.js.

 You might already have Node installed on your machine,

 and to figure out whether or not you do,

 open up your terminal and execute the command npm help.

 If you see a result come back, that means you probably already have

 Node installed.

 Once you have Node installed,

 you'll do a npm install command that will install Claude Code itself.

 Finally, by default, Claude Code tries to access Anthropic's API.

 So we need to update a little bit of configuration

 just to get Claude Code to make use of Bedrock.

 This takes the form of setting three different environment variables,

 which I've listed on here at the bottom of the screen.

 One last thing to just keep in mind,

 you also need to set up your AWS credentials,

 or alternatively, set the AWS access key and secret key.

 Now, a full setup guide can be found at the official

 Anthropic documentation at docs.anthropic.com.

 Now, I'm going to let you go through this setup process on your own,

 again, just these three steps right here.

 As soon as you are done,

 we're going to walk through a little project together

 and see what Claude Code can really do for us.

---

#### Lesson 75: Claude Code in action

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276811](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276811)

**Video:** 12 - 003 - Claude Code in Action.mp4 | **Duration:** 10m 29s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

To get you some hands-on experience with Claude Code,

 I created a small project for us to work on.

 You should find the source for this project in

 a zip file attached to this lecture.

 I would encourage you to download this zip,

 extract its contents, and then start up

 your code editor inside of this new project directory.

 I've already opened up the project inside of my editor.

 Once you have the project open,

 you might be tempted to look through the project contents,

 and maybe go through a little bit of setup,

 which is described inside the readme file.

 But before you do, there's something important I would

 like you to understand about Claude Code.

 Claude Code is not a tool that is just going to write code for you.

 Naturally, it absolutely can,

 but that's not the only thing that Claude Code is about.

 Instead, you really want to view Claude Code as

 another engineer who's working on this project alongside you.

 Every task that you would normally go through on a normal project

 can really be fully delegated off to Claude.

 So this includes everything from initially setting up a project,

 to designing new features, to deployment, and to support.

 As we go through this project,

 we're going to leverage Claude heavily to aid us in various steps.

 We will use Claude to set up the project for us,

 to plan out a new feature, to write tests and code,

 and then later on, on a slightly different project,

 I'll show you how we can use Claude Code to automatically discover

 and fix errors in a production environment.

 So let's get to it.

 Back inside my editor, I'm going to open up my terminal,

 and then launch Claude Code inside there by executing Claude.

 Then, once I have this open,

 I'm going to put in my first directive to Claude.

 I'm going to ask it to read the contents of the README file,

 and go through any setup directions that are listed inside of here.

 I will ask Claude to read the contents of the README file

 and execute these setup directions listed in it.

 Claude will then use a variety of different tools to read that file

 and then execute a series of different commands.

 It will create a new virtual environment,

 activate the environment, and then install some dependencies.

 Once that is complete, we are going to run a command

 that will help Claude get a better understanding of our project.

 We're going to do so by running the init command.

 This is a command that we're going to execute inside of Claude Code

 itself.

 When you execute this command,

 Claude will automatically scan your code base

 to understand your project's general architecture,

 coding style, and so on.

 Once complete, Claude will write all of its findings

 into a special file named Claude.md.

 Whenever we run Claude again in the future,

 this file will be automatically included as context.

 Just so you know, there are three different Claude files.

 Project, local, and user.

 We're going to see some references to these in a minute,

 so we'll discuss what they're all about then.

 Whenever you run this init command,

 you can also optionally add in some special directions

 for some areas for Claude to focus on.

 So let's try this out right now

 and see what is generated for our project.

 I'm going to run the init command,

 and when I do, I'm going to pass in some special instructions.

 I'm going to ask Claude to include some detailed notes

 on defining MCP tools.

 Once it is all done, I'm going to take a look

 at the newly generated Claude.md file.

 So this is a summary of what Claude thinks of our code base.

 At the top, it will list out some important commands

 that it might need to run in the future.

 We'll get some listing around our coding style

 that we've used inside this project,

 and then as I specially requested,

 it also included some information

 around defining MCP tools.

 As I mentioned a moment ago,

 this file is going to be included as context for Claude

 in any follow-up request we make in the future.

 Now, projects change over time.

 We might change our coding style

 or add in some additional commands.

 So if that ever happens,

 we can very easily manually edit this file,

 or we can choose to rerun the init command.

 If you rerun this command,

 Claude will update the contents of the Claude.md file.

 Finally, as a very small shortcut,

 we can put in a pound and then type in some specific note

 that we want to be appended into the contents of that file.

 So we can use this as a tool

 to give very specific small directions to Claude

 that will be included in all follow-up requests.

 So for me, I might add in a direction here

 that says something like always apply appropriate types

 to function arcs.

 If I run that, I'll then be asked

 where I want to add this little note.

 This is where we see that project memory,

 local memory, and user memory appear.

 In my case, this is a note that I want to be shared

 with everyone who is working on this project,

 so I will add it to project memory.

 Once I add that in,

 I can then check the contents of my Claude.md file,

 and either somewhere under a code style

 or perhaps at the very bottom,

 I'll probably see whatever note I just added in.

 At this point, we have added a new file to our project,

 and this project is being managed by Git.

 So normally, we would open up our terminal,

 stage this new file that we just created into Git

 and then commit those changes.

 We could do all that manually,

 but it'd be a lot faster

 if we just ask Claude to do it for us.

 So I'll ask Claude to stage and commit all changes.

 Claude will then take a look at all the different changes

 we have made to the code base,

 write a descriptive commit message,

 and commit those files.

 Next up, I would like to show you some techniques

 for increasing Claude's effectiveness when writing code.

 We are going to add a new feature into this project.

 As a reminder, this project is a very small,

 very simple MCP server.

 We are going to ask Claude to add in a new tool to the server

 that will read a Word document or a PDF file

 and convert the contents to Markdown.

 Now, we absolutely could just type in directions

 for that to Claude, something like make a Word doc plus PDF file

 to Markdown conversion tool.

 But before doing that,

 I want you to know that we can dramatically increase

 the effectiveness of Claude by putting in

 a little bit more effort.

 So let me show you how.

 Think of Claude code as being an effort multiplier.

 If you put a little effort into how you direct Claude,

 you will get back significantly better results.

 I'm going to show you two different workflows,

 two different ways of instructing Claude

 on how to approach a task.

 Both of these workflows require a little bit

 of effort on your side,

 but they allow Claude to tackle much more complex problems.

 In this first workflow,

 we're going to go through three distinct steps.

 First, we're going to identify some areas of our code base

 that we know are relevant to a feature

 that we are trying to work on.

 We're then going to ask Claude

 to specifically read and analyze those files.

 Second, we're going to tell Claude about the feature

 we want to build and ask it to plan out a solution.

 So the steps will actually go through to implement

 whatever feature or problem you're trying to solve.

 And then finally, after Claude has gone through that planning step,

 we will ask Claude to actually implement these solution.

 Let me show you how we would do this

 for our particular feature

 of adding in some new document conversion tool.

 So first, I'm going to go through my code base

 and identify some different relevant files.

 You'll notice there is a tools directory

 and inside there is a math.py file.

 This is an example of a tool

 that has already been put together.

 So this might be some file that is relevant

 for the feature that we are trying to build

 just because it gives Claude a better idea

 of how to author a tool.

 Second, we might ask Claude to take a look

 at the document.py file,

 which includes a very helpful function,

 binary document to markdown.

 So this will take in some amount of binary data

 and convert it to markdown.

 So we can tell Claude to take a look at these files

 and Claude will get a better idea

 of how to write a tool in the first place

 and then how to actually do the conversion.

 So I'm going to add in some instructions to Claude

 and ask it to just read the contents of those files.

 Next, I'm going to ask Claude to plan out the implementation

 of a new tool called document path to markdown,

 which will take in a path to a PDF or Word document,

 read the file, convert the contents to markdown

 and return the result.

 I'm also going to tell Claude specifically

 to just plan the feature out

 and not to write any code just yet.

 In response, Claude is going to give us

 a pretty well detailed plan

 that's going to go through a couple of different steps

 that will be required to implement this entire thing.

 Finally, I

---

#### Lesson 76: Enhancements with MCP servers

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276806](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276806)

**Video:** 12 - 004 - Enhancements with MCP Servers.mp4 | **Duration:** 2m 30s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, I want to show you one of the most interesting aspects

 of Claude Code.

 Claude Code has an MCP client embedded inside of it. That means we can

 connect MCP servers to

 Claude Code and dramatically expand its functionality. To demonstrate

 this, we are going to connect

 Claude Code to the MCP server that we have been working on. We just

 authored a tool called

 Document Path to Markdown. We can now expose this tool to Claude Code,

 allowing it to read the contents

 of PDF and Word documents. So we are dynamically expanding the

 capabilities of Claude Code.

 Let me show you how to set this up. Back inside of my terminal, I'm

 going to end my running session

 with a control C. I'm then going to add in an MCP server to Claude

 Code by executing Claude,

 MCP, add. Then we're going to put in the name for our MCP server. Now

 the name can be anything you

 want it to be. In our case, we are making a server related to

 documents. So I'm going to call our

 server documents. And then finally, we're going to put in the command

 that we use to start up our

 server, which for us is uv run main.py. So uv run main.py. And that's

 it. I'm going to execute that,

 and I'll start Claude Code back up with Claude. And now we can make use

 of that tool that we just

 put together. To really test it out inside of our test directory,

 there's a fixtures folder,

 inside there are two demo files, so a Word doc and a PDF doc. Both

 contain just a tiny bit of

 documentation around MCP itself. So I'm now going to ask Claude to

 convert the contents of either

 one of those files into Markdown. And my expectation is that Claude

 will make use of that tool that

 we just authored a moment ago. And if we scroll up just a little bit

 here, sure enough, it worked.

 So this actually is the contents of that file. This ability to

 consume MCP servers adds an

 incredible amount of flexibility to Claude Code, and really opens the

 door to some really interesting

 development opportunities. For example, you might decide to add in a

 series of MCP servers related

 to your particular development flow. For example, if you use Sentry

 for production monitoring,

 you can add a Sentry MCP server to allow Claude to fetch details

 about errors that are occurring

 in production. If you make use of Jira, you can add in an MCP server

 that will allow Claude to

 view the contents of specific tickets. If you're a Slack user, you

 can add Slack to message you

 whenever Claude is completed working on some particular problem.

 These are just a small fraction of the

 possible enhancements that you can add into Claude Code. So it would

 definitely be worth your time

 to think about how you can enhance your particular development

 workflow.

---

#### Lesson 77: Parallelizing Claude Code

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276810](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276810)

**Video:** 12 - 005 - Parallelizing Claude Code.mp4 | **Duration:** 8m 12s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

In this video, we are going to explore

 one of the greatest productivity gains around Claude Code.

 Because Claude is a lightweight process,

 you can easily run multiple copies of it.

 Each instance can then be given a task,

 and the separate instances will then work in parallel.

 This technique allows a single developer

 to command their own team of virtual software engineers.

 So in the remainder of this video,

 I'd like to show you some of the specifics

 of implementing this workflow on a real project.

 The first big challenge to address

 is the fact that two instances of Claude

 might want to work with the same file around the same time.

 They might end up writing conflicting code

 or even invalid code,

 because they're not aware that some other process

 is modifying that same file.

 To solve this, we can make sure

 that each instance gets its own separate workspace.

 Each instance can then work with its own copy

 of your project, make changes,

 and then eventually merge those changes

 back into your primary project workspace.

 A common way of implementing this

 is by using a Git work tree.

 Git work trees are a feature of Git.

 So if your project is already managed by Git,

 you can use work trees immediately.

 Work trees are like an extension

 of Git's built-in branching functionality.

 A work tree allows you to create a total copy

 of your project inside of a new directory

 on your development machine.

 Each work tree corresponds to a separate branch.

 So if we have feature A on the left

 and feature branch B on the right,

 we can easily create two separate folders,

 each of which contain a complete copy of our code base.

 Then we can run separate instances of Claude code

 for each work tree.

 They will each work in their own separate environment

 in total complete isolation.

 Once each copy of Claude code has then finished some feature,

 we can then commit the work for each work tree,

 and then merge them back into our main branch,

 just like we would merge a normal branch.

 Now, this might sound like a really complicated workflow

 that would be very tough to manage,

 but remember, you can delegate an amazing amount of work

 to Claude code, including tasks around Git,

 so we can actually get Claude code itself

 to manage this entire workflow.

 Let me show you how.

 First, we could write out a prompt

 that will ask Claude to create the work tree for us.

 We might ask it to also open up our code editor

 inside of the newly created work tree folder,

 and that's what I'm asking for inside this prompt.

 I'm asking Claude to make a new work tree

 inside of a directory at trees slash feature A.

 I'm then going to ask it to SimLink in some dependencies

 because those are not tracked by Git,

 and so they will not be automatically copied

 into the work tree directory.

 And then I'll ask Claude to also open up my code editor

 inside of that new subdirectory.

 Now, let me show you how this would actually all work.

 So I'm gonna take this exact prompt right here.

 I'm going to run it inside of Claude code.

 Claude will then create the work tree,

 create the SimLink of the virtual environment,

 and then open up a new code editor instance

 inside of this new subproject folder.

 Inside of my original editor window,

 I'll see that there is a new trees directory,

 and inside there is a feature A folder.

 Inside that feature, a folder is a total copy of my project,

 and that copy has been opened up automatically

 inside of this new editor window.

 So inside this new editor window,

 I can launch Claude code

 and ask it to fulfill some task.

 Maybe add in some new feature or write tasks

 or do whatever else I need.

 And now this instance of Claude code

 is running in total isolation.

 Before I ask Claude code to do anything inside of here,

 however, I want to point out

 that this is a really long prompt to remember,

 and it's really tedious to have to copy paste

 all over the place anytime that we would want

 to create a new work tree.

 So we're gonna do a quick side topic here really quickly,

 a little side feature of Claude code

 that makes it really easy to create

 and merge in these separate work trees.

 So we could automate this entire prompt

 by making use of another feature of Claude code,

 support for custom commands.

 You can add in custom slash commands to Claude code

 by creating a markdown file inside of a special directory

 inside of your project.

 The special directory is dot Claude slash commands.

 Inside of a file inside that directory,

 we'll write out our entire prompt,

 and then we can easily run this custom prompt

 anytime we want to.

 Let me show you how we can use this feature

 to easily create a new work tree.

 So inside of my original editor window,

 I'm going to make a new folder called dot Claude.

 Inside there, I'll make another folder called commands.

 And then inside that, I'm gonna make a file

 called how about create work tree dot MD.

 And then inside of that,

 I'm gonna paste the prompt that we saw just a moment ago.

 Now this prompt has a hard coded feature name

 or a hard code branch of feature underscore A.

 And I don't always want to have exactly that string.

 So I'm gonna replace it with a special string

 of dollar sign arguments, all capitals.

 This allows us to inject some additional argument

 when we actually run this custom command.

 So now if I save this file

 and restart Claude code very quickly,

 I can run slash project colon,

 create work tree.

 It's called specifically create work tree

 'cause that is the name of the file

 I create inside that commands directory.

 I'll then put in a space

 and then the name of this new work tree.

 I'm gonna call it feature underscore B this time around.

 So now feature B is gonna be taken

 and substituted in for wherever I had placed dollar sign

 capital arguments.

 So now if I run this,

 I should very quickly see a new work tree created.

 And before long, I've got my new code editor instance.

 So now this one is open inside of work tree

 feature underscore B.

 And I can see that the additional work tree

 has been created inside that tree's directory.

 Now that we've seen how we can create multiple different

 work trees, I want to give you a full demo here.

 I'm going to create four separate work trees.

 Each one is going to be designed

 to complete some different tasks.

 So I'm gonna have four instances of Claude code running.

 The first one is going to add in some tests

 around documents.

 The second one is gonna add in some logging.

 The third one is gonna add in two new tools

 and then the fourth one is gonna add in a subtract tool.

 I'm going to run all these tasks in parallel

 and then I'm going to merge the changes from all them

 back into my main branch.

 So for step number one,

 I'm going to create four separate work trees.

 I now have four separate editor instances,

 one for each feature that I want to implement.

 I will start up Claude code in each

 and give each of them some directions

 on some feature to add in.

 When a work tree is complete,

 I will ask Claude to commit that code.

 Then when they are all complete,

 it is time to merge all these changes

 from these different branches back into my main branch.

 We do not have to do this by hand.

 Instead, we can ask Claude to do it for us.

 So I put together another prompt here,

 which I'm going to wire up

 as an additional custom command inside my project.

 This prompt is asking Claude to go

 into one of our different feature work trees,

 take a look at the most recent commit

 just to understand what was done

 and then attempt to merge those changes

 back into the main branch.

 I'm going to add this prompt in

 as another custom prompt inside my project.

 So inside of Claude commands, I'll make a new file.

 I'll call this one merge work tree, paste that in.

 I'll then restart Claude code.

 I'll then run the merge work tree command

 and I'm going to first ask it to merge

 and how about the document tests branch

 that was just created.

 I can then repeat this process

 for all the other work trees as well.

 When I merge in the subtract feature,

 there will be a merge conflict,

 but Claude is going to automatically resolve

 the conflict for me.

 When everything is merged in,

 I can then ask Claude to clean up

 all these different work trees that have been created.

 And that's it.

 So I've now implemented four separate features

 entirely in parallel through the use of Git work trees.

 This is clearly a really big productivity increase

00:08:05,560 --> 00:08:07

---

#### Lesson 78: Automated debugging

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276812](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276812)

**Video:** 12 - 006 - Automated Debugging.mp4 | **Duration:** 4m 24s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Claude Code is not just about helping you

author some code inside of your editor.

It can also help you after you have deployed your application

in monitoring for errors and helping you fix those errors as they

arise.

So in this video, I'm going to walk you through a sample workflow

where we are going to take a look at a production application

that is throwing some errors but only in a production environment.

We're going to see how we can make use of Claude Code

to automatically find and fix those errors.

So first, let me show you a little sample application I put together.

This is a very simple chatbot, and I'm currently running it locally

on my own computer.

You can see the evidence for that.

I'm currently at localhost 3000.

If I ask any question here, let's say maybe what's one plus one,

no problem, I'll get back an answer rather quickly.

This chat application also has the ability to make simple artifacts.

So for example, it can show a built-in spreadsheet.

I'm going to ask for a spreadsheet with some fake data.

And it appears that everything is working 100% as expected.

Now, remember, this application is currently running

in my local development environment.

But because everything is working just fine, as I'm testing it right

now,

I might decide to go ahead and deploy it into production.

So I've already done that ahead of time.

I've already taken this exact app and deployed it off to AWS Amplify.

So this is a production version of the exact same app.

It is hosted at Amplify right now.

I'm then going to execute the exact same test that I showed you a

moment to go.

I'm going to first ask, what is one plus one?

Then I will follow up with the exact same request that I made a

moment to go

in the local application.

So make a spreadsheet with some fake data.

And we're going to see that the request goes through.

But unfortunately, the spreadsheet itself is completely empty.

There's actually no data that has been generated.

So it is now clear that something in this production environment

is not really working as expected.

Everything in development worked just fine.

The exact same series of operations, completely fine in development,

but specifically in a production environment, I am running into this

error.

To figure out what the issue is, I could take a look at my CloudWatch

logs.

I already opened those up and I've already hunted through those logs

and found this source of this error.

So I've got an error message here.

It states the provided model identifier is invalid.

And then I've got a lot of debug information included in here as well.

So I, as an engineer, could take this error message,

which I had to hunt down inside of my logs and do a little bit of

local debugging

to try to figure out why this is failing in production, but not

locally.

Alternatively, I could delegate this entire task off to Claude.

Let me show you how inside of my GitHub repository for this project,

I created a GitHub action, which is going to run automatically every

day

very early in the morning.

On the screen right now, I have the results of a sample run from

earlier today.

I'll show you some of these logs from the GitHub action in just a

moment.

But first, let me show you a diagram that's going to help you

understand

what is going on inside this.

OK, so whenever this GitHub action runs, it's going to check out my

repository,

install some dependencies, and then install and set up Claude code.

I then also install an AWS CLI, which allows me to reach out and get

some logs from CloudWatch.

I then pass off some directions to Claude code.

I ask it to reach out to CloudWatch and find all the errors that have

occurred

in the last 24 hours.

I also include some logic in there to remove duplicate errors

and reduce the total number of errors down just to be manageable for

Claude's context window.

Once Claude has a list of errors, it then iterates over them and

attempts to fix each one.

And then once Claude hopefully has successfully fixed these errors,

it will commit those changes and automatically open a pull request

where I can view its work.

So in this case, as we just saw, I'm getting an error in our

production environment.

And I saw that error inside the logs.

If I now go over to my list of pull requests right here,

I'll say that Claude automatically ran.

It automatically found the issue, applied a fix, and then created a

pull request.

So now I could very easily review this pull request right here.

The entire issue is explained to me in plain detail.

And in this case, it was just a typo on my behalf.

I accidentally put in a invalid model ID that was only used in a

production environment.

So Claude noticed that it found the correct model ID and put the

correct one in committed the changes.

So now I can very easily review the changes and merge the pull

request.

This is just one sample workflow that you might use to automatically

monitor

and fix your apps in a production environment.

Remember, Claude code is very flexible and you can create your own

custom workflows

just like this one to aid your own debugging efforts.

---

#### Lesson 79: Computer Use

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276807](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276807)

**Video:** 12 - 007 - Computer Use.mp4 | **Duration:** 3m 5s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Let's take a look at the computer use feature inside of

 Claude. We're going to cover this in three different parts.

 I'm going to first give you a quick demonstration of

 computer use and help you understand why it's useful.

 We'll then take a look at some behind the scenes stuff and

 understand how computer use works.

 And then I'll show you how to set up the reference implementation,

 so you can test out computer use on your own.

 So let's get to it. Let's first go over a quick demonstration of

 computer use.

 For this demonstration, I've put together a very small web

 application.

 All it does is show a text area that supports the ability to

 mention a file or some kind of resource using the at symbol.

 So if I enter test and then at, I can scroll through a bunch of

 different

 options and eventually hit enter to select that particular option.

 Now, first glance, this thing appears to be working just fine.

 I can add in as many different mentions as I want.

 But if we use it a little bit more, we'll start to see a lot of janky

 behavior.

 For example, if I add in two mentions and then press the backspace

 key,

 I'll see that I suddenly get a pop up on the top left hand side of

 the screen.

 So it's clear that this thing doesn't quite work as expected.

 Now I could spend my time as a software engineer to sit here and

 figure out all the different cases in which this component fails.

 Or alternatively, I can delegate this task off to Claude's computer

 use.

 Let me show you how we do that.

 Now I have already set up a computer use environment in this window.

 So this is a demo that you and I are going to eventually set up on

 your computer

 a little bit later on inside this section.

 On the right hand side is a browser that is running inside of a

 Docker container.

 So this browser is completely isolated from the rest of my system.

 And then on the left hand side, I have a chat interface where I can

 give

 direct instructions to Claude and get Claude to interact with this

 browser

 in some particular way.

 Inside of that chat interface, I'm going to enter in a rather large

 prompt to Claude.

 I'm going to tell Claude that it's going to do some QA testing on a

 React

 component hosted at some particular address.

 I then outline some testing process for Claude and then some

 different test cases

 to go through.

 And at the very end, I'm asking Claude to write out a concise report

 that summarizes

 the output of all these different tests.

 So again, I'm using Claude computer use here to automate some QA

 testing,

 just to save myself some time.

 I'm going to take this big prompt, enter it into this chat interface.

 And then Claude is immediately going to spring into action.

 Claude is going to follow us in the instructions I listed inside

 there.

 So it's going to try to navigate to that site where I hosted this

 application

 and then go through each of those different test cases.

 The first test case will just verify that the autocomplete options

 appear.

 The second test case will verify that pressing enter will insert a

 mention.

 And the third will make sure that pressing that backspace key

 shows the autocomplete options underneath the mention itself and not

 on the top left hand side.

 After all the test cases run, we'll see some output in the chat

 window.

 So it tells me that the first test and the second test passed, but

 the third one failed.

 So again, this is a sign to me that I probably need to go and

 investigate

 this test case myself and figure out how to fix this.

 Either way, Claude's computer use functionality saved me, the

 developer,

 a lot of time in this QA process.

---

#### Lesson 80: How Computer Use works

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276805](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276805)

**Video:** 12 - 008 - How Computer Use Works.mp4 | **Duration:** 3m 30s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Now that we have seen a demonstration of computer use, let's get a

 better understanding of how

 computer use actually works behind the scenes. To help you understand

 computer use, we're going

 to first get a quick reminder on how tool use works with Claude. So

 whenever we want to use a tool,

 we will make a request off to Claude including a user message and some

 tool schema. This tool schema

 describes some additional functionality that we want to expose to Cl

aude. So in this example,

 I might send across a tool schema of something like get weather that

 would presumably allow Claude

 to affect some weather in a particular location like maybe San

 Francisco. Claude is going to take a

 look at the user's message and realize that it can't really answer

 the question by itself,

 so it's going to decide to use that get weather tool. To use the tool

, Claude will respond with a

 tool use part. So this will have a tool use ID, a name, and some

 input that it wants to feed

 into the tool. In this case, it would probably be a location of San

 Francisco. Then our server

 is going to have some amount of code written by you and me that will

 receive that location and

 then return the current weather at that spot. We're then going to

 take that result and send it back

 to Claude inside of a tool result part. So we can summarize this entire

 process in a diagram like

 this. We initially send Claude some kind of question and a list of

 tools. Claude decides to use a tool.

 We run some code or do something on Claude's behalf and then send the

 result back to Claude.

 It turns out that computer use follows the exact same flow because

 computer use itself

 is actually implemented with this exact same tool system. So here's

 how computer use actually

 works. We send a request off to Claude that includes a very special

 tool schema. The schema we send is

 very small. It's exactly what you see on the left hand side and it

 doesn't match the typical

 structure of a tool schema. Behind the scenes, this schema will be

 expanded into a much, much larger

 structure like the one you see on the right. And this larger

 structure is what actually gets fed

 into Claude. This large schema tells Claude that it can call an action

 function. And that the action

 function takes arguments like mouse move, left click, screenshot, and

 more. Claude might then decide

 to make use of that tool in some way. So it will send a tool use part

 back to us. Remember what we

 saw a moment ago with the get weather function. Whenever Claude decides

 to use a tool, it is up to

 us, the developers, to actually fulfill Claude's tool use request in

 some way. So to simulate a

 computing environment for Claude, we can set up a Docker container

 running some program that can

 programmatically execute key presses and mouse movements. Once we

 execute the requested key press

 or mouse movement, we then send a response back to Claude. So to

 summarize, this is exactly what's

 going on behind the scenes with computer use. Claude isn't actually

 directly manipulating a computer.

 Instead, computer use is implemented using the tool system, and it is

 up to us to provide the

 actual computing environment. The last thing I'd like to do is tell

 you how you can get started

 with computer use on your own. Luckily, you do not have to create

 that Docker container from

 scratch on your own. Anthropic has already implemented a reference

 implementation. This is a Docker

 container that already contains code to receive tool request from Cl

aude and execute programmatic

 mouse movements and key presses inside of the container. I've

 provided a link to the reference

 implementation on the left hand side. Setting up this implementation

 is really easy. All you need to

 do is get a Docker implementation. You might already have one

 installed. You then also need a local AWS

 profile. And once you have both of those, you'll execute a simple

 Docker command. And that's going

 to give you access to the same interface I showed you just a moment

 ago. You can then chat directly

 with Claude on the left hand side of the screen and test out Claude's

 computer use functionality.

---

#### Lesson 81: Qualities of agents

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276808](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276808)

**Video:** 12 - 009 - Qualities of Agents.mp4 | **Duration:** 3m 28s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

We have now taken a look at two agent type tools authored by Anthropic.

 

 So let's now spend some time to reflect on how they work and use that

 knowledge

 to better understand what agents are all about.

 First, I want to review Claude code.

 I went back to our small project and gave Claude an additional task.

 I asked it to write out some tasks for a particular corner case.

 Claude then used a series of tools to fulfill the request.

 And I've shown the entire log for this operation on the screen.

 Now, out of all these different tool calls, two were used to read

 existing

 files inside the project, one was used to write to a file, and one

 was used to run a test.

 Now, I'd like to think critically about each of these different tool

 calls

 and what they were meant to achieve.

 In other words, why did Claude decide to use each?

 Well, three out of the four tool calls were really intended to gather

 information

 about the environment.

 By environment here, I really mean the code base that Claude was

 operating on.

 The one remaining call was intended to modify the environment in some

 way.

 We can see a similar pattern with computer use.

 When I asked Claude to test out that mentioner component, Claude

 made a variety of different tool calls.

 Just so you know, the computer use tools automatically return

 screenshots.

 So if Claude attempts to type or move the mouse, it'll immediately

 get

 some visual feedback of the environment.

 So as we examine the tool use of Claude code and computer use, we

 start to

 notice a pattern really quickly.

 Both of them are using tools and these tools are largely focused on

 just

 delivering or getting information into Claude.

 Let's summarize some of this tool use inside of a table and use it to

 better

 understand what agents are all about and what really goes into making

 a

 successful agent.

 So in both Claude code and computer use, we're going to see that they

 share

 a wide variety of different qualities in how they work, how they run

 and how

 they are getting information into Claude.

 Both these make use of tools extensively and they both run tools

 inside of a

 loop until some goal is achieved or until some unrecoverable error

 occurs.

 They both rely upon tool calls as their primary source of information

 about

 the environment, as opposed to relying upon some kind of rag process

 or

 relying upon a developer to write out a super detail prompt or

 relying upon a

 user to write out extensive instructions.

 They're both given a very small, very focused set of tools where each

 tool

 has a very clear purpose.

 Finally, they are both intended to work on high value problems, where

 failure doesn't cost much money.

 In other words, Claude is writing code, which is traditionally a very

 high

 value task.

 It takes a tremendous amount of knowledge and experience to write

 effective code.

 At the same time, if Claude makes a mistake in the code it generates,

 there's not necessarily an immediate, inherent economic or safety

 impact.

 Compare this to Claude, say, building a complex design for a bridge

 where an

 error could have a very large safety impact.

 In summary, when we consider building an agent, there are a few

 concepts we

 need to keep in mind.

 First, an agent is a language model that has access to a set of tools

 and is

 being executed repeatedly until a goal has been achieved.

 Second, context is king.

 Claude doesn't have any knowledge of the outside world at all, and it

 relies entirely upon being given a set of tools to inspect the

 environment.

 Third, we really want to think about using agents only when we have a

 high

 value task, where an error or failure won't have a large economic or

 safety

 impact.

 And finally, the best way to make sure you are building an effective

 agent is

 EVALS, creating some evaluation criteria and evaluating your agent

 against it is

 the only way to ensure that you are making an effective agent.

---

### Final assessment

#### Lesson 82: Final assessment quiz

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/290881](https://anthropic.skilljar.com/claude-in-amazon-bedrock/290881)

---

### Wrap up

#### Lesson 83: Course wrap up

*Source:* [https://anthropic.skilljar.com/claude-in-amazon-bedrock/276827](https://anthropic.skilljar.com/claude-in-amazon-bedrock/276827)

**Video:** 07_course_wrap_up.mp4 | **Duration:** 2m 49s | **Platform:** jwplayer | **Captions:** English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish

**Video Transcript (JW Player):**

Welcome to the final video. We've covered a ton of information in

 this course.

 We really just have two goals in this video. We want to review, recap

 some of the things we

 talked about, and then explore some next steps. So as a recap, we

 covered a lot. We learned about

 Anthropic and some of the research we do. We talked about the family

 of models and various use cases.

 We covered fundamental topics in the world of generative AI. And then

 we covered working with

 the API to actually send requests to the model. And we covered things

 like sending basic text prompts,

 parameters, like max tokens, what stop sequences are, what stop

 reason means, what temperature

 does, what system prompts do. We covered prompt engineering. We

 talked about tool use and computer

 use and some agentic workflow basics. We talked about writing emails.

 Really, really critical. I

 know I've said that a million times, but I'm going to use this video

 to highlight the importance of

 evaluations again. Do not forget them. Do not let customers skip them

 or try and convince you to

 skip them. They are critical. And then we talked about some more

 advanced topics, including rag

 and fine tuning. A lot of information here. So what is there left?

 Where to go next? There are

 some topics that we recommend you look into as next steps. Always

 stay up to date with the latest

 in Anthropic's research. We published quite a bit. And then moving

 beyond that to more specific

 actionable topics, large language model orchestration. Basically,

 workflows involving more than one

 model, different models, maybe just from the Anthropic family,

 orchestrating Haiku alongside

 Sonnet as an example. We hinted at some of this when we talked about

 agents and agentic workflows.

 We can have a slower but smarter model dispatch actions to a whole

 bunch of, you know, a team of

 cheaper Haiku models or something like that. Explore rag alternatives

 and then explore

 agentic workflows. This is still very much an emerging field that is

 changing constantly,

 but we expect this to be the big trend going forward. The thing that

 companies are most interested in

 and that customers are probably also going to be most interested in

 implementing.

 The trouble is that it's still a new field. There's a lot of

 exploration to be done,

 a lot of research that's being done and experimentation that you can

 do yourself

 to decide and understand which of these workflows work. Are there

 novel approaches? I showed a slide

 with seven or eight different possible agentic workflows. There are

 many, many others out there.

 There are libraries and frameworks out there to help you build agent

ic workflows. This is an

 emerging field and again, something we expect to be a big trend going

 forward. So thanks for joining

 us. I hope you learned something. I know it's a lot of content and

 this slide alone is three

 or four separate courses easily worth of content. All right.

---

*Extracted from Anthropic Academy via authenticated session | Deep Extraction v3 | 2026-04-12*
