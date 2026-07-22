<div align="center">

# Wesley Simplicio

### AI systems builder · agent orchestration · local-first runtimes · practical automation

[![GitHub followers](https://img.shields.io/github/followers/wesleysimplicio?style=for-the-badge&color=0f172a)](https://github.com/wesleysimplicio)
[![Profile views](https://komarev.com/ghpvc/?username=wesleysimplicio&style=for-the-badge&color=0f172a)](https://github.com/wesleysimplicio)
[![Open source projects](https://img.shields.io/badge/23-public%20non--fork%20projects-0f172a?style=for-the-badge&logo=github)](https://github.com/wesleysimplicio?tab=repositories)
[![Focus](https://img.shields.io/badge/focus-AI%20that%20executes-7C3AED?style=for-the-badge)](https://github.com/wesleysimplicio?tab=repositories)

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Français](README.fr.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [Bahasa Melayu](README.ms.md) · [Bahasa Indonesia](README.id.md)

</div>

---

## The mission

I build AI systems that turn context into reliable execution: agents that can understand a repository, runtimes that can coordinate models and tools, and automation that leaves behind evidence instead of vague status messages.

The goal is practical leverage for people and teams: less context loss, less repetitive work, safer automation, and software that can keep moving from idea to verified result.

## The Simplicio ecosystem

The projects below are connected. Each one attacks a different failure mode in modern AI-assisted work.

| Project | What problem it solves |
|---|---|
| [**simplicio-loop**](https://github.com/wesleysimplicio/simplicio-loop) · `v3.38.0` | AI agents often stop at planning or produce an unverified patch. The flagship orchestrator drives **discover → implement → verify → merge → watch 24/7**, with safety gates, 48 extension points, and any LLM/runtime. |
| **Simplicio Runtime** *(private core)* | Agent products otherwise duplicate model routing, execution policy, evidence, receipts, and token accounting. The shared runtime provides one operational spine for local/cloud models, agents, and verifiable effects. |
| [**simplicio-agent**](https://github.com/wesleysimplicio/simplicio-agent) · `v2026.7.20` | Autonomous agents can act without durable checkpoints or a trustworthy audit trail. This project adds gated actions, checkpoints, evidence receipts, MCP, skills, and multi-model freedom. |
| [**simplicio-code**](https://github.com/wesleysimplicio/simplicio-code) | Coding agents frequently drift from the runtime that is supposed to execute them. Simplicio Code connects a Rust coding agent to the Simplicio Runtime. |
| [**simplicio-dev-cli**](https://github.com/wesleysimplicio/simplicio-dev-cli) · `v0.16.1` | A one-line task is not a delivery process. The CLI maps context, applies a reviewable diff, runs tests, and emits validation evidence — positioned around **99% accuracy** across major LLM hosts. |
| [**simplicio-mapper**](https://github.com/wesleysimplicio/simplicio-mapper) · `v0.23.1` | Agents begin coding blind when they lack repository structure and dependency context. Mapper creates a stack-neutral project map and a usable context pack from minute one. |
| [**simplicio-loop-marketing**](https://github.com/wesleysimplicio/simplicio-loop-marketing) · `v0.4.0` | Marketing teams get locked into one model provider and a chain of manual tools. This provider-agnostic pipeline covers **brief → script → creative → caption → compliance → publish → metrics → ads**. |
| [**simplicio-local**](https://github.com/wesleysimplicio/simplicio-local) | Cloud inference can add latency, cost, and privacy constraints. This Apple Silicon runtime targets **100% on-device** inference with MLX, Metal, and ANE-oriented paths. |
| [**simplicio-prompt**](https://github.com/wesleysimplicio/simplicio-prompt) · `v1.14.1` | Large agent systems waste context searching for capabilities. The yool + tuple + HAMT pattern provides precise addressing, structured memory, and a reported **75% token economy**. |
| [**simplicio-sprint**](https://github.com/wesleysimplicio/simplicio-sprint) · `v1.2.14` | Sprint tickets do not automatically carry repository architecture or delivery proof. This multi-agent skill reads the sprint, maps the repo, dispatches work, and verifies the result. |
| [**WaveSpeedAI-Skills**](https://github.com/wesleysimplicio/WaveSpeedAI-Skills) · `v1.2.0` | AI teams repeatedly rebuild provider integrations. One installer and CLI exposes **700+ models** across agentskills.io-compatible hosts. |
| [**PiAPI-Skills**](https://github.com/wesleysimplicio/PiAPI-Skills) · `v1.2.0` | Media-generation capabilities are fragmented across agent platforms. This portable skill bundle gives Claude, Codex, Hermes, OpenClaw, Cursor, Windsurf, and generic agents one reusable surface. |

### The numbers I keep visible

- **96%** — maximum token savings reported by the Simplicio coding-agent project; the profile also preserves the comparison figures **65%** for Caveman and **80%** for RTK.
- **90%** — current public positioning for Simplicio Loop's token reduction, alongside **48** extension points.
- **99%** — accuracy positioning published by Simplicio Dev CLI.
- **75%** — token-economy positioning published by Simplicio Prompt.
- **700+** — models supported by WaveSpeedAI Skills.
- **6 skills** and **11 runtimes** — the original Loop integration numbers retained as part of the project's compatibility story.

These are project-reported positioning/results, not a claim that every workload reaches the maximum. The goal is to keep the numbers visible while making the problem and the engineering behind each result clear.

## Current public ranking

Top public repositories by stars, excluding forks and this profile repository. Snapshot from the GitHub API on **2026-07-22**; star and fork badges remain live.

| Rank | Project | Stars | Forks | Role |
|---:|---|---:|---:|---|
| 1 | [**hermes-turbo-agent**](https://github.com/wesleysimplicio/hermes-turbo-agent) | **17** | **4** | Agent performance, benchmarks, and low-latency research |
| 2 | [**simplicio-local**](https://github.com/wesleysimplicio/simplicio-local) | **14** | **1** | Apple Silicon on-device inference |
| 3 | [**simplicio-loop**](https://github.com/wesleysimplicio/simplicio-loop) | **12** | **2** | Universal AI work orchestrator · flagship |
| 4 | [**simplicio**](https://github.com/wesleysimplicio/simplicio) | **10** | **0** | Coding-agent runtime and multi-agent execution |
| 5 | [**simplicio-loop-marketing**](https://github.com/wesleysimplicio/simplicio-loop-marketing) | **7** | **1** | Provider-agnostic AI marketing pipeline |
| 6 | [**simplicio-mapper**](https://github.com/wesleysimplicio/simplicio-mapper) | **7** | **0** | Repository mapping and agent context |
| 7 | [**PiAPI-Skills**](https://github.com/wesleysimplicio/PiAPI-Skills) | **6** | **0** | Portable AI media-generation skills |
| 8 | [**simplicio-prompt**](https://github.com/wesleysimplicio/simplicio-prompt) | **6** | **1** | Efficient capability addressing for agents |
| 9 | [**simplicio-agent**](https://github.com/wesleysimplicio/simplicio-agent) | **4** | **0** | Gated autonomous agent runtime |
| 10 | [**simplicio-dev-cli**](https://github.com/wesleysimplicio/simplicio-dev-cli) | **2** | **1** | Verified task-to-diff execution |

<div align="center">

![Simplicio Loop stars](https://img.shields.io/github/stars/wesleysimplicio/simplicio-loop?style=for-the-badge&logo=github&label=simplicio-loop%20stars&color=7C3AED)
![Simplicio Local stars](https://img.shields.io/github/stars/wesleysimplicio/simplicio-local?style=for-the-badge&logo=github&label=simplicio-local%20stars&color=facc15)
![Simplicio Agent stars](https://img.shields.io/github/stars/wesleysimplicio/simplicio-agent?style=for-the-badge&logo=github&label=simplicio-agent%20stars&color=38bdf8)

</div>

## Engineering surface

`Python` · `Rust` · `TypeScript` · `C++` · `Node.js` · `MLX` · `Metal` · `MCP` · `Docker` · `GitHub Actions` · local-first AI agents

The work spans the full path from model/runtime primitives to repository mapping, agent skills, verified code changes, marketing automation, and open-source distribution.

## Live profile analytics

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=wesleysimplicio&show_icons=true&theme=tokyonight&hide_border=true&rank_icon=github&include_all_commits=true&count_private=false" alt="GitHub public statistics" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=wesleysimplicio&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" alt="Top public languages" />

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=wesleysimplicio&theme=tokyonight" alt="GitHub profile details" width="90%" />

<a href="https://star-history.com/#wesleysimplicio/hermes-turbo-agent&wesleysimplicio/simplicio-local&wesleysimplicio/simplicio-loop&wesleysimplicio/simplicio&wesleysimplicio/simplicio-loop-marketing&wesleysimplicio/simplicio-mapper&wesleysimplicio/PiAPI-Skills&wesleysimplicio/simplicio-prompt&wesleysimplicio/simplicio-agent&wesleysimplicio/simplicio-dev-cli&Date">
  <img src="https://api.star-history.com/svg?repos=wesleysimplicio/hermes-turbo-agent,wesleysimplicio/simplicio-local,wesleysimplicio/simplicio-loop,wesleysimplicio/simplicio,wesleysimplicio/simplicio-loop-marketing,wesleysimplicio/simplicio-mapper,wesleysimplicio/PiAPI-Skills,wesleysimplicio/simplicio-prompt,wesleysimplicio/simplicio-agent,wesleysimplicio/simplicio-dev-cli&type=Date&theme=dark" alt="Star history across the current top ten" width="90%" />
</a>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=wesleysimplicio&theme=tokyo-night&hide_border=true&area=true&custom_title=Contribution%20activity" alt="Contribution activity graph" width="90%" />

</div>

> Ranking and counts above were refreshed from the public GitHub API on 2026-07-22. GitHub profile cards and badges are live widgets. Clone counts and release-download counts are not included because GitHub's Traffic API requires authenticated access.

## Connect

- GitHub: [@wesleysimplicio](https://github.com/wesleysimplicio)
- X: [@wesleysimplic](https://x.com/wesleysimplic)
- LinkedIn: [wesleysimplicio](https://br.linkedin.com/in/wesleysimplicio)
- YouTube: [@wesleysimplicio](https://www.youtube.com/@wesleysimplicio)

<div align="center">

### Turning AI ideas into systems that execute.

</div>
