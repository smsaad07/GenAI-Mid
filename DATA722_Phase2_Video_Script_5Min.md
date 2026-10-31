# DATA722 Phase 2 — Deliverable 3: 5-Minute Video Script & Screen-Recording Guide
**Student Name:** Syed Muhammad Saad  
**Course:** DATA722 — Generative AI & Strategic Forecasting | **Instructor:** Danish Haroon  
**Target Duration:** ~4 minutes 20 seconds (Strictly under the 5:00 ceiling)  
**Recommended Recording Tool:** Clipchamp, Canva Screen Recorder, or Loom + ElevenLabs Voiceover (or your own voice)  

---

## Segment 1 — The Problem (0:00 – 0:40 | Strictly Under 45 Seconds)
**What to Show on Screen:**
- Open the live Vercel Web Application on **Tab 1: Executive Audit & Control Dashboard**.
- Highlight the top KPI banner (**89,475 records / 100% population coverage** vs. **<0.15% manual sampling**) and the **3 Factories (Karachi Port Qasim in Sindh, Hattar in KP, Sundar Lahore in Punjab) + 15 Service Providers** table.

**Voiceover Script (105 words — ~40 seconds):**
> "Assalam-o-Alaikum. I am Syed Muhammad Saad, presenting Use Case A for DATA722 Phase 2: Organisation-Wide Continuous Control Monitoring for Internal Audit.  
> The Company is a large biscuit and cake manufacturer in Pakistan operating three factories in Sindh, Khyber Pakhtunkhwa, and Punjab on SAP S/4HANA, alongside 15 contracted labour, security, canteen, and transport providers.  
> Today, internal audit is manual and sample-based—spending 2,000 auditor hours a year to test less than 0.15% of transactions, or roughly 60 purchase orders out of 40,000. Control failures like duplicate invoices, split POs, contractor wages below provincial minimums, ghost employees, and toxic SAP role conflicts take 3 to 12 months to discover."

---

## Segment 2 — Live Demo of the Product Doing the Thing (0:40 – 2:15 | ~1 min 35 sec)
**What to Show on Screen:**
1. Click **"⚡ Trigger Nightly 100% Population Scan"** in the header, which switches to **Tab 2: Exception Queue & Live AI Inspector (29)**.
2. Click **`TXN-PTP-001` (Duplicate Invoice — Sindh Fine Roller Flour Mills, PKR 1,770,000)** and point to:
   - The **PII Redaction Gate** (`NTN-*****84-3`, `PK36SCBL************9821`).
   - The **OCR Evidence Extract** showing invoice `SFRM-2026-8841` and resubmitted copy `SFRM-2026-8841-A` against a single GRN.
   - Click **"🔄 Re-Run Live Groq AI"** to show `openai/gpt-oss-120b` returning a live JSON rating (`Non-Compliant / High Risk`) with verified citations.
3. Click **`TXN-PAY-002` (Hattar Factory, KP — 24 Wafer Helpers)** to show how the system catches a contractor paying PKR 31,000 base wage + PKR 5,500 overtime to disguise a breach of KP's PKR 36,000 Minimum Wage Notification.
4. Click **`TXN-PTP-003` (Dual Sugar Truck Delivery)** to show `openai/gpt-oss-120b` clearing a legitimate look-alike as **`Compliant`** after reading two distinct weighbridge slips and truck numbers.
5. Click **"✓ Confirm AI Rating"** to demonstrate the human-in-the-loop auditor sign-off, then briefly show **Tab 3 (Statutory Clauses & IR Questionnaire)** and **Tab 6 (Live Groq Custom Audit Sandbox)** where you click **"🚀 Run Live Groq AI Audit Test"**.

**Voiceover Script (~230 words — ~95 seconds):**
> "Here is the live application deployed on Vercel. In accordance with our Phase 1 verdict—'Go, with in-country compute'—this public demo runs on 100% synthetic SAP, ZKTeco biometric, and Industrial Relations data with seeded ground-truth breaches.  
> When we trigger the nightly scan across all 89,475 records, deterministic rules flag 29 exception candidates across Procure-to-Pay, Payroll and Provincial Labour Law, and SAP Segregation of Duties.  
> Let's inspect `TXN-PTP-001` at the Karachi biscuit plant. Notice first that the PII Redaction Gate masks the supplier's NTN and IBAN before any prompt leaves the engine. When I click 'Re-Run Live Groq AI', OpenAI's open-weight model `gpt-oss-120b` reads the OCR scan of both invoices, detects that invoice `SFRM-2026-8841-A` is a duplicate billing of PKR 1.77 million against the same Goods Receipt Note, cites Section 220 of the Companies Act 2017 and Section 23 of the Sales Tax Act 1990, and proposes 'Non-Compliant / High Risk'.  
> Next, look at `TXN-PAY-002` at the Hattar factory in KP. Here, a contractor paid 24 wafer helpers PKR 31,000 basic pay plus PKR 5,500 overtime so gross pay looked like PKR 36,500—above KP's PKR 36,000 minimum wage. Our engine strips overtime under the KP Factories Act 2013 and flags the PKR 5,000 per worker shortfall.  
> Conversely, on `TXN-PTP-003`, two identical PKR 1.42 million sugar invoices on the same day are cleared as 'Compliant' because the model reads two separate truck numbers and weighbridge slips. Finally, the auditor confirms or overrides the rating, and we can also assess all four sites in the Statutory Questionnaire or test any custom scenario live."

---

## Segment 3 — The Implementation: What Happens on Each Request (2:15 – 3:15 | ~1 min)
**What to Show on Screen:**
- Switch to **Tab 1** (the 5-stage pipeline diagram) and briefly show the Jupyter Notebook (`DATA722_Phase2_CCM_Internal_Audit_Notebook.ipynb`) cells showing the PII masking function, `production_batch_system_prompt`, and citation faithfulness verifier.

**Voiceover Script (~150 words — ~60 seconds):**
> "As justified in Phase 1 Row 4a, this system is a fixed, scheduled AI pipeline—not an autonomous agent—because it never chooses an open-ended action path and writes nothing back to SAP.  
> On every request, five deterministic and AI steps run in sequence:  
> First, read-only extracts are pulled from SAP `EKKO`, `RBKP`, `PA0000`, `PAYR`, `USR02`, and ZKTeco biometrics.  
> Second, deterministic Python rules execute 100% population tests—fuzzy invoice normalization, 72-hour rolling PO aggregation below the PKR 500,000 DoA limit, provincial wage floor comparison across Sindh, KP, and Punjab, and SAP Segregation of Duties intersections.  
> Third, a regex redaction gate masks CNICs, IBANs, and NTNs while preserving PKR amounts and dates.  
> Fourth, `openai/gpt-oss-120b` on Groq evaluates the unstructured OCR and log evidence under a statutory-grounded system prompt.  
> Fifth, a post-generation verifier checks that 100% of cited document IDs and PKR numbers exist in the source record before logging the result as Pending Auditor Confirmation."

---

## Segment 4 — Eval Numbers, Cost, and One Thing That Does Not Work (3:15 – 4:25 | ~1 min 10 sec)
**What to Show on Screen:**
- Switch to **Tab 5: Phase 1 Eval Scorecard, Failure Study & Cost** and **Tab 6: Deliverable 4 — The Honesty Section**.
- Point to the 6 Scorecard Cards, the **Prompt v1 vs. Prompt v3 Failure Comparison Table**, the **Token & Cost Telemetry box**, and the **Honesty Section**.

**Voiceover Script (~175 words — ~70 seconds):**
> "Every metric fixed in Phase 1 Rows 7 and 7a was run against the built system:  
> Seeded-breach recall achieved 100%—catching all 23 breaches, beating our 95% target.  
> Exception precision rose from 79.31% at the deterministic rule stage to 95.83% after AI evidence triage, beating our 70% target.  
> Rating agreement with a Senior Auditor across the 200-item Gold Set reached 100%, and our Row 7a False-Clear rate dropped from 50% on disguised wage breaches in Prompt v1 down to 0.0% in Prompt v3 after we decomposed base pay from overtime.  
> Total token consumption for the entire evaluation run—29 exceptions plus 200 Gold Set items—was 65,293 tokens, costing just 2.73 cents USD, or PKR 7.60.  
> Finally, what still does not work? On `TXN-PAY-004`, `gpt-oss-120b` falsely flagged a compliant mid-month joiner who worked 15 of 26 days and received PKR 21,346 pro-rata on a PKR 37,000 contract, because the model compared the pro-rated payout directly against the monthly floor. In production, pro-rata daily normalization must happen deterministically before the prompt, and the model must run on in-country compute rather than a cloud API. Thank you!"
