# INFRASTRUCTURE LAYER BOUNDARY

## Purpose

The infrastructure layer contains technical implementations required
to connect ALIP application capabilities to external systems.

## Dependency Direction

```text
INFRASTRUCTURE
      |
      v
APPLICATION PORTS
      |
      v
APPLICATION
      |
      v
DOMAIN
```

## Rules

Infrastructure implementations may depend on application ports.
Application code must not depend directly on infrastructure implementations.
Domain business rules remain independent of infrastructure.

## v1.0 Scope

The first infrastructure implementation is the TAT calculator adapter.
