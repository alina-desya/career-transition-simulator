# Career Transition Simulator

Created and owned by **Alina Desiatnikova**.

An open, AI-assisted framework for exploring career directions before committing to a new role, industry, or professional path. It helps people translate experience into market language, assess role fit, distinguish meaningful gaps, and choose a low-risk next step.

This is a proof of concept, not a validated assessment, career-counseling service, or promise of employment. Its outputs are hypotheses to investigate.

## Getting started in Codex

This repository includes a project-local Codex skill at `.agents/skills/career-transition-simulator/`.

1. Clone or download this repository.
2. Open the repository folder as a project in Codex.
3. Start a new chat and invoke **Career Transition Simulator** from the skills picker or slash-command menu (typically `/career-transition-simulator`). You can also ask Codex to use it directly.
4. Share a CV or a short description of your experience, what you want to explore, and the market or location that matters to you.

You do not need a CV, target role, or polished career story to begin. For example:

> Use the Career Transition Simulator to help me explore a move from customer support into operations in Mexico. I have ten years of support and implementation experience, including leading a team, but I am unsure which roles fit.

The skill is available while this repository is open. To use it in every Codex project, install or copy it into your personal Codex skills directory.

## What it does

The conversation moves through four stages, with the user deciding whether to continue after each one:

1. **Market Lens Analysis** — explores a target role or plausible directions and connects market expectations to the person's experience.
2. **Hiring Simulation** — considers how a recruiter and hiring manager might interpret the available evidence; this is a reasoned simulation, not a prediction.
3. **Role Gap Calibration** — separates transferable strengths from competency, evidence, positioning, and exposure gaps.
4. **Transition Strategy Design** — turns the findings into one primary next action and up to two supporting actions.

The maintained instructions are in [SKILL.md](.agents/skills/career-transition-simulator/SKILL.md). They cover the staged flow, careful use of market research, privacy, and file creation.

## Who it is for

It can support people who are starting a career, changing roles or industries, returning after a break, moving between markets, or trying to make sense of responsibilities that have outgrown their job title. Informal work, caregiving, volunteering, study, and short descriptions of experience are valid starting evidence.

It is useful for questions like:

- What else could I do with my experience?
- Which parts of my background are transferable?
- How might a hiring team interpret my profile?
- Is the issue a capability gap, an evidence gap, or a positioning gap?
- What is the smallest useful step to test this direction?

## Use it thoughtfully

The simulator supports reflection and research; it does not replace qualified career, legal, immigration, financial, medical, or mental-health advice. It does not apply for jobs, message people, make purchases, or publish anything on a user's behalf.

Before sharing career materials with an AI tool, remove personal contact details, identification numbers, health or financial information, and confidential employer or client information. Share only what is needed for the analysis and review the AI tool's privacy and retention settings.

## Project notes

This project was created for a Grace Hopper Celebration session on using AI as a structured thinking partner for career transitions. Grace Hopper Celebration and its organizers are not responsible for this independent project or its outputs unless explicitly stated otherwise.

See [tests/README.md](tests/README.md) for the current manual regression scenarios and their limitations.

## License

[MIT](LICENSE)
