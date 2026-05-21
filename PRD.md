# PRD - GitHub Profile README Refresh

## Objective

Improve the GitHub profile README for `wesleysimplicio` so it presents Wesley Simplicio as an AI systems builder, highlights the most important repositories, embeds images from those project READMEs, and links directly to each repository.

## Context

The profile repository is `wesleysimplicio/wesleysimplicio`. The current README already introduces the profile, but it does not prominently feature `simplicio-prompt`, `llm-project-mapper`, `us4-v6-simplicio-apple`, or the broader AI tooling and runtime work with project images.

## Requirements

- [x] Highlight `simplicio-prompt`, `llm-project-mapper`, and `us4-v6-simplicio-apple`.
- [x] Include other relevant repositories from the current public repo set.
- [x] Add images sourced from project READMEs where public assets are available.
- [x] Link every featured project to its GitHub repository.
- [x] Include a mission statement about contributing to humanity through AI work.
- [x] Include a clear recognition signal for impactful work and opportunities with a great company.
- [x] Keep the README suitable for a public GitHub profile.

## Non-Goals

The agent must not:

- expose private repository assets in the public README
- push to remote without explicit instruction
- remove agent process files
- add unrelated dependencies or tooling

## Technical Notes

Relevant files:

```text
README.md
PROGRESS.md
GOAL_RESULT.md
```

## Validation Commands

```bash
git diff --check
Invoke-WebRequest -Method Head for every embedded raw README image
```

## Done When

- [x] README is updated
- [x] Embedded image URLs return HTTP 200
- [x] Local diff validation passes
- [x] Tuple-space task routing flow completes
- [x] GOAL_RESULT.md is written
