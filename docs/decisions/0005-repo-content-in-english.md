# 0005 All repo content in English

- Date: 2026-10-17
- Status: Accepted. Supersedes the documentation-language part of ADR 0003.

## Context

The repo is public on GitHub. ADR 0003 put skills in English but kept `docs/` and the ADRs in Traditional Chinese.

## Options

1. Keep docs in Chinese, skills in English.
2. Put everything in the repo in English.

## Decision

Option 2. All files in the repo are in English: `CLAUDE.md`, `docs/`, ADRs, session notes, READMEs and skills. Commit messages from now on are in English too. The first four commits keep their Chinese messages; rewriting the history of a pushed public repo is not worth it.

Conversation with Claude is unaffected: Claude replies in the language the user writes in.

## Rationale

- A public repo reaches more readers in English.
- One language across docs and skills avoids translating between them.
- The user is not a native English speaker and has asked Claude to correct their English; how those corrections are handled is decided separately.
