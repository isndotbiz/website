# CLI Project Template

TypeScript CLI scaffolding and engineering standards used to build internal command-line tools quickly and consistently.

## Purpose
- Standardize CLI structure, testing, and quality gates.
- Provide a repeatable foundation for new tooling efforts.
- Improve developer velocity and reliability across internal utilities.

## What Is Included
- Agreed directory layout for commands and shared libraries.
- Testing guidance and coverage targets.
- Build, lint, and formatting conventions.
- Conventional commit and PR standards.

## Expected Structure
```
src/main.ts           CLI handler
bin/cli.ts            Binary entry
src/commands/         Command modules
src/lib/              Shared utilities
tests/                Test suite
```

## Development Commands
- npm install
- npm run dev
- npm run build
- npm test
- npm run lint
- npm run format

## Status
This repo currently contains the standards and scaffolding documentation. Application code can be added following AGENTS.md and CLAUDE.md.
