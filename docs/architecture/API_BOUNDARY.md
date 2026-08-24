# API / INTERFACE LAYER BOUNDARY

## Purpose

The interface layer exposes ALIP application capabilities to external clients without containing domain business rules.

## Dependency Direction

HTTP / CLIENT
      |
      v
INTERFACE / API
      |
      v
APPLICATION
      |
      v
DOMAIN

## Allowed Dependencies

- Application commands
- Application DTOs
- Application services
- Application ports
- API schemas

## Prohibited Dependencies

- Domain business rules
- Persistence logic
- Database sessions
- Infrastructure implementations
- Direct SQL
- Business calculations

## v1.0 Initial Capability

Calculate TAT

## Request Flow

HTTP Request -> API Schema -> CalculateTATCommand -> CalculateTATService -> TATCalculationResult -> API Response

## Architectural Rule

The API translates external requests into application commands and application results into external responses.

Business logic remains outside the interface layer.
