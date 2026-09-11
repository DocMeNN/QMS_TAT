# ALIP v2.0 — Development Contract

## Release
ALIP v2.0 — Intelligent TAT & Laboratory Operations

## Baseline
ALIP v1.0 is formally released and frozen.

## Objective
Extend the stable TAT foundation into an intelligent laboratory
operations platform without destabilizing the v1.0 release baseline.

## Architectural Principle
Platform
→ Domains
→ Modules
→ Components

## Core v2.0 Domains

### 1. Laboratory Operations
- Laboratory Workflow
- Test Orders
- Specimen Lifecycle
- Work Queues
- Processing Stages

### 2. TAT Intelligence
- Expected TAT
- Historical TAT
- TAT Distribution
- Delay Detection
- Bottleneck Detection
- Predictive TAT

### 3. Operational Analytics
- Workload Analytics
- Throughput
- Turnaround Performance
- Queue Analytics
- Delay Analytics
- Department Analytics

### 4. Intelligent Decision Support
- Risk Scoring
- Delay Alerts
- Operational Recommendations
- Exception Detection
- Forecasting

## v2.0 Rules

1. Preserve v1.0 domain contracts.
2. Preserve v1.0 API compatibility.
3. Do not introduce ORM/domain coupling.
4. Keep bounded contexts explicit.
5. Application services orchestrate use cases.
6. Domain models contain domain behaviour.
7. Infrastructure implements ports.
8. API schemas remain separate from domain models.
9. Intelligence components remain replaceable.
10. Every new capability requires tests.
11. Coverage target remains >=90%.
12. Ruff check commands MUST use --fix.
13. Freeze checkpoints require:
   - Ruff
   - Ruff format
   - Black
   - isort
   - mypy
   - bandit
   - pytest
   - coverage
   - git synchronization

## v2.0 Initial Capability Set

BUILD-20A
Architecture and development contract

BUILD-20B
Laboratory operations domain foundation

BUILD-20C
Operational workflow and specimen lifecycle

BUILD-21A
Historical TAT analytics

BUILD-21B
Workload and queue intelligence

BUILD-22A
Expected TAT intelligence

BUILD-22B
Delay and bottleneck detection

BUILD-23A
Predictive TAT foundation

BUILD-23B
Operational decision support

BUILD-24A
Integrated Streamlit intelligence dashboard

BUILD-24B
End-to-end intelligent workflow validation

BUILD-25A
v2.0 release checkpoint

BUILD-25B
v2.0 formal freeze
