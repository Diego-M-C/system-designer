#!/usr/bin/env python3
"""
Extract key engineering intelligence from Anthropic Academy courses.
Generate .md and .json references for expert AI system development with Claude.
"""

import json
import os
from datetime import date

BASE = "/mnt/c/Users/Diego/Desktop/AGENC_IA/Informes_Cursos_Anthropic"
MD_DIR = os.path.join(BASE, "md")
JSON_DIR = os.path.join(BASE, "json")

TODAY = date.today().strftime("%Y-%m-%d")

# =============================================================================
# COURSE DATA - ENGINEERING INTELLIGENCE EXTRACTION
# =============================================================================

courses = [
    {
        "id": "01",
        "slug": "building-with-claude-api",
        "title": "Building with the Claude API",
        "url": "https://anthropic.skilljar.com/claude-with-the-anthropic-api/",
        "course_id": "ca6k4fml7abo",
        "category": "core-api",
        "difficulty": "intermediate",
        "tags": ["api", "sdk", "python", "prompt-engineering", "tool-use", "rag", "mcp", "agents", "multimodal", "caching"],
        "summary": "End-to-end training on integrating Claude AI into applications via the Anthropic API. Covers the full development lifecycle from API setup to production agent architectures.",
        "prerequisites": ["Python programming proficiency", "Basic JSON handling knowledge"],
        "target_roles": ["Backend developers", "Full-stack engineers", "Data engineers", "DevOps professionals", "Technical architects", "Software engineers transitioning to AI/ML", "Chatbot developers"],
        "engineering_knowledge": {
            "api_fundamentals": [
                "API setup and authentication with key management",
                "Single and multi-turn conversation implementation",
                "System prompts for model behavior configuration",
                "Streaming responses and temperature control",
                "Structured data extraction from model outputs"
            ],
            "prompt_engineering": [
                "XML tag structuring for prompt organization",
                "Example-based learning (few-shot prompting)",
                "Prompt evaluation workflows with test datasets",
                "Model-based and code-based grading approaches for prompt evaluation",
                "Output control and format specification"
            ],
            "tool_use": [
                "Custom tool development and function calling",
                "JSON Schema for tool definitions",
                "Tool integration patterns with external APIs",
                "Batch processing with tools"
            ],
            "rag_systems": [
                "Text chunking strategies",
                "Embeddings for semantic search",
                "BM25 search integration",
                "Contextual retrieval techniques",
                "Knowledge-grounded application patterns"
            ],
            "advanced_features": [
                "Extended thinking mode for complex reasoning",
                "Multimodal features (vision, PDF processing)",
                "Citation generation from source documents",
                "Prompt caching strategies for cost and performance optimization"
            ],
            "mcp_integration": [
                "Building MCP servers for extended functionality",
                "Defining tools, resources, and prompts via MCP",
                "Client application integration with MCP"
            ],
            "agent_architectures": [
                "Parallelization patterns for concurrent task execution",
                "Routing patterns for task distribution",
                "Orchestration of multi-step agent workflows",
                "Claude Code for automated development tasks"
            ]
        },
        "key_patterns": [
            "API authentication -> Conversations -> Prompt Engineering -> Tool Use -> RAG -> Advanced Features -> MCP -> Agents",
            "Always evaluate prompts with test datasets before production deployment",
            "Use XML tags to structure complex prompts for better model comprehension",
            "Implement prompt caching to reduce latency and cost in production",
            "Design agent systems with parallelization for throughput and routing for specialization"
        ],
        "production_considerations": [
            "Key management and secure authentication",
            "Prompt caching for performance optimization",
            "Streaming for real-time response delivery",
            "Evaluation frameworks for quality assurance",
            "Agent orchestration patterns for complex workflows"
        ]
    },
    {
        "id": "02",
        "slug": "claude-code-in-action",
        "title": "Claude Code in Action",
        "url": "https://anthropic.skilljar.com/claude-code-in-action",
        "course_id": "3n2veylcj0hl",
        "category": "developer-tools",
        "difficulty": "intermediate",
        "tags": ["claude-code", "cli", "git", "github", "mcp", "automation", "context-management", "tools"],
        "summary": "Comprehensive training on using Claude Code for software development: AI coding assistant architecture, implementation techniques, context management, MCP servers, and GitHub integration.",
        "prerequisites": ["Familiarity with CLI and terminal operations", "Basic Git version control knowledge"],
        "target_roles": ["Software developers", "Engineering teams implementing AI-powered GitHub workflows"],
        "engineering_knowledge": {
            "architecture": [
                "AI coding assistant architecture and how it interacts with codebases",
                "Tool integration foundations enabling code analysis and modification",
                "Multi-tool combination for complex, multi-step programming tasks"
            ],
            "context_management": [
                "Strategies for maintaining relevant context throughout conversations",
                "Effective referencing of project resources for optimal AI assistance",
                "Context window optimization techniques"
            ],
            "visual_workflows": [
                "Visual inputs to communicate interface changes",
                "Advanced planning features for complex codebase modifications",
                "Screenshot-based communication for UI work"
            ],
            "custom_automation": [
                "Building reusable custom commands (slash commands)",
                "Automations that streamline repetitive development tasks",
                "Custom workflow creation"
            ],
            "mcp_extension": [
                "Integrating external tools and services via MCP servers",
                "Browser automation through MCP",
                "Specialized development workflow extensions"
            ],
            "github_integration": [
                "Automated code review processes",
                "AI assistance in version control workflows",
                "PR review and issue management automation"
            ],
            "reasoning_modes": [
                "Thinking mode for deep analysis of complex problems",
                "Planning mode for multi-step codebase modifications",
                "Choosing appropriate reasoning approach by task complexity"
            ]
        },
        "key_patterns": [
            "Use thinking/planning modes for complex tasks, standard mode for simple edits",
            "Extend Claude Code capabilities via MCP servers for specialized tools",
            "Automate repetitive tasks with custom slash commands",
            "Integrate AI into GitHub workflow for automated code reviews",
            "Manage context deliberately to keep AI assistance focused and relevant"
        ],
        "production_considerations": [
            "Context window limits require strategic context management",
            "MCP servers extend capabilities without modifying Claude Code core",
            "GitHub integration enables team-wide AI-assisted development",
            "Custom automations reduce repetitive manual work"
        ]
    },
    {
        "id": "03",
        "slug": "claude-101",
        "title": "Claude 101",
        "url": "https://anthropic.skilljar.com/claude-101",
        "course_id": "22npsux5ldfq0",
        "category": "foundations",
        "difficulty": "beginner",
        "tags": ["introduction", "fundamentals", "claude-features", "everyday-use"],
        "summary": "Foundational entry point to Claude. Practical introduction to everyday work tasks, core features, and pathways to advanced learning.",
        "prerequisites": [],
        "target_roles": ["New Claude users", "Professionals exploring AI assistants", "Anyone seeking structured onboarding"],
        "engineering_knowledge": {
            "core_capabilities": [
                "Core Claude features and capabilities overview",
                "Everyday work task applications",
                "Foundational AI interaction concepts",
                "Understanding Claude's strengths and appropriate use cases"
            ],
            "learning_pathways": [
                "Entry point to Anthropic Academy curriculum",
                "Pathways to specialized courses (API, MCP, agents, etc.)",
                "Progressive skill building from basic to advanced"
            ]
        },
        "key_patterns": [
            "Start with Claude 101 for team onboarding before specialized courses",
            "Establishes baseline understanding of Claude capabilities for all team members"
        ],
        "production_considerations": [
            "Recommended as prerequisite for non-technical team members before AI integration projects"
        ]
    },
    {
        "id": "04",
        "slug": "introduction-to-claude-cowork",
        "title": "Introduction to Claude Cowork",
        "url": "https://anthropic.skilljar.com/introduction-to-claude-cowork",
        "course_id": "okcui6s1t0",
        "category": "developer-tools",
        "difficulty": "beginner-intermediate",
        "tags": ["cowork", "files", "plugins", "skills", "task-loop", "context"],
        "summary": "Hands-on training for working alongside Claude directly on files, folders, and applications. Covers the Cowork task loop, plugins, skills, and multi-step work steering.",
        "prerequisites": [],
        "target_roles": ["Professionals integrating Claude into daily workflows", "Users wanting file-level AI collaboration"],
        "engineering_knowledge": {
            "cowork_architecture": [
                "Cowork = Claude working directly with files, folders, and apps on your machine",
                "Reading, editing, and producing real outputs locally",
                "Task loop: how Cowork plans and executes multi-step work"
            ],
            "context_and_planning": [
                "How context shapes Claude's planning decisions",
                "Providing effective context for better task execution",
                "Steering longer-running tasks without losing direction"
            ],
            "extensibility": [
                "Setting up plugins for specific workflows",
                "Configuring skills for task-specific behavior",
                "Workflow customization for domain-specific needs"
            ],
            "task_execution": [
                "Running end-to-end tasks from start to completion",
                "Multi-step work steering techniques",
                "Responsible delegation of complex file operations"
            ]
        },
        "key_patterns": [
            "Context quality directly determines Cowork planning quality",
            "Use plugins and skills to specialize Cowork for your domain",
            "Steer multi-step tasks actively rather than fire-and-forget",
            "From first launch to confident daily use is the learning trajectory"
        ],
        "production_considerations": [
            "File-level access requires trust boundaries and review workflows",
            "Plugin ecosystem extends capabilities per team needs",
            "Context management is critical for long-running task accuracy"
        ]
    },
    {
        "id": "05",
        "slug": "ai-fluency-framework-foundations",
        "title": "AI Fluency: Framework & Foundations",
        "url": "https://anthropic.skilljar.com/ai-fluency-framework-foundations",
        "course_id": "17owe4fx9adox",
        "category": "fluency-framework",
        "difficulty": "beginner",
        "tags": ["4d-framework", "delegation", "description", "discernment", "diligence", "ethics", "safety"],
        "summary": "Cornerstone course establishing the 4D AI Fluency Framework. Teaches practical skills for effective, efficient, ethical, and safe AI interaction. Developed with Prof. Joseph Feller and Prof. Rick Dakan.",
        "prerequisites": [],
        "target_roles": ["Anyone new to AI interaction", "Seasoned AI practitioners", "All professionals developing AI fluency"],
        "engineering_knowledge": {
            "four_d_framework": [
                "Delegation: knowing what tasks to assign to AI and how to scope them",
                "Description: crafting clear, complete instructions for AI systems",
                "Discernment: evaluating AI outputs critically and identifying errors",
                "Diligence: maintaining ethical standards and safety in AI use"
            ],
            "interaction_principles": [
                "Effective AI collaboration techniques",
                "Efficient use of AI capabilities",
                "Ethical considerations in AI interaction",
                "Safety practices for responsible AI use"
            ]
        },
        "key_patterns": [
            "4D Framework: Delegation -> Description -> Discernment -> Diligence",
            "Prerequisite for all other AI Fluency series courses",
            "Applicable across all roles interacting with AI systems",
            "Certificate of completion available after final assessment"
        ],
        "production_considerations": [
            "Foundation for organizational AI adoption strategy",
            "Provides shared vocabulary for team AI interactions",
            "Ethics and safety framework applicable to all AI projects"
        ]
    },
    {
        "id": "06",
        "slug": "introduction-to-mcp",
        "title": "Introduction to Model Context Protocol",
        "url": "https://anthropic.skilljar.com/introduction-to-model-context-protocol",
        "course_id": "47ajyxsragmw",
        "category": "mcp",
        "difficulty": "intermediate",
        "tags": ["mcp", "protocol", "tools", "resources", "prompts", "python-sdk", "servers", "clients"],
        "summary": "Foundational training on MCP: Anthropic's open protocol for connecting AI systems to external tools and data. Covers three core primitives (tools, resources, prompts), Python SDK server/client construction, and integration patterns.",
        "prerequisites": ["Working knowledge of Python programming", "Basic understanding of JSON and HTTP request-response patterns"],
        "target_roles": ["Developers building MCP servers", "Engineers integrating external tools with Claude AI"],
        "engineering_knowledge": {
            "mcp_architecture": [
                "MCP transfers tool definition and execution to specialized servers",
                "Transport-agnostic communication system",
                "Complete request-response flow from user queries to external services",
                "Server-client architecture with clear separation of concerns"
            ],
            "three_primitives": {
                "tools": [
                    "Server-side functions that Claude can invoke",
                    "Defined with decorators in Python SDK",
                    "Enable interaction with external systems and APIs",
                    "Document management operations (read, edit, create)"
                ],
                "resources": [
                    "Read-only data exposed to Claude",
                    "Static URIs for fixed data endpoints",
                    "Templated URIs for dynamic data access",
                    "MIME type handling for different content types"
                ],
                "prompts": [
                    "Pre-built, high-quality instruction templates",
                    "Reusable prompt patterns for common tasks",
                    "Parameterized prompts with dynamic inputs"
                ]
            },
            "implementation": [
                "Building MCP servers using Python SDK with decorators",
                "MCP Server Inspector for browser-based testing",
                "Client-side resource reading with MIME type handling",
                "Autocomplete integration patterns",
                "Primitive selection: when to use tools vs resources vs prompts"
            ]
        },
        "key_patterns": [
            "Tools = actions (read/write), Resources = data (read-only), Prompts = instructions (templates)",
            "Use MCP Server Inspector for testing before client integration",
            "Decorators simplify server construction in Python SDK",
            "Choose primitives based on: action needed? -> Tool | Data access? -> Resource | Instruction template? -> Prompt"
        ],
        "production_considerations": [
            "MCP servers can be shared across multiple AI applications",
            "Transport-agnostic design allows flexible deployment",
            "Server Inspector enables rapid development iteration",
            "Clear primitive separation improves maintainability"
        ]
    },
    {
        "id": "07",
        "slug": "ai-fluency-for-educators",
        "title": "AI Fluency for Educators",
        "url": "https://anthropic.skilljar.com/ai-fluency-for-educators",
        "course_id": "f6as998uhezb",
        "category": "fluency-framework",
        "difficulty": "beginner-intermediate",
        "tags": ["education", "4d-framework", "teaching", "institutional-strategy"],
        "summary": "Extends the 4D AI Fluency Framework into educational practice and institutional strategy for faculty, instructional designers, and educational leaders.",
        "prerequisites": ["4D AI Fluency Framework knowledge (from Framework & Foundations course)"],
        "target_roles": ["Academic faculty", "Instructional designers", "Educational leaders"],
        "engineering_knowledge": {
            "educational_ai_integration": [
                "Applying 4D Framework in teaching practice",
                "Institutional strategy for AI adoption in education",
                "Assessment methods for AI fluency in students",
                "Curriculum design incorporating AI tools"
            ]
        },
        "key_patterns": [
            "4D Framework adapted for educational contexts",
            "Requires foundational Framework & Foundations course",
            "Certificate available upon completion"
        ],
        "production_considerations": [
            "Relevant for teams building educational AI products",
            "Informs AI tool design for educational institutions"
        ]
    },
    {
        "id": "08",
        "slug": "ai-fluency-for-students",
        "title": "AI Fluency for Students",
        "url": "https://anthropic.skilljar.com/ai-fluency-for-students",
        "course_id": "1yao8gc9rmfcz",
        "category": "fluency-framework",
        "difficulty": "beginner",
        "tags": ["students", "4d-framework", "learning", "career-planning", "academic-success"],
        "summary": "Applies the 4D AI Fluency Framework to student experience: learning enhancement, career planning, and academic success through responsible AI collaboration.",
        "prerequisites": ["4D AI Fluency Framework knowledge (from Framework & Foundations course)"],
        "target_roles": ["Students enhancing learning with AI", "Students planning careers with AI skills"],
        "engineering_knowledge": {
            "student_ai_collaboration": [
                "Responsible AI use for academic work",
                "AI-enhanced learning strategies",
                "Career planning with AI tools",
                "Ethical boundaries in academic AI use"
            ]
        },
        "key_patterns": [
            "4D Framework adapted for student use cases",
            "Emphasis on responsible and ethical AI collaboration",
            "Certificate available upon completion"
        ],
        "production_considerations": [
            "Relevant for teams building AI tools targeting students/education"
        ]
    },
    {
        "id": "09",
        "slug": "mcp-advanced-topics",
        "title": "Model Context Protocol: Advanced Topics",
        "url": "https://anthropic.skilljar.com/model-context-protocol-advanced-topics",
        "course_id": "322b89z3mttch",
        "category": "mcp",
        "difficulty": "advanced",
        "tags": ["mcp", "sampling", "notifications", "transport", "stdio", "sse", "http", "production", "scaling"],
        "summary": "Advanced MCP implementation patterns for production: sampling, notifications, file system access, transport mechanisms (Stdio, StreamableHTTP), scaling considerations, and transport selection criteria.",
        "prerequisites": ["Python development with async patterns", "JSON message formats and HTTP protocols", "Basic Server-Sent Events (SSE) knowledge"],
        "target_roles": ["MCP implementation developers", "Engineers building production MCP servers/clients"],
        "engineering_knowledge": {
            "sampling": [
                "MCP servers requesting language model calls through connected clients",
                "Architecture shifting AI costs/complexity from server to client",
                "Server-initiated AI inference without server-side model access"
            ],
            "notifications_and_logging": [
                "Real-time feedback via context objects",
                "Logging callbacks for operation tracking",
                "Progress reporting for long-running operations",
                "Bidirectional notification patterns"
            ],
            "file_access": [
                "Roots-based permission system for directory access",
                "Security boundaries for MCP server file operations",
                "Friendly file discovery within permitted directories"
            ],
            "message_architecture": [
                "Full MCP message specification (JSON-based)",
                "Request-result pairs vs notification messages",
                "Bidirectional communication patterns",
                "Message routing and handling"
            ],
            "transport_mechanisms": {
                "stdio": [
                    "Standard input/output stream communication",
                    "Required initialization handshake sequence",
                    "Best for local, single-client scenarios"
                ],
                "streamable_http": [
                    "Server-Sent Events (SSE) for server-to-client communication",
                    "Session management for stateful connections",
                    "Dual-connection architecture patterns"
                ],
                "http_limitations": [
                    "Configuration flags affecting server-initiated requests",
                    "Streaming capability constraints",
                    "Stateless mode trade-offs"
                ]
            },
            "production_scaling": [
                "Stateless HTTP for horizontal scaling with load balancers",
                "Stateful vs stateless server trade-offs",
                "Transport selection based on deployment requirements",
                "Functional needs vs scaling constraints analysis"
            ]
        },
        "key_patterns": [
            "Stdio for local dev -> StreamableHTTP for production deployment",
            "Sampling shifts AI costs to client, keeping servers lightweight",
            "Roots-based file access provides security without complexity",
            "Stateless HTTP enables horizontal scaling; stateful preserves context",
            "Transport selection: local? -> Stdio | web? -> StreamableHTTP | scale? -> Stateless HTTP"
        ],
        "production_considerations": [
            "Transport choice directly impacts scalability architecture",
            "Sampling enables server-side AI features without server-side model costs",
            "File access permissions must be scoped tightly for security",
            "Progress notifications are essential for long-running operations UX",
            "Load balancer compatibility requires stateless transport consideration"
        ]
    },
    {
        "id": "10",
        "slug": "claude-with-amazon-bedrock",
        "title": "Claude with Amazon Bedrock",
        "url": "https://anthropic.skilljar.com/claude-in-amazon-bedrock",
        "course_id": "3i2kpf9wzkzfs",
        "category": "cloud-integration",
        "difficulty": "intermediate-advanced",
        "tags": ["aws", "bedrock", "api", "rag", "tool-use", "agents", "mcp", "production", "evaluation"],
        "summary": "Comprehensive guide to deploying Claude through Amazon Bedrock. Originally an AWS accreditation program. Covers API integration, RAG, tool use, agents, MCP, and production optimization within AWS.",
        "prerequisites": ["Python programming proficiency", "Basic AWS services and Amazon Bedrock understanding"],
        "target_roles": ["Backend developers", "ML engineers", "DevOps engineers (AWS)", "Full-stack developers", "Technical architects", "Automation engineers"],
        "engineering_knowledge": {
            "bedrock_integration": [
                "Anthropic models on Amazon Bedrock setup and configuration",
                "Multi-turn conversations with system prompt configuration",
                "Bedrock-specific API patterns and endpoints"
            ],
            "prompt_engineering": [
                "Structured prompt building and evaluation",
                "Model-based and code-based grading approaches",
                "Test dataset workflows for prompt iteration"
            ],
            "tool_use": [
                "Custom tools via JSON Schema for function calling",
                "Batch processing patterns with tools",
                "External API integration through tool definitions"
            ],
            "rag_pipeline": [
                "Text chunking strategies for document processing",
                "Embeddings generation and management",
                "BM25 search for keyword-based retrieval",
                "Contextual retrieval combining semantic and keyword search"
            ],
            "advanced_features": [
                "Extended thinking for complex reasoning tasks",
                "Vision capabilities for image analysis",
                "Prompt caching for latency and cost reduction",
                "Streaming and temperature control optimization"
            ],
            "mcp_and_agents": [
                "MCP for tools, resources, and prompts in client applications",
                "Claude Code for automated debugging and task execution",
                "Autonomous agent construction patterns"
            ],
            "evaluation": [
                "Prompt evaluation frameworks",
                "Model-based grading (LLM-as-judge)",
                "Code-based grading for deterministic checks",
                "Structured data extraction validation"
            ]
        },
        "key_patterns": [
            "Bedrock API wraps Anthropic API with AWS auth (IAM/Cognito)",
            "RAG pipeline: chunk -> embed -> index -> retrieve (BM25 + semantic) -> generate",
            "Evaluation: test dataset -> model-based + code-based grading -> iterate",
            "Production: streaming + caching + tool use for optimal performance",
            "Agents: autonomous task execution with tool access and reasoning"
        ],
        "production_considerations": [
            "AWS IAM for authentication instead of API keys",
            "Bedrock quotas and rate limiting management",
            "VPC endpoints for private API access",
            "CloudWatch integration for monitoring",
            "Cost optimization through prompt caching and model selection"
        ]
    },
    {
        "id": "11",
        "slug": "claude-with-google-vertex-ai",
        "title": "Claude with Google Cloud's Vertex AI",
        "url": "https://anthropic.skilljar.com/claude-with-google-vertex",
        "course_id": "1k0qj1i9wgzt",
        "category": "cloud-integration",
        "difficulty": "intermediate-advanced",
        "tags": ["gcp", "vertex-ai", "api", "rag", "tool-use", "agents", "mcp", "computer-use", "production"],
        "summary": "Comprehensive training on deploying Claude through Google Cloud's Vertex AI. Covers API implementation, conversations, prompt engineering, tool use, RAG, MCP, Computer Use, and agent workflows.",
        "prerequisites": ["Python programming proficiency", "Google Cloud Platform experience", "JSON data structures understanding"],
        "target_roles": ["Backend developers", "Full-stack engineers", "ML engineers", "DevOps professionals", "Technical architects", "Developers transitioning to Claude", "Document processing engineers"],
        "engineering_knowledge": {
            "vertex_integration": [
                "Claude model setup and configuration on Vertex AI",
                "Multi-turn conversations with message handling and context management",
                "Vertex AI-specific API patterns"
            ],
            "prompt_engineering": [
                "Systematic testing workflows for prompt design",
                "Automated grading techniques for evaluation",
                "XML tag structuring for prompt organization",
                "Example-based learning and output control"
            ],
            "tool_use": [
                "External function and API interaction via tools",
                "Tool definition and implementation patterns",
                "Function calling integration"
            ],
            "rag_pipeline": [
                "Text chunking for document processing",
                "Embeddings and BM25 search combination",
                "Contextual retrieval techniques"
            ],
            "advanced_features": [
                "Vision capabilities for image understanding",
                "PDF processing and data extraction",
                "Citation generation from source documents",
                "Prompt caching for performance optimization"
            ],
            "anthropic_apps": [
                "Claude Code deployment for automated development",
                "Computer Use for UI automation tasks",
                "Application deployment on Vertex AI infrastructure"
            ],
            "agent_workflows": [
                "Parallelization patterns for concurrent execution",
                "Chaining patterns for sequential task processing",
                "Routing patterns for intelligent task distribution",
                "Complex multi-agent system design"
            ]
        },
        "key_patterns": [
            "Vertex AI uses GCP auth (service accounts/ADC) instead of API keys",
            "Same Claude capabilities as direct API, wrapped in GCP infrastructure",
            "Computer Use enables UI automation not available in other deployments",
            "Agent patterns: parallelization (throughput) | chaining (sequence) | routing (specialization)",
            "Citation generation enables traceable, auditable AI outputs"
        ],
        "production_considerations": [
            "GCP IAM for authentication and access control",
            "Vertex AI quotas and pricing model",
            "Regional deployment for latency optimization",
            "Integration with GCP monitoring and logging",
            "Computer Use requires careful security scoping"
        ]
    },
    {
        "id": "12",
        "slug": "teaching-ai-fluency",
        "title": "Teaching AI Fluency",
        "url": "https://anthropic.skilljar.com/teaching-ai-fluency",
        "course_id": "zjx5xtwwhlir",
        "category": "fluency-framework",
        "difficulty": "intermediate",
        "tags": ["teaching", "4d-framework", "instructor-led", "assessment", "pedagogy"],
        "summary": "Strategies for teaching and assessing AI Fluency in instructor-led settings. Built on the 4D Framework, developed with Prof. Joseph Feller and Prof. Rick Dakan.",
        "prerequisites": ["4D AI Fluency Framework knowledge (from Framework & Foundations course)"],
        "target_roles": ["Academic faculty", "Instructional designers", "Educators"],
        "engineering_knowledge": {
            "pedagogical_strategies": [
                "Teaching AI fluency in instructor-led environments",
                "Assessment methods for AI competency",
                "4D Framework delivery strategies",
                "Classroom integration of AI tools"
            ]
        },
        "key_patterns": [
            "Complements self-paced courses with instructor facilitation",
            "Assessment-driven approach to AI fluency education"
        ],
        "production_considerations": [
            "Relevant for building AI training programs within organizations"
        ]
    },
    {
        "id": "13",
        "slug": "ai-fluency-for-nonprofits",
        "title": "AI Fluency for Nonprofits",
        "url": "https://anthropic.skilljar.com/ai-fluency-for-nonprofits",
        "course_id": "37f6rpi1f0h0",
        "category": "fluency-framework",
        "difficulty": "beginner",
        "tags": ["nonprofits", "4d-framework", "fundraising", "communications", "operations", "mission-driven"],
        "summary": "Adapts the 4D AI Fluency Framework for nonprofit organizations. Partnership with GivingTuesday. Covers AI for fundraising, communications, program delivery, operations, and leadership.",
        "prerequisites": ["Recommended: AI Fluency Framework & Foundations course", "Access to an AI chat tool (Claude.ai recommended)"],
        "target_roles": ["Nonprofit professionals (fundraising, comms, programs, ops, leadership)"],
        "engineering_knowledge": {
            "nonprofit_ai_application": [
                "4D Framework: Delegation, Description, Discernment, Diligence for nonprofits",
                "AI for fundraising optimization",
                "AI for communications and content",
                "AI for program delivery enhancement",
                "AI for operational efficiency",
                "AI for leadership decision support",
                "Mission-aligned responsible AI use"
            ]
        },
        "key_patterns": [
            "Limited resources require high-impact AI application choices",
            "Mission alignment must guide all AI adoption decisions",
            "Multiple stakeholder accountabilities affect AI use policies"
        ],
        "production_considerations": [
            "Relevant for building AI tools for nonprofit sector",
            "Data privacy and mission-alignment as design constraints"
        ]
    },
    {
        "id": "14",
        "slug": "introduction-to-agent-skills",
        "title": "Introduction to Agent Skills",
        "url": "https://anthropic.skilljar.com/introduction-to-agent-skills",
        "course_id": "377fuwy2g2o8k",
        "category": "agent-development",
        "difficulty": "intermediate",
        "tags": ["skills", "claude-code", "SKILL.md", "plugins", "automation", "enterprise", "subagents"],
        "summary": "Build, configure, and distribute reusable markdown Skills for Claude Code. Covers creation, triggers, organization, configuration, team/enterprise distribution, and subagent integration.",
        "prerequisites": [],
        "target_roles": ["Developers building Claude Code workflows", "Teams standardizing AI dev practices", "Enterprise Claude Code deployments"],
        "engineering_knowledge": {
            "skill_fundamentals": [
                "Skills = reusable markdown instructions auto-applied to matching tasks",
                "Skills vs CLAUDE.md vs hooks vs subagents: when to use each",
                "SKILL.md frontmatter formatting and structure",
                "Trigger descriptions for reliable automatic skill matching"
            ],
            "organization": [
                "Skill directory organization with progressive disclosure",
                "Context efficiency through structured skill layout",
                "Priority management between competing skills"
            ],
            "advanced_configuration": [
                "Tool access restrictions within skills",
                "Script execution from skills",
                "Conditional behavior based on context"
            ],
            "distribution": [
                "Team distribution via repository commits",
                "Organization distribution via plugins",
                "Enterprise deployment via managed settings",
                "Version control and update strategies"
            ],
            "subagent_integration": [
                "Integrating skills into custom subagents",
                "Specialized task delegation through skill-equipped subagents",
                "Workflow composition with skill-aware agents"
            ],
            "troubleshooting": [
                "Trigger failure diagnosis and resolution",
                "Priority conflict resolution",
                "Runtime error handling in skills"
            ]
        },
        "key_patterns": [
            "Skills auto-match tasks via trigger descriptions - write precise triggers",
            "Progressive disclosure: show Claude only what it needs per task",
            "Distribution ladder: local -> repository -> plugin -> managed settings",
            "Skills + subagents = specialized autonomous workflows",
            "SKILL.md frontmatter is the contract between skill and Claude Code"
        ],
        "production_considerations": [
            "Enterprise managed settings for organization-wide skill deployment",
            "Plugin distribution for cross-team standardization",
            "Trigger precision prevents false skill activation",
            "Tool access restrictions enforce security boundaries in skills"
        ]
    },
    {
        "id": "15",
        "slug": "introduction-to-subagents",
        "title": "Introduction to Subagents",
        "url": "https://anthropic.skilljar.com/introduction-to-subagents",
        "course_id": "305ppx2mtvlia",
        "category": "agent-development",
        "difficulty": "intermediate",
        "tags": ["subagents", "claude-code", "delegation", "context-management", "workflows", "agents"],
        "summary": "Create and use sub-agents in Claude Code for context management, task delegation, and specialized workflows. Covers architecture, custom creation, design patterns, and when-to-use decision frameworks.",
        "prerequisites": [],
        "target_roles": ["Claude Code users managing complex workflows", "Developers building AI dev pipelines"],
        "engineering_knowledge": {
            "subagent_architecture": [
                "Separate context window per sub-agent",
                "Input flow: main context -> sub-agent context",
                "Output flow: sub-agent summary -> main context",
                "Context isolation keeps main conversation clean"
            ],
            "creation": [
                "Custom sub-agent creation via /agents command",
                "Tailored sub-agents: code reviewers, doc generators, etc.",
                "Configuration of sub-agent capabilities and constraints"
            ],
            "design_patterns": [
                "Structured output formats for consistent results",
                "Obstacle reporting for transparent failure handling",
                "Tool access limiting for security and focus",
                "Clear task scoping for reliable completion"
            ],
            "decision_framework": [
                "When sub-agents help most: independent, parallelizable tasks",
                "When NOT to use: tightly coupled tasks needing shared context",
                "Anti-patterns: over-delegation, vague task scoping, unrestricted tool access",
                "Cost-benefit: delegation overhead vs context management benefit"
            ]
        },
        "key_patterns": [
            "Sub-agents = context isolation + task delegation + focused execution",
            "Break complex work into focused pieces, each handled by a specialized sub-agent",
            "Structured outputs + obstacle reporting = reliable sub-agent behavior",
            "Limit tool access per sub-agent to prevent scope creep and security issues",
            "Don't sub-agent everything: overhead must be justified by complexity"
        ],
        "production_considerations": [
            "Sub-agent count affects token usage and cost",
            "Tool access restrictions are critical for security",
            "Structured outputs enable downstream automation",
            "Obstacle reporting prevents silent failures"
        ]
    },
    {
        "id": "16",
        "slug": "ai-capabilities-and-limitations",
        "title": "AI Capabilities and Limitations",
        "url": "https://anthropic.skilljar.com/ai-capabilities-and-limitations",
        "course_id": "3oa2jr8dqiak3",
        "category": "fluency-framework",
        "difficulty": "beginner",
        "tags": ["capabilities", "limitations", "mental-model", "generative-ai", "4d-framework-companion"],
        "summary": "Working mental model of generative AI behavior. Companion to the 4D Framework: teaches the machine properties that human competencies (Delegation, Description, Discernment, Diligence) respond to.",
        "prerequisites": [],
        "target_roles": ["Anyone seeking to understand AI system behavior", "4D Framework learners wanting technical foundation"],
        "engineering_knowledge": {
            "ai_mental_model": [
                "Capability-to-limitation continuum for task assessment",
                "Types of unexpected AI outputs and their causes",
                "Targeted fixes for different types of AI failures",
                "Machine properties underlying 4D Framework competencies"
            ],
            "diagnostic_skills": [
                "Recognizing WHICH KIND of unexpected an output is",
                "Locating WHERE on the capability-limitation spectrum a task falls",
                "Responding with TARGETED fixes rather than generic retries"
            ]
        },
        "key_patterns": [
            "Not all AI failures are the same: diagnose before fixing",
            "Capability-limitation continuum guides task feasibility assessment",
            "Targeted fixes > generic retries for unexpected outputs",
            "Companion to 4D Framework: machine side of human-AI collaboration"
        ],
        "production_considerations": [
            "Essential for setting realistic expectations in AI system design",
            "Informs error handling and fallback strategy design",
            "Helps teams understand when AI is/isn't the right solution"
        ]
    },
]


def generate_course_md(course):
    """Generate individual course .md file."""
    lines = []
    lines.append(f"# {course['title']}")
    lines.append("")
    lines.append(f"> **Source:** [{course['url']}]({course['url']})")
    lines.append(f"> **Category:** {course['category']} | **Difficulty:** {course['difficulty']} | **Course ID:** {course['course_id']}")
    lines.append(f"> **Tags:** {', '.join(course['tags'])}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(course['summary'])
    lines.append("")

    if course['prerequisites']:
        lines.append("## Prerequisites")
        lines.append("")
        for p in course['prerequisites']:
            lines.append(f"- {p}")
        lines.append("")

    if course['target_roles']:
        lines.append("## Target Roles")
        lines.append("")
        for r in course['target_roles']:
            lines.append(f"- {r}")
        lines.append("")

    lines.append("## Engineering Knowledge")
    lines.append("")
    ek = course['engineering_knowledge']
    for section_key, section_val in ek.items():
        section_title = section_key.replace("_", " ").title()
        lines.append(f"### {section_title}")
        lines.append("")
        if isinstance(section_val, list):
            for item in section_val:
                lines.append(f"- {item}")
        elif isinstance(section_val, dict):
            for sub_key, sub_val in section_val.items():
                sub_title = sub_key.replace("_", " ").title()
                lines.append(f"**{sub_title}:**")
                if isinstance(sub_val, list):
                    for item in sub_val:
                        lines.append(f"- {item}")
                lines.append("")
        lines.append("")

    lines.append("## Key Engineering Patterns")
    lines.append("")
    for p in course['key_patterns']:
        lines.append(f"- {p}")
    lines.append("")

    lines.append("## Production Considerations")
    lines.append("")
    for p in course['production_considerations']:
        lines.append(f"- {p}")
    lines.append("")

    lines.append("---")
    lines.append(f"*Extracted from Anthropic Academy | {TODAY}*")
    lines.append("")

    return "\n".join(lines)


def generate_course_json(course):
    """Generate individual course .json file."""
    return json.dumps(course, indent=2, ensure_ascii=False)


def generate_master_md(courses):
    """Generate master reference .md with all engineering intelligence."""
    lines = []
    lines.append("# Anthropic Academy - Engineering Intelligence Reference")
    lines.append("")
    lines.append(f"> **Generated:** {TODAY} | **Courses:** {len(courses)} | **Source:** anthropic.skilljar.com")
    lines.append("> **Purpose:** Key engineering knowledge for building expert AI systems with Claude")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Quick reference index
    lines.append("## Course Index")
    lines.append("")
    lines.append("| # | Course | Category | Difficulty | Key Focus |")
    lines.append("|---|--------|----------|------------|-----------|")
    for c in courses:
        lines.append(f"| {c['id']} | [{c['title']}](md/{c['id']}_{c['slug']}.md) | {c['category']} | {c['difficulty']} | {', '.join(c['tags'][:4])} |")
    lines.append("")

    # Architecture categories
    lines.append("---")
    lines.append("")
    lines.append("## Architecture Map")
    lines.append("")
    lines.append("### Core API Development")
    lines.append("```")
    lines.append("Building with the Claude API")
    lines.append("  |-> API Setup & Auth -> Conversations -> Prompt Engineering")
    lines.append("  |-> Tool Use -> RAG Systems -> Advanced Features (thinking, vision, caching)")
    lines.append("  |-> MCP Integration -> Agent Architectures (parallel, routing, chaining)")
    lines.append("```")
    lines.append("")
    lines.append("### Developer Tools")
    lines.append("```")
    lines.append("Claude Code in Action          -> coding assistant, context mgmt, GitHub integration")
    lines.append("Introduction to Claude Cowork   -> file-level collaboration, task loops, plugins")
    lines.append("Introduction to Agent Skills    -> SKILL.md, triggers, enterprise distribution")
    lines.append("Introduction to Subagents       -> context isolation, delegation, design patterns")
    lines.append("```")
    lines.append("")
    lines.append("### Model Context Protocol (MCP)")
    lines.append("```")
    lines.append("Introduction to MCP             -> 3 primitives: Tools | Resources | Prompts")
    lines.append("MCP Advanced Topics             -> Sampling, Transport (Stdio/HTTP), Production Scaling")
    lines.append("```")
    lines.append("")
    lines.append("### Cloud Deployment")
    lines.append("```")
    lines.append("Claude with Amazon Bedrock      -> AWS integration, IAM auth, Bedrock-specific patterns")
    lines.append("Claude with Google Vertex AI     -> GCP integration, Computer Use, Vertex patterns")
    lines.append("```")
    lines.append("")
    lines.append("### AI Fluency & Foundations")
    lines.append("```")
    lines.append("Claude 101                      -> entry-level onboarding")
    lines.append("AI Fluency: Framework            -> 4D: Delegation, Description, Discernment, Diligence")
    lines.append("AI Capabilities & Limitations    -> capability-limitation continuum, diagnostic skills")
    lines.append("AI Fluency for Educators/Students/Nonprofits -> domain-specific adaptations")
    lines.append("Teaching AI Fluency              -> instructor-led delivery strategies")
    lines.append("```")
    lines.append("")

    # Critical engineering patterns
    lines.append("---")
    lines.append("")
    lines.append("## Critical Engineering Patterns (All Courses)")
    lines.append("")

    lines.append("### API & Prompt Engineering")
    lines.append("- Use XML tags to structure complex prompts for better model comprehension")
    lines.append("- Always evaluate prompts with test datasets before production deployment")
    lines.append("- Implement prompt caching to reduce latency and cost in production")
    lines.append("- Use model-based grading (LLM-as-judge) + code-based grading for evaluation")
    lines.append("- Streaming for real-time responses, temperature control for output variation")
    lines.append("")

    lines.append("### Tool Use & Function Calling")
    lines.append("- Define tools with JSON Schema for type-safe function calling")
    lines.append("- Tools enable Claude to interact with external systems and APIs")
    lines.append("- Batch processing patterns for high-throughput tool operations")
    lines.append("- Tool access restrictions enforce security boundaries")
    lines.append("")

    lines.append("### RAG (Retrieval-Augmented Generation)")
    lines.append("- Pipeline: chunk -> embed -> index -> retrieve (BM25 + semantic) -> generate")
    lines.append("- Contextual retrieval combines keyword (BM25) and semantic search")
    lines.append("- Text chunking strategy directly impacts retrieval quality")
    lines.append("- Citation generation enables traceable, auditable AI outputs")
    lines.append("")

    lines.append("### MCP (Model Context Protocol)")
    lines.append("- Three primitives: Tools (actions) | Resources (read-only data) | Prompts (instruction templates)")
    lines.append("- Transport: Stdio (local dev) -> StreamableHTTP (production) -> Stateless HTTP (scale)")
    lines.append("- Sampling: servers request LLM calls through clients (cost stays client-side)")
    lines.append("- MCP Server Inspector for rapid development and testing iteration")
    lines.append("- Roots-based file access for security-scoped filesystem operations")
    lines.append("")

    lines.append("### Agent Architectures")
    lines.append("- Parallelization: concurrent execution for throughput-sensitive tasks")
    lines.append("- Routing: intelligent task distribution to specialized handlers")
    lines.append("- Chaining: sequential processing where each step feeds the next")
    lines.append("- Sub-agents: context isolation + delegation + focused execution")
    lines.append("- Skills: reusable markdown instructions auto-matched to tasks via triggers")
    lines.append("")

    lines.append("### Claude Code & Developer Workflow")
    lines.append("- Thinking mode for deep analysis, planning mode for multi-step changes")
    lines.append("- Custom slash commands for repetitive task automation")
    lines.append("- MCP servers extend capabilities without modifying core")
    lines.append("- GitHub integration for automated code reviews and PR management")
    lines.append("- Sub-agents for context management in complex workflows")
    lines.append("")

    lines.append("### Cloud Deployment")
    lines.append("- AWS Bedrock: IAM auth, VPC endpoints, CloudWatch monitoring, Bedrock quotas")
    lines.append("- GCP Vertex AI: service account auth, regional deployment, Computer Use capability")
    lines.append("- Both platforms: same Claude capabilities, different auth and infrastructure patterns")
    lines.append("")

    lines.append("### 4D AI Fluency Framework")
    lines.append("- **Delegation:** knowing what tasks to assign to AI and how to scope them")
    lines.append("- **Description:** crafting clear, complete instructions for AI systems")
    lines.append("- **Discernment:** evaluating AI outputs critically and identifying errors")
    lines.append("- **Diligence:** maintaining ethical standards and safety in AI use")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Recommended Learning Paths")
    lines.append("")
    lines.append("### Path 1: AI Engineer / Backend Developer")
    lines.append("```")
    lines.append("Claude 101 -> Building with the Claude API -> Intro to MCP -> MCP Advanced -> Claude Code in Action")
    lines.append("```")
    lines.append("")
    lines.append("### Path 2: Claude Code Power User")
    lines.append("```")
    lines.append("Claude 101 -> Claude Code in Action -> Intro to Agent Skills -> Intro to Subagents -> Intro to Claude Cowork")
    lines.append("```")
    lines.append("")
    lines.append("### Path 3: AWS Cloud Deployment")
    lines.append("```")
    lines.append("Building with the Claude API -> Claude with Amazon Bedrock -> Intro to MCP -> MCP Advanced")
    lines.append("```")
    lines.append("")
    lines.append("### Path 4: GCP Cloud Deployment")
    lines.append("```")
    lines.append("Building with the Claude API -> Claude with Google Vertex AI -> Intro to MCP -> MCP Advanced")
    lines.append("```")
    lines.append("")
    lines.append("### Path 5: AI Fluency (Non-Technical)")
    lines.append("```")
    lines.append("Claude 101 -> AI Fluency: Framework & Foundations -> AI Capabilities & Limitations -> [Domain-specific course]")
    lines.append("```")
    lines.append("")

    lines.append("---")
    lines.append(f"*All information extracted from public Anthropic Academy pages. Nothing fabricated. Date: {TODAY}*")
    lines.append("")

    return "\n".join(lines)


def generate_master_json(courses):
    """Generate master .json with all structured data."""
    master = {
        "metadata": {
            "title": "Anthropic Academy - Engineering Intelligence Reference",
            "generated": TODAY,
            "source": "https://anthropic.skilljar.com/",
            "total_courses": len(courses),
            "purpose": "Key engineering knowledge for building expert AI systems with Claude",
            "disclaimer": "All content extracted from public Anthropic Academy pages. Nothing fabricated."
        },
        "categories": {
            "core-api": {"description": "Core Claude API development", "courses": []},
            "developer-tools": {"description": "Claude Code, Cowork, and development workflow tools", "courses": []},
            "mcp": {"description": "Model Context Protocol implementation", "courses": []},
            "cloud-integration": {"description": "Cloud platform deployment (AWS, GCP)", "courses": []},
            "agent-development": {"description": "Agent skills and sub-agent architecture", "courses": []},
            "fluency-framework": {"description": "AI Fluency and foundations", "courses": []},
            "foundations": {"description": "Introductory and foundational courses", "courses": []},
        },
        "learning_paths": {
            "ai_engineer": {
                "name": "AI Engineer / Backend Developer",
                "sequence": ["claude-101", "building-with-claude-api", "introduction-to-mcp", "mcp-advanced-topics", "claude-code-in-action"]
            },
            "claude_code_power_user": {
                "name": "Claude Code Power User",
                "sequence": ["claude-101", "claude-code-in-action", "introduction-to-agent-skills", "introduction-to-subagents", "introduction-to-claude-cowork"]
            },
            "aws_deployment": {
                "name": "AWS Cloud Deployment",
                "sequence": ["building-with-claude-api", "claude-with-amazon-bedrock", "introduction-to-mcp", "mcp-advanced-topics"]
            },
            "gcp_deployment": {
                "name": "GCP Cloud Deployment",
                "sequence": ["building-with-claude-api", "claude-with-google-vertex-ai", "introduction-to-mcp", "mcp-advanced-topics"]
            },
            "ai_fluency": {
                "name": "AI Fluency (Non-Technical)",
                "sequence": ["claude-101", "ai-fluency-framework-foundations", "ai-capabilities-and-limitations"]
            }
        },
        "critical_patterns": {
            "api_and_prompts": [
                "Use XML tags to structure complex prompts",
                "Evaluate prompts with test datasets before production",
                "Implement prompt caching for latency and cost optimization",
                "Model-based grading (LLM-as-judge) + code-based grading for evaluation",
                "Streaming for real-time responses"
            ],
            "tool_use": [
                "JSON Schema for type-safe tool definitions",
                "Tools enable Claude to interact with external systems",
                "Batch processing for high-throughput operations",
                "Tool access restrictions for security"
            ],
            "rag": [
                "Pipeline: chunk -> embed -> index -> retrieve (BM25 + semantic) -> generate",
                "Contextual retrieval combines keyword and semantic search",
                "Citation generation for auditable outputs"
            ],
            "mcp": [
                "Three primitives: Tools (actions) | Resources (data) | Prompts (templates)",
                "Transport: Stdio (local) -> StreamableHTTP (prod) -> Stateless HTTP (scale)",
                "Sampling shifts AI costs to client side",
                "Roots-based file access for security"
            ],
            "agents": [
                "Parallelization for throughput",
                "Routing for specialization",
                "Chaining for sequential processing",
                "Sub-agents for context isolation and delegation",
                "Skills (SKILL.md) for reusable auto-matched instructions"
            ],
            "cloud": [
                "AWS Bedrock: IAM auth, VPC endpoints, CloudWatch",
                "GCP Vertex AI: service accounts, regional deployment, Computer Use",
                "Same Claude capabilities, different infrastructure patterns"
            ],
            "four_d_framework": [
                "Delegation: scope tasks for AI appropriately",
                "Description: craft clear AI instructions",
                "Discernment: evaluate outputs critically",
                "Diligence: maintain ethics and safety"
            ]
        },
        "courses": courses
    }

    # Populate category course lists
    for c in courses:
        cat = c['category']
        if cat in master['categories']:
            master['categories'][cat]['courses'].append(c['slug'])

    return json.dumps(master, indent=2, ensure_ascii=False)


# =============================================================================
# GENERATE ALL FILES
# =============================================================================

print("=" * 70)
print("  ANTHROPIC ACADEMY - Engineering Intelligence Extraction")
print("  Generating .md and .json files...")
print("=" * 70)

# Individual course files
for course in courses:
    slug = course['slug']
    cid = course['id']

    # .md
    md_content = generate_course_md(course)
    md_path = os.path.join(MD_DIR, f"{cid}_{slug}.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    # .json
    json_content = generate_course_json(course)
    json_path = os.path.join(JSON_DIR, f"{cid}_{slug}.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(json_content)

    print(f"  [OK] {cid}_{slug}.md + .json")

# Master files
master_md = generate_master_md(courses)
master_md_path = os.path.join(BASE, "ANTHROPIC_ACADEMY_MASTER_REFERENCE.md")
with open(master_md_path, 'w', encoding='utf-8') as f:
    f.write(master_md)
print(f"\n  [MASTER] ANTHROPIC_ACADEMY_MASTER_REFERENCE.md")

master_json = generate_master_json(courses)
master_json_path = os.path.join(BASE, "ANTHROPIC_ACADEMY_MASTER_REFERENCE.json")
with open(master_json_path, 'w', encoding='utf-8') as f:
    f.write(master_json)
print(f"  [MASTER] ANTHROPIC_ACADEMY_MASTER_REFERENCE.json")

print("")
print("=" * 70)
print(f"  COMPLETE: {len(courses)} courses x 2 formats = {len(courses)*2} files")
print(f"  + 2 master reference files")
print(f"  Total: {len(courses)*2 + 2} files generated")
print(f"  Output: {BASE}")
print("=" * 70)
