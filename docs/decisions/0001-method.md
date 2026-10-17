# 0001 Method for building a workflow

- Date: 2026-10-17
- Status: Accepted

## Context

This repo builds a personal workflow skill set. Before writing any skills, we need a method, and we need to decide when the user steps in.

## Options

1. Pick one existing skill set and modify it.
2. Extract the design *dimensions* from existing skill sets, have the user take a position on each, then design skills from those positions.

## Decision

Option 2, in six phases (see `docs/method.md`). The user steps in at every phase in a defined way: decide, confirm, approve or supply material.

## Rationale

- Every skill set embodies a set of design positions. Matt Pocock's has the user act as tech lead; pstack has the agent judge for itself by its principles. Adopting one set means accepting all of its positions.
- Deciding dimension by dimension allows mixing practices from different sources, and every choice has a recorded reason.
- Dimensions are split into general and domain ones, so the general ones can be reused in other domains.
