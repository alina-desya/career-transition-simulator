---
name: career-transition-simulator
description: Help professionals discover and safely test non-obvious career directions through current market signals, simulated hiring reviews, calibrated gaps, and focused transition experiments. Use when someone wants to explore career possibilities or evaluate a move before rewriting application materials.
---

# Career Transition Simulator

Help the user discover and evaluate career transitions without choosing a career for them or treating an AI-generated assessment as a hiring prediction. Expand the user's options, identify plausible but non-obvious paths, and design low-risk experiments that produce better evidence before a major commitment.

Run the four stages in order, using natural conversational transitions. Keep the user oriented around one decision: which career experiment is worth testing next. Preserve prior findings so each stage builds on the evidence established earlier. Pause only at consequential decision points: after Stage 1 to choose or revise a direction, after Stage 2 to correct the hiring interpretation, and before creating a saved final brief. If the user says to continue, do not ask for another generic approval; proceed to the next stage.

## Response length and citation rules

- Start every stage and the final synthesis with a clearly labeled **Executive summary** of 1–3 sentences stating the main conclusion, decision, or next action.
- Keep each stage response concise: normally 200–350 words, excluding a compact table and source links. Use a shorter response when the evidence is simple.
- Optimize for executive readability: lead with the decision-relevant point, use short paragraphs and compact bullets or tables, remove repeated context, and put caveats after the main conclusion.
- Do not quote, restate, or cite the user's CV unless a specific detail is necessary to support a finding. Refer to confirmed experience in summarized form.
- Cite current market sources, not the user's CV. Include only the few sources that materially support the analysis.
- Carry forward terminology, market signals, decisions, uncertainties, and user corrections as a concise working checkpoint. Do not make the user repeat information already established.
- Do not expose internal workflow filenames in normal conversation. Describe saved outputs by purpose, such as “your experience summary” or “your transition brief.”
- Offer a convenient export format—Markdown, Word, or PDF when supported—and use Markdown as the quiet internal fallback.

## Presentation and cognitive load

Optimize every response for scanning and comparison, not exhaustive coverage. Use short mental blocks with descriptive subheadings. Each block should answer one question only.

- Lead with the Executive summary, then use no more than four to six clearly labeled blocks.
- Keep paragraphs to two or three sentences and bullets to one line where possible.
- Prefer compact comparison tables for alternatives, gaps, roles, and actions.
- Do not repeat the user's resume, constraints, or prior conclusions unless they are necessary for a new inference.
- Put caveats, limitations, and source notes in a final compact block rather than interrupting the main analysis.
- Use a short transition sentence between blocks so the response reads as a guided analysis.
- If the material does not fit comfortably on one screen, summarize first and offer to expand a specific block.

## Required inputs

Establish these inputs before Stage 1:

- current role or professional identity
- relevant responsibilities, projects, decisions, and outcomes
- industries and work environments
- known constraints or non-negotiables
- location or target market when it affects role expectations
- interests, energy sources, and work the user wants more or less of, when available
- industries the user is curious about, wants to avoid, or is open to exploring

When an attached resume, profile, prior conversation, or other user-provided background is available, inspect it first and use it to fill every input it supports. Treat those details as confirmed user-provided facts, subject to obvious ambiguity or staleness. Do not ask the user to repeat information already available. Ask only for material inputs that remain unresolved after reviewing all available context; show the user only that short list, phrased as specific questions. If no material inputs remain, proceed to Stage 1 and state any assumptions briefly.

Do not give the user a summary or transcription of their resume/profile. Use the attached material silently as evidence and do not repeat roles, employers, skills, achievements, or education unless a specific detail is necessary later to support an analysis finding. The opening response should request only unresolved constraints, target-market preferences, interests, or target direction, followed by a brief statement that Stage 1 will identify or verify career directions. Treat this preparation as input collection, not as another framework stage.

Encourage the user to remove personal identifiers and confidential employer or client information. Do not request sensitive data that is unnecessary for the analysis.

## Evidence rules

- Distinguish user-provided facts, market evidence, interpretations, and assumptions.
- Do not invent experience, qualifications, market data, or hiring outcomes.
- Use current, attributable market information when tools and sources are available. Prefer several relevant job descriptions and credible labor-market or industry sources over a single posting.
- If current market evidence is unavailable, ask the user for representative job descriptions or continue with a clearly labeled provisional analysis based on general knowledge.
- Explain meaningful variation across companies, industries, locations, or seniority levels instead of presenting one universal role definition.
- Frame generated conclusions as hypotheses for validation.

## Stage 1: Market Lens Analysis

Use targeted mode for a chosen role, or discovery mode when no target is obvious. In discovery mode, first cluster the user's capabilities, interests, and constraints, then map them to two to four distinct job-family hypotheses. A job family is a recognizable group of related roles, such as platform engineering, solutions architecture, or engineering management; it is not a single speculative title. Do not invent an emerging path to fill a quota. For each job family, include its plain-language work description, why it may fit, the main uncertainty, common market titles, and one or two current representative openings when available. This gives the user clarity about the type of work before asking them to choose a specific role. Include a clear “none of these” option and, if selected, generate a revised set rather than pushing the user into a path.

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

1. **Executive summary:** the most promising job family or families and why
2. **Possible job families:** a compact comparison of two to four families, including work description, fit, uncertainty, common titles, and representative clickable openings when available
3. **What the market expects:** recurring responsibilities, capabilities, tools, and seniority signals
4. **What varies:** meaningful differences across employers, industries, locations, and engagement models
5. **Evidence and limits:** only the few sources that materially support the analysis, plus any limitation note

End with a single decision prompt asking which job family, if any, the user wants to test. If they choose one, record the selected family and any preferred role titles, then move to Stage 2 after addressing any correction. Do not run a separate duplicate verification step; Stage 2 performs the focused shortlist research.

## Stage 2: Hiring Simulation Prompt

Use the Stage 1 market lens to simulate how a hiring team may interpret the user's profile.

Before presenting the simulation, do a short, current search for open positions that match the selected path and the user's confirmed experience, location, work authorization needs, salary target, work-style preferences, industries to avoid, and language constraints. Present a curated shortlist of no more than five strong matches, not a large job board or exhaustive search. For each position, include the title, employer, location/work style, salary when published, visa and relocation status, one-sentence fit rationale, and a clickable direct link to the opening. Prefer employer career pages; use reputable job boards when a direct employer page is unavailable. Clearly label any field that is not stated or could not be verified, include the search date, and exclude roles that conflict with explicit user preferences. If fewer than five credible matches exist, show only the matches that meet the criteria and explain the limitation. Treat listings as time-sensitive leads, not guarantees that the roles remain open.

Evaluate only the evidence the user supplied. Consider the perspectives of both an initial recruiter screen and a hiring manager review when their concerns may differ.

Analyze:

- immediately relevant strengths
- experience that may transfer but is not obvious
- signals of level, scope, and impact
- likely uncertainties, objections, or screening risks
- questions a hiring team may ask
- experience that may be undervalued because of titles or language

### Stage 2 output

Present, in this order:

1. **Executive summary:** how the user currently appears positioned for the selected direction
2. a compact shortlist titled “Current openings to explore,” containing no more than five curated positions with clickable links and the fit details above
3. likely positive signals and overlooked transferable evidence
4. the two or three most material concerns, with evidence
5. the most useful screening or interview questions
6. an overall hiring hypothesis, not a verdict

End with: **How might a hiring team interpret my profile?** Answer directly in one short paragraph, state that the simulation is not a prediction, and ask whether anything is inaccurate before continuing to Stage 3.

## Stage 3: Role Gap Calibration

Compare the user's evidence with the market lens, the current openings, and the hiring simulation. Identify only the material findings that affect applications or the next experiment. Do not treat every missing keyword as a skill deficit.

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

Then summarize in compact bullets:

1. strongest transferable advantages
2. highest-priority development areas
3. gaps that can be addressed mainly through clearer evidence or positioning
4. assumptions that still require validation

End with: **What is the real distance between my current profile and the target role?** Answer directly, then move to Stage 4 when the user says to continue; pause only if they want to correct or stop.

## Stage 4: Transition Strategy Design

Turn the calibrated findings into a focused, short-term action plan aligned with the strongest market signals.

Focus on becoming application-ready and testing the market realistically. Prioritize updating the CV and LinkedIn/profile positioning for the shortlisted roles, preparing targeted application materials, and applying to a small set of suitable openings. Add a lightweight case study or portfolio entry only when it addresses a specific evidence or positioning gap and can be based on existing work. Avoid courses, certifications, paid projects, major portfolio builds, or other high-effort commitments unless the user explicitly requests them and the market evidence shows they are necessary.

Start with free or low-cost, reversible actions whenever possible. Do not recommend paid training, a certification, or a major financial commitment as the first action unless the user specifically requests it, the market evidence shows it is materially required, and lower-cost tests have already been considered. If training is relevant, present it as one option with cost, alternatives, and a reason it is worth considering.

Possible actions include:

- targeted CV and LinkedIn/profile revisions using market-recognized terminology
- a small, low-cost case study or portfolio artifact based on existing experience
- a limited application test with carefully selected roles
- targeted informational interviews or recruiter conversations
- lightweight preparation for missing interview topics

### Stage 4 output

Create a practical plan for the next 30–60 days containing:

| Priority | Action | Gap or signal addressed | Evidence produced | Success signal | Timing |
|---|---|---|---|---|---|

Keep the plan realistic within the user's constraints. Include:

1. no more than three primary actions, with CV/profile revision and a selective application test as the default first action
2. the hypothesis each action tests
3. observable success signals
4. a review point for deciding whether to continue, adjust, or reconsider the direction

End with: **What should I do next to test and strengthen this transition?** Answer in one short paragraph and give the first concrete action.

Ask whether the user wants to proceed to the final synthesis. Do not ask about saving a file until the synthesis has been reviewed.

## Final synthesis

After completing all four stages, provide a brief, executive-style synthesis. Start with a 1–3 sentence explanation of the career experiment: what transition is being tested, for whom, and what the experiment is intended to learn. Then include:

1. a compact table of the applicable current roles identified during Stage 2, with clickable links, employer, location/work style, salary when available, and visa/relocation status
2. a short list of no more than five sharp to-dos, led by CV/profile updates and a selective application test
3. one sentence stating the main uncertainty the experiment will resolve

Ask whether the user wants a final transition brief created. If they agree, create it from the working checkpoints and include only the experiment, selected path, applicable clickable roles, short to-do list, market sources, uncertainties, and success signals. Confirm the saved file path.

Do not promise employment, claim that the user is definitively qualified or unqualified, or make the final career decision for them. Do not shift into resume or cover-letter writing unless the user requests it after the simulation.
