# Project Requirements Document (PRD): Troop 222 Outing Coordinator

## 1. Product Overview
**Name:** Outing Coordinator (Troop 222 Edition)
**Target Audience:** Outdoor Committee (Adults), Patrol Leaders' Council (PLC / Youth), and Parents/Guardians.
**Purpose:** A centralized web application to manage the scouting outdoor program by strictly aligning with the BSA model: **Youth own the program, Adults own the logistics.** The app bridges the gap between the PLC's scout-led planning and the Outdoor Committee's execution of reservations, permits, and financial responsibilities.

## 2. Core Philosophy: Program vs. Logistics
The application's architecture and permissions are built around a strict division of labor:

**PLC (Youth) — Owns the Program:**
- Select themes, candidate destinations, and trip types.
- Determine cooking styles, patrol assignments, and duty rosters.
- Plan menus and in-trip execution.

**Outdoor Committee (Adults) — Owns the Logistics:**
- Manage reservations, lotteries, and permit applications.
- Handle fees, payments, and vendor contracts.
- Coordinate transportation, health forms, and tour plans.
- Execute parent communication and track post-trip gear dry-out.

## 3. Goals & Success Metrics
- **Logistical Continuity:** Prevent institutional knowledge loss regarding complex booking windows (e.g., Yosemite lotteries, Point Reyes 90-day permits) across adult volunteer transitions.
- **Scout Empowerment:** Free the PLC from impossible logistical tracking so they can focus on authentic leadership (running patrols, planning meals).
- **Consolidation:** Move away from scattered spreadsheets into a single platform that handles both youth program outputs and adult logistical execution.

## 4. User Roles & Permissions
- **Outdoor Committee Chair / Adult Leader (Logistics Admin):** Full access to the Destination Catalog, financial tracking, permit uploads, and parent communications.
- **PLC Member / Patrol Leader (Program Admin):** Access to select candidate destinations, input patrol assignments, create duty rosters, and approve menus.
- **Scout / Participant:** Can view itineraries, view their assigned roles, and submit meal plans/expenses (as Grubmaster).
- **Parent/Guardian:** Can view trip details, sign digital permission slips/health forms, pay trip fees, and volunteer for transportation.

## 5. Core Features & Requirements

### 5.1 The Destination Catalog (The "Outings Retrospective" Database)
*Owned by: Outdoor Committee*
- **Location Database:** A searchable database of historically successful locations (e.g., Philmont, Pinnacles, May Lake).
- **Booking Mechanics Engine:** Track complex booking windows:
  - Rolling windows (e.g., 6 months in advance).
  - Lotteries (e.g., 24-week lottery with weekly submission windows).
  - Phone-only vs. in-person permit pickups.
- **Automated Alerts:** Notify the Outdoor Committee when a booking window is approaching based on the PLC's annual calendar.

### 5.2 Annual Planning & Monthly PLC Workflows
*Owned by: PLC (Youth)*
- **Annual Calendar Builder:** PLC selects monthly themes and candidate destinations from the Destination Catalog.
- **Monthly Trip Dashboard:** For upcoming trips, the PLC inputs:
  - Patrol assignments and crew structures.
  - Grubmasters and duty rosters.
  - Trip-specific skill training plans.

### 5.3 Logistics Execution & Compliance
*Owned by: Outdoor Committee*
- **Permit & Reservation Tracker:** Upload and verify secured permits, vendor contracts, and reservation confirmations.
- **Transportation Coordinator:** Assign scouts to driver vehicles, track adult driver insurance/requirements.
- **Health & Safety Compliance:** Ensure Tour Plans are filed and all participants have up-to-date BSA Health and Medical Records (Parts A/B/C).

### 5.4 Meal Planning & Grubmaster Workflows
*Owned by: PLC / Scouts*
- **Menu Builder:** Scouts input menus for patrol cooking or buddy cooking.
- **Allergy Tracker:** Display dietary restrictions for the specific patrol.
- **Receipt & Expense Submission:** Grubmasters upload receipts (e.g., Amazon Fresh) directly to the app.

### 5.5 Financials & Budgeting
*Owned by: Outdoor Committee*
- **Trip Budgets:** Set per-person costs based on actual reservation fees and estimated food costs.
- **Payment Tracking:** Track non-refundable deposits and final fee payments from parents.
- **Reimbursements:** Process Grubmaster and Quartermaster expense reimbursements quickly based on submitted receipts.

## 6. Technical Requirements
- **Frontend:** Mobile-responsive design, prioritizing easy data entry for scouts on phones, and comprehensive dashboard views for adults on desktops.
- **Notifications:** Email and SMS integration for Parent Communications (pre/during/post-trip) and logistical deadline reminders for the Outdoor Committee.

## 7. Next Steps for Handoff & Development
1. **Digitize the Retrospective:** Import the ≈32 recurring locations and their booking mechanics into the initial database.
2. **Wireframe the Dual-Dashboard:** Design distinct UI flows for the PLC (focused on program) and the Outdoor Committee (focused on logistics).
3. **Review with Leadership:** Validate the feature set against the agreed-upon BSA division of labor framework.
