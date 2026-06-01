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

---

# PRD Addendum - Multilingual README Expansion

## Objective

Provide the GitHub profile README in the requested languages while keeping the canonical project links, public images, star ranking, and Star History consistent across every language file.

## Required Languages

- [x] English (`README.md`)
- [x] Portuguese (`README.pt-BR.md`)
- [x] Spanish (`README.es.md`)
- [x] Japanese (`README.ja.md`)
- [x] Korean (`README.ko.md`)
- [x] Simplified Chinese (`README.zh-CN.md`)
- [x] Italian (`README.it.md`)
- [x] French (`README.fr.md`)
- [x] Russian (`README.ru.md`)
- [x] Polish (`README.pl.md`)
- [x] Hindi (`README.hi.md`)
- [x] Arabic (`README.ar.md`)
- [x] Hebrew (`README.he.md`)
- [x] Malay (`README.ms.md`)
- [x] Indonesian (`README.id.md`)

## Requirements

- [x] Add a language selector to every README file.
- [x] Preserve the same repository cards, public images, analytics blocks, and Star History repositories across languages.
- [x] Update the public star ranking from the current GitHub public API snapshot.
- [x] Avoid embedding broken public image services.

## Validation Commands

```bash
simplicio-mapper index . --json
taskflow inspect .
git diff --check -- README*.md
curl -L -s -o /dev/null -w '%{http_code}' <embedded-image-url>
taskflow run .
```
