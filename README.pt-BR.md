<div align="center">

# Wesley Simplicio

### construtor de sistemas de IA · orquestração de agentes · runtimes local-first · automação prática

[![Seguidores](https://img.shields.io/github/followers/wesleysimplicio?style=for-the-badge&color=0f172a)](https://github.com/wesleysimplicio)
[![Visualizações](https://komarev.com/ghpvc/?username=wesleysimplicio&style=for-the-badge&color=0f172a)](https://github.com/wesleysimplicio)
[![Projetos públicos](https://img.shields.io/badge/23-projetos%20públicos%20sem%20fork-0f172a?style=for-the-badge&logo=github)](https://github.com/wesleysimplicio?tab=repositories)
[![Foco](https://img.shields.io/badge/foco-IA%20que%20executa-7C3AED?style=for-the-badge)](https://github.com/wesleysimplicio?tab=repositories)

[English](README.md) · **Português** · [Español](README.es.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Français](README.fr.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [Bahasa Melayu](README.ms.md) · [Bahasa Indonesia](README.id.md)

</div>

---

## A missão

Eu construo sistemas de IA que transformam contexto em execução confiável: agentes que entendem um repositório, runtimes que coordenam modelos e ferramentas, e automações que deixam evidências em vez de apenas mensagens de status.

O objetivo é criar alavancagem prática para pessoas e equipes: menos perda de contexto, menos trabalho repetitivo, automação mais segura e software capaz de avançar da ideia ao resultado verificado.

## O ecossistema Simplicio

Os projetos abaixo são conectados. Cada um resolve um modo diferente de falha no desenvolvimento assistido por IA.

| Projeto | Problema que resolve |
|---|---|
| [**simplicio-loop**](https://github.com/wesleysimplicio/simplicio-loop) · `v3.38.0` | Agentes costumam parar no planejamento ou entregar um patch sem verificação. O orquestrador principal executa **descobrir → implementar → verificar → mergear → acompanhar 24/7**, com gates de segurança, 48 pontos de extensão e qualquer LLM/runtime. |
| **Simplicio Runtime** *(core privado)* | Produtos de agentes duplicam roteamento de modelos, políticas de execução, evidências, recibos e contabilidade de tokens. O runtime compartilhado fornece uma espinha operacional para modelos locais/cloud, agentes e efeitos verificáveis. |
| [**simplicio-agent**](https://github.com/wesleysimplicio/simplicio-agent) · `v2026.7.20` | Agentes autônomos podem agir sem checkpoints duráveis ou trilha de auditoria confiável. Este projeto adiciona ações controladas, checkpoints, recibos de evidência, MCP, skills e liberdade entre modelos. |
| [**simplicio-code**](https://github.com/wesleysimplicio/simplicio-code) | Agentes de código podem se afastar do runtime que deveria executá-los. O Simplicio Code conecta um agente de programação Rust ao Simplicio Runtime. |
| [**simplicio-dev-cli**](https://github.com/wesleysimplicio/simplicio-dev-cli) · `v0.16.1` | Uma tarefa em uma linha não é um processo de entrega. A CLI mapeia contexto, aplica diff revisável, executa testes e produz evidência de validação — com posicionamento de **99% de precisão** entre os principais hosts de LLM. |
| [**simplicio-mapper**](https://github.com/wesleysimplicio/simplicio-mapper) · `v0.23.1` | Agentes começam a programar no escuro quando não têm estrutura e dependências do repositório. O Mapper cria um mapa stack-neutral e um pacote de contexto utilizável desde o primeiro minuto. |
| [**simplicio-loop-marketing**](https://github.com/wesleysimplicio/simplicio-loop-marketing) · `v0.4.0` | Times de marketing ficam presos a um provedor e a ferramentas manuais. O pipeline independente de provedor cobre **briefing → roteiro → criativo → legenda → compliance → publicação → métricas → anúncios**. |
| [**simplicio-local**](https://github.com/wesleysimplicio/simplicio-local) | Inferência cloud pode trazer latência, custo e restrições de privacidade. Este runtime busca inferência **100% no dispositivo** em Apple Silicon usando MLX, Metal e caminhos orientados a ANE. |
| [**simplicio-prompt**](https://github.com/wesleysimplicio/simplicio-prompt) · `v1.14.1` | Sistemas grandes de agentes desperdiçam contexto procurando capacidades. O padrão yool + tuple + HAMT oferece endereçamento preciso, memória estruturada e economia publicada de **75% em tokens**. |
| [**simplicio-sprint**](https://github.com/wesleysimplicio/simplicio-sprint) · `v1.2.14` | Tickets de sprint não carregam automaticamente arquitetura do repositório nem prova de entrega. Esta skill multiagente lê a sprint, mapeia o repo, despacha trabalho e verifica o resultado. |
| [**WaveSpeedAI-Skills**](https://github.com/wesleysimplicio/WaveSpeedAI-Skills) · `v1.2.0` | Equipes de IA reconstroem integrações de provedores repetidamente. Um instalador e uma CLI expõem **700+ modelos** em hosts compatíveis com agentskills.io. |
| [**PiAPI-Skills**](https://github.com/wesleysimplicio/PiAPI-Skills) · `v1.2.0` | Capacidades de geração de mídia ficam fragmentadas entre plataformas. Este bundle portável oferece uma superfície reutilizável para Claude, Codex, Hermes, OpenClaw, Cursor, Windsurf e agentes genéricos. |

### Os números que representam os resultados

- **96%** — economia máxima de tokens publicada pelo projeto do agente de código Simplicio; os números de comparação também foram preservados: **65%** para Caveman e **80%** para RTK.
- **90%** — posicionamento público atual do Simplicio Loop para redução de tokens, junto de **48** pontos de extensão.
- **99%** — posicionamento de precisão publicado pelo Simplicio Dev CLI.
- **75%** — posicionamento de economia de tokens publicado pelo Simplicio Prompt.
- **700+** — modelos suportados pelo WaveSpeedAI Skills.
- **6 skills** e **11 runtimes** — números originais de integração do Loop mantidos na história de compatibilidade do projeto.

São números publicados/posicionados pelos projetos, não uma promessa de que todo workload atingirá o máximo. Os números permanecem visíveis junto da explicação do problema e da engenharia que os sustenta.

## Ranking público atual

Principais repositórios públicos por estrelas, excluindo forks e este repositório de perfil. Snapshot da API do GitHub em **2026-07-22**; badges de estrelas e forks continuam dinâmicos.

| Posição | Projeto | Estrelas | Forks | Papel |
|---:|---|---:|---:|---|
| 1 | [**hermes-turbo-agent**](https://github.com/wesleysimplicio/hermes-turbo-agent) | **17** | **4** | Performance, benchmarks e pesquisa de baixa latência |
| 2 | [**simplicio-local**](https://github.com/wesleysimplicio/simplicio-local) | **14** | **1** | Inferência local em Apple Silicon |
| 3 | [**simplicio-loop**](https://github.com/wesleysimplicio/simplicio-loop) | **12** | **2** | Orquestrador universal de trabalho com IA · flagship |
| 4 | [**simplicio**](https://github.com/wesleysimplicio/simplicio) | **10** | **0** | Runtime de coding agent e execução multiagente |
| 5 | [**simplicio-loop-marketing**](https://github.com/wesleysimplicio/simplicio-loop-marketing) | **7** | **1** | Pipeline de marketing com IA independente de provedor |
| 6 | [**simplicio-mapper**](https://github.com/wesleysimplicio/simplicio-mapper) | **7** | **0** | Mapeamento de repositório e contexto para agentes |
| 7 | [**PiAPI-Skills**](https://github.com/wesleysimplicio/PiAPI-Skills) | **6** | **0** | Skills portáveis para geração de mídia |
| 8 | [**simplicio-prompt**](https://github.com/wesleysimplicio/simplicio-prompt) | **6** | **1** | Endereçamento eficiente de capacidades |
| 9 | [**simplicio-agent**](https://github.com/wesleysimplicio/simplicio-agent) | **4** | **0** | Runtime de agente autônomo controlado |
| 10 | [**simplicio-dev-cli**](https://github.com/wesleysimplicio/simplicio-dev-cli) | **2** | **1** | Execução verificável de tarefa até diff |

## Superfície de engenharia

`Python` · `Rust` · `TypeScript` · `C++` · `Node.js` · `MLX` · `Metal` · `MCP` · `Docker` · `GitHub Actions` · agentes de IA local-first

O trabalho cobre todo o caminho: primitivas de modelo/runtime, mapeamento de repositórios, skills de agentes, mudanças de código verificadas, automação de marketing e distribuição open source.

## Analytics vivos do perfil

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=wesleysimplicio&show_icons=true&theme=tokyonight&hide_border=true&rank_icon=github&include_all_commits=true&count_private=false" alt="Estatísticas públicas do GitHub" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=wesleysimplicio&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" alt="Principais linguagens públicas" />

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=wesleysimplicio&theme=tokyonight" alt="Resumo do perfil no GitHub" width="90%" />

<a href="https://star-history.com/#wesleysimplicio/hermes-turbo-agent&wesleysimplicio/simplicio-local&wesleysimplicio/simplicio-loop&wesleysimplicio/simplicio&wesleysimplicio/simplicio-loop-marketing&wesleysimplicio/simplicio-mapper&wesleysimplicio/PiAPI-Skills&wesleysimplicio/simplicio-prompt&wesleysimplicio/simplicio-agent&wesleysimplicio/simplicio-dev-cli&Date">
  <img src="https://api.star-history.com/svg?repos=wesleysimplicio/hermes-turbo-agent,wesleysimplicio/simplicio-local,wesleysimplicio/simplicio-loop,wesleysimplicio/simplicio,wesleysimplicio/simplicio-loop-marketing,wesleysimplicio/simplicio-mapper,wesleysimplicio/PiAPI-Skills,wesleysimplicio/simplicio-prompt,wesleysimplicio/simplicio-agent,wesleysimplicio/simplicio-dev-cli&type=Date&theme=dark" alt="Histórico de estrelas do top 10" width="90%" />
</a>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=wesleysimplicio&theme=tokyo-night&hide_border=true&area=true&custom_title=Atividade%20de%20contribuição" alt="Gráfico de atividade" width="90%" />

</div>

> Ranking e contagens atualizados pela API pública do GitHub em 2026-07-22. Cards e badges são widgets vivos. Contagem de clones e downloads de releases não foi incluída porque a Traffic API do GitHub exige acesso autenticado.

## Conecte-se

- GitHub: [@wesleysimplicio](https://github.com/wesleysimplicio)
- X: [@wesleysimplic](https://x.com/wesleysimplic)
- LinkedIn: [wesleysimplicio](https://br.linkedin.com/in/wesleysimplicio)
- YouTube: [@wesleysimplicio](https://www.youtube.com/@wesleysimplicio)

<div align="center">

### Transformando ideias de IA em sistemas que executam.

</div>
