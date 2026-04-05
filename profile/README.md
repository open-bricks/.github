<p align="center">
  <img src="open-bricks-banner.png" alt="open-bricks" width="700">
</p>

<h1 align="center">open-bricks</h1>

<p align="center">
  <strong>A New Open Office — AI-native desktop software for the modern age.</strong><br>
  Open source. Future-proof. Connected to LLMs from day one.
</p>

<p align="center">
  <a href="https://github.com/ellmos-ai">AI Infrastructure by ellmos-ai</a> ·
  <a href="#file-management">File Management</a> ·
  <a href="#document-tools">Document Tools</a> ·
  <a href="#developer-tools">Developer Tools</a> ·
  <a href="#entertainment">Entertainment</a>
</p>

---

## What is open-bricks?

**open-bricks** is a collection of **open-source desktop applications** designed for people who want powerful, local-first software — with optional AI superpowers.

Every app works **standalone without any cloud dependency**. But when connected to a local LLM (via [Ollama](https://ollama.com/)) or an AI assistant (via [ellmos-ai](https://github.com/ellmos-ai) MCP servers), they become something more: intelligent tools that understand your work.

### Why open-bricks?

- **No subscriptions.** No telemetry. No cloud lock-in. Your data stays on your machine.
- **AI-ready by design.** Every app exposes CLI or API interfaces that LLM agents can use.
- **Cross-category.** From file management to bioinformatics — one ecosystem, consistent quality.
- **Built with Python + PySide6.** Easy to extend, easy to contribute.

---

## The Suite

### <a id="file-management"></a> File Management — [file-bricks](https://github.com/file-bricks)

Tools for organizing, searching, synchronizing, and protecting your files.

| App | Description |
|-----|-------------|
| [ExplorerPro](https://github.com/file-bricks/ExplorerPro) | Advanced file explorer with privacy monitor, preview panel, sync manager, and built-in code editor. |
| [ProFiler](https://github.com/file-bricks/ProFiler) | Professional file management with full-text search, OCR (Tesseract), PDF editing, and privacy traffic light. |
| [ProSync](https://github.com/file-bricks/ProSync) | Intelligent backup synchronization with automatic database protection, WAL checkpoint for SQLite, and system tray integration. |
| [AmpelClip](https://github.com/file-bricks/AmpelClip) | Clipboard privacy monitor — real-time detection of sensitive data (IBAN, email, credit cards) with automatic anonymization. |
| [KnowledgeDigest](https://github.com/file-bricks/knowledgedigest) | Portable knowledge base with full-text search, LLM summaries, desktop GUI, and web viewer. Indexes PDF, DOCX, TXT, MD. |
| [NoteSpaceLLM](https://github.com/file-bricks/NoteSpaceLLM) | Local, privacy-first alternative to Google NotebookLM. Document analysis, chat interface, and report generation with local LLMs. |
| [ProfiPrompt](https://github.com/file-bricks/ProfiPrompt) | AI prompt manager with board system, versioning, drag & drop, and clipboard integration. |
| [MetaWiki](https://github.com/file-bricks/MetaWiki) | Universal knowledge scaffold — 630+ compact stubs in JSON, bilingual (DE/EN), with AI-powered translation pipeline. |
| [SoftwareCenter](https://github.com/file-bricks/SoftwareCenter) | Lightweight desktop organizer for software shortcuts with tab-based categorization and drag & drop. |
| [SQLiteViewer](https://github.com/file-bricks/SQLiteViewer) | Fast SQLite database browser with SQL editor, schema view, syntax highlighting, and CSV export. Zero dependencies. |
| [WinStorePackager](https://github.com/file-bricks/WinStorePackager) | GUI tool to prepare Python apps for the Microsoft Store — generates AppxManifest, icon assets, and MSIX builds. |

### <a id="document-tools"></a> Document Tools — [doc-bricks](https://github.com/doc-bricks)

Tools for reading, managing, and converting documents.

| App | Description |
|-----|-------------|
| [MediaBrain](https://github.com/doc-bricks/MediaBrain) | Local media hub — unifies streaming services, local files, and browser activity in one dashboard with tags and smart filters. |
| [DokuReader](https://github.com/doc-bricks/DokuReader) | Topic-based document manager with preview, read/unread tracking, and batch PDF export for all common file formats. |
| [LitZentrum](https://github.com/doc-bricks/LitZentrum) | Folder-based literature manager for academic work — PDF integration, notes, citations, BibTeX, and optional Ollama support. |
| [PDFtoPDFocr](https://github.com/doc-bricks/PDFtoPDFocr) | PDF OCR converter — batch processing, automatic language detection, multi-language support, and portable Tesseract integration. |

### <a id="developer-tools"></a> Developer Tools — [dev-bricks](https://github.com/dev-bricks)

Tools for developers — analysis, testing, and automation.

| App | Description |
|-----|-------------|
| [DevCenter](https://github.com/dev-bricks/DevCenter) | Developer dashboard for managing local projects, Git repos, and development environments from a single interface. |
| [pythonbox](https://github.com/dev-bricks/pythonbox) | Sandboxed Python execution environment for testing and experimenting with code snippets safely. |
| [MethodenAnalyser](https://github.com/dev-bricks/MethodenAnalyser) | Static Python code analyzer with AST analysis — detects unused imports, dead code, and similar code blocks. Zero dependencies. |
| [apiprober](https://github.com/dev-bricks/apiprober) | Systematic API discovery tool with OpenAPI detection, wordlist probing, and automatic documentation generation. |

### <a id="entertainment"></a> Entertainment — [entertain-and-more](https://github.com/entertain-and-more)

Games and creative tools with AI integration.

| App | Description |
|-----|-------------|
| [ChatAndChess](https://github.com/entertain-and-more/ChatAndChess) | Text-based chess with 4 modes: 2-player, bot (minimax + alpha-beta), Claude API, and file-based Claude Code integration. |
| [RPX Pro](https://github.com/entertain-and-more/rpx) | Professional pen & paper RPG control center — multi-map, soundboard, lighting, combat system, and LLM integration via JSON-RPC API. |

---

## Specialist Software

Beyond the main suite, our ecosystem includes specialized tools:

### Bioinformatics — [biotec-line](https://github.com/biotec-line)

| App | Description |
|-----|-------------|
| [VFDistiller](https://github.com/biotec-line/VFDistiller) | Genetic variant processing — supports VCF/gVCF/23andMe/FASTA with multi-source annotation (gnomAD, Ensembl VEP). Optional Cython acceleration (5x speedup). |
| [genotype-to-vcf](https://github.com/biotec-line/genotype-to-vcf) | Convert DTC DNA raw data (23andMe, MyHeritage, etc.) to VCF 4.2 format with auto-build detection and NCBI dbSNP integration. |

### Financial Tools — [assistassets-ai](https://github.com/assistassets-ai)

| App | Description |
|-----|-------------|
| [FinancialProof](https://github.com/assistassets-ai/FinancialProof) | Financial document verification and proof management. |

---

## Research

Independent research repositories are maintained under **[research-line](https://github.com/research-line)** — a separate organization for academic publications, reproducible research, and open science.

| Repository | Field | Description |
|------------|-------|-------------|
| [functional-stability-theory](https://github.com/research-line/functional-stability-theory) | Physics / Math | Functional stability framework for quantum field theory and cosmology |
| [crm-cosmology](https://github.com/research-line/crm-cosmology) | Cosmology | Conformal Rescaling Model — alternative dark energy framework |
| [rh-even-dominance](https://github.com/research-line/rh-even-dominance) | Mathematics | Even-dominance approach to the Riemann Hypothesis |
| [ai-elite-swr](https://github.com/research-line/ai-elite-swr) | AI / Social Science | LLM-based worldview reconstruction of 100 key AI leaders |
| [multiaxial-diagnostic-system](https://github.com/research-line/multiaxial-diagnostic-system) | Psychology | Multiaxial diagnostic system for clinical assessment |
| [system-medicine](https://github.com/research-line/system-medicine) | Medicine | Systems medicine framework for integrative diagnostics |
| [fst-nash](https://github.com/research-line/fst-nash) | Game Theory | Nash equilibrium analysis via functional stability theory |

---

## AI Infrastructure

All open-bricks apps are designed to work with the **[ellmos-ai](https://github.com/ellmos-ai)** AI infrastructure:

| Component | Description |
|-----------|-------------|
| [BACH](https://github.com/ellmos-ai/bach) | Text-based OS for LLMs — 109+ handlers, 373+ tools, 932+ skills |
| [FileCommander MCP](https://github.com/ellmos-ai/ellmos-filecommander-mcp) | 43-tool MCP server for filesystem, processes, and interactive sessions |
| [CodeCommander MCP](https://github.com/ellmos-ai/ellmos-codecommander-mcp) | 17-tool MCP server for code analysis and developer workflows |
| [Clatcher MCP](https://github.com/ellmos-ai/ellmos-clatcher-mcp) | 12-tool MCP server for file repair, conversion, and batch ops |
| [n8n Manager MCP](https://github.com/ellmos-ai/n8n-manager-mcp) | 13-tool MCP server for n8n workflow automation |
| [clutch](https://github.com/ellmos-ai/clutch) | Provider-neutral LLM orchestration with auto-routing and budget tracking |
| [rinnsal](https://github.com/ellmos-ai/rinnsal) | Lightweight agent memory and automation infrastructure |
| [ellmos-stack](https://github.com/ellmos-ai/ellmos-stack) | Self-hosted AI stack: Ollama + n8n + Rinnsal + KnowledgeDigest |

**MCP servers on npm:** Install with `npm install -g <package-name>` — works with Claude Desktop, Claude Code, Cursor, Windsurf, and any MCP-compatible client.

---

## Tech Stack

- **Language:** Python 3.10+
- **GUI Framework:** PySide6 (LGPL, official Qt bindings)
- **Database:** SQLite with FTS5 full-text search
- **AI Integration:** Ollama (local), Claude API (optional), MCP protocol
- **Packaging:** PyInstaller, MSIX (Windows Store ready)
- **License:** MIT (most apps) / individual licenses noted per repo

---

## Contributing

Each app lives in its own repository under the respective organization. To contribute:

1. Pick an app from the table above
2. Check its README for setup instructions
3. Open an issue or pull request in that repo

---

<p align="center">
  <strong>open-bricks</strong> — Open Source Software for the Age of AI<br>
  A partner project of <a href="https://github.com/ellmos-ai">ellmos-ai</a>
</p>
