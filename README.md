# Career Transition Simulator

An open AI-assisted framework that helps professionals explore career transitions, translate their experience into market language, assess role fit, identify meaningful gaps, and design low-risk next-step experiments.

The Career Transition Simulator uses a structured, evidence-aware conversation to help you think more clearly before committing to a new role, industry, or professional direction.

## MVP status

This is a working MVP of a product intended to improve continuously. It is not a finished career oracle: market evidence changes, users arrive with different levels of information, and the quality of a transition hypothesis improves through repeated experiments and feedback. The current version prioritizes a useful first analysis, explicit uncertainty, real-world constraints, and a small next test.

The simulator can work from a recent CV, an old CV, a LinkedIn-style history, project notes, or a short narrative. When evidence is incomplete, it should label assumptions and ask only for the smallest missing information needed to move forward.

## Why this exists

Many professionals reach a point where their next career move is no longer obvious.

They may have valuable experience but struggle to see how it translates beyond their current title, company, or industry. They may be considering several possible paths without knowing which are realistic, which require additional evidence, or which should be tested before making a major change.

Most AI-supported job-search workflows begin after a target role has already been chosen. They focus on rewriting resumes, drafting cover letters, or preparing interview answers.

The Career Transition Simulator starts earlier. It can begin with a role the user is considering, or with their experience and constraints when no target is obvious.

It helps you use AI as a structured thinking partner to explore possible directions, examine how the market may interpret your background, and decide what to investigate next.

## Who this is for

This framework is designed for professionals asking questions such as:

- What else could I do with my experience?
- Which parts of my background are transferable?
- Am I a plausible candidate for this role?
- What might a hiring team misunderstand or overlook?
- Is the real issue a skill gap, an evidence gap, or a positioning gap?
- Which career paths are adjacent, and which would require a larger transition?
- What can I test before making a major career decision?

It may be especially useful for:

- mid-career professionals
- people changing roles, industries, or functions
- professionals returning after a career break
- immigrants translating experience across markets
- caregivers re-entering the workforce
- people whose responsibilities have outgrown their formal job titles
- professionals navigating changes caused by automation or AI

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
- a replacement for human judgment, coaching, mentorship, or professional advice
- a definitive assessment of your ability or potential
- a personality test or automated career decision-maker
- a substitute for researching real roles, companies, and labor-market conditions
- primarily a resume-writing or cover-letter tool

The simulator supports decisions; it does not make them for you.

## How the simulator works

The simulator uses a reverse-prompting approach. Instead of asking AI a broad question such as “What career should I pursue?”, you begin with evidence from your experience, preferences, and constraints. If you have a target role, the simulator evaluates it. If you do not, it maps your capabilities to several materially different market hypotheses, including less obvious paths.

Before beginning, provide whatever evidence you have: responsibilities, decisions, constraints, collaborators, outcomes, and the scale of your work—not only job titles. A polished or recent CV is not required. The model should make provisional hypotheses from incomplete information, show what is confirmed or uncertain, and propose a low-cost next test rather than blocking on missing details.

Each stage builds on the previous one. The goal is not to generate an instant career verdict, but to develop a transition hypothesis grounded in market signals and personal evidence.

## The four-stage Reverse Prompting Framework

### 1. Market Lens Analysis

Understand how a target role is positioned in current market demand—or discover plausible directions when no target has been chosen. Discovery produces a small, evidence-based set of distinct job-family directions—usually two to five—grounded in the user's capabilities, interests, constraints, and market signals. It does not force a fixed number or invent options to fill a quota.

Examine current job descriptions, recurring responsibilities, required capabilities, common terminology, seniority expectations, and relevant industry signals. The aim is to build a market-informed picture of the role before evaluating personal fit.

**Key question:** What is the market actually asking for?

### 2. Hiring Simulation Prompt

Use AI to simulate hiring evaluation and surface blind spots.

Ask AI to review your background from the perspective of a recruiter or hiring manager. Identify what appears relevant, what may be overlooked, what creates uncertainty, and which questions or objections may arise during screening.

The simulation is a hypothesis—not a prediction of how every employer will respond.

**Key question:** How might a hiring team interpret my profile?

### 3. Role Gap Calibration

Identify transferable strengths and development areas.

Compare the market lens with the hiring simulation and your experience evidence. Determine where your background already aligns and where further work may be needed. Distinguish among:

- **Competency gaps:** capabilities you still need to develop
- **Evidence gaps:** capabilities you may have but cannot yet demonstrate convincingly
- **Positioning gaps:** relevant experience described in language the target audience may not recognize
- **Exposure gaps:** limited access to the people, environments, or opportunities needed to validate the path

**Key question:** What is the real distance between my current profile and the target role?

### 4. Transition Strategy Design

Prepare for a focused, short-term application experiment aligned with market signals.

Turn the calibrated gaps into no more than three prioritized actions, led by updating the CV/profile and testing a carefully selected group of roles. Add only lightweight evidence or interview preparation when it addresses a specific gap.

The plan should be time-bounded, realistic, and designed to generate new evidence.

**Key question:** What should I do next to test and strengthen this transition?

## How to use it

You can use the framework with an AI assistant or work through the stages independently.

1. Copy the recommended input template below, or provide rough notes instead.
2. Complete as much of it as you can; do not wait for a perfect CV.
3. Ask the AI assistant to guide you through one framework stage at a time. If you do not have a target role, ask it to use proactive discovery mode.
4. Review the short executive summary and real-role shortlist, correct assumptions, and choose a direction worth testing.
5. Treat generated paths and assessments as hypotheses to investigate—not conclusions.
6. Use the final stage to update your CV/profile and run a small, selective application experiment. Avoid major training or portfolio commitments unless the evidence requires them.
7. Ask for a convenient copy of the final experiment in Markdown, Word, or PDF when supported.

Suggested opening prompt:

```text
Act as a proactive, structured career-transition thinking partner. Use the Career Transition Simulator framework and guide me through one stage at a time. Use any CV, old profile, rough notes, projects, education, volunteer work, or narrative I provide; do not require a polished or recent CV. If evidence is incomplete, build a provisional profile labeled confirmed, inferred, and unknown, ask only the smallest useful questions, and still offer two or three evidence-based directions, a recommendation, and the lowest-cost next test. Distinguish facts, interpretations, assumptions, market evidence, and access constraints; do not choose a career for me. At the end, help me design a small, low-risk experiment to test the direction I select.
```

## Recommended input

```text
Current role or professional identity:

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
What has changed since my last role:
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

The simulator should keep stage responses concise, avoid unnecessary repetition of CV content, preserve market terminology in the saved Stage 1 checkpoint, and ask before moving to the next stage or creating files.

## Guiding principle

> A career transition is not only a job search. It is the process of interpreting existing experience against new forms of market demand—and gathering better evidence before making a decision.

The aim is not to predict the future or recommend the most obvious job title. It is to help people see their experience more clearly, expand plausible directions, and test a selected next step with less guesswork and limited downside.

The product should evolve through use. New role patterns, access constraints, user corrections, and experiment outcomes should improve future versions of the framework without turning the output into a definitive judgment.

## Created for Grace Hopper Celebration

The Career Transition Simulator was created for a Grace Hopper Celebration session about using AI as a structured thinking partner for career transitions.

The project is intended to make the session practical, reusable, and accessible beyond the event. It can be adapted for workshops, peer-learning groups, coaching conversations, and individual reflection.

Grace Hopper Celebration and its organizers are not responsible for the content or outputs of this independent project unless explicitly stated otherwise.

## License

<!-- Choose and add a license before publishing. Common options include MIT, Apache-2.0, and Creative Commons licenses. Confirm that the selected license fits both the software components and written framework materials in this repository. -->

License: **To be determined.**
