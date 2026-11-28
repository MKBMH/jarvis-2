JARVIS 15.0 — THE ONE PROTOCOL — Mobile Menu Fix
Build 15-menu2

Back up your existing deployment and local records. Replace index.html and sw.js in the same repository; keep all other files and the private backend unchanged. The manifest is included unchanged. Open your existing JARVIS website with ?v=15-menu2 appended after deployment. Close and reopen the Home Screen app. Do not clear site data. If the live site is newer than the saved Smart Parking build, merge rather than overwrite.

All 88 module identifiers from the saved Smart Parking build are preserved. Global action links now wrap as complete boxes; the public security screening menu uses full-width buttons, larger touch targets and aligned checkboxes. No new services or permissions.

Tests: JavaScript syntax passed; Chromium at 320, 390, 430 and 768 CSS pixels showed no overlap between successive elements in screening cards and no horizontal document overflow. All 12 screening links remained present; checklist prepare/clear passed; all 88 module identifiers matched baseline. Tested with simulated local storage, direct HTML loading and external requests blocked. Actual iPhone Safari, live deployment, external links and other modules' functions were not tested.
