# DATA722 Phase 2 — Deliverable 4: The One-Page Honesty Section
**Student Name:** Syed Muhammad Saad  
**Course:** DATA722 — Generative AI & Strategic Forecasting | **Instructor:** Danish Haroon  
**Use Case Built:** Use Case A — Organisation-Wide Continuous Control Monitoring (Internal Audit)  
**Models Evaluated:** OpenAI Open-Weight `openai/gpt-oss-120b` (Primary) & `openai/gpt-oss-20b` (High-Throughput Failover) via Groq Cloud  

---

## 1. What the System Gets Wrong Today (Measured Failures & Limitations)

1. **Mid-Month Pro-Rata Wage False Positive (`TXN-PAY-004` — 95.83% Post-AI Exception Precision vs. 100%)**:
   - In our live evaluation across all 29 rule-flagged exception candidates, `openai/gpt-oss-120b` accurately detected **23 out of 23 seeded breaches (100% Recall)** and cleared **5 out of 6 legitimate look-alikes** (dual-truck sugar delivery `TXN-PTP-003`, emergency breakdown split PO with Head of Procurement ratification `TXN-PTP-007`, signed flour fortification premix addendum `TXN-PTP-013`, retired foreman `9F01` gratuity settlement `TXN-PAY-007`, and approved zero-posting SAP Firefighter session `TXN-ITG-004`).
   - However, on **`TXN-PAY-004`** (a direct factory operator at Port Qasim hired on 14-Oct-2026 who worked 15 out of 26 working days and received **PKR 21,346.15** pro-rata on a compliant **PKR 37,000/month** base contract), `openai/gpt-oss-120b` still rated the record **`Non-Compliant / High Risk`**. In its explanation, the model acknowledged the 15-day pro-rata calculation in SAP `PA0000` and ZKTeco attendance, but over-strictly asserted that the Sindh Minimum Wage Notification (`SINDH-MW-2015-NOTIF`) prohibits any monthly payout below PKR 37,000 regardless of hiring date.
   - While this errs on the safe side (raising a False Exception for human auditor review rather than a dangerous False Clear), it means HR/IR teams would waste review effort on mid-month joiners and unpaid-leave cases until daily wage normalization (`(disbursed_base / days_worked) * 26`) is enforced deterministically in Python *before* calling the model.

2. **Unrequested Arithmetic in Cited Figures (`TXN-PAY-003` — 99.14% Figure Faithfulness vs. 100%)**:
   - On **`TXN-PAY-003`** (19 sanitation workers at the Sundar Lahore plant subjected to an unlawful PKR 3,500 PPE/uniform deduction from a PKR 37,000 nominal gross wage, leaving PKR 33,500 net), the model's prose explanation quoted every source figure accurately (`PKR 37,000`, `PKR 3,500`, `PKR 33,500`). However, inside its JSON `cited_amounts_pkr` array, it also emitted `66500.0` (`19 workers × PKR 3,500 total monthly deduction shortfall`). Because `66,500` was not pre-multiplied in the input text, our deterministic numeric citation verifier flagged it, bringing Figure Faithfulness to **99.14%** across the 29 items (with **100.0% Document Citation Faithfulness**).

3. **Clean OCR Text Assumption vs. Real Factory Paperwork**:
   - Our synthetic dataset provides clean OCR text extracts for Urdu/English transporter Bilty receipts, weighbridge slips, and stamped EOBI `PR-02A` bank challans. In real operations across Karachi, Hattar, and Lahore, carbon-copy gate passes and faded thermal weighbridge tickets frequently suffer from 10–15% character error rates on handwritten weights and truck numbers. Without an upstream OCR confidence gate, noisy digits could cause false quantity variances in `PTP-03`.

4. **Off-Book Collusion Blindspot**:
   - The monitoring engine only sees recorded digital trails in SAP S/4HANA, ZKTeco turnstiles, and the IR portal. If a third-party labour contractor transfers the full statutory PKR 37,000 via banking channels to satisfy our audit test but demands PKR 5,000 back in cash outside the factory gate, or if a buyer and supplier collude to inflate the locked SAP `ME13` contract rate itself, the system will rate the transaction `Compliant`.

---

## 2. What We Would Not Yet Put in Front of a Customer (Production Readiness Gaps)

1. **Offshore Cloud API vs. Phase 1 In-Country Compute Mandate**:
   - For marking convenience, this Phase 2 Vercel application calls Groq's cloud-hosted `openai/gpt-oss-120b` and `openai/gpt-oss-20b` API on **100% synthetic data**. We would **not** connect the Company's live SAP S/4HANA general ledger, contract pricing, or payroll records to an offshore cloud API. Before live customer deployment, the inference endpoint must be pointed to an **in-country / on-premise vLLM cluster** inside the Company's Karachi data center, fulfilling our Phase 1 Verdict (*"Go, with in-country compute"*).
2. **Groq Free/On-Demand Rate Limit (`8,000 TPM`) Under Concurrent Load**:
   - Groq's on-demand tier caps `openai/gpt-oss-120b` at **8,000 Tokens Per Minute (TPM)**. Because `gpt-oss` models allocate internal chain-of-thought reasoning tokens before emitting JSON, firing unbatched requests triggers `HTTP 429` or `HTTP 413`. We mitigated this in production code via 4-item micro-batching, dual-model failover (`120b` → `20b`), and a verified cache fallback, but enterprise production requires dedicated GPU capacity.
3. **Remaining 8 of 12 Process Areas in the Annual Audit Plan**:
   - Phase 2 proves the architecture on **3 process families (8 controls)**: Procure-to-Pay, Payroll & Provincial Labour Law, and IT User Access. The remaining 8 process areas (Order-to-Cash credit overrides, near-expiry cake stock write-offs, manual GL journals, BOM yield variances, Capex, Treasury, FBR Sales Tax Annex-C reconciliation, and Fleet Fuel anomalies) are mapped in the system's roadmap and questionnaire but are not yet wired to automated SQL extractors.

---

## 3. What It Cost to Run (Exact Token & Financial Telemetry)

| Cost & Usage Metric | Measured Value (`openai/gpt-oss-120b` + `20b`) | Basis / Notes |
| :--- | :--- | :--- |
| **Total Prompt (Input) Tokens** | **36,143 tokens** | 29 full-evidence exceptions + 200 Gold Set items + 4 v1 runs |
| **Total Completion (Output + Reasoning) Tokens** | **29,150 tokens** | Internal reasoning + structured JSON citations & explanations |
| **Total Tokens Consumed (Full Eval Run)** | **65,293 tokens** | 15 batched Groq API calls |
| **Representative Evaluation Run Cost** | **\$0.0273 USD (PKR 7.60)** | `$0.15 / 1M` input & `$0.75 / 1M` output (`278.50 PKR/USD`) |
| **Single Live Exception Analysis (Web App)** | **\$0.00058 USD (PKR 0.16)** | ~1,150 input tokens + ~550 output tokens per live click |
| **Projected Monthly Production Cost (Cloud API eq.)** | **\$0.82 USD / month (PKR 228 / month)** | Nightly delta runs analyzing ~450 new exceptions/month |
| **Vercel Hosting & Frontend Cost** | **\$0.00 USD (Free Tier)** | Zero-dependency Python serverless function + static UI |
