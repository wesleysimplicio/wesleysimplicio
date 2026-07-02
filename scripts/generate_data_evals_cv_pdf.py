from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUT_PDF = "Wesley_Simplicio_CV_Data_Evaluations_Engineer.pdf"


def bullet_list(items, style, left_indent=12):
    flow = []
    for item in items:
        flow.append(ListItem(Paragraph(item, style)))
    return ListFlowable(
        flow,
        bulletType="bullet",
        start="circle",
        leftIndent=left_indent,
        bulletFontName="Helvetica",
        bulletFontSize=7,
    )


def p(text, style):
    return Paragraph(text, style)


def section(title, body, title_style, body_style):
    return [Paragraph(title.upper(), title_style), Spacer(1, 3), body, Spacer(1, 7)]


def main():
    doc = SimpleDocTemplate(
        OUT_PDF,
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=15 * mm,
        bottomMargin=14 * mm,
    )
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "Title",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=23,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#132238"),
        spaceAfter=2,
    )
    role_style = ParagraphStyle(
        "Role",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#0F5BD8"),
        spaceAfter=5,
    )
    contact_style = ParagraphStyle(
        "Contact",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.7,
        leading=10.5,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#566579"),
        spaceAfter=2,
    )
    section_title = ParagraphStyle(
        "SectionTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9.3,
        leading=11,
        textColor=colors.HexColor("#132238"),
        spaceBefore=2,
        spaceAfter=1,
        borderPadding=0,
        borderWidth=0,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.4,
        leading=11.5,
        textColor=colors.HexColor("#132238"),
        spaceAfter=5,
    )
    bullet_style = ParagraphStyle(
        "Bullet",
        parent=body_style,
        fontSize=9.2,
        leading=11.2,
        leftIndent=0,
        spaceAfter=2,
    )
    small_head = ParagraphStyle(
        "SmallHead",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9.5,
        leading=11,
        textColor=colors.HexColor("#132238"),
        spaceBefore=2,
        spaceAfter=2,
    )
    blue_role = ParagraphStyle(
        "BlueRole",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8.9,
        leading=10.4,
        textColor=colors.HexColor("#0F5BD8"),
        spaceAfter=2,
    )
    muted_style = ParagraphStyle(
        "Muted",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.4,
        leading=10,
        textColor=colors.HexColor("#566579"),
        spaceAfter=3,
    )

    story = []

    hero = Table(
        [[
            [
                Paragraph("WESLEY SIMPLICIO", title_style),
                Paragraph("Data/Evaluations Engineer | AI Agents | Evaluation Systems | Runtime Reliability", role_style),
                Paragraph("Guarulhos, Sao Paulo, Brazil  |  +55 11 94669-4305  |  wesleysimplicio@live.com", contact_style),
                Paragraph("GitHub: github.com/Wesleysimplicio  |  LinkedIn: br.linkedin.com/in/wesleysimplicio", contact_style),
            ]
        ]],
        colWidths=[178 * mm],
    )
    hero.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 1.2, colors.HexColor("#132238")),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    story.append(hero)
    story.append(Spacer(1, 10))

    summary = [
        p(
            "Senior Full Stack Engineer with 10+ years of experience building production systems across finance, healthcare, retail, and enterprise software. Strong background in distributed systems, cloud infrastructure, automated testing, CI/CD, messaging, and software architecture for reliable and scalable applications.",
            body_style,
        ),
        p(
            "Over the last year, I have worked deeply with AI agent engineering, repository-scale automation, evaluation-oriented workflows, and runtime tooling. My focus includes multi-agent orchestration, plan-first execution, validation loops, controlled write scopes, architecture-aware code generation, and operational guardrails across Claude Code, Codex, Cursor, GitHub Copilot, Hermes Agent, and OpenClaw.",
            body_style,
        ),
        p(
            "I am especially interested in evaluation systems, failure analysis, runtime predictability, automated and human review loops, and the tooling needed to make agent behavior measurable and improvable at scale.",
            body_style,
        ),
    ]
    story += section("Professional Summary", summary[0], section_title, body_style)
    story += summary[1:]

    highlights_box = Table(
        [[
            [
                Paragraph("Hermes Agent Runtime and Quality Improvements", small_head),
                Paragraph(
                    "Contributed directly to Hermes Agent runtime quality, CI structure, and prompt assembly behavior, including work that improves determinism, stability, and future cache-aware execution.",
                    body_style,
                ),
            ]
        ]],
        colWidths=[178 * mm],
    )
    highlights_box.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.9, colors.HexColor("#CDDDFF")),
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E9F1FF")),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    story.append(Paragraph("EVALUATION AND AGENT ENGINEERING HIGHLIGHTS", section_title))
    story.append(Spacer(1, 3))
    story.append(highlights_box)
    story.append(Spacer(1, 6))
    story.append(
        bullet_list(
            [
                "Active contributor to the Hermes Agent ecosystem with more than 152 PRs opened in 24 hours, spanning bug fixes, runtime quality, workflow improvements, and test/CI infrastructure.",
                "Designed and implemented a provider-agnostic stable context prefix builder for Hermes Agent with deterministic ordering, stable hashing, structured segment modeling, and XML-like rendering.",
                "Built and maintained AI-friendly starter structures for multi-agent project bootstrap, standardized execution, documentation, and architecture-aware onboarding.",
                "Worked with repository-wide changes, controlled automation, validation-first workflows, read/write constraints, and repeatable instruction layers to reduce regressions and improve delivery quality.",
                "Standardized agent behavior across multiple CLIs and model providers to improve repeatability, safety, and operational consistency.",
            ],
            bullet_style,
        )
    )
    story.append(Spacer(1, 8))

    story.append(Paragraph("SELECTED OPEN SOURCE WORK", section_title))
    story.append(Spacer(1, 3))
    story.append(Paragraph("Hermes Agent Contributions", small_head))
    story.append(
        bullet_list(
            [
                "<b>PR #23479 - feat(runtime): add stable context prefix builder.</b> Implemented a provider-agnostic StableContextBuilder to support stable and dynamic prompt assembly, future prefix caching, and more predictable runtime behavior.",
                "<b>151 PRs created for Hermes Agent in 24 hours.</b> Contributed a high-volume stream of fixes and improvements across runtime quality, workflow consistency, validation, and developer experience.",
            ],
            bullet_style,
        )
    )
    story.append(Spacer(1, 4))
    story.append(Paragraph("Agentic Starter", small_head))
    story.append(
        p(
            "AI-friendly, stack-neutral starter pack for multi-agent project bootstrap. Designed to standardize handoff, execution flow, documentation structure, instruction layers, and controlled agent operation across Claude Code, Codex, Copilot, Cursor, Hermes Agent, OpenClaw, and similar environments.",
            body_style,
        )
    )
    story.append(Paragraph("Other AI Projects", small_head))
    story.append(
        bullet_list(
            [
                "PiAPI-Skills / WaveSpeedAI-Skills - reusable skill packs with support for 700+ models.",
                "SendSprint - structured multi-agent sprint automation workflow.",
            ],
            bullet_style,
        )
    )
    story.append(Spacer(1, 8))

    story.append(Paragraph("BEST MATCH FOR DATA/EVALS WORK", section_title))
    story.append(Spacer(1, 3))
    story.append(
        bullet_list(
            [
                "Strong experience with automated validation, CI pipelines, test reliability, and regression-resistant workflows.",
                "Hands-on work with failure reduction, deterministic runtime behavior, and measurable quality improvements in agent systems.",
                "Comfortable designing processes that combine automation and human review.",
                "Track record of OSS contributions and shipping practical improvements in active AI-agent codebases.",
            ],
            bullet_style,
        )
    )
    story.append(Spacer(1, 8))

    story.append(Paragraph("CORE TECHNICAL STRENGTHS", section_title))
    story.append(Spacer(1, 3))
    strengths = [
        "Evaluation workflows and validation systems",
        "Failure analysis and runtime reliability",
        "Controlled automation and review loops",
        "Distributed systems and microservices",
        "RabbitMQ, Kafka, AWS SQS, Azure Service Bus",
        "AWS and Azure cloud infrastructure",
        "CI/CD and automated testing",
        "xUnit, NUnit, Moq, TestContainers",
        "C#, .NET Core, Entity Framework, Dapper, Web API",
        "Angular, React, Vue.js, JavaScript, HTML5, CSS3",
        "DDD, Hexagonal Architecture, event-driven systems",
        "SQL Server, PostgreSQL, MySQL, Oracle, MongoDB",
    ]
    story.append(bullet_list(strengths, bullet_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_title))
    story.append(Spacer(1, 3))

    experiences = [
        ("Banco Fibra | Oct 2025 - Feb 2026", "Senior Full Stack .NET / React Developer", [
            "Worked on modernization efforts migrating legacy systems into microservices and micro frontend architectures.",
            "Delivered improvements and fixes in .NET and React applications while preserving architecture and operational reliability.",
            "Used AI-assisted workflows to coordinate frontend and backend delivery under controlled execution constraints.",
        ]),
        ("EY | Jan 2025 - Oct 2025", "Senior Full Stack Developer (.NET Core 9 / Angular 19)", [
            "Improved internal workflow and enterprise process systems using .NET Core, Angular, Azure, and Entity Framework.",
            "Worked with CI/CD, Git Flow, Scrum, and automated testing in process-heavy enterprise environments.",
        ]),
        ("Banco BMG | Jan 2024 - Dec 2024", "Senior Full Stack Developer (.NET Core 8 / Angular)", [
            "Built and improved PIX-related systems aligned with Brazilian Central Bank requirements.",
            "Worked with AWS, RabbitMQ, Kafka, Entity Framework, and Hexagonal Architecture on reliable regulated systems.",
        ]),
        ("IOB | Jan 2022 - Dec 2023", "Senior Full Stack Developer (.NET Core 8 / React / Angular)", [
            "Maintained and evolved product features with strong attention to process improvement, stability, and scalable delivery.",
            "Worked with AWS, SQS, CI/CD, DDD, and Hexagonal Architecture.",
        ]),
        ("Earlier Experience | 2016 - 2021", "Fast Shop, United Health Group / Amil, and TIVIT", [
            "Built enterprise systems using .NET, Angular, React, Azure Functions, Azure Service Bus, MongoDB, PostgreSQL, SQL Server, and microservices.",
            "Integrated enterprise systems with SAP and Microsiga while maintaining operational reliability across corporate environments.",
        ]),
    ]
    for title, role, bullets in experiences:
        story.append(Paragraph(title, small_head))
        story.append(Paragraph(role, blue_role))
        story.append(bullet_list(bullets, bullet_style))
        story.append(Spacer(1, 4))

    story.append(Paragraph("AI ECOSYSTEM EXPOSURE", section_title))
    story.append(Spacer(1, 3))
    story.append(
        p(
            "Hands-on with Claude, GPT, Gemini, Grok, Kimi, GLM, MiniMax, Hermes Agent, Codex, Cursor, GitHub Copilot, and OpenClaw, with a focus on operational quality, predictability, and agent workflow standardization.",
            body_style,
        )
    )

    story.append(Paragraph("EDUCATION", section_title))
    story.append(Spacer(1, 3))
    story.append(Paragraph("Bachelor's Degree in Systems Analysis and Development", small_head))
    story.append(Paragraph("ENIAC - Completed Dec 2014", muted_style))
    story.append(Paragraph("Technical Degree in Information Technology", small_head))
    story.append(Paragraph("ETEC Horacio", muted_style))
    story.append(Paragraph("Additional coursework", small_head))
    story.append(Paragraph("Web Design - Senac", muted_style))

    story.append(Paragraph("LINKS", section_title))
    story.append(Spacer(1, 3))
    story.append(Paragraph("GitHub: github.com/Wesleysimplicio", body_style))
    story.append(Paragraph("LinkedIn: br.linkedin.com/in/wesleysimplicio", body_style))
    story.append(Paragraph("Highlighted Hermes PR: github.com/NousResearch/hermes-agent/pull/23479", body_style))

    doc.build(story)


if __name__ == "__main__":
    main()
