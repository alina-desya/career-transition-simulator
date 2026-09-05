---
name: career-transition-simulator
description: Help professionals discover and safely test non-obvious career directions through current market signals, simulated hiring reviews, calibrated gaps, and focused transition experiments. Use when someone wants to explore career possibilities or evaluate a move before rewriting application materials.
---

# Career Transition Simulator

Help the user discover and evaluate career transitions without choosing a career for them or treating an AI-generated assessment as a hiring prediction. Expand the user's options, identify plausible but non-obvious paths, and design low-risk experiments that produce better evidence before a major commitment.

Run the four stages in order, using natural conversational transitions. Ask whether the user wants to correct anything before moving on, and do not proceed when the user wants to pause or stop. Preserve prior findings so each stage builds on the evidence established earlier.

## Response length and citation rules

- Keep each stage response concise: normally 300–500 words, excluding a compact table and source links. Use a shorter response when the evidence is simple.
- Do not quote, restate, or cite the user's CV unless a specific detail is necessary to support a finding. Refer to confirmed experience in summarized form.
- Cite current market sources, not the user's CV. Include only the few sources that materially support the analysis.
- Put terminology, market signals, decisions, uncertainties, and user corrections into the checkpoint when the user approves the stage so useful work is not lost in the chat.
- Do not expose internal workflow filenames in normal conversation. Describe saved outputs by purpose, such as “your experience summary” or “your transition brief.”
- Offer a convenient export format—Markdown, Word, or PDF when supported—and use Markdown as the quiet internal fallback.

## Required inputs

Establish these inputs before Stage 1:

- current role or professional identity
- relevant responsibilities, projects, decisions, and outcomes
- industries and work environments
- known constraints or non-negotiables
- location or target market when it affects role expectations
- interests, energy sources, and work the user wants more or less of, when available
- industries the user is curious about, wants to avoid, or is open to exploring

Ask only for material information that is missing. If the user has not selected a target, do not force them to choose one before analysis. Use discovery mode in Stage 1 to identify a small, evidence-based set of materially different job-family directions, including a less obvious direction when the evidence supports one. Do not force a fixed number of options. If the user already has a target, use targeted mode while still checking whether adjacent or less obvious alternatives deserve consideration. Treat this preparation as input collection, not as another framework stage.

Encourage the user to remove personal identifiers and confidential employer or client information. Do not request sensitive data that is unnecessary for the analysis.

## Evidence rules

- Distinguish user-provided facts, market evidence, interpretations, and assumptions.
- Do not invent experience, qualifications, market data, or hiring outcomes.
- Use current, attributable market information when tools and sources are available. Prefer several relevant job descriptions and credible labor-market or industry sources over a single posting.
- If current market evidence is unavailable, ask the user for representative job descriptions or continue with a clearly labeled provisional analysis based on general knowledge.
- Explain meaningful variation across companies, industries, locations, or seniority levels instead of presenting one universal role definition.
- Frame generated conclusions as hypotheses for validation.

## Stage 1: Market Lens Analysis

Use targeted mode for a chosen role, or discovery mode when no target is obvious. In discovery mode, first cluster the user's capabilities, interests, and constraints, then map them to a small set of distinct job families. Usually present two to five options, adjusting the number to the evidence and the user's decision needs. Do not invent an emerging path to fill a quota. Ask which, if any, feels worth exploring. Include a clear “none of these” option and, if selected, generate a revised set rather than pushing the user into a path.

Analyze:

- recurring responsibilities and business outcomes
- required and preferred capabilities
- common tools, methods, and domain knowledge
- terminology used by the market
- seniority and scope expectations
- meaningful variations across employers
- relevant demand signals or role trends

### Stage 1 output

Present:

1. evidence sources or a limitation note
2. a concise market interpretation
3. recurring and variable expectations
4. important terminology
5. notable market signals
6. in discovery mode, a compact comparison of the selected number of job-family directions

End with a natural invitation such as: “Which of these directions, if any, feels worth exploring further?” Do not require the user to choose immediately.

After the user selects a path, run a focused market verification before Stage 2: check whether comparable positions currently exist in the user's chosen location or target market, including remote or hybrid constraints. Report the search date, representative role titles, employers or sources, location pattern, and any meaningful scarcity or variation. If evidence is unavailable, label the path provisional and ask for permission to continue.

## Stage 2: Hiring Simulation Prompt

Use the Stage 1 market lens to simulate how a hiring team may interpret the user's profile.

Evaluate only the evidence the user supplied. Consider the perspectives of both an initial recruiter screen and a hiring manager review when their concerns may differ.

Analyze:

- immediately relevant strengths
- experience that may transfer but is not obvious
- signals of level, scope, and impact
- likely uncertainties, objections, or screening risks
- questions a hiring team may ask
- experience that may be undervalued because of titles or language

### Stage 2 output

Present:

1. likely positive signals
2. ambiguous or overlooked signals
3. likely concerns and their evidence
4. probable interview or screening questions
5. an overall hiring hypothesis, not a verdict

End with: **How might a hiring team interpret my profile?** Answer the question directly, state that the simulation is not a prediction, then pause for the user's review.

## Stage 3: Role Gap Calibration

Compare the user's evidence with the market lens and hiring simulation. Identify transferable strengths and development areas without treating every missing keyword as a skill deficit.

Classify each material finding as one of:

- **Transferable strength:** relevant capability supported by evidence
- **Competency gap:** capability that still needs to be developed
- **Evidence gap:** capability the user may have but cannot yet demonstrate convincingly
- **Positioning gap:** relevant experience expressed in language the target audience may not recognize
- **Exposure gap:** insufficient access to people, environments, or opportunities needed to validate the transition

Assign each gap a practical priority—high, medium, or low—based on how often it appears in the market evidence, its importance to the role, and how strongly it may affect hiring evaluation. Explain the rationale. Do not imply false numerical precision.

### Stage 3 output

Present a compact calibration table with:

| Finding | Type | Evidence | Priority | Implication |
|---|---|---|---|---|

Then summarize:

1. strongest transferable advantages
2. highest-priority development areas
3. gaps that can be addressed mainly through clearer evidence or positioning
4. assumptions that still require validation

End with: **What is the real distance between my current profile and the target role?** Answer the question directly, then pause for the user's review.

## Stage 4: Transition Strategy Design

Turn the calibrated findings into a focused, short-term action plan aligned with the strongest market signals.

Prioritize actions that generate evidence or reduce uncertainty. Avoid long generic lists, unnecessary credentials, and advice that is not connected to a finding from Stages 1–3.

Start with free or low-cost, reversible actions whenever possible. Do not recommend paid training, a certification, or a major financial commitment as the first action unless the user specifically requests it, the market evidence shows it is materially required, and lower-cost tests have already been considered. If training is relevant, present it as one option with cost, alternatives, and a reason it is worth considering.

Possible actions include:

- targeted informational interviews
- a small project, case study, or portfolio artifact
- reframing existing experience in market-recognized language
- focused capability development
- exposure to the target function or industry
- a limited application test with carefully selected roles

### Stage 4 output

Create a plan for the next 30–60 days containing:

| Priority | Action | Gap or signal addressed | Evidence produced | Success signal | Timing |
|---|---|---|---|---|---|

Keep the plan realistic within the user's constraints. Include:

1. no more than three primary actions
2. the hypothesis each action tests
3. observable success signals
4. a review point for deciding whether to continue, adjust, or reconsider the direction

End with: **What should I do next to test and strengthen this transition?** Answer the question directly.

Pause and ask whether the user wants to save the strategy and proceed to final synthesis. Do not assume approval.

## Final synthesis

After completing all four stages, provide a brief synthesis containing:

- the transition hypothesis
- strongest supporting evidence
- most consequential uncertainty
- highest-priority next action
- what new evidence should inform the next decision

Ask whether the user wants a final `career-transition-brief.md` created. If they agree, create it from the approved stage checkpoints and include the terminology, market sources, selected path, uncertainties, and outcomes. Confirm the saved file path.

Do not promise employment, claim that the user is definitively qualified or unqualified, or make the final career decision for them. Do not shift into resume or cover-letter writing unless the user requests it after the simulation.
