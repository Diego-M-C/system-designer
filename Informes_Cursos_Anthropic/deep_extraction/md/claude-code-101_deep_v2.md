# Claude Code 101

> **Source:** [https://anthropic.skilljar.com/claude-code-101](https://anthropic.skilljar.com/claude-code-101)
> **Category:** developer-tools | **Difficulty:** beginner-intermediate | **Domain:** Developer Tools
> **Tags:** claude-code, agentic-loop, explore-plan-code-commit
> **Extracted:** 2026-04-11 | **Version:** v3 (with YouTube transcripts + quiz content)

---

## Extraction Statistics

| Metric | Value |
|--------|------:|
| Total Lessons | 13 |
| Sections | 5 |
| JW Player Transcripts | 0 |
| YouTube Transcripts | 10 |
| Modular Text Lessons | 0 |
| Quiz Assessments | 1 |
| JW Transcript Chars | 0 |
| YouTube Transcript Chars | 26,483 |
| Modular Text Chars | 0 |
| **Total Content** | **26,483** |

## Curriculum Structure

- **What is Claude Code?** (2 lessons)
- **Your first prompt** (2 lessons)
- **Daily workflows** (3 lessons)
- **Customizing Claude Code** (5 lessons)
- **Quiz** (1 lessons)

---

## Complete Lesson Content

### What is Claude Code?

#### Lesson 1: What is Claude Code?

*Source:* [https://anthropic.skilljar.com/claude-code-101/469788](https://anthropic.skilljar.com/claude-code-101/469788)

**Video:** What is Claude Code? | **Platform:** youtube

**Video Transcript (YouTube via yt-dlp):**

Cloud Code is an agentic coding tool that understands your codebase, edits your files, run commands, and integrates with your existing developer tools to help you get things done faster. It's available in your terminal, Visual Studio Code, the Claw desktop app, on the web, and Jetrains IDEs. but we'll be using it in the terminal for this video. If you've ever used Cloud AI, you're probably wondering what the difference is between the two. Unlike Cloud AI, Cloud Code has direct access to your files, your terminal, and your entire codebase. So, instead of copying and pasting code back and forth, it can go in and do all the work itself. The easiest differentiator is that Cloud Code works as an AI agent. An AI agent is a software that can interact with this environment and perform actions to complete a defined goal. The most basic way this can be done is by having a large language model in a loop in real time. AI agents have access to things like tools, external services, or other AI agents to help it reach its predefined goals. So, what does that actually look like? Well, here's a couple of examples. It can read and understand your codebase. You can ask Cloud Code to explain a feature or trace a bug throughout your code. Cloud Code can execute your build script, run your tests, install packages, and use the output to decide what to do next. Cloud Code can search the web. If it needs documentation on the latest API references, for example, it can do that for you. To use Cloud Code effectively, it's important to know these concepts. First is the context window. Think of this as Claude's working memory. It can hold a lot, but not everything at once. This is where the agentic aspect of it comes in. Finding strategic ways to find the answers within your codebase without storing your entire codebase into context. Second is that it asks for permission. By default, cloud code will ask you before running commands or making changes to your codebase. You're always in control, whether that's being more hands-on or passive. Third, it can make mistakes. Just like any tool, cloud code isn't perfect. It might misunderstand your intent, introduce a new bug, or overengineer a solution. Quick recap. Clot code is an agentic coding tool. It reads your codebase, edits your files, runs commands, and connects to external tools to help you ship faster. You can download it today in your terminal, VS Code, Jet Brains, and the Claw desktop app.

---

#### Lesson 2: How Claude Code works

*Source:* [https://anthropic.skilljar.com/claude-code-101/469789](https://anthropic.skilljar.com/claude-code-101/469789)

**Video:** How Claude Code Works | **Platform:** youtube

**Video Transcript (YouTube via yt-dlp):**

We know that cloud code is different from usual child applications. But how does it work? Cloud code is best explained through the agentic loop. You enter a prompt into cloud code. Cloud code will then gather context required to complete your prompt. It does so by interacting with the model which will return text or a tool call that cloud code can execute. Then it takes action. For example, editing a file or running a command. Finally, it verifies those results and determines if they achieve what your prompt set out to do in the first place. If they do, then Claude finishes and waits for the next prompt. And if they don't, Claude goes back and runs the loop again until the results are complete and verifiable. Throughout this loop, you're able to add context, interrupt it, or steer the model to help guide it towards your end goal. Claude has a context window which determines how much of your conversation, file content, command outputs, and more it can store and look back on. Once you reach that limit, cloud code compacts your conversation, which automatically determines what it can take out of the context window and what it can summarize in order to bring the context window back down. Tools are the backbone of how agents work. Currently, most AI assistants are simply input text and output text. Nothing in between. Tools let Claude Code and other agents determine when to execute code to get closer to a task. This could be read file tool or search web tool for example. Cloud code uses semantic searching to determine when to call a tool and get the output of it. Cloud code also has permission modes. Default behavior is that it has to ask explicit permission before editing a file or running a shell command. You can use shift and tab to toggle between different modes. Auto accept edits files without asking but still ask for commands. Plan mode uses readonly tools to help compile a plan of action before starting. It's worth being cautious when skipping permissions. Giving Claude code free reign to run commands means a mistake could be harder to catch before it even happens. Claw code works by combining different agentic concepts. an agentic loop, a manage context window, tools, and configurable permissions into your terminal. It can read your codebase, take action, and verify its own work. And that makes it fundamentally different from a chat window.

---

### Your first prompt

#### Lesson 3: Installing Claude Code

*Source:* [https://anthropic.skilljar.com/claude-code-101/469790](https://anthropic.skilljar.com/claude-code-101/469790)

**Video:** Installing Claude Code | **Platform:** youtube

**Video Transcript (YouTube via yt-dlp):**

Cloud Code is simple to install whether you want to use it in your terminal, the web, or your IDE. If you're on Mac OS, Linux, or WSL, use this curl command to install it in one go. If you prefer to use Homebrew, you can also use brew install to install it. But note that this doesn't have auto update capabilities. For Windows, there's also a couple ways. In PowerShell, use the invoke rest method command. If you're on cmd, you can also use this curl command. We also have a winget command as well if you'd prefer, but just like homebrew, it won't auto update. Now go to your project directory and run claude. You will go through some initial instructions like choosing your color theme and signing in with your claude account, which could be the pro, max, or enterprise. Or you can use an API key. If your organization has a cloud enterprise account, be sure to select that option. Whatever directory you decide to run cloud in, it will have access to that directory in all of its subfolders. In Visual Studio Code, open up your extensions panel and search for cloud code. You will see the extension by anthropic. Make sure it has the blue check and hit install. After installation, you might need to restart VS Code. After that, you can open up the control palette with control or command and shift and P and search Claude Code. Open a new tab. You can also click on the Claw logo if you see it when a file is open. You can also opt out of the UI and just use the terminal experience directly in your settings file. For Jet Brains IDEs, you can install the Cloud Code plugin from the Jetrains marketplace. Once you install, restart your IDE. And when you reopen, you'll see the Cloud logo. This will open up a pane where you can see the terminal experience. And this will work alongside you. On Cloud Desktop, you can also run Cloud Code. After you installed Claude desktop and signed in, you will see a toggle at the top that says code. The look and feel is similar to Cloud Chat side of things, but allows you to work in a specific folder, change permissions, and even work in a cloud environment. On the web, you can access Cloud Code by going to cloud.ai/code. This works very similar to the desktop app. However, you're restricted to GitHub repositories only. If you want to constantly keep up to date with everything, the terminal is the best bet. Features ship there the fastest. For the most part, you'll have extremely similar experiences with the IDE integrations if you like cloud code to feel more intertwined with your favorite code editor. Desktop is great for letting Claude run in the background while you run other tasks. Cloud Code on the web is a great option if you want to remotely work on a project through a GitHub repository or have multiple sessions work in parallel. However you want to use cloud code, it's up to you.

---

#### Lesson 4: Your first prompt

*Source:* [https://anthropic.skilljar.com/claude-code-101/469791](https://anthropic.skilljar.com/claude-code-101/469791)

**Video:** Your first Claude Code prompt | **Platform:** youtube

**Video Transcript (YouTube via yt-dlp):**

You talk to clot code like you would talk to any AI assistant. When entering your prompt, here are some things that you can consider that can both protect and make things easier for you. You can choose whether Claude auto accepts every file change it suggests or require it to ask you for explicit permission each time. With shift plus tab, you can cycle between both modes. In auto accept mode, it will automatically approve an edit or creation of a file, but still ask your permission to run commands. There isn't a right or wrong way. It's just whatever you feel the most comfortable with. Within this shift tab menu is the plan mode. Plan mode takes your prompt and uses readonly tools to analyze your codebase and do research on your suggested implementation. It will also ask you questions on items that it wants clarification on. It then returns to you a long detailed plan that it can execute on in more detail. Plan mode works great for planning complex changes or doing a safe code review. A lot of the time you're asking claw to do multi-step implementations towards a feature and this is exactly what plan mode excels at. So why don't we give it a try? I have an application here that desperately needs a uh dark dark mode toggle. So I'm going to use cloud code to implement this for me. So I'm in the root directory of my project. I'm going to hit the shift tab a couple times to go into plan mode. Then let's write out the prompt. My app needs a dark mode implemented across the entire app. Can you create a toggle switch on the header that allows user to toggle between light mode and dark mode? I need you to find a good contrast color that works based on my existing light theme. And let's let Claude plan this out. And after reviewing, I think it looks pretty good. At the end of all this, we can see explicitly what Claude did and how it came to its conclusion. And the dark mode is looking pretty good. Awesome. When using Cloud Code, try to be as descriptive as possible with your prompt. If you want to stay in the loop at every step, you can do that. Use plan mode to let Claude get a little bit more in the nitty-gritty with what you want to achieve before executing on that plan.

---

### Daily workflows

#### Lesson 5: The explore → plan → code → commit workflow

*Source:* [https://anthropic.skilljar.com/claude-code-101/469792](https://anthropic.skilljar.com/claude-code-101/469792)

**Video:** The Explore → Plan → Code → Commit workflow in Claude Code | **Platform:** youtube

**Video Transcript (YouTube via yt-dlp):**

If you take one thing away from cloud code, let it be this workflow. Explore, plan, code, and commit. Without this, most people jump straight to asking Claude to write code, which means more course correcting later on. The fastest way to handle step one and two is with plan mode. With plan mode, Claude can't edit files. It just reads files to gather research on how to tackle its implementation. To enter plan mode, hit shift and tab until you see the plan mode under the text input. I need to add webp conversion to our image upload pipeline. Figure out where the pipeline should happen, whether we need new dependencies and how to approach it and claude will read relevant files, do some web searches, and give you a plan of action. Make sure you review it and determine if it meets your criteria. Otherwise, I can ask it to add on or revise some areas. Perfect. And this right here is the best place to course correct because it's before any code is written. You can also use explore without being in plan mode by just asking Claude to explore your codebase. Now, once the plan looks good, you can select approve to accept the plan and let Claude tackle all the list items it provided. You can determine if you want Claude to auto accept the file edits or ask every single time. Cloud will do its best to troubleshoot your codebase before considering the plan finished, but at times you'll need to course correct. This is the benefit of working with plan mode because after the plan is finished, we also have the context of how it got to the results to help it guide its next decision. In order for Claw to be confident in its results, it has to be clear on what it deems correct. When writing your plan, make this explicit. Adding tools that will help Claude complete its goals will remove a lot of back and forth. For example, if you're building web UIs, make sure you have the Claude and Chrome extension so that Claude code can control a tab and test out the UI before deeming it finished. In your project, include a test suite that Claude can continuously validate on. Claude can even write tests for you. Before passing this off to Claude, make sure that the tests are a source of truth for you and your team to avoid any false positives. Quick tip. If you find Claude keeps running into these same issues, ask Claude to save the solution to his Claude MD file. Now, once you have tested for yourself and are happy with the results, it's time to push your code. A tip before you commit, run a sub agent code reviewer to look at your code. Then you get Claude to generate a commit message for you in your style. Rinse and repeat. If you want to be effective with Cloud Code, follow the explore, plan, code, and commit workflow. Exploration will give the relevant context Claude needs for your project. Plan will create a plan of action that Claude will use to determine if they are successful. Code is the back and forth that you and Claude do before settling on the final outcomes of the plan. Commit helps you review and push your code so you can start on your next feature.

---

#### Lesson 6: Context management

*Source:* [https://anthropic.skilljar.com/claude-code-101/469793](https://anthropic.skilljar.com/claude-code-101/469793)

**Video:** Context Management in Claude Code | **Platform:** youtube

**Video Transcript (YouTube via yt-dlp):**

Context is Claw's working memory. Every file it reads, every command it runs, every message you send, it all takes up space in the context window. Think of the context window as the amount of space that Claude could hold in his memory. Whenever you enter a prompt, Claude reads a file, runs a tool call, gets a tool call result. This is added on to the context window. And since there's only a finite amount you can put in the context window, it becomes extremely important to optimize this as much as possible. Now, when you approach this limit, the context window is automatically compacted. Compaction will summarize important details and remove the unnecessary tool call results and free up a lot of space in your context window. Do note though that this could potentially lose details in your previous conversation. You can run the compaction manually as well with the /compact command. This will compact everything that you've done up to that point, which could be handy if you want to clear up context space, but also have a memory of what you previously worked on. If you want to completely start from scratch without memory of what was previously worked on, you can also run /cle and that will remove everything starting from scratch. To check the state of your context, run the /context command. Here you'll get a big picture of how large your context size is, the different categories that are taking up the most context, and a graphic showing you all of this. A general rule of thumb is when you're working on a specific feature and are going over the context window, but need to continue, then compact. Keeping the context relevant for this feature is important when continuing development. If you have finished the plan and want to start on a new feature, then clear. You don't want the previous conversation to present bias in anything new that you want to create. For things that you do want Claude to remember in other sessions, put it in the claw.md file. That way, it doesn't have to rediscover things from scratch all over again. Be specific. The irony behind writing a smaller prompt is that it in the long run, it will take up more context. Without being explicit, Claude is forced to look around your codebase more and do its own thinking, which takes up a lot more context. window space than if you were just a little bit more clear with a sentence or two. MCP servers load all of the tools available into context by default. So, if you have a lot of MCP servers for things that are unrelated to the project, it might be worth turning them off. You can also try out skills, which works similarly to MCP servers, but doesn't put the entire thing into context, saving you space. Sub agents run in parallel with your main agent but has a complete separate context window. So for tasks that require an answer without the journey like where is the authentication endpoints located, you can have the sub agent do the work and return just a summary to your main agent. Managing context within cloud code is crucial. Use slash compact to summarize long sessions and slashclear to start fresh. To use your context window effectively, be specific with what you want. Check what's using your current context window and use sub agents to delegate tasks you only need the answer for.

---

#### Lesson 7: Code review

*Source:* [https://anthropic.skilljar.com/claude-code-101/469794](https://anthropic.skilljar.com/claude-code-101/469794)

**Video:** Introducing Code Review | **Platform:** youtube

---

### Customizing Claude Code

#### Lesson 8: The CLAUDE.md file

*Source:* [https://anthropic.skilljar.com/claude-code-101/469795](https://anthropic.skilljar.com/claude-code-101/469795)

**Video:** The CLAUDE.md file | **Platform:** youtube

**Video Transcript (YouTube via yt-dlp):**

One of the most useful parts of claw code is the claw.md file. It gives cloud code persistent memory about your project. When you open up cloud code without a cloud.md file, it's like it has to start fresh every single time. It has to reexplore your codebase, understand what dependencies are needed and the features that are already implemented. Sometimes it has to make assumptions which makes it harder for us to steer claude in the right direction. But that's where claw.md comes in. It's a markdown file that you add to the root of your project and claude code reads it automatically every time you start a session. It's like an onboarding script for your codebase. Simply put, the contents of claw.md file are appended to your own prompt. You can run the /init command which will make claw generate one based off of your codebase. So let's have a look at one. This is a Nex.js15 app using the app router Tailwind and Drizzle OM command dev server run test lint code style use two space indentation prefer named exports all API routes go in app/ API use server actions instead of API routes where possible and it's pretty straightforward. Now, if I ask Claw Code to create a React component, it knows how to style it with Tailwind or any other CSS framework that I'm using, we can see that Claw does a better job at doing its job right off the bat versus having to understand where everything is at first. And before you ask, the answer is yes. You share this in your version control for your team to use, but there's actually a hierarchy of memory files depending on who it's for. So, first you have your project level claw.md that lives in the root directory of your project. You have a user level claw.md that lives in your configuration folder. This one is just for you and goes across all your projects. So, put your personal preferences here like how you write code comments. First, if you have to correct Claude to do something like always use server actions instead of API routes, then explicitly ask Claude to save this to memory so that when you come back to this project, it will know every single time. Second, if you have docs in your project that you want claw to reference, just use the at symbol with the file path. And third is we recommend you start off a project without a claw.md file so you can see where you have to constantly course correct the model. This keeps your claw.md file compact and contain only the necessary information that clock can work with. The difference between a frustrating clock code session and a productive one comes down to the context and the clot.md file is how you provide that context. Start with your stack, your preferences and then commands and just build from there as you go.

---

#### Lesson 9: Subagents

*Source:* [https://anthropic.skilljar.com/claude-code-101/469796](https://anthropic.skilljar.com/claude-code-101/469796)

**Video:** What are subagents? | **Platform:** youtube

**Video Transcript (YouTube via yt-dlp):**

Sub agents are specialized assistants that cloud code can delegate tasks to each sub agent runs in its own conversation contacts window with a custom system prompt that you define. When finished, it returns a summary to the main thread while all the intermediate work stays isolated. One of the main advantages of sub aents is that they help manage context window usage. When you chat with clot code, you're adding context to the main context window. Every tool call and its results get stored in this main context window. And so when Claude uses a sub agent, a separate window starts. The sub agent receives two inputs, a custom system prompt from your configuration file and a task description written by the parent or parent agent based on what you ask for. The sub agent then works autonomously when it reads files, edits files, or uses tools. None of these will appear in the main conversation. Just a summary is returned back. The entire sub aent conversation then gets completely discarded. Consider a task like investigating how the payment system works in an unfamiliar codebase. Maybe you're trying to use claw code to figure out which service handles refunds. Well, without a sub agent, Cloud might read 15 files, run several searches, and trace through multiple function calls, all of that context fills your context window, even if you only needed one single fact. Which service handles refunds? With a sub agent, you get the answer without the journey. The sub agent explores, discovers the answer, and returns a focus summary, keeping your main context clean. But the main window loses visibility into how the sub agent reaches its conclusions and what it discovered along the way. Cloud code includes several built-in sub aents that you can use immediately like the general purpose sub agent used for multi-step tasks that require both exploration and action. The explore sub aent used for fast searching of code bases. The plan sub agent use during plan mode for research and analysis of your codebase before presenting a plan. And you can also create your own sub aents with custom system prompts and tool access. Sub aents let clock code break work into focused pieces, keep your main context window clean, and bring back just what you need. Whether you're using the built-in ones or creating your own, they're a practical way to get more out of longer clawed code sessions.

---

#### Lesson 10: Skills

*Source:* [https://anthropic.skilljar.com/claude-code-101/469848](https://anthropic.skilljar.com/claude-code-101/469848)

**Video:** What are skills? | **Platform:** youtube

**Video Transcript (YouTube via yt-dlp):**

Every time you explain your team's coding standards to Claude, you're repeating yourself. Every PR review, you redescribe how you want feedback [music] structured. Every commit message, you remind Claude of your preferred format, and skills fix this. A skill is a markdown file that teaches Claude [music] how to do something once, and Claude applies that knowledge automatically whenever it's relevant. Agent skills are folders of instructions, scripts, and resources that Asia can discover and use to do things more accurately and efficiently. With Claw Code, we have the skill MD file. The description is how Claw decides whether to use the skill. When you ask Claude to review this PR, it matches your request against available skill descriptions and finds this one. Claude reads your request, compares it to all available skill descriptions, and activates the ones that match. You can store skills in a few places depending on who needs them. Personal skills go in the home directory.cloud/skills and follow you across all your project. These are your preferences, your commit message style, your documentation format, how you like code explained. Project skills go in the do.claw/skills inside of the root directory of your repository. Anyone who clones the repository gets these skills automatically. This is where team standards live, like your company's brand guidelines, preferred fonts, and colors that you use for web design. Cloud code has several ways to customize behavior. Skills are unique because they're automatic and task specific. CloudMD files load into every conversation. If you want claw to always use typescript strict mode that goes in your claw.md file. Skills on the other hand load on demand when they match your request. It only loads in the name and description. So it doesn't fill up your entire context window. Your PR review checklist doesn't need to be in the context when you're debugging. It loads when you actually ask for a review. Slash commands require you to type them. Skills don't. Claude applies them when it recognizes the situation. Skills work best for specialized knowledge that applies to specific tasks, code review standards your team follows, commit message formats that you prefer, brand guidelines of your organization. If you find yourself explaining the same thing [music] to Claude repeatedly, well, that's a skill waiting to be written.

---

#### Lesson 11: MCP

*Source:* [https://anthropic.skilljar.com/claude-code-101/469797](https://anthropic.skilljar.com/claude-code-101/469797)

---

#### Lesson 12: Hooks

*Source:* [https://anthropic.skilljar.com/claude-code-101/469798](https://anthropic.skilljar.com/claude-code-101/469798)

**Video:** Hooks in Claude Code | **Platform:** youtube

**Video Transcript (YouTube via yt-dlp):**

Hooks let you run commands at different points in Cloud Code's life cycle. The key difference between hooks and everything else we covered is that hooks are deterministic. They always run. So, put it this way. You can tell claude in your claw.md file to run prettier after every file edit. And most of the time it will do that. But sometimes it won't. It's not perfect, but a hook makes it happen every single time with no exceptions. Common use cases could include auto formatting after file edits, logging all executed commands for compliance, blocking dangerous operations like modifying production files, and sending yourself notifications when Claude finishes a task. Hooks are configured in your settings.json file. You pick an event, optionally set a matcher for which tools it applies to, and provide a command to run. User prompt submit runs when you submit a prompt before Claude processes it. Pre-tool use, which runs before a tool call. Post tool use runs after a tool call completes. Notification runs when Claude sends a notification. And stop runs when Claude finishes responding. The most common hook auto formatting after edit. You set a post tool use hook with a matcher of edit or multi-edit, right? So it fires whenever cla modifies a file. The command checks the file extension and runs the appropriate formatter. This could be prettier for TypeScript, go format for Go, rough for Python, whatever your project uses. Pre-tool use hooks can block tool calls before they execute. So your hook receives the tool name and input as JSON on stdin. If it exits with code two, the action is blocked and the std error message gets fed back to cla feedback. So Claude knows why it was blocked and can adjust. Exit code zero means proceed. Exit code 2 means block. This is how you enforce hard rules. Block writes to a production config directory. block bash commands that contain rm-rf block commits domain whatever your team needs to be guaranteed not suggested hooks configured include/ settings.json JSON are project level and can be checked into your repo. This means that your entire team gets the same hooks automatically. Use the claude project dur environment variable in your command set reference scripts stored in your project so they work regardless of claw's current working directory. Hooks gives you deterministic control over cloud code behavior. Use post tool use for auto formatting and logging. Use pre-tool use to block dangerous operations. Configure them in the /hooks or in settings.json and check them into your repository so your team gets them too. If something needs to happen every time without fail, don't put it in a prompt. Put it in a hook.

---

### Quiz

#### Lesson 13: Course quiz

*Source:* [https://anthropic.skilljar.com/claude-code-101/469849](https://anthropic.skilljar.com/claude-code-101/469849)

**Assessment (7 questions):**

**Q1:** Claude Code works as an AI agent. What is an AI agent?

- [ ] A chatbot that responds to questions in real time
- [ ] A code editor with built-in autocomplete features
- [ ] A cloud service that hosts your development projects
- **[CORRECT]** AI that takes action to complete goals

**Q2:** What happens when Claude Code reaches its context window limit?

- [ ] It switches to a smaller, faster model to save memory
- [ ] It removes your oldest files to make room for new ones
- **[CORRECT]** It automatically compacts your conversation to free up space
- [ ] It stops working and asks you to restart the session

**Q3:** What is the recommended workflow for using Claude Code effectively?

- [ ] Code > Test > Deploy > Monitor
- **[CORRECT]** Explore > Plan > Code > Commit
- [ ] Write > Review > Merge > Ship
- [ ] Prompt > Accept > Push > Repeat

**Q4:** How does Claude Code use the CLAUDE.md file?

- [ ] It reads it only after you run the /init command
- [ ] It reads it once when you first create the project
- **[CORRECT]** It reads it automatically at the start of every session
- [ ] It only reads it when you explicitly ask it to

**Q5:** How satisfied are you with the content provided in this course?

- [ ] Not at all satisfied
- [ ] Not very satisfied
- [ ] Unsure
- [ ] Satisfied
- [ ] Very satisfied

**Q6:** How likely are you to recommend this course to a friend or coworker?

- [ ] Very unlikely
- [ ] Unlikely
- [ ] Not sure
- [ ] Likely
- [ ] Very likely

**Q7:** Is there any feedback you'd like to provide based upon your experience with this course so far?


---

*Extracted from Anthropic Academy via authenticated session | Deep Extraction v3 | 2026-04-12*
