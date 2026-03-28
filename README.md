# The Momentum — Claude Code Plugin Marketplace

Plugin marketplace for compliance, governance, and regulatory skills for [Claude Code](https://claude.ai/code).

## Available Plugins

| Plugin | Version | Description |
|--------|---------|-------------|
| [opengdpr](./opengdpr/) | 0.5.0 | OpenGDPR — AI-assisted GDPR compliance scanner (288 checkpoints, regex code analysis, risk scoring) |

## Installation

### Option 1: CLI install (recommended)

Add the marketplace and install the plugin:

```bash
claude plugin marketplace add the-momentum/skills
claude plugin install opengdpr@the-momentum
```

Restart Claude Code to activate the plugin.

### Option 2: Manual registration

Add this marketplace to your Claude Code settings (`~/.claude/settings.json`):

```json
{
  "extraKnownMarketplaces": {
    "the-momentum": {
      "source": {
        "source": "github",
        "repo": "the-momentum/skills"
      }
    }
  }
}
```

Then install the plugin via CLI:

```bash
claude plugin install opengdpr@the-momentum
```

### Option 3: Direct skill copy

If you prefer not to use the marketplace system, clone the repo and copy the skill directly:

```bash
git clone https://github.com/the-momentum/skills.git the-momentum-skills
cp -r the-momentum-skills/opengdpr/skills/gdpr ~/.claude/skills/gdpr
```

## Usage

After installation, you can use the GDPR scanner in three ways:

### Slash command
```
/openGDPR
```

### Natural language
```
Scan this project for GDPR compliance issues
```

### Modes

| Mode | Time | Description |
|------|------|-------------|
| **A — Code Scan** | 15-30 min | Automated regex scan for consent libraries, tracking pixels, data flows |
| **B — Checklist Interview** | 30-45 min | Guided Q&A across 288 compliance checkpoints in 21 sections |
| **C — Full Audit** | 2-4 hours | Combines A + B with risk scoring, escalation triggers, and legal recommendations |

## Repository Structure

```
the-momentum/skills/
├── .claude-plugin/
│   └── marketplace.json        # Marketplace catalog
├── opengdpr/
│   ├── .claude-plugin/
│   │   └── plugin.json         # Plugin metadata (v0.5.0)
│   ├── skills/
│   │   └── gdpr/
│   │       ├── SKILL.md        # Main skill definition
│   │       ├── scripts/
│   │       │   └── scan_codebase.py   # Deterministic regex scanner (stdlib only)
│   │       ├── references/
│   │       │   ├── gdpr-reference-tables.md
│   │       │   ├── gdpr-checklist.md
│   │       │   └── report-template.md
│   │       └── assets/
│   │           └── gdpr-severity-matrix.json
│   └── README.md               # Plugin documentation
└── README.md                   # This file
```

## Adding New Plugins

To contribute a new plugin to this marketplace:

1. Create a directory at root level (e.g., `my-plugin/`)
2. Add `.claude-plugin/plugin.json` with metadata
3. Add `skills/my-skill/SKILL.md` with the skill definition
4. Optionally add `commands/` for slash commands and `references/` for documentation
5. Register the plugin in `.claude-plugin/marketplace.json`

## Credits

- **OpenGDPR** — Author: [Creativa Legal](https://www.creativa.legal) | Tested by: [The Momentum](https://www.themomentum.ai)
- Licensed under GNU GPLv3

## Disclaimer

The GDPR scanner provides a preliminary, exploratory evaluation. It does not constitute legal advice and does not replace a professional legal audit. See [opengdpr/README.md](./opengdpr/README.md) for full terms of use.
