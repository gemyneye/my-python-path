# Case Review Tracker App

## Project Overview
A Dataverse-based app for managing internal case reviews. Users can submit cases, assign reviewers, log comments, and route cases for action or closure.

## Core Components
### Tables
- **Cases** – Main table tracking each case and its status
- **ReviewCaseUsers** – Simulated user directory with roles
- **CaseReviews** – Stores reviewer feedback and routing actions

### Power Apps Logic
- Role-filtered ComboBoxes (Reviewer, AssignedTo)
- Patch functions to update Dataverse records
- Display and form logic based on user selection

### Power Automate
- Sends notification emails based on office
- Uses SharePoint list (OfficeDirectory) to map office names to group email addresses
- Automates flow routing logic based on reviewer actions

## Design Highlights
- Lookup relationships for scalable structure
- Choice fields with integer values for maintainability
- Simulated directory allows learning user lookups without live Office 365 integration

## Tools Used
- Power Apps (Canvas)
- Dataverse
- SharePoint (for email directory)
- Power Automate
- Git (for tracking Markdown + code progress)

## Summary
Built to simulate a real business process using scalable, testable, and maintainable architecture — while gaining hands-on experience with key Power Platform concepts.
