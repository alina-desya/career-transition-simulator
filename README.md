# Career Transition Simulator

Created and owned by **Alina Desiatnikova**.

An open AI-assisted framework that helps people explore career directions, translate their experience into market language, assess role fit, identify meaningful gaps, and design low-risk next-step experiments.

The Career Transition Simulator uses a structured, evidence-aware conversation to help you think more clearly before committing to a new role, industry, or professional direction.

## MVP status

This is a working MVP testing the hypothesis that AI can be used as a structured, evidence-aware, and safer thinking partner for exploring possible career paths before making a major commitment. It is not a finished career oracle: market evidence changes, users arrive with different levels of information, and the quality of a transition hypothesis improves through repeated experiments and feedback.

This project is experimental. The skill, prompts, conversation flow, and guidance are subject to change as the hypothesis is tested and the system is improved. The current version prioritizes explicit uncertainty, real-world constraints, user correction, and small reversible experiments.

The simulator can work from a recent CV, an old CV, a LinkedIn-style history, project notes, or a short narrative. When evidence is incomplete, it should label assumptions and ask only for the smallest missing information needed to move forward.

## Why this exists

Many professionals reach a point where their next career move is no longer obvious.

They may have valuable experience but struggle to see how it translates beyond their current title, company, or industry. They may be considering several possible paths without knowing which are realistic, which require additional evidence, or which should be tested before making a major change.

Most AI-supported job-search workflows begin after a target role has already been chosen. They focus on rewriting resumes, drafting cover letters, or preparing interview answers.

The Career Transition Simulator starts earlier. It can begin with a role the user is considering, or with their experience and constraints when no target is obvious. When the user lacks career clarity, it begins with plain-language work patterns and small comparisons rather than asking them to choose a job title immediately.

It helps you use AI as a structured thinking partner to explore possible directions, examine how the market may interpret your background, and decide what to investigate next.

## Who this is for

This framework is open to people from any country and any background, including those starting their first career or drawing on informal and unpaid experience. No country, nationality, citizenship, education level, or work authorization is a prerequisite for participation. Eligibility for a particular opportunity is assessed separately when relevant.

The conversation follows the user's language and chosen market. Local titles, sources, work arrangements, and salary currencies matter; a country, relocation plan, CV, or LinkedIn account is not required to begin exploring.

It supports questions such as:

- What else could I do with my experience?
- Which parts of my background are transferable?
- Am I a plausible candidate for this role?
- What might a hiring team misunderstand or overlook?
- Is the real issue a skill gap, an evidence gap, or a positioning gap?
- Which career paths are adjacent, and which would require a larger transition?
- What can I test before making a major career decision?

It may be especially useful for:

- people starting their first career or moving from informal work
- mid-career professionals
- people changing roles, industries, or functions
- professionals returning after a career break
- immigrants translating experience across markets
- caregivers re-entering the workforce
- people whose responsibilities have outgrown their formal job titles
- professionals navigating changes caused by automation or AI

## Purpose and limitations

This project tests a method for using AI to support career exploration. It is not a validated counseling or assessment instrument, and its outputs should be treated as hypotheses for reflection and investigation rather than as professional judgments.

The Career Transition Simulator should not replace career counseling, psychotherapy, coaching, legal or immigration advice, financial advice, medical care, employment services, or other professional support. Seek appropriately qualified professional help when a decision involves specialized expertise, significant financial or legal consequences, mental health, safety, or other high-stakes concerns.

## What it is and what it is not

### It is

- a guided framework for career-transition analysis
- a way to translate experience into clearer market language
- a tool for comparing possible career directions
- a simulation of how hiring teams may interpret a profile
- a method for separating different kinds of gaps
- a starting point for designing small, practical career experiments

### It is not

- a guarantee of employment or career success
- a validated career assessment or counseling service
- a replacement for human judgment, coaching, mentorship, or professional advice
- a definitive assessment of your ability or potential
- a personality test or automated career decision-maker
- a substitute for researching real roles, companies, and labor-market conditions
- primarily a resume-writing or cover-letter tool

The simulator supports decisions; it does not make them for you.

## How the simulator works

The simulator uses a reverse-prompting approach. Instead of asking AI a broad question such as “What career should I pursue?”, you begin with evidence from your experience, preferences, and constraints. If you have a target role, the simulator evaluates it. If you do not, it maps your capabilities to several materially different market hypotheses, including less obvious paths.

Before beginning, provide whatever evidence you have: responsibilities, decisions, constraints, collaborators, outcomes, and the scale of your work—not only job titles. A polished or recent CV is not required. The model should make provisional hypotheses from incomplete information, show what is confirmed or uncertain, and propose a low-cost next test rather than blocking on missing details.

The stages build on the evidence already available. A targeted hiring evaluation can use all four stages. An exploration-only session can move from work patterns and market hypotheses directly to a comparison experiment and synthesis. Hiring simulation, current vacancies, and choosing one career are optional. When current research is unavailable, the assistant can use supplied descriptions or clearly labeled provisional analysis.

The maintained skill starts at [SKILL.md](.agents/skills/career-transition-simulator/SKILL.md), which owns routing and shared rules and links to stage details. This README is a product overview.

Every direction has two separate questions: could this be feasible, and would its everyday work suit you? Experience and market demand help assess feasibility; your preferences and experience of the activities help assess work fit. Either can remain unknown. Being good at something does not mean you want more of it.

## The four-stage Reverse Prompting Framework

### 1. Market Lens Analysis

Understand how a target role is positioned in current market demand—or discover plausible directions when no target has been chosen. Discovery produces a small, evidence-based set of distinct directions grounded in the user's experience, interests, constraints, and market signals. It does not force a fixed number or invent options to fill a quota.

Examine current job descriptions, recurring responsibilities, required capabilities, common terminology, seniority expectations, and relevant industry signals. The aim is to build a market-informed picture of the role before evaluating personal fit.

**Key question:** What is the market actually asking for?

### 2. Hiring Simulation Prompt

When a hiring perspective is relevant to the user's goal, use AI to simulate evaluation and surface blind spots. This stage owns focused research into current openings when useful; a live shortlist is not required to complete the analysis.

Ask AI to review your background from the perspective of a recruiter or hiring manager. Identify what appears relevant, what may be overlooked, what creates uncertainty, and which questions or objections may arise during screening.

The simulation is a hypothesis—not a prediction of how every employer will respond.

**Key question:** How might a hiring team interpret my profile?

### 3. Role Gap Calibration

Identify transferable strengths and development areas.

Compare the market lens with your experience evidence and any hiring simulation performed. Determine where your background already aligns and where further work may be needed. Distinguish among:

- **Competency gaps:** capabilities you still need to develop
- **Evidence gaps:** capabilities you may have but cannot yet demonstrate convincingly
- **Positioning gaps:** relevant experience described in language the target audience may not recognize
- **Exposure gaps:** limited access to the people, environments, or opportunities needed to validate the path

Keep hiring uncertainties and opportunity-specific access constraints separate from competency gaps. Missing information does not establish a lack of ability.

**Key question:** What is the real distance between my current profile and the target role?

### 4. Transition Strategy Design

Design an experiment that fits the user's purpose, readiness, available time, and resources.

Turn the most important findings or open questions into no more than three prioritized actions. These may involve comparing work activities, exploring an internal move, testing a service concept, or making selective applications when ready. CV/profile updates are one option, not a universal first step.

The plan should be time-bounded, realistic, and designed to generate new evidence.

**Key question:** What should I do next to test and strengthen this transition?

## How to use it

You can use the framework with an AI assistant or work through the stages independently.

1. Copy the recommended input template below, or provide rough notes instead.
2. Complete as much of it as you can; do not wait for a perfect CV.
3. Share what you want help with. The assistant should clarify only missing purpose or material context. It uses targeted mode for a known direction, discovery for comparing possibilities, or clarity-first mode when you want help recognizing work patterns.
4. Review the analysis, correct assumptions, and select a direction, compare alternatives, or remain undecided.
5. Treat generated paths and assessments as hypotheses to investigate—not conclusions.
6. Use the final stage to design a small experiment and a review point. Applications are optional. Consider major training or portfolio commitments only after clarifying their relevance and lower-cost ways to test fit.
7. Ask for a convenient copy of the final experiment in Markdown, Word, or PDF when supported.
8. Return with what you tried, what happened, what you wanted more or less of, and any constraints you discovered. The assistant revisits the original hypothesis, updates feasibility and work fit separately, and helps you continue, adjust, or stop the test without restarting intake. Partial or inconclusive results are valid inputs.

Suggested opening prompt:

```text
Use the Career Transition Simulator to help me explore or evaluate career directions. Start with my purpose and whatever background I can share, asking only for missing context that matters. Help me understand the evidence and uncertainty, then design a small experiment suited to my readiness. I may want to compare possibilities without choosing a career or applying for jobs.
```

## Recommended input

```text
Current activities, learning, or role, if any:

Years and types of experience:

Industries or environments I have worked in:

Responsibilities I have owned:

Problems I have solved:

Decisions I have made:

People or teams I have worked with:

Outcomes I can demonstrate:

Tools, methods, or domain knowledge I use:

Work I enjoy:

Work I want less of:

Constraints or non-negotiables:

Roles or directions I am considering, if any:

What I most want to learn from this simulation:
```

You do not need perfect answers. Concrete examples are more useful than polished language. You can answer only the questions that are relevant to your situation.

If you have no current CV, start with:

```text
What I have done repeatedly, paid or unpaid:
Problems people rely on me to solve:
Decisions or responsibilities I have owned:
Work that gave me energy:
Work I want less of:
What has changed in my situation, if relevant:
What my next opportunity must accommodate:
```

## Privacy notes

Career materials can contain sensitive personal and organizational information. Before sharing content with any AI system:

- remove names, email addresses, phone numbers, and exact home addresses
- remove confidential employer, client, customer, or project information
- replace sensitive names and figures with neutral labels or approximate ranges
- avoid sharing identification numbers, financial records, health information, or immigration documents
- review the privacy and data-retention settings of the AI tool you use
- share only the information needed for the analysis

When in doubt, anonymize the material first.

Keep personal inputs in a local `personal/` folder and generated work in `tmp/` or `output/`; these locations are ignored for new files. Already tracked fictional demo artifacts remain in the repository. Ignore rules do not remove files from Git history.

## Example use case

**Starting point:** A senior event-program manager wants to explore a move into product operations but is unsure whether their background will be taken seriously.

**The simulator applies the four stages:**

1. **Market Lens Analysis:** Review current product-operations roles to identify recurring responsibilities, language, capabilities, and seniority expectations.
2. **Hiring Simulation Prompt:** Simulate how a recruiter or hiring manager might interpret the event-program-management background, including likely strengths, uncertainties, and screening questions.
3. **Role Gap Calibration:** Identify transferable strengths—such as cross-functional planning, operational design, stakeholder alignment, risk management, and metrics review—and separate true competency gaps from evidence or positioning gaps.
4. **Transition Strategy Design:** Update the CV/profile for the target market, apply selectively to suitable roles, and add lightweight evidence only if a specific gap requires it.

**Result:** Not a verdict, but a clearer transition hypothesis, a more precise gap analysis, and a practical application experiment before making a larger commitment.

## Outputs

Depending on the question and the available evidence, the simulator can produce:

- an experience and capability inventory
- a transferable-skills map
- market-language translations of existing experience
- a shortlist of adjacent, cross-functional, emerging, and stretch career paths
- a role-fit hypothesis
- a simulated recruiter or hiring-manager review
- a list of likely strengths, concerns, and follow-up questions
- a competency, evidence, positioning, and exposure gap analysis
- a set of assumptions that require validation
- a time-bounded, low-risk transition experiment
- suggested success signals and reflection questions

Outputs should clearly distinguish:

- facts provided by the user
- interpretations based on those facts
- assumptions that need validation
- possible actions the user may choose to take

The simulator keeps responses concise and carries forward findings in the conversation. It pauses for missing decisions or consequential corrections and honors requests to continue. It never prompts to save after intake or individual stages; intermediate exports are available on request. It offers a final brief at most once per simulation, respects a previous decline, and creates an already requested file without asking again. Saving checkpoints is not required to proceed or return with results.

## Guiding principle

> A career transition is not only a job search. It is the process of interpreting existing experience against new forms of market demand—and gathering better evidence before making a decision.

The aim is not to predict the future or recommend the most obvious job title. It is to help people see their experience more clearly, expand plausible directions, and test a selected next step with less guesswork and limited downside.

The product should evolve through use. New role patterns, access constraints, user corrections, and experiment outcomes should improve future versions of the framework without turning the output into a definitive judgment.

## Created for Grace Hopper Celebration

The Career Transition Simulator was created for a Grace Hopper Celebration session about using AI as a structured thinking partner for career transitions.

The project is intended to make the session practical, reusable, and accessible beyond the event. It can be adapted for workshops, peer-learning groups, coaching conversations, and individual reflection.

Grace Hopper Celebration and its organizers are not responsible for the content or outputs of this independent project unless explicitly stated otherwise.

## License

License: [MIT](LICENSE).
