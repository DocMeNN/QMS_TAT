# ALIP v2.0 — Architecture

## Platform

ALIP Intelligent Laboratory Operations Platform

## Domains

### Laboratory Operations
Responsible for operational laboratory workflow.

### TAT Intelligence
Responsible for turnaround-time intelligence.

### Operational Analytics
Responsible for descriptive and diagnostic analytics.

### Intelligence
Responsible for prediction, risk scoring, anomaly detection,
and operational recommendations.

## Layering

Domain
    ↓
Application
    ↓
Ports
    ↓
Infrastructure

Interface/API
    ↓
Application

Streamlit
    ↓
API
    ↓
Application

## Intelligence Boundary

The intelligence layer MUST NOT directly control persistence.

Intelligence consumes defined application/domain contracts and
returns explicit analytical or decision-support results.

## v1.0 Boundary

The following remain frozen:

- TATMeasurement
- TATStatus
- CalculateTATService
- RecordTATService
- TATCalculatorAdapter
- InMemoryTATRepository
- Existing health endpoint
- Existing TAT calculation endpoint

v2.0 extends capability around these contracts rather than
rewriting the frozen foundation.
