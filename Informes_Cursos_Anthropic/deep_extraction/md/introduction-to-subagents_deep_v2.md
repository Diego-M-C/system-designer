# Introduction to subagents

> **Source:** [https://anthropic.skilljar.com/introduction-to-subagents](https://anthropic.skilljar.com/introduction-to-subagents)
> **Category:** agent-development | **Difficulty:** intermediate | **Domain:** Agent Development
> **Tags:** subagents, claude-code, delegation, context-management
> **Extracted:** 2026-04-11 | **Version:** v3 (with YouTube transcripts + quiz content)

---

## Extraction Statistics

| Metric | Value |
|--------|------:|
| Total Lessons | 4 |
| Sections | 1 |
| JW Player Transcripts | 0 |
| YouTube Transcripts | 4 |
| Modular Text Lessons | 4 |
| Quiz Assessments | 0 |
| JW Transcript Chars | 0 |
| YouTube Transcript Chars | 12,861 |
| Modular Text Chars | 18,268 |
| **Total Content** | **31,129** |

## Curriculum Structure

- **(uncategorized)** (4 lessons)

---

## Complete Lesson Content

### (uncategorized)

#### Lesson 1: What are subagents?

*Source:* [https://anthropic.skilljar.com/introduction-to-subagents/450698](https://anthropic.skilljar.com/introduction-to-subagents/450698)

**Video:** What are subagents? | **Platform:** youtube

Subagents are specialized assistants that Claude Code can delegate tasks to. Think of them as focused helpers: each one runs in its own conversation context window, does its work, and returns a summary to the main thread. The intermediate steps -- all the file reads, searches, and tool calls -- stay isolated and never clutter your main conversation.
Why Subagents Matter
Every time you chat with Claude Code, you're adding to the main context window. Every tool call, every file read, every search result gets stored there. That space is finite, and once it fills up, Claude starts losing track of earlier parts of the conversation.

Subagents solve this by spinning up a separate context window. The subagent receives two things:

A custom system prompt from your configuration file that defines the subagent's role and behavior
A task description written by the parent agent based on what you asked for

The subagent then works on its own. It reads files, runs searches, edits code -- whatever it needs to do. When it's done, only a summary comes back to your main conversation. The entire subagent conversation is then discarded.
This means your main context stays clean. You get the answer without all the noise of the journey it took to find it. The tradeoff is that you lose visibility into how the subagent reached its conclusions.
A Practical Example
Say you're exploring an unfamiliar codebase and you want to know which service handles refunds. Without a subagent, Claude might read 15 files, run several searches, and trace through multiple function calls. All of that fills your context window, even though you only needed one fact.
With a subagent, the experience is much cleaner. You ask the question, the Explore subagent spins up, does all that digging in its own context, and hands back a focused answer.
Your main context window only records the question and the summary -- not the 15 files that were read along the way.
Built-in Subagents
Claude Code ships with several built-in subagents you can use right away:

General purpose subagent -- for multi-step tasks that require both exploration and action
Explore -- for fast searching and navigation of codebases
Plan -- used during plan mode for research and analysis of your codebase before presenting a plan

Custom Subagents
Beyond the built-in options, you can create your own subagents with custom system prompts and tool access. This lets you define specialized agents tailored to your workflow -- a code reviewer, a test writer, a documentation generator, or anything else you need.
Key Takeaways
Subagents give you three main benefits:

They break work into focused pieces, letting each subagent concentrate on a specific task
They keep your main context window clean by isolating all the intermediate work
They bring back just the information you need as a concise summary

Whether you're using the built-in subagents or creating your own, they're a practical way to get more out of longer Claude Code sessions. The less noise in your main context, the longer and more effectively you can work.

**Video Transcript (YouTube via yt-dlp):**

Sub agents are specialized assistants that cloud code can delegate tasks to each sub agent runs in its own conversation contacts window with a custom system prompt that you define. When finished, it returns a summary to the main thread while all the intermediate work stays isolated. One of the main advantages of sub aents is that they help manage context window usage. When you chat with clot code, you're adding context to the main context window. Every tool call and its results get stored in this main context window. And so when Claude uses a sub agent, a separate window starts. The sub agent receives two inputs, a custom system prompt from your configuration file and a task description written by the parent or parent agent based on what you ask for. The sub agent then works autonomously when it reads files, edits files, or uses tools. None of these will appear in the main conversation. Just a summary is returned back. The entire sub aent conversation then gets completely discarded. Consider a task like investigating how the payment system works in an unfamiliar codebase. Maybe you're trying to use claw code to figure out which service handles refunds. Well, without a sub agent, Cloud might read 15 files, run several searches, and trace through multiple function calls, all of that context fills your context window, even if you only needed one single fact. Which service handles refunds? With a sub agent, you get the answer without the journey. The sub agent explores, discovers the answer, and returns a focus summary, keeping your main context clean. But the main window loses visibility into how the sub agent reaches its conclusions and what it discovered along the way. Cloud code includes several built-in sub aents that you can use immediately like the general purpose sub agent used for multi-step tasks that require both exploration and action. The explore sub aent used for fast searching of code bases. The plan sub agent use during plan mode for research and analysis of your codebase before presenting a plan. And you can also create your own sub aents with custom system prompts and tool access. Sub aents let clock code break work into focused pieces, keep your main context window clean, and bring back just what you need. Whether you're using the built-in ones or creating your own, they're a practical way to get more out of longer clawed code sessions.

---

#### Lesson 2: Creating a subagent

*Source:* [https://anthropic.skilljar.com/introduction-to-subagents/450699](https://anthropic.skilljar.com/introduction-to-subagents/450699)

**Video:** Creating a subagent | **Platform:** youtube

Claude Code comes with built-in subagents, but you can also create your own. Custom subagents specialize in specific tasks -- like reviewing code, writing tests, or checking documentation. They are defined as markdown files with YAML frontmatter that tell Claude when to use the subagent and how the subagent should behave.
Creating a Subagent
The easiest way to create a subagent is with the /agents slash command. This opens the main interface for managing your subagents. From there, select Create new agent.
You will first be asked to choose the scope of your subagent:

Project-level -- available only in the current project
User-level -- shared across all projects on your machine

Next, you can choose how to create it. You can write the configuration manually, but the recommended approach is to let Claude generate it for you. Just describe what you want the subagent to do, and Claude will produce a name, description, and system prompt based on your input.

Customizing Tools
During creation, you get the chance to customize which tools the subagent can access. The tool categories include:

Read-only tools
Edit tools
Execution tools
MCP tools
Other tools

Think about what your subagent actually needs. A code reviewer probably does not need edit tools -- it should read and analyze code, not change it. However, you might want to keep execution tools enabled so it can more easily identify pending changes.
Choosing a Model and Color
After configuring tools, you select which Claude model powers the subagent. Your options are:

Haiku -- best for fast, lightweight tasks
Sonnet -- a good middle ground between speed and depth
Opus -- best for complex analysis
Inherit -- uses whatever model your main conversation is running

Finally, you pick a color. This shows up in the UI so you can quickly tell which subagent is active. It is a small touch, but it helps when you have multiple subagents running.

The Config File
Once creation is complete, the subagent config file is saved into your project (typically at .claude/agents/your-agent-name.md). Here is what a typical subagent config looks like:

---
name: code-quality-reviewer
description: Use this agent when you need to review recently written or modified code for quality, security, and best practice compliance.
tools: Bash, Glob, Grep, Read, WebFetch, WebSearch
model: sonnet
color: purple
---

You are an expert code reviewer specializing in quality assurance, security best practices, and
adherence to project standards. Your role is to thoroughly examine recently written or modified code
and identify issues that could impact reliability, security, maintainability, or performance.
Let's break down each field:

name -- A unique identifier for the subagent. This is how you reference it, either by asking Claude directly or by typing @agent code-quality-reviewer in your message.
description -- Controls when Claude decides to use the subagent. This must be a single line (use escaped newline characters \n if you need breaks). You can include example conversations here to help Claude understand when delegation is appropriate.
tools -- Lists which tools the subagent can access. This matches whatever you selected during generation, but you can edit the list here at any time.
model -- Specifies which Claude model to use: sonnet, opus, haiku, or inherit.
color -- The UI color for identifying the subagent.

System Prompts
The body of the markdown file (everything below the YAML frontmatter) is the system prompt. This is where you give the subagent its instructions: what it should focus on, how it should analyze things, and how it should report findings back to the main agent.
A well-written system prompt is the difference between a useful subagent and one that misses the point. Be specific about what the subagent should look for and how it should structure its output.
Making Claude Use Your Subagent Automatically
If you want Claude to delegate tasks to the subagent without you explicitly asking, include the word "proactively" in the description field. For example:
description: Proactively suggest running this agent after major code changes...
You can also add example conversations to the description to help Claude understand specific scenarios where the subagent should be used. The more concrete your examples, the better Claude gets at knowing when to delegate.
Testing Your Subagent
After creating your subagent, test it by making some code changes and asking Claude to review them.

If the subagent is not being used when you expect it to be, go back and check the description. Adding more specific examples and trigger scenarios helps Claude understand when to delegate work to your subagent.

**Video Transcript (YouTube via yt-dlp):**

In the previous video, we covered what sub aents are and how they work. Cloud code includes built-in sub aents, but you can also create your own sub aents that specialize in certain tasks. Custom sub aents are markdown files with YAML front matter. These markdown files contain configuration that helps claude understand when to use the sub aent and provides directions to the sub aent itself. Now, the easiest way to create a sub agent is with the / agents command. This panel is the main interface for managing your sub aents. Once here, select create new agent. You'll then be asked if you want to create a sub aent for the current project or a sub aent that will be shared between all the projects on your machine. Next, you can create a sub aent manually, but we recommend using claw code to automatically generate it for you. Our first sub aent will be a code reviewer. I'll ask Claude to make a sub agent that reviews code quality and security issues. Claude will use your input to generate a name, description, and system prompt for the sub agent. We'll see those in a moment, but before we do, we get the opportunity to customize the tools that this sub agent has access to. Now, given that our sub agent is only responsible for reviewing code, you might decide to disallow tools for editing, but I'll leave an execution to allow the sub agent to more easily identify pending changes. Next, you'll be prompted to select the model that powers this sub agent. And finally, a color. This color is used in the UI to help you better identify the sub agent. And it also just adds a little bit of personal flare. Now at the summary window, we see that the sub aent config file will be saved into my current project at this path. Now let's open up that file to get a better idea of what's going on. The name field is a unique identifier. This is how you reference the sub agent either by asking claw directly or using at agent code quality reviewer in your message. The description controls when cla decides to use the sub aent. The description must be on a single line. Notice that there are escaped new line characters in there. If you want Claude to use the sub agent automatically more often, add in the word proactively to the description. You can also add example conversations to help Claude understand when it should be using the sub agent. The tools field lists which tools the sub agent can access. The list of tools will match the tools we granted access to during the agent generation, but you can further edit the list of tools in this file if you want. The model field specifies which claw model to use. Sonnet, opus, haiku or inherit. Use haiku for fast tasks. Opus for complex analysis and sonnet if you need something between the two. Inherit will use the same model as your main conversation. The body of the file contains the system prompt that is given to the sub aent. The system prompt will provide guidance to the sub agent, helping it understand how to complete its task and how it should return information back to the main agent. Now for the fun part. After creating your sub agent, test it by making some code changes and asking claw to review them. If the sub agent isn't being used when you expect, check your description. Adding more specific examples helps Claude understand when to delegate.

**Code Examples:**

```
/agents
```

```
.claude/agents/your-agent-name.md
```

```
---
name: code-quality-reviewer
description: Use this agent when you need to review recently written or modified code for quality, security, and best practice compliance.
tools: Bash, Glob, Grep, Read, WebFetch, WebSearch
model: sonnet
color: purple
---

You are an expert code reviewer specializing in quality assurance, security best practices, and
adherence to project standards. Your role is to thoroughly examine recently written or modified code
and identify issues that could impact reliability, security, maintainability, or performance.
```

```
---
name: code-quality-reviewer
description: Use this agent when you need to review recently written or modified code for quality, security, and best practice compliance.
tools: Bash, Glob, Grep, Read, WebFetch, WebSearch
model: sonnet
color: purple
---

You are an expert code reviewer specializing in quality assurance, security best practices, and
adherence to project standards. Your role is to thoroughly examine recently written or modified code
and identify issues that could impact reliability, security, maintainability, or performance.
```

```
name
```

```
@agent code-quality-reviewer
```

```
description
```

```
\n
```

```
tools
```

```
model
```

```
sonnet
```

```
opus
```

```
haiku
```

```
inherit
```

```
color
```

```
description: Proactively suggest running this agent after major code changes...
```

```
description: Proactively suggest running this agent after major code changes...
```

---

#### Lesson 3: Designing effective subagents

*Source:* [https://anthropic.skilljar.com/introduction-to-subagents/450700](https://anthropic.skilljar.com/introduction-to-subagents/450700)

**Video:** Designing effective subagents | **Platform:** youtube

Now that you know how to create subagents, let's look at the patterns that make them actually effective. A subagent that's poorly configured will wander, run too long, or produce output the main agent can't use. The fixes come down to four things: writing good descriptions, defining an output format, reporting obstacles, and limiting tool access.
How Subagent Config Data Gets Used
When you send a message to the main context window agent, the name and description of every available subagent are included in the system prompt. This is how the main agent decides which subagent to launch and when. If you want better control over when a subagent gets triggered automatically, the name and description are what you should tweak.
The description also plays a second role. When the main agent launches a subagent, it writes an input prompt to kick off the task. It uses the description as guidance for writing that prompt. So the description doesn't just control when a subagent runs -- it shapes what the subagent is told to do.

Writing Descriptions That Shape Input Prompts
Consider a code review subagent. With a generic description, the main agent might write an input prompt like "use get diff to find the current changes." That's vague. The subagent has to figure out which files matter on its own.
If you update the description to include something like "You must tell the agent precisely which files you want it to review," the main agent will now write a much more specific input prompt that lists the actual files to review.
This same technique works across different types of subagents. For example, adding "return sources that can be cited" to a web search subagent's description causes the main agent to include that instruction when delegating the task.

Defining an Output Format
The single most important improvement you can make to a subagent is defining an output format in its system prompt. This does two things:

It creates natural stopping points -- the subagent knows it's done when it has filled in each section of the format.
It prevents the subagent from running too long. Without a defined output, subagents struggle to decide when enough research has been done and tend to run much longer than necessary.

Here's an example of a structured output format for a code review subagent:
Provide your review in a structured format:

1. Summary: Brief overview of what you reviewed and overall assessment
2. Critical Issues: Any security vulnerabilities, data integrity risks,
 or logic errors that must be fixed immediately
3. Major Issues: Quality problems, architecture misalignment, or
 significant performance concerns
4. Minor Issues: Style inconsistencies, documentation gaps, or
 minor optimizations
5. Recommendations: Suggestions for improvement, refactoring
 opportunities, or best practices to apply
6. Approval Status: Clear statement of whether the code is ready
 to merge/deploy or requires changes
This format gives the subagent a clear checklist to work through. Once every section is filled in, the subagent knows it can stop.
Reporting Obstacles
When a subagent discovers a workaround during its work -- like solving a dependency issue or finding that a certain command needs particular flags -- those details need to appear in the summary it returns. If they don't, the main thread has to rediscover the same solutions on its own, which wastes time and tokens.
The kinds of things you want surfaced include:

Setup issues or environment quirks
Workarounds discovered during the task
Commands that needed special flags or configuration
Dependencies or imports that caused problems

The way to get this information is to explicitly ask for it in the output format. Adding an "Obstacles Encountered" section to your output template surfaces this information reliably.
7. Obstacles Encountered: Report any obstacles encountered during the
 review process. This can be: setup issues, workarounds discovered or
 environment quirks. Report commands that needed a special flag or
 configuration. Report dependencies or imports that caused problems.

Limiting Tool Access
Not every subagent needs access to every tool. Think about what a subagent actually needs to do, and only give it the tools required for that job. This does two things: it prevents unintended side effects, and it makes each subagent's role clearer when you have several of them.
Here's how to think about tool access for common subagent types:

Research / read-only subagent -- Only needs Glob, Grep, and Read. Cannot accidentally modify files.
Code reviewer -- Needs Bash access to run git diff and see what changed, but still doesn't need Edit or Write.
Styling / code modification agent -- This is where you give Edit and Write access, because the subagent's job is to actually change your code.

Putting It All Together
Effective subagents share four characteristics:

Specific descriptions -- The description controls when the subagent is launched and what instructions it receives. Write it to steer both.
Structured output -- Define an output format in the system prompt so the subagent knows when it's done and returns information the main thread can use.
Obstacle reporting -- Include a section in the output format for workarounds, quirks, and problems so the main thread doesn't have to rediscover them.
Limited tool access -- Only give a subagent the tools it actually needs. Read-only for research, bash for reviewers, edit/write only for agents that should change code.

Each of these patterns is simple on its own, but together they turn a subagent from something that vaguely tries to help into a focused, predictable worker that finishes on time and reports back clearly.

**Video Transcript (YouTube via yt-dlp):**

Now that you know how to create sub aents, let's look at patterns that lead to effective sub aents. First, let's get a better idea of how subit data in the sub aent config file is used. Whenever you send a message to the main context window agent, the name and description of each sub aent is included in the system prompt. So, if you want to better control when the main agent launches a sub agent automatically, you should modify the name and description. Next, remember that when a sub agent is launched, the main agent writes an input prompt. When writing this input prompt, it uses the description as guidance. So, if you want to better control when the main agent launches a sub agent automatically, you should modify the name and description. Let's consider our review sub aent again. Right now, when the main agent runs this sub agent, the sub aent is given an input prompt telling it to use get diff to find the current changes. If we wanted the main agent to more reliably tell the sub agent exactly which files to review, we would update the description. You must tell the agent precisely which files you want it to review. Now, if we ask claw to run the code reviewer agent, we'll see a different input. You can also influence what the main thread tells a sub agent through the description. So adding return sources that can be cited to a web search sub aents description causes the main thread to include that instruction when delegating the task. The most important improvement that you can make is defining an output format in the system prompt. This creates natural stopping points for the sub aent. Without a defined output format, sub aents struggle to decide when enough research has been done and they tend to run much much longer than sub agents that are given an output format. When a sub agent discovers a workaround to some issue like solving a dependency issue or finding that a certain command needs particular flags, these details should appear in the summary. Otherwise, the main thread has to rediscover the same solutions, obstacles encountered, any setup issues, workarounds discovered or environment quirks, commands that needed special flags or configuration, dependencies or imports that cause problems. Explicitly asking for obstacle reporting in the output format surfaces this information. A readonly sub aent using just glob grap read cannot accidentally modify files. This constraint clarifies that the sub aents role and prevents unintended side effects. So think about what sub aents actually needs to do. If it's just researching it only needs to read files. So keep it read only. That way it can't accidentally modify anything while exploring. A reviewer needs to run get diff to see what changed. So give it bash access, but it still doesn't need to edit files. Only give edit and write to sub aents that should actually change your code, like a styling agent applying CSS updates. This also helps clarify what each sub aent is for when you have several of them. So effective sub aents use structured output report obstacles have specific descriptions and limit tool access.

**Code Examples:**

```
Provide your review in a structured format:

1. Summary: Brief overview of what you reviewed and overall assessment
2. Critical Issues: Any security vulnerabilities, data integrity risks,
   or logic errors that must be fixed immediately
3. Major Issues: Quality problems, architecture misalignment, or
   significant performance concerns
4. Minor Issues: Style inconsistencies, documentation gaps, or
   minor optimizations
5. Recommendations: Suggestions for improvement, refactoring
   opportunities, or best practices to apply
6. Approval Status: Clear statement of whether the code is ready
   to merge/deploy or requires changes
```

```
Provide your review in a structured format:

1. Summary: Brief overview of what you reviewed and overall assessment
2. Critical Issues: Any security vulnerabilities, data integrity risks,
   or logic errors that must be fixed immediately
3. Major Issues: Quality problems, architecture misalignment, or
   significant performance concerns
4. Minor Issues: Style inconsistencies, documentation gaps, or
   minor optimizations
5. Recommendations: Suggestions for improvement, refactoring
   opportunities, or best practices to apply
6. Approval Status: Clear statement of whether the code is ready
   to merge/deploy or requires changes
```

```
7. Obstacles Encountered: Report any obstacles encountered during the
   review process. This can be: setup issues, workarounds discovered or
   environment quirks. Report commands that needed a special flag or
   configuration. Report dependencies or imports that caused problems.
```

```
7. Obstacles Encountered: Report any obstacles encountered during the
   review process. This can be: setup issues, workarounds discovered or
   environment quirks. Report commands that needed a special flag or
   configuration. Report dependencies or imports that caused problems.
```

```
Glob
```

```
Grep
```

```
Read
```

```
Bash
```

```
git diff
```

```
Edit
```

```
Write
```

```
Edit
```

```
Write
```

---

#### Lesson 4: Using subagents effectively

*Source:* [https://anthropic.skilljar.com/introduction-to-subagents/450701](https://anthropic.skilljar.com/introduction-to-subagents/450701)

**Video:** Using subagents effectively | **Platform:** youtube

You know how to create subagents and design them well. Now the question is: when do they actually help, and when do they get in the way? The difference comes down to one thing -- whether the intermediate work matters to your main thread.
When subagents shine
Subagents work best when the exploration is separate from the execution. If each step in a task depends on what the previous step discovered, you want that work in your main thread. But if you just need an answer and don't care about the journey, delegate it.
Subagents excel at tasks where:

You need a result, not a play-by-play of how it was found
The exploratory work would clutter your main thread's context
The task benefits from a fresh perspective or a custom system prompt

Research tasks
Research is the classic subagent use case. Consider investigating how authentication works in an unfamiliar codebase. Your main thread needs to know where the JWT is validated, but it doesn't need to see every file that was searched along the way.
A research subagent can read dozens of files, trace through function calls, and explore different code paths. All that exploration stays in the subagent's context. Your main thread receives a clean summary like:
JWT validation happens in middleware/auth.js line 42,
called from the Express router in route/api.js
The subagent did the heavy lifting. Your main thread gets exactly what it needs to move forward.
Code Reviews
Claude reviews code more effectively when the code is presented as being authored by someone else. If you built a feature over many turns with your main thread, asking that same thread to review it often produces weak feedback. Claude was involved in creating it, so it has trouble seeing it with fresh eyes.
A reviewer subagent sees the changes in a separate context. It runs git diff, reads the modified files, and applies its specialized review criteria without the history of how the code was written. This separation also lets you encode project-specific review standards in the subagent's system prompt, ensuring consistent review criteria across the team.
Custom System Prompts
Claude Code's default system prompt emphasizes concise, code-focused responses. That works great for coding, but not for everything.
Here are two cases where a custom system prompt makes the subagent genuinely better than the main thread:

Copywriting subagent -- Give it instructions about tone, audience, and style. Claude Code's default prompt tends toward concise technical writing, which really isn't what you want for a landing page or email campaign. A copywriting subagent can have completely different instructions about voice and structure.
Styling subagent -- Point it at your design system files. When the subagent runs, those files load into its context automatically, so it knows your color variables, spacing conventions, and component patterns before it even starts writing any CSS.

When Subagents Hurt
The overhead of launching a subagent -- losing visibility into its work and compressing its findings into a summary -- only makes sense when the subagent does something the main thread can't. There are three common anti-patterns to watch out for.
Expert Claims
Subagents that claim expertise rarely help. Prompts like "you are a Python expert" or "you are a Kubernetes specialist" add no value because Claude already has that knowledge. There's nothing a so-called expert subagent can do that your main thread can't do directly.
Sequential Pipelines
Sequential subagent pipelines create problems. Consider a three-agent flow: one to reproduce a bug, one to debug it, and one to fix it. Pipelines work when tasks are truly independent. They fail when each step depends on discoveries from the previous step -- and bug fixing almost always does. Information gets lost in the handoff between agents.
Test Runners
Test runner subagents tend to hide information you need. When tests fail, you want the full output to diagnose issues. A subagent that returns "tests failed" forces you to create additional debug scripts to get details that would have been visible in direct output. Testing has shown that the test runner pattern performed worse among all configurations.
The Decision Rule
When you're deciding whether to use a subagent, ask yourself one question: does the intermediate work matter?
If the answer is no -- you just need the final result -- delegate it to a subagent. If the answer is yes -- you need to see and react to what's happening along the way -- keep it in your main thread.
Use subagents for:

Research and exploration
Code reviews
Tasks that need a custom system prompt

Avoid subagents for:

"Expert" personas that don't add real capability
Multi-step pipelines where each step depends on the last
Running tests where you need full output for debugging

**Video Transcript (YouTube via yt-dlp):**

you know how to create sub agents and design them. Well, now let's cover when they actually help and when they get in the way. Simply put, the difference comes down to whether the intermediate work matters to your main thread. When exploration is separate from execution, sub agents shine. When each step depends on what the previous step discovered, well, information gets lost in the handoff process. Sub agents excel at research tasks where you just need an answer, not the journey. Consider investigating how authentication works in an unfamiliar codebase. Well, the main thread might need to know where is the JWT validated, but doesn't need to see every file that was searched. A research sub agent can read dozens of files, trace through function calls, and explore different code paths. All that exploration stays in the sub agents context. Your main thread receives JWT validation happens in middleware/offJS at line 42 called from the express router and route/ API.js or something like that. Cloud reviews work more effectively when the code is presented as being authored by someone else. If you build a feature over many turns with your main thread, asking the main thread to then review it often doesn't give the best feedback. Claude was involved in creating it, so it has trouble seeing it with fresh eyes. A reviewer sub agent sees the changes in a separate context. It runs git diff, reads the modified files, and applies it specialized review criteria without the history of how the code was written. And this separation also lets you encode project specific review standards in the sub aent system prompt ensuring consistent review criteria across the team. Cloud code's default system prompt emphasizes concise code focused response and this works great for coding but not for everything. So one is a copywriting sub aent with instructions about tone, audience and style. This will produce better marketing text than the main thread would. Claude Code's default prompt tends towards concise technical writing, which really isn't what you want for a landing page or email campaign, unless you want to put your customers to sleep. A copywriting sub agent can have completely different instructions about voice and structure. A styling sub agent that app mentions your design system files will apply consistent CSS patterns. When the sub aent runs, those files load into the context automatically. So, it knows your color variables, spacing conventions, and component patterns before it even starts writing any CSS. Sub aents that claim expertise rarely help. Prompts like you are a Python expert or you are a Kubernetes specialist add no value because Claude already has that knowledge. The overhead of launching a sub agent, losing visibility into its work, and compressing its findings into a summary only makes sense when the sub agent does something that the main thread can't, like applying a custom system prompt or keeping exploratory work isolated. Sequential sub agent pipelines create problems. Consider a three agent flow. One to reproduce a bug, one to debug it, and one to fix it. Pipelines work when tasks are truly independent. They fail when each step depends on discoveries from the previous step. Testr runner sub aents tend to hide information you need. When tests fail, you want the full output to diagnose issues. A sub aent that returns a test failed forces you to create additional debug scripts to get details that would have been visible in direct output. testing has showed that the testr runner pattern performed worse among all configurations. Across the series, we covered how sub aents work as isolated threads that return summaries, how to create them with the / aents command, and how to design them with structured outputs and specific descriptions. Use them for research, reviews, and tasks needing custom system prompts, but avoid them for expert claims, multi-step pipelines, and test runners. The key question, does the intermediate work matter? If not, then delegate it.

**Code Examples:**

```
JWT validation happens in middleware/auth.js line 42,
called from the Express router in route/api.js
```

```
JWT validation happens in middleware/auth.js line 42,
called from the Express router in route/api.js
```

```
git diff
```

---

*Extracted from Anthropic Academy via authenticated session | Deep Extraction v3 | 2026-04-12*
