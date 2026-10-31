#!/usr/bin/env python3
"""
Builds the comprehensive Regulatory, Statutory, Professional Standards,
Risk & Control Matrix (RCM), and IR/Audit Questionnaire Framework
for Use Case A: Organisation-Wide Continuous Control Monitoring.
"""
import json
import os

os.makedirs("data", exist_ok=True)

regulatory_frameworks = {
    "company_profile": {
        "anonymised_name": "The Company (Pakistan National Biscuits & Confectionery Pvt. Ltd. — Anonymised)",
        "industry": "Fast-Moving Consumer Goods (FMCG) — Biscuits, Cakes & Wafers Manufacturing",
        "erp_system": "SAP S/4HANA (ECC 6.0 / S/4 Modules: MM, FI-AP, FI-AR, FI-GL, PP, SD, HCM/PY, GRC/Authorizations)",
        "auxiliary_systems": [
            "ZKTeco Biometric Time & Attendance System (Plant Turnstiles & Shift Logs)",
            "Industrial Relations (IR) Audit Application (Contractor & Factory Labour-Law Checklists)",
            "Approved Vendor Contract Price Master (SAP ME11/ME13 Info Records)",
            "Provincial Minimum Wage Gazette Notifications Repository (Sindh, KP, Punjab)"
        ],
        "sites": [
            {
                "site_id": "PLANT-KHI-01",
                "name": "Sindh Factory — Port Qasim Industrial Area, Karachi",
                "province": "Sindh",
                "products": "Plain & Cream Biscuits, Marie, Glucose Biscuits",
                "regular_headcount": 620,
                "contract_workers": 480,
                "applicable_labour_laws": [
                    "Sindh Factories Act 2015",
                    "Sindh Minimum Wages Act 2015 (2025/2026 Gazette Notification: PKR 37,000/month)",
                    "Sindh Terms of Employment (Standing Orders) Act 2015",
                    "Sindh Employees' Social Security Act 2016 (SESSI)",
                    "Employees' Old-Age Benefits Act 1976 (EOBI)"
                ]
            },
            {
                "site_id": "PLANT-KPK-02",
                "name": "Khyber Pakhtunkhwa Factory — Hattar Industrial Estate, Haripur",
                "province": "Khyber Pakhtunkhwa",
                "products": "Layer Cakes, Swiss Rolls, Wafer Biscuits",
                "regular_headcount": 410,
                "contract_workers": 350,
                "applicable_labour_laws": [
                    "Khyber Pakhtunkhwa Factories Act 2013",
                    "Khyber Pakhtunkhwa Minimum Wages Act 2013 (Gazette Notification: PKR 36,000/month)",
                    "Khyber Pakhtunkhwa Industrial and Commercial Employment (Standing Orders) Act 2013",
                    "Khyber Pakhtunkhwa Employees' Social Security Institution (ESSI KP)",
                    "Employees' Old-Age Benefits Act 1976 (EOBI)"
                ]
            },
            {
                "site_id": "PLANT-LHE-03",
                "name": "Punjab Factory — Sundar Industrial Estate, Lahore",
                "province": "Punjab",
                "products": "Cupcakes, Shortbread Cookies, Savoury Crackers",
                "regular_headcount": 540,
                "contract_workers": 430,
                "applicable_labour_laws": [
                    "Factories Act 1934 (as adapted and enforced in Punjab)",
                    "Punjab Minimum Wages Ordinance 1961 (Gazette Notification: PKR 37,000/month)",
                    "Industrial and Commercial Employment (Standing Orders) Ordinance 1968 (Punjab)",
                    "Provincial Employees' Social Security Ordinance 1965 (PESSI)",
                    "Employees' Old-Age Benefits Act 1976 (EOBI)"
                ]
            },
            {
                "site_id": "HO-KHI-00",
                "name": "Corporate Head Office — Clifton, Karachi",
                "province": "Sindh",
                "products": "Corporate Finance, Procurement, Central HR, IT, Supply Chain & Internal Audit",
                "regular_headcount": 230,
                "contract_workers": 65,
                "applicable_labour_laws": [
                    "Sindh Shops and Commercial Establishments Act 2015",
                    "Sindh Minimum Wages Act 2015 (PKR 37,000/month)",
                    "Employees' Old-Age Benefits Act 1976 (EOBI)",
                    "Sindh Employees' Social Security Act 2016 (SESSI)"
                ]
            }
        ],
        "service_providers_count": 15,
        "annual_process_areas": 12,
        "baseline_manual_audit_hours_per_year": 2000,
        "baseline_sample_coverage_pct": 0.15
    },
    "frameworks": [
        {
            "framework_id": "FW-SECP-2017",
            "short_name": "SECP Companies Act 2017",
            "regulator": "Securities and Exchange Commission of Pakistan (SECP)",
            "instrument": "Companies Act, 2017 (Act No. XIX of 2017)",
            "jurisdiction": "Federal (Pakistan)",
            "ai_and_cloud_mandate": "No explicit AI or cloud computing mandate for private manufacturers. Mandates preservation of accurate books of account and adequacy of internal financial controls; therefore SAP remains the authoritative system of record and the monitoring tool operates on read-only extracts.",
            "clauses": [
                {
                    "clause_id": "SECP-CA2017-S220",
                    "section": "Section 220 — Books of Account to be Kept by Company",
                    "title": "Maintenance of Proper Books of Account at Registered Office & Plants",
                    "requirement_text": "Every company shall prepare and keep at its registered office books of account and other relevant books and papers and financial statements for every financial year which give a true and fair view of the state of the affairs of the company, including all sums of money received and expended, all sales and purchases of goods, and all assets and liabilities. Where a company has a branch office or factory in Pakistan, proper summarized returns must be preserved for at least 10 years.",
                    "mapped_controls": ["PTP-01", "PTP-02", "PTP-03", "FIN-01", "INV-01"],
                    "verification_test": "Verify 100% of purchase orders (EKKO/EKPO), vendor invoices (RBKP/RSEG), and general ledger journal entries (BKPF/BSEG) have valid supporting documents, unique reference numbers, and immutable audit trails."
                },
                {
                    "clause_id": "SECP-CA2017-S223",
                    "section": "Section 223 & 249 — Internal Financial Controls & Audit Committee Oversight",
                    "title": "Adequacy and Operating Effectiveness of Internal Financial Controls",
                    "requirement_text": "Directors and management are responsible for establishing and maintaining adequate internal financial controls to prevent and detect fraud and error, safeguard company assets, and ensure completeness and accuracy of accounting records reported to the Board Audit Committee.",
                    "mapped_controls": ["PTP-01", "PTP-02", "PTP-03", "PAY-02", "ITG-01", "ITG-02", "FIN-01"],
                    "verification_test": "Continuous monitoring of Delegation of Authority (DoA) approval thresholds, three-way match integrity, Segregation of Duties (SoD) in SAP, and dual-verified closure of audit exceptions."
                },
                {
                    "clause_id": "SECP-CA2017-S230",
                    "section": "Section 230 — Cost Accounts for Manufacturing Entities",
                    "title": "Raw Material, Production & Inventory Record Integrity",
                    "requirement_text": "Manufacturing companies engaged in food processing shall maintain particulars of utilization of material, labour, and other items of cost, including stock write-offs and scrap disposals.",
                    "mapped_controls": ["INV-01", "PTP-03"],
                    "verification_test": "Verify all stock write-offs and contract raw material price variances (flour, sugar, palm oil, cocoa, packaging film) are approved per DoA limits."
                }
            ]
        },
        {
            "framework_id": "FW-FBR-TAX",
            "short_name": "FBR Sales Tax Act 1990 & Income Tax Ordinance 2001",
            "regulator": "Federal Board of Revenue (FBR)",
            "instrument": "Sales Tax Act 1990 & Income Tax Ordinance 2001",
            "jurisdiction": "Federal (Pakistan)",
            "ai_and_cloud_mandate": "No AI/cloud mandate. Requires 6-year statutory retention of electronic and physical tax invoices, withholding certificates, and banking channel transfer proofs.",
            "clauses": [
                {
                    "clause_id": "FBR-STA1990-S22-23",
                    "section": "Sales Tax Act 1990 — Sections 22, 23 & 73",
                    "title": "Valid Sales Tax Invoice, Unique Supplier Invoice Numbering & Banking Channel Rule",
                    "requirement_text": "Every registered person shall maintain records of supplies and purchases showing Sales Tax Registration Number (STRN), National Tax Number (NTN), unique tax invoice number, description/quantity of goods, and value. Under Section 73, input tax is inadmissible if payment exceeding PKR 50,000 is not made through a verifiable business bank account of the supplier or if duplicate/fictitious invoices are booked.",
                    "mapped_controls": ["PTP-01", "PTP-03"],
                    "verification_test": "Detect exact and fuzzy duplicate supplier tax invoices (same vendor + invoice date/amount or altered invoice string suffix like '-A' / '/1') to prevent duplicate input sales tax claims and double payments."
                },
                {
                    "clause_id": "FBR-ITO2001-S153-174",
                    "section": "Income Tax Ordinance 2001 — Sections 153 & 174",
                    "title": "Withholding Tax Deduction on Goods/Services & 6-Year Record Retention",
                    "requirement_text": "Prescribed persons making payments in full or part (including by way of advance) for supply of goods or rendering of contracted services (labour, security, transport, canteen) must deduct withholding tax at applicable Active Taxpayer List (ATL) / non-ATL rates and retain records for six years.",
                    "mapped_controls": ["PTP-01", "PTP-02", "PTP-03"],
                    "verification_test": "Verify vendor NTN/STRN status (masked in AI prompts) and detect split purchase orders designed to bypass procurement contract tendering and withholding controls."
                }
            ]
        },
        {
            "framework_id": "FW-SINDH-LABOUR",
            "short_name": "Sindh Factories Act 2015, Minimum Wage & SESSI",
            "regulator": "Sindh Labour & Human Resources Department / SESSI",
            "instrument": "Sindh Factories Act 2015, Sindh Minimum Wages Act 2015, Sindh Terms of Employment (Standing Orders) Act 2015, Sindh Employees' Social Security Act 2016",
            "jurisdiction": "Province of Sindh (Port Qasim Factory & Karachi Head Office)",
            "ai_and_cloud_mandate": "No AI or cloud mandate. Requires statutory factory registers (Form-U Adult Worker Register, Muster Roll, Overtime Register, Wage Slips) to be available for Labour Inspector inspection.",
            "clauses": [
                {
                    "clause_id": "SINDH-MW-2015-NOTIF",
                    "section": "Sindh Minimum Wages Act 2015 — Provincial Minimum Wage Gazette Notification",
                    "title": "Statutory Minimum Wage Floor in Sindh (PKR 37,000/month)",
                    "requirement_text": "No employer or third-party labour contractor operating in the Province of Sindh shall pay any adult unskilled, semi-skilled, or junior worker (whether direct employee or contracted through a service provider for production, packing, security, canteen, or sanitation) gross base monthly wages for full standard working hours below the notified minimum rate of PKR 37,000 per month (PKR 1,423.08 per day for 26 working days), excluding overtime.",
                    "mapped_controls": ["PAY-01", "PAY-03"],
                    "verification_test": "Test 100% of Sindh factory and Head Office payroll lines and contractor wage sheets against PKR 37,000/month base floor (pro-rated only for verified unpaid absences; overtime cannot be used to mask a base wage below PKR 37,000)."
                },
                {
                    "clause_id": "SINDH-FA2015-S51-66",
                    "section": "Sindh Factories Act 2015 — Sections 51, 52, 54, 65 & 66",
                    "title": "Weekly/Daily Working Hours (48h/week, 9h/day), Weekly Rest & Double-Rate Overtime",
                    "requirement_text": "No adult worker shall be required or allowed to work in a factory for more than 48 hours in any week or 9 hours in any day without overtime. Where a worker works beyond 9 hours a day or 48 hours a week, they are entitled to overtime wages at twice the ordinary rate of pay (2.0x), and total overtime in any week must remain within statutory limits with mandatory weekly holiday.",
                    "mapped_controls": ["PAY-01", "PAY-03"],
                    "verification_test": "Cross-check biometric turnstile attendance hours against payroll overtime payouts and flag unpaid/underpaid overtime (<2.0x) or excessive weekly hours (>60 hrs/week total)."
                },
                {
                    "clause_id": "SINDH-SESSI-2016-S20",
                    "section": "Sindh Employees' Social Security Act 2016 — Section 20 & 21",
                    "title": "Mandatory SESSI Registration & Monthly Employer Contribution",
                    "requirement_text": "Every eligible worker (direct and contracted through service providers) working at the Sindh factory or establishment must be registered with SESSI upon joining, with monthly employer social security contributions deposited on time.",
                    "mapped_controls": ["PAY-03"],
                    "verification_test": "Reconcile active employee and contractor worker roster at PLANT-KHI-01 and HO-KHI-00 against verified SESSI contribution schedules."
                }
            ]
        },
        {
            "framework_id": "FW-KPK-LABOUR",
            "short_name": "Khyber Pakhtunkhwa Factories Act 2013, Minimum Wage & ESSI KP",
            "regulator": "Directorate of Labour Khyber Pakhtunkhwa / ESSI KP",
            "instrument": "KP Factories Act 2013, KP Minimum Wages Act 2013, KP Industrial and Commercial Employment (Standing Orders) Act 2013",
            "jurisdiction": "Province of Khyber Pakhtunkhwa (Hattar Factory)",
            "ai_and_cloud_mandate": "No AI or cloud mandate. Mandates maintenance of factory worker registers, wage payment registers, and contractor compliance records at the Hattar plant.",
            "clauses": [
                {
                    "clause_id": "KPK-MW-2013-NOTIF",
                    "section": "KP Minimum Wages Act 2013 — KP Minimum Wage Notification",
                    "title": "Statutory Minimum Wage Floor in Khyber Pakhtunkhwa (PKR 36,000/month)",
                    "requirement_text": "Every adult unskilled worker employed in industrial or commercial establishments in Khyber Pakhtunkhwa (including workers supplied by third-party contractors for loading, packing, security, canteen, and transport) shall be paid minimum wages of not less than PKR 36,000 per month (PKR 1,384.62 per day) for normal working hours, exclusive of overtime.",
                    "mapped_controls": ["PAY-01", "PAY-03"],
                    "verification_test": "Test 100% of Hattar factory direct payroll and contractor worker disbursement records against the PKR 36,000/month statutory floor."
                },
                {
                    "clause_id": "KPK-FA2013-S34-47",
                    "section": "KP Factories Act 2013 — Sections 34 to 47",
                    "title": "Working Hours, Rest Intervals, Shift Rotation & Overtime at 2x Ordinary Rate",
                    "requirement_text": "Adult factory workers shall not work more than 48 hours per week (or 9 hours per day) without overtime paid at twice the ordinary rate of wages. Every worker must be recorded in the Register of Adult Workers and biometric attendance must reconcile with payroll.",
                    "mapped_controls": ["PAY-02", "PAY-03"],
                    "verification_test": "Reconcile ZKTeco biometric attendance at PLANT-KPK-02 with SAP HCM payroll and contractor invoices; flag ghost workers (paid with 0 biometric punches) and uncompensated overtime."
                }
            ]
        },
        {
            "framework_id": "FW-PUNJAB-LABOUR",
            "short_name": "Punjab Factories Act 1934, Minimum Wage & PESSI",
            "regulator": "Labour & Human Resource Department Punjab / PESSI",
            "instrument": "Factories Act 1934 (as adapted in Punjab), Punjab Minimum Wages Ordinance 1961, Standing Orders Ordinance 1968, PESSI Ordinance 1965",
            "jurisdiction": "Province of Punjab (Sundar Industrial Estate Lahore Factory)",
            "ai_and_cloud_mandate": "No AI or cloud mandate. Mandates preservation of statutory registers and PESSI contribution schedules.",
            "clauses": [
                {
                    "clause_id": "PUNJAB-MW-1961-NOTIF",
                    "section": "Punjab Minimum Wages Ordinance 1961 — Punjab Minimum Wage Notification",
                    "title": "Statutory Minimum Wage Floor in Punjab (PKR 37,000/month)",
                    "requirement_text": "The minimum rate of wages for adult unskilled workers employed in all industrial and commercial undertakings in the Punjab (whether hired directly or through outsource contractors) is PKR 37,000 per month for 26 working days (PKR 1,423.08 per day). Deductions that reduce net take-home basic wage below the notified floor (other than statutory EOBI/income tax) are prohibited.",
                    "mapped_controls": ["PAY-01", "PAY-03"],
                    "verification_test": "Test 100% of Lahore factory payroll and service provider worker wage registers against PKR 37,000/month statutory minimum."
                },
                {
                    "clause_id": "PUNJAB-FA1934-S34-49",
                    "section": "Factories Act 1934 (Punjab) & Standing Orders Ordinance 1968 — Final Settlement & Muster Roll",
                    "title": "Removal of Terminated/Resigned Workers from Payroll & Muster Roll",
                    "requirement_text": "Upon resignation, dismissal, or completion of contract, an employee's final settlement must be processed and their active status terminated in the payroll register. Disbursing regular monthly salary to an inactive or separated employee constitutes a payroll control failure / ghost worker leakage.",
                    "mapped_controls": ["PAY-02"],
                    "verification_test": "Cross-check SAP HR Employment Status (PA0000/PA0001) and Biometric Last-Punch Date against monthly payroll disbursements (PAYR) to flag payments made after separation date."
                }
            ]
        },
        {
            "framework_id": "FW-EOBI-1976",
            "short_name": "Employees' Old-Age Benefits Act 1976 (EOBI)",
            "regulator": "Employees' Old-Age Benefits Institution (EOBI)",
            "instrument": "Employees' Old-Age Benefits Act, 1976 (Act No. XIV of 1976)",
            "jurisdiction": "Federal (Applicable across all 3 Factories, Head Office & 15 Service Providers)",
            "ai_and_cloud_mandate": "No AI/cloud mandate. Requires electronic monthly PR-02A contribution schedules and PE-01 registration cards for all direct and contractor workers.",
            "clauses": [
                {
                    "clause_id": "EOBI-1976-S9-11",
                    "section": "EOBI Act 1976 — Sections 9, 9B & 11",
                    "title": "Mandatory Registration & Principal Employer Liability for Contract Workers",
                    "requirement_text": "Every insured person employed directly or through a contractor in an industry or establishment must be registered with EOBI within 30 days of employment, and monthly employer (5%) and employee (1%) contributions must be paid. Under Section 9, the Principal Employer (the Company) is jointly liable if a contracted service provider fails to register workers or deposit EOBI contributions.",
                    "mapped_controls": ["PAY-03"],
                    "verification_test": "Verify every active direct and contractor worker in the IR Audit Application has a valid EOBI registration number (masked in LLM prompts) and current monthly PR-02A payment receipt before releasing contractor invoice payment."
                }
            ]
        },
        {
            "framework_id": "FW-PECA-MOITT",
            "short_name": "PECA 2016 (Amended 2025), National AI Policy 2025 & Cloud First Policy 2022",
            "regulator": "Ministry of IT and Telecommunication (MoITT)",
            "instrument": "Prevention of Electronic Crimes Act 2016 (Amended 2025), National AI Policy 2025, Pakistan Cloud First Policy 2022, Draft Personal Data Protection Bill",
            "jurisdiction": "Cross-Cutting Federal (Pakistan)",
            "ai_and_cloud_mandate": "National AI Policy 2025 is non-binding policy guidance emphasizing human oversight and transparency. Cloud First Policy 2022 binds public-sector entities only. Draft PDPB is not yet enacted. PECA 2016 criminalises unauthorised access to and unauthorised disclosure of sensitive personal/identity data. Phase 1 Verdict ('Go, with in-country compute') is driven by corporate data governance over general ledger, contract pricing, and payroll records, combined with mandatory PII masking (CNIC, IBAN, NTN) before model inference.",
            "clauses": [
                {
                    "clause_id": "PECA-2016-S3-16",
                    "section": "PECA 2016 (Amended 2025) — Sections 3, 4, 14 & 16",
                    "title": "Protection Against Unauthorised Access & Identity Information Disclosure",
                    "requirement_text": "Unauthorised access to critical information systems or unauthorised transmission/disclosure of identity information (CNIC numbers, bank account IBANs, biometric templates) is an offence. Internal audit tools must enforce strict Role-Based Access Control (RBAC), Segregation of Duties (SoD), and mask identity numbers before external model calls.",
                    "mapped_controls": ["ITG-01", "ITG-02", "PRIV-01"],
                    "verification_test": "Verify 100% of LLM prompts mask CNIC (`42101-*******-3`), Bank IBAN (`PK36SCBL************9821`), and Tax NTN (`NTN-*****42-8`), while testing SAP user access for SoD conflicts and dormant accounts."
                }
            ]
        },
        {
            "framework_id": "FW-IIA-2024",
            "short_name": "IIA Global Internal Audit Standards (2024)",
            "regulator": "The Institute of Internal Auditors (Professional Standard)",
            "instrument": "IIA Global Internal Audit Standards (Domain III & IV — Principle 10, 12 & 14)",
            "jurisdiction": "International Professional Internal Audit Standard",
            "ai_and_cloud_mandate": "Mandates that Internal Audit evaluate the reliability, faithfulness, and false-clear risk of automated/AI tools relied upon in audit engagements, and maintain human auditor judgement over final ratings.",
            "clauses": [
                {
                    "clause_id": "IIA-GIAS-STD-12-2",
                    "section": "Standard 12.2 & 14.1 — Technological Resources, Evaluation & Human Confirmation",
                    "title": "Validation of Automated Audit Tests, AI Explanation Faithfulness & Auditor Sign-off",
                    "requirement_text": "Internal auditors must exercise due professional care by validating automated control tests against seeded ground-truth breaches, measuring the false-clear rate on high-confidence outputs, verifying that every cited document/amount/date matches source evidence, and ensuring every AI-proposed control rating remains 'Pending Auditor Review' until confirmed by a qualified auditor.",
                    "mapped_controls": ["PTP-01", "PTP-02", "PTP-03", "PAY-01", "PAY-02", "PAY-03", "ITG-01", "ITG-02"],
                    "verification_test": "Enforce Phase 1 Row 7 & 7a evaluation targets: Seeded-breach recall >= 95%, Exception precision >= 70%, Senior Auditor rating agreement >= 85% on 200-item gold set, Figure citation faithfulness = 100%, Evidence citation faithfulness >= 95%, and False-clear rate <= 2%."
                }
            ]
        }
    ],
    "risk_and_control_matrix": [
        {
            "control_id": "PTP-01",
            "process_family": "Procure-to-Pay (P2P)",
            "control_name": "Duplicate Vendor Invoice & Double Payment Prevention",
            "process_owner": "Head of Procurement / Accounts Payable Manager",
            "frequency": "Nightly (Automated Batch)",
            "source_systems": ["SAP FI-AP (RBKP/RSEG)", "SAP MM (EKKO/EKPO)", "Scanned Supplier Tax Invoices (OCR)"],
            "deterministic_rule": "Flag invoice pairs sharing (a) same Vendor ID + Invoice Amount + Invoice Date within 30 days, OR (b) same Vendor ID + normalized Supplier Invoice Reference (stripping spaces, hyphens, leading zeros, or suffixes like '-A', '/1', 'REV'), OR (c) same PO Line + Goods Receipt with multiple posted invoices exceeding PO quantity.",
            "ai_judgement_role": "Reads OCR text of both supplier invoices and goods receipt notes, distinguishes genuine recurring utility/retainer bills or credit-memo re-bills from true duplicate billing, cites exact document numbers/dates/PKR amounts, and proposes a severity rating.",
            "mapped_clauses": ["SECP-CA2017-S220", "FBR-STA1990-S22-23", "IIA-GIAS-STD-12-2"]
        },
        {
            "control_id": "PTP-02",
            "process_family": "Procure-to-Pay (P2P)",
            "control_name": "Split Purchase Order Detection (DoA Threshold Circumvention)",
            "process_owner": "Head of Procurement",
            "frequency": "Nightly (Automated Batch)",
            "source_systems": ["SAP MM (EKKO/EKPO)", "Company Delegation of Authority (DoA) Matrix", "Purchase Requisition Notes"],
            "deterministic_rule": "Group Purchase Orders by (Plant + Vendor ID + Material Group or Creator User ID) within a rolling 72-hour window where individual POs are below the Plant Manager approval limit (PKR 500,000) or Director limit (PKR 2,000,000), but the combined total exceeds the threshold.",
            "ai_judgement_role": "Analyzes PR/PO header texts, delivery schedules, and buyer justifications to determine whether multiple POs reflect genuine emergency line breakdown requests across separate lines or deliberate splitting to bypass competitive bidding and DoA sign-off.",
            "mapped_clauses": ["SECP-CA2017-S223", "FBR-ITO2001-S153-174", "IIA-GIAS-STD-12-2"]
        },
        {
            "control_id": "PTP-03",
            "process_family": "Procure-to-Pay (P2P)",
            "control_name": "Contract Price Compliance & Three-Way Match (PO / GRN / Invoice)",
            "process_owner": "Head of Procurement / Plant Commercial Manager",
            "frequency": "Nightly (Automated Batch)",
            "source_systems": ["SAP MM (ME13 Contract Info Records)", "SAP EKKO/EKPO", "SAP MIGO (GRN)", "SAP MIRO (Invoice)"],
            "deterministic_rule": "Flag any PO or Invoice where billed unit price exceeds the active approved SAP Contract Price List by >0.5% without a signed Price Escalation Addendum, or where invoiced quantity exceeds Goods Receipt Note (GRN) accepted quantity.",
            "ai_judgement_role": "Reads attached Commodity Rate Addendum emails or Quality Deduction notes to check if an apparent price override was formally authorized by the Head of Procurement or represents unauthorized overpayment.",
            "mapped_clauses": ["SECP-CA2017-S230", "FBR-STA1990-S22-23", "IIA-GIAS-STD-12-2"]
        },
        {
            "control_id": "PAY-01",
            "process_family": "Payroll, HR & Labour-Law Compliance",
            "control_name": "Provincial Statutory Minimum Wage Compliance (Direct & Contract Workers)",
            "process_owner": "Head of Industrial Relations (IR) / Head of HR",
            "frequency": "Weekly & Monthly Payroll/Contractor Cycle",
            "source_systems": ["SAP HCM Payroll (PY)", "IR Audit Application (15 Service Providers)", "Provincial Minimum Wage Notifications"],
            "deterministic_rule": "Compare gross base monthly wage (standardized to 26 working days, excluding overtime and non-statutory ad-hoc allowances) against provincial minimum wage floor: Sindh = PKR 37,000/mo, Punjab = PKR 37,000/mo, Khyber Pakhtunkhwa = PKR 36,000/mo.",
            "ai_judgement_role": "Reads contractor wage sheets, attendance pro-ration remarks, and allowance breakdowns to verify whether a sub-threshold payment is a legitimate pro-rated mid-month joiner/unpaid leave case or an illegal below-minimum wage rate / illegal deduction breach.",
            "mapped_clauses": ["SINDH-MW-2015-NOTIF", "KPK-MW-2013-NOTIF", "PUNJAB-MW-1961-NOTIF"]
        },
        {
            "control_id": "PAY-02",
            "process_family": "Payroll, HR & Labour-Law Compliance",
            "control_name": "Payments to Inactive, Terminated or Ghost Employees",
            "process_owner": "Head of HR / Payroll Manager",
            "frequency": "Monthly Pre/Post-Payroll Run",
            "source_systems": ["SAP HCM Master Data (PA0000/PA0001)", "SAP Payroll Run (PAYR)", "ZKTeco Biometric Attendance Logs", "HR Exit Clearance Forms"],
            "deterministic_rule": "Flag any employee or contractor worker receiving regular salary disbursement where (a) SAP Employment Status is 'Inactive/Separated' prior to the pay period start, OR (b) Separation Date precedes pay period end without a 'Final Settlement' wage type, OR (c) Biometric turnstile punches = 0 for >= 30 consecutive days with no approved medical/maternity leave.",
            "ai_judgement_role": "Reviews HR Exit Clearance forms, Final Settlement calculation sheets, and leave sanction letters to distinguish legitimate delayed full-and-final gratuity/encashment payouts from unauthorized post-termination salary leakage or ghost workers.",
            "mapped_clauses": ["PUNJAB-FA1934-S34-49", "KPK-FA2013-S34-47", "SECP-CA2017-S223"]
        },
        {
            "control_id": "PAY-03",
            "process_family": "Payroll, HR & Labour-Law Compliance",
            "control_name": "EOBI, Provincial Social Security (SESSI/PESSI/ESSI) & Overtime Compliance",
            "process_owner": "Head of Industrial Relations (IR)",
            "frequency": "Weekly (Biometric Overtime) & Monthly (Contractor IR Audit)",
            "source_systems": ["IR Audit Application", "ZKTeco Biometric System", "EOBI PR-02A & SESSI/PESSI/ESSI Challans"],
            "deterministic_rule": "Flag (a) active factory or contractor workers missing verified EOBI or SESSI/PESSI/ESSI registration & monthly contribution challan, (b) weekly working hours > 48h without 2.0x overtime rate, or (c) total weekly hours > 60h violating Factories Act limits.",
            "ai_judgement_role": "Inspects uploaded contractor EOBI PR-02A schedules, social security deposit slips, and shift roster logs to verify headcount reconciliation and identify under-reported contractor workers.",
            "mapped_clauses": ["EOBI-1976-S9-11", "SINDH-FA2015-S51-66", "SINDH-SESSI-2016-S20", "KPK-FA2013-S34-47"]
        },
        {
            "control_id": "ITG-01",
            "process_family": "IT User Access & Segregation of Duties (SoD)",
            "control_name": "Conflicting SAP ERP Roles & Segregation of Duties (SoD)",
            "process_owner": "Head of IT / SAP Basis & Security Lead",
            "frequency": "Weekly (Automated Access Scan)",
            "source_systems": ["SAP GRC / USR02 & AGR_USERS", "SAP Transaction Execution Log (STAD/SM20)", "IT Role Request Tickets"],
            "deterministic_rule": "Cross-check active user role assignments against the SAP SoD Conflict Matrix: (1) Vendor Master Creation (`FK01/XK01`) + Invoice Entry/Payment Run (`MIRO/FB60/F110`), (2) PO Creation (`ME21N`) + PO Release/Approval (`ME29N`) or Goods Receipt (`MIGO`), (3) HR Master Maintenance (`PA30/PA40`) + Payroll Execution (`PC00_M99_CALC`), (4) Production User holding `SAP_ALL` or `SU01` + Finance Posting (`FB01`).",
            "ai_judgement_role": "Reads IT access request tickets, emergency firefighting logs, and actual transaction execution history (`SM20`) to assess whether the user actively exploited both sides of the toxic combination or has a valid, time-bound mitigating control.",
            "mapped_clauses": ["SECP-CA2017-S223", "PECA-2016-S3-16", "IIA-GIAS-STD-12-2"]
        },
        {
            "control_id": "ITG-02",
            "process_family": "IT User Access & Segregation of Duties (SoD)",
            "control_name": "Dormant & Terminated User Active SAP Access Revocation",
            "process_owner": "Head of IT",
            "frequency": "Weekly (Automated Access Scan)",
            "source_systems": ["SAP USR02", "SAP HCM Separation Feed", "IT Service Desk Offboarding Tickets"],
            "deterministic_rule": "Flag any unlocked SAP user account (`UFLAG = 0`) where the employee is terminated in SAP HR or has not logged in for > 45 days, especially if transactions were posted after the HR separation date.",
            "ai_judgement_role": "Evaluates IT offboarding ticket timestamps against SAP login audit logs to determine severity and unauthorized post-exit activity.",
            "mapped_clauses": ["PECA-2016-S3-16", "SECP-CA2017-S223"]
        }
    ],
    "full_12_process_universe_roadmap": [
        {"id": 1, "area": "Procure-to-Pay (Duplicate Invoices, Split POs, Contract Price & 3-Way Match)", "status": "Built & Active in Phase 2"},
        {"id": 2, "area": "Payroll & HR Master (Payments to Inactive Staff, Final Settlements, Bank Masking)", "status": "Built & Active in Phase 2"},
        {"id": 3, "area": "Provincial Labour-Law & Contractor IR Compliance (Minimum Wage, EOBI, SESSI/PESSI/ESSI, Overtime)", "status": "Built & Active in Phase 2"},
        {"id": 4, "area": "IT User Access & Segregation of Duties (Conflicting SAP Roles, Dormant/Terminated Accounts)", "status": "Built & Active in Phase 2"},
        {"id": 5, "area": "Order-to-Cash (Distributor Credit-Limit Overrides, Unapproved Trade Discounts & Rebates)", "status": "Next Increment (Architecture Proven)"},
        {"id": 6, "area": "Inventory & Warehousing (Unapproved Stock Write-Offs, Near-Expiry Cake Scrap, Cycle Counts)", "status": "Next Increment (Architecture Proven)"},
        {"id": 7, "area": "Financial Close & General Ledger (Unreviewed Manual Journal Entries, Weekend/Backdated Postings)", "status": "Next Increment (Architecture Proven)"},
        {"id": 8, "area": "Production & Yield Variance (Flour/Sugar/Oil BOM Consumption Variance, Line Scrap Thresholds)", "status": "Next Increment (Architecture Proven)"},
        {"id": 9, "area": "Fixed Assets & Capex (Split Capex Requisitions, Unverified Plant Machinery Disposals)", "status": "Next Increment (Architecture Proven)"},
        {"id": 10, "area": "Treasury & Cash Management (Off-Cycle Bank Signatories, Cash Imprest Reconciliation)", "status": "Next Increment (Architecture Proven)"},
        {"id": 11, "area": "Tax & Statutory Filings (FBR Sales Tax Annex-C/H Reconciliation, WHT Section 153 Defaults)", "status": "Next Increment (Architecture Proven)"},
        {"id": 12, "area": "Logistics & Fleet Contractors (Duplicate Freight Bills, Fuel Card Anomalies Across 3 Plants)", "status": "Next Increment (Architecture Proven)"}
    ],
    "questionnaire_framework": [
        {
            "q_id": "Q-PTP-01",
            "domain": "Procure-to-Pay & FBR/SECP Record Keeping",
            "framework_ref": "SECP Companies Act 2017 Sec 220 & FBR Sales Tax Act 1990 Sec 23/73",
            "control_id": "PTP-01",
            "question": "Does the SAP FI-AP system enforce automated duplicate checks across Vendor ID, Tax Invoice Reference, Invoice Date, and Gross Amount—including fuzzy string normalization to catch suffix alterations (e.g., '-A', '/1') before payment release?",
            "weight": 10,
            "evidence_required": "SAP RBKP/RSEG Duplicate Exception Report & Vendor Tax Invoice Scans",
            "default_site_status": {
                "PLANT-KHI-01": "Non-Compliant (Breaches Detected)",
                "PLANT-KPK-02": "Needs Improvement",
                "PLANT-LHE-03": "Non-Compliant (Breaches Detected)",
                "HO-KHI-00": "Compliant"
            }
        },
        {
            "q_id": "Q-PTP-02",
            "domain": "Procure-to-Pay & FBR/SECP Record Keeping",
            "framework_ref": "SECP Companies Act 2017 Sec 223 & Company Delegation of Authority (DoA)",
            "control_id": "PTP-02",
            "question": "Are multiple Purchase Orders issued to the same vendor within a 72-hour rolling window aggregated to prevent buyers from splitting requisitions below the PKR 500,000 Plant Manager or PKR 2,000,000 Director approval threshold?",
            "weight": 10,
            "evidence_required": "SAP EKKO/EKPO Rolling 72h Aggregation Log & DoA Matrix",
            "default_site_status": {
                "PLANT-KHI-01": "Non-Compliant (Breaches Detected)",
                "PLANT-KPK-02": "Non-Compliant (Breaches Detected)",
                "PLANT-LHE-03": "Needs Improvement",
                "HO-KHI-00": "Compliant"
            }
        },
        {
            "q_id": "Q-PTP-03",
            "domain": "Procure-to-Pay & FBR/SECP Record Keeping",
            "framework_ref": "SECP Companies Act 2017 Sec 230 & FBR Income Tax Ordinance Sec 153",
            "control_id": "PTP-03",
            "question": "Is three-way matching (Approved PO, Biometric/Weighbridge Goods Receipt Note, and Supplier Tax Invoice) enforced against locked SAP Info Record contract rates for flour, sugar, palm oil, and packaging film?",
            "weight": 8,
            "evidence_required": "SAP ME13 Contract Price Master vs. MIRO Invoice Variance Report",
            "default_site_status": {
                "PLANT-KHI-01": "Needs Improvement",
                "PLANT-KPK-02": "Compliant",
                "PLANT-LHE-03": "Non-Compliant (Breaches Detected)",
                "HO-KHI-00": "Compliant"
            }
        },
        {
            "q_id": "Q-PAY-01",
            "domain": "Provincial Minimum Wage & Factories Acts",
            "framework_ref": "Sindh MW Act 2015 (PKR 37k), Punjab MW Ord 1961 (PKR 37k), KP MW Act 2013 (PKR 36k)",
            "control_id": "PAY-01",
            "question": "Are 100% of direct factory workers and third-party contracted workers (labour, security, canteen, transport) paid at least the notified provincial minimum base wage (PKR 37,000 in Sindh/Punjab; PKR 36,000 in KP) for standard 26-day hours without counting overtime towards the base floor?",
            "weight": 12,
            "evidence_required": "SAP Payroll Register, Contractor Wage Disbursal Sheets & Provincial Gazette Notifications",
            "default_site_status": {
                "PLANT-KHI-01": "Non-Compliant (Breaches Detected)",
                "PLANT-KPK-02": "Non-Compliant (Breaches Detected)",
                "PLANT-LHE-03": "Non-Compliant (Breaches Detected)",
                "HO-KHI-00": "Compliant"
            }
        },
        {
            "q_id": "Q-PAY-02",
            "domain": "Payroll Integrity & Ghost Worker Prevention",
            "framework_ref": "Factories Act 1934 / Standing Orders & SECP Internal Financial Controls Sec 223",
            "control_id": "PAY-02",
            "question": "Are separated, resigned, or terminated employees immediately blocked in SAP HCM (`PA0000`) and cross-checked against ZKTeco biometric turnstile logs so that no regular monthly salary is disbursed after the exit date?",
            "weight": 12,
            "evidence_required": "SAP PA0000 Separation Log vs. PAYR Disbursement & ZKTeco Attendance Report",
            "default_site_status": {
                "PLANT-KHI-01": "Non-Compliant (Breaches Detected)",
                "PLANT-KPK-02": "Needs Improvement",
                "PLANT-LHE-03": "Non-Compliant (Breaches Detected)",
                "HO-KHI-00": "Compliant"
            }
        },
        {
            "q_id": "Q-PAY-03",
            "domain": "EOBI & Provincial Social Security (SESSI / PESSI / ESSI KP)",
            "framework_ref": "EOBI Act 1976 Sec 9-11, SESSI Act 2016 Sec 20, PESSI Ord 1965, ESSI KP",
            "control_id": "PAY-03",
            "question": "Does the Industrial Relations (IR) team verify monthly EOBI PR-02A schedules and SESSI/PESSI/ESSI deposit challans against active biometric headcount for all 15 contracted service providers before releasing contractor invoice payments?",
            "weight": 10,
            "evidence_required": "IR Audit Application Checklist, EOBI PR-02A Challans & SESSI/PESSI/ESSI Receipts",
            "default_site_status": {
                "PLANT-KHI-01": "Needs Improvement",
                "PLANT-KPK-02": "Non-Compliant (Breaches Detected)",
                "PLANT-LHE-03": "Needs Improvement",
                "HO-KHI-00": "Compliant"
            }
        },
        {
            "q_id": "Q-PAY-04",
            "domain": "Statutory Working Hours & Double-Rate Overtime",
            "framework_ref": "Sindh Factories Act 2015 Sec 51-66, KP Factories Act 2013 Sec 34-47, Factories Act 1934",
            "control_id": "PAY-03",
            "question": "Are adult factory shift rosters capped at 48 regular hours per week (9 hours/day), with all overtime hours paid at 2.0x the ordinary wage rate and mandatory weekly rest days enforced across biscuit and cake lines?",
            "weight": 8,
            "evidence_required": "ZKTeco Biometric Shift Logs & Overtime Calculation Sheet",
            "default_site_status": {
                "PLANT-KHI-01": "Needs Improvement",
                "PLANT-KPK-02": "Needs Improvement",
                "PLANT-LHE-03": "Non-Compliant (Breaches Detected)",
                "HO-KHI-00": "Compliant"
            }
        },
        {
            "q_id": "Q-ITG-01",
            "domain": "SAP ERP Segregation of Duties (SoD)",
            "framework_ref": "SECP Companies Act 2017 Sec 223 & IIA Global Internal Audit Standards",
            "control_id": "ITG-01",
            "question": "Are toxic SAP role combinations—such as Vendor Creation (`FK01`) + Payment Run (`F110`), PO Creation (`ME21N`) + PO Release (`ME29N`), and HR Master (`PA30`) + Payroll Execution (`PC00_M99_CALC`)—blocked or covered by logged mitigating controls?",
            "weight": 10,
            "evidence_required": "SAP AGR_USERS Role Assignment Matrix & SM20 Transaction Log",
            "default_site_status": {
                "PLANT-KHI-01": "Non-Compliant (Breaches Detected)",
                "PLANT-KPK-02": "Compliant",
                "PLANT-LHE-03": "Needs Improvement",
                "HO-KHI-00": "Non-Compliant (Breaches Detected)"
            }
        },
        {
            "q_id": "Q-ITG-02",
            "domain": "Dormant & Terminated User Access Revocation",
            "framework_ref": "PECA 2016 (Amended 2025) Sec 3 & Corporate IT Security Policy",
            "control_id": "ITG-02",
            "question": "Are SAP user accounts (`USR02`) automatically locked within 24 hours of employee separation and reviewed weekly for accounts dormant over 45 days?",
            "weight": 8,
            "evidence_required": "SAP USR02 Lock Status vs. HR Separation Feed",
            "default_site_status": {
                "PLANT-KHI-01": "Compliant",
                "PLANT-KPK-02": "Needs Improvement",
                "PLANT-LHE-03": "Compliant",
                "HO-KHI-00": "Needs Improvement"
            }
        },
        {
            "q_id": "Q-PRIV-01",
            "domain": "Data Governance, PII Masking & In-Country Compute Readiness",
            "framework_ref": "PECA 2016 Sec 14/16, National AI Policy 2025 & Phase 1 Verdict Condition",
            "control_id": "PRIV-01",
            "question": "Are all personal identity numbers (CNIC), bank account numbers (IBAN), and tax registration numbers (NTN/STRN) masked prior to AI model inference, and does every AI-proposed control rating require explicit human auditor confirmation before closure?",
            "weight": 12,
            "evidence_required": "PII Redaction Pipeline Log & Auditor Sign-off Audit Trail",
            "default_site_status": {
                "PLANT-KHI-01": "Compliant",
                "PLANT-KPK-02": "Compliant",
                "PLANT-LHE-03": "Compliant",
                "HO-KHI-00": "Compliant"
            }
        }
    ]
}

with open("data/regulatory_frameworks.json", "w", encoding="utf-8") as f:
    json.dump(regulatory_frameworks, f, indent=2, ensure_ascii=False)

print("Saved data/regulatory_frameworks.json successfully.")
print(f"Frameworks: {len(regulatory_frameworks['frameworks'])}")
print(f"Clauses: {sum(len(fw['clauses']) for fw in regulatory_frameworks['frameworks'])}")
print(f"RCM Controls: {len(regulatory_frameworks['risk_and_control_matrix'])}")
print(f"Questionnaire Items: {len(regulatory_frameworks['questionnaire_framework'])}")
