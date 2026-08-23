# TAT DOMAIN MODEL

## Purpose

The TAT domain represents the laboratory workflow required to measure,
evaluate, and manage turnaround time.

## Core Workflow

REQUEST CREATED
SPECIMEN COLLECTED
SPECIMEN RECEIVED
ANALYSIS STARTED
ANALYSIS COMPLETED
RESULT VALIDATED
RESULT RELEASED

## Domain Concepts

- LaboratoryRequest
- Specimen
- WorkflowEvent
- TATPolicy
- TATMeasurement
- TATStatus

## TAT Statuses

- WITHIN_TARGET
- AT_RISK
- BREACHED
- NOT_MEASURABLE

## Domain Rule

TAT is calculated from recorded laboratory workflow events.

## Engineering Boundary

The domain layer must remain independent of:

- FastAPI
- SQLAlchemy
- HTTP
- database infrastructure
- frontend/UI
