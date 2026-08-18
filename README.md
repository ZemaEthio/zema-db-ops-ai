# ZEMA DB Operations AI

An early multi-tenant SaaS MVP for intelligent SQL Server monitoring, security posture management, capacity forecasting, and human-approved incident response.

## MVP features

- Organization/tenant switching
- SQL Server instance health overview
- CPU, memory, storage, backup, and availability signals
- Prioritized incident queue and resolution workflow
- AI-assisted recommendations with explicit safety boundaries
- Security findings and posture score
- Capacity trend and forecast visualization
- Responsive, dependency-free interface
- Synthetic demo data only—no credentials or customer data

## Run locally

No build step or package installation is required.

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080`.

### Run with Streamlit

```bash
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

The Streamlit entry point packages the existing dependency-free dashboard into the hosted application without duplicating the product logic.

## Architecture direction

The browser MVP demonstrates the product workflow. The next implementation phase adds:

1. A read-only collector deployed near each customer SQL Server environment.
2. An authenticated ingestion API with tenant-scoped authorization.
3. Durable telemetry, findings, and incident storage.
4. Background rules and forecasting jobs.
5. OIDC authentication, RBAC, audit logs, and subscription entitlements.

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) and [`collector/health-check.sql`](collector/health-check.sql).

## Safety principles

- Never collect customer table data by default.
- Use least-privilege, read-only monitoring identities.
- Mask query text and potentially sensitive metadata before transmission.
- Encrypt telemetry in transit and at rest.
- Enforce tenant isolation in every query and API operation.
- Keep remediation recommendation-only until a separate approval and execution control plane is validated.

## Capstone alignment

This MVP supports research and evaluation across database administration, software engineering, cloud computing, cybersecurity, AI/analytics, HCI, and project management.

## Status

Capstone MVP / pre-production prototype. Not approved for production database access.
