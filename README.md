# DATA722 Phase 2 — Organisation-Wide Continuous Control Monitoring (Internal Audit)
**Student Name:** Syed Muhammad Saad  
**Course:** DATA722 — Generative AI & Strategic Forecasting | **Instructor:** Danish Haroon  
**Use Case Built:** Use Case A — Organisation-Wide Continuous Control Monitoring (Internal Audit)  
**Models Used:** OpenAI Open-Weight `openai/gpt-oss-120b` & `openai/gpt-oss-20b` via Groq Cloud  

---

## Repository Contents & Phase 2 Deliverables

1. **Hosted Web Application (`index.html`, `api/index.py`, `vercel.json`)**
   - Full-stack SAP S/4HANA & Statutory Continuous Control Monitoring Portal deployed on Vercel.
   - Runs immediately out-of-the-box for the marker without installing anything or holding an API key.
   - Features:
     - **Tab 1 — Executive Audit & Control Dashboard**: 100% population coverage (89,475 synthetic records) across 3 Factories (Sindh Port Qasim, KP Hattar, Punjab Sundar Lahore), Karachi Head Office, and 15 Contracted Service Providers.
     - **Tab 2 — Exception Queue & Live Groq AI Inspector**: Inspect all 29 flagged candidates (23 seeded breaches + 6 legitimate look-alikes), verify PII redaction (`CNIC`, `IBAN`, `NTN`), re-run live `openai/gpt-oss-120b` inference, and confirm/override ratings as Senior Auditor.
     - **Tab 3 — Statutory Clauses & Interactive IR Questionnaire**: Full clause library and weighted compliance assessment across SECP Companies Act 2017, FBR Sales Tax & Income Tax laws, Sindh/KP/Punjab Factories Acts & Minimum Wage Notifications, EOBI Act 1976, SESSI/PESSI/ESSI, PECA 2016, and IIA Global Internal Audit Standards.
     - **Tab 4 — Corrective-Action Tracker (CAPA)**: Process Owner remediation workflow with dual verification.
     - **Tab 5 — Phase 1 Eval Scorecard, Documented Failure Study & Cost Telemetry**: Full Phase 1 Row 7 & Row 7a benchmark results, `Prompt v1` vs. `Prompt v3` failure comparison, and 200-item Gold Set results.
     - **Tab 6 — Live Groq Custom Audit Sandbox & Deliverable 4 (Honesty Section)**: Live scenario tester with real-time PII masking and embedded 1-page Honesty report.

2. **Deliverable 2 — Working Record Notebook (`DATA722_Phase2_CCM_Internal_Audit_Notebook.ipynb`)**
   - Complete implementation and iterative development record containing:
     - Synthetic SAP/Biometric/IR data generation & PII masking pipeline
     - Fixed 5-stage AI architecture & statutory-grounded system prompts
     - Concrete failure discovered during development (`Prompt v1` confident False-Clear on overtime-padded KP minimum wage breaches + residual mid-month pro-rata false positive on `TXN-PAY-004`) and what we did about it
     - Full Phase 1 evaluation scorecard across 29 monitored candidates and 200-item Gold Set
     - Exact token and cost telemetry (`65,293` total tokens = `$0.0273 USD` / `PKR 7.60`)

3. **Deliverable 3 — 5-Minute Video Script & Guide (`DATA722_Phase2_Video_Script_5Min.md`)**
   - Timed screen-recording and voiceover script covering the problem (<45s), live demo, request lifecycle implementation, evaluation numbers, and one thing that does not work.

4. **Deliverable 4 — One-Page Honesty Section (`DATA722_Phase2_Honesty_Section.md` + inside Notebook & Web App)**
   - Detailed account of what the system gets wrong (`TXN-PAY-004` pro-rata joiner false positive, `TXN-PAY-003` unrequested arithmetic in JSON array, OCR noise, off-book cash kickbacks), what we would not yet put in front of a customer (cloud inference vs. in-country compute mandate, Groq 8,000 TPM limit, remaining 8 of 12 audit areas), and exact run costs.
