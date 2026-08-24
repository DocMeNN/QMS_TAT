# PERSISTENCE USE-CASE BOUNDARY

## Purpose

The application layer owns the use case.

Persistence is accessed through an application port.

The infrastructure layer provides the concrete persistence adapter.

## Dependency Direction

```text
INTERFACE / API
       |
       v
APPLICATION SERVICE
       |
       +----> APPLICATION PORT
       |            |
       |            v
       |      INFRASTRUCTURE
       |      PERSISTENCE ADAPTER
       |
       v
DOMAIN
```

## Rule

Application services MUST NOT depend directly on infrastructure implementations.

Infrastructure implements application-defined ports.

This preserves the dependency inversion boundary.
