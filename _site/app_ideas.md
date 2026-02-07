# MedShift UI Specification for Demo Implementation

## Project Overview

**MedShift** is a medication change management app based on EMRC (Event Memory Retrieval and Comparison) theory from cognitive neuroscience. It helps patients remember medication changes by creating "recursive representations" that integrate old and new medication memories.

## Core Concept

When medications change, patients often:
- Forget they switched
- Take the old medication by mistake
- Can't remember which one is current

**Solution**: Use the brain's natural event memory updating mechanisms by:
1. **Retrieval**: Actively recall old medication before taking new one
2. **Prediction**: Generate expectation of what you'll take
3. **Prediction Error**: Explicitly highlight the change
4. **Integration**: Encode the full sequence into one memory

## User Flow Specification

### Scenario Setup
- **User**: Sarah, 68 years old
- **Old Medication**: Blue pill (Metformin 500mg) - taken at 8 AM daily for 2 years
- **New Medication**: White pill (Metformin XR 750mg) - prescribed Jan 15, 2025
- **Change Reason**: Doctor switched to extended-release version for better blood sugar control

---

## Screen-by-Screen Specifications

### Screen 0: Landing Page (Demo Start)

```markdown
┌─────────────────────────────────────────┐
│                                         │
│         💊 MedShift Demo                │
│                                         │
│   Evidence-Based Medication Memory      │
│                                         │
│  Based on cognitive neuroscience        │
│  research on memory updating            │
│                                         │
│  ─────────────────────────────────      │
│                                         │
│  Scenario:                              │
│  Sarah's doctor changed her morning     │
│  diabetes medication from a blue pill   │
│  to a white pill yesterday.             │
│                                         │
│  Let's see how MedShift helps her       │
│  remember the change...                 │
│                                         │
│         [Start Demo]                    │
│                                         │
│  ─────────────────────────────────      │
│  Research basis: Wahlheim & Zacks       │
│  (2024) TICS - EMRC Theory              │
│                                         │
└─────────────────────────────────────────┘
```

**Interaction**: Click "Start Demo" → Go to Screen 1

---

### Screen 1: Morning Reminder

```markdown
┌─────────────────────────────────────────┐
│  8:15 AM                        [×]     │
├─────────────────────────────────────────┤
│                                         │
│         🔔                              │
│                                         │
│   Good morning, Sarah!                  │
│                                         │
│   Time for your morning medication      │
│                                         │
│                                         │
│         [Continue]                      │
│                                         │
│                                         │
│  ───────────────────────────────────    │
│  🧠 What's happening:                   │
│  The app is triggering at your normal   │
│  medication time (8:15 AM)              │
└─────────────────────────────────────────┘
```

**Interaction**: Click "Continue" → Go to Screen 2

---

### Screen 2: Pre-Change Retrieval (Step 1: RETRIEVAL)

```markdown
┌─────────────────────────────────────────┐
│  ← Back                          [×]    │
├─────────────────────────────────────────┤
│                                         │
│   BEFORE YOU TAKE YOUR MEDICATION       │
│                                         │
│   Let's remember what you used to       │
│   take at this time...                  │
│                                         │
│   ┌───────────────────────┐             │
│   │                       │             │
│   │     [Blue Pill]       │             │
│   │      (Image)          │             │
│   │                       │             │
│   └───────────────────────┘             │
│                                         │
│   Metformin 500mg                       │
│                                         │
│   Where did you keep it?                │
│   ○ Medicine cabinet                    │
│   ○ Kitchen counter                     │
│   ○ Bedside table                       │
│                                         │
│         [Next]                          │
│                                         │
│  ───────────────────────────────────    │
│  🧠 Memory Science:                     │
│  Actively retrieving old medication     │
│  strengthens that memory and prepares   │
│  for comparison with new routine        │
└─────────────────────────────────────────┘
```

**Interactions**: 
- Select location (any option works)
- Click "Next" → Go to Screen 3

**Data to capture**:
```javascript
{
  screen: "retrieval",
  timestamp: Date.now(),
  old_medication_shown: "Metformin 500mg (blue)",
  location_selected: "medicine_cabinet" | "kitchen_counter" | "bedside_table",
  retrieval_success: true // user engaged with memory task
}
```

---

### Screen 3: Prediction Generation (Step 2: PREDICTION)

```markdown
┌─────────────────────────────────────────┐
│  ← Back                          [×]    │
├─────────────────────────────────────────┤
│                                         │
│   WHAT DO YOU EXPECT TO SEE?            │
│                                         │
│   Based on your past routine...         │
│                                         │
│   I expect to take:                     │
│                                         │
│   ┌───────────────────────┐             │
│   │                       │             │
│   │     [Blue Pill]       │             │
│   │   (Pre-filled)        │             │
│   │                       │             │
│   └───────────────────────┘             │
│                                         │
│   Metformin 500mg                       │
│                                         │
│                                         │
│     [✓ Tap to confirm prediction]       │
│                                         │
│                                         │
│  ───────────────────────────────────    │
│  🧠 Memory Science:                     │
│  Making an explicit prediction creates  │
│  a "prediction error" when you see      │
│  something different                    │
└─────────────────────────────────────────┘
```

**Interaction**: Click "Tap to confirm prediction" → Go to Screen 4

**Data to capture**:
```javascript
{
  screen: "prediction",
  timestamp: Date.now(),
  predicted_medication: "Metformin 500mg (blue)",
  user_confirmed: true
}
```

---

### Screen 4: Prediction Error Alert (Step 3: PREDICTION ERROR)

```markdown
┌─────────────────────────────────────────┐
│                                  [×]    │
├─────────────────────────────────────────┤
│                                         │
│   ⚠️ IMPORTANT CHANGE ALERT ⚠️          │
│                                         │
│   Your doctor changed your              │
│   prescription!                         │
│                                         │
│   ┌─────────────────┐                   │
│   │ OLD:            │                   │
│   │ [Blue Pill]     │                   │
│   │ Metformin 500mg │                   │
│   └─────────────────┘                   │
│          ↓                              │
│   ┌─────────────────┐                   │
│   │ NEW:            │                   │
│   │ [White Pill]    │                   │
│   │ Metformin XR    │                   │
│   │ 750mg           │                   │
│   └─────────────────┘                   │
│                                         │
│   Take the WHITE pill now               │
│                                         │
│     [I understand the change]           │
│                                         │
│  ───────────────────────────────────    │
│  🧠 Memory Science:                     │
│  Explicit prediction errors improve     │
│  memory updating. You expected blue,    │
│  but it's white now!                    │
└─────────────────────────────────────────┘
```

**Interaction**: Click "I understand the change" → Go to Screen 5

**Visual requirements**:
- Use red/orange warning color for alert header
- Show clear visual contrast between OLD and NEW
- Arrow or transition visual between them

**Data to capture**:
```javascript
{
  screen: "prediction_error",
  timestamp: Date.now(),
  old_shown: "Metformin 500mg (blue)",
  new_shown: "Metformin XR 750mg (white)",
  change_acknowledged: true
}
```

---

### Screen 5: Recursive Memory Encoding (Step 4: INTEGRATION)

```markdown
┌─────────────────────────────────────────┐
│  ← Back                          [×]    │
├─────────────────────────────────────────┤
│                                         │
│   ✓ MEDICATION TAKEN                    │
│                                         │
│   Let's strengthen this memory...       │
│                                         │
│   Today you:                            │
│   • Went to medicine cabinet            │
│   • EXPECTED to take blue pill          │
│   • FOUND white pill instead            │
│   • Took the new white pill             │
│                                         │
│   ─────────────────────────────────     │
│                                         │
│   Why did it change?                    │
│   ┌───────────────────────────────┐     │
│   │ Dr. Chen switched me to       │     │
│   │ extended release version      │     │
│   │                               │     │
│   └───────────────────────────────┘     │
│                                         │
│         [Save Memory]                   │
│                                         │
│  ───────────────────────────────────    │
│  🧠 Memory Science:                     │
│  Encoding the ENTIRE sequence           │
│  (retrieval + prediction + error +      │
│  change) creates a "recursive           │
│  representation" that prevents          │
│  interference                           │
└─────────────────────────────────────────┘
```

**Interactions**:
- Text area is pre-filled but editable
- Click "Save Memory" → Go to Screen 6

**Data to capture**:
```javascript
{
  screen: "integration",
  timestamp: Date.now(),
  memory_encoding: {
    location: "medicine cabinet",
    prediction: "blue pill",
    actual: "white pill",
    reason: "Dr. Chen switched to extended release"
  },
  full_sequence_encoded: true
}
```

---

### Screen 6: Confirmation & Timeline

```markdown
┌─────────────────────────────────────────┐
│  ← Home                          [×]    │
├─────────────────────────────────────────┤
│                                         │
│   ✓ Memory Saved!                       │
│                                         │
│   Your medication change has been       │
│   recorded with full context.           │
│                                         │
│   ─────────────────────────────────     │
│                                         │
│   📅 YOUR MEDICATION TIMELINE            │
│                                         │
│   Today, 8:15 AM                        │
│   ✓ Metformin XR 750mg (white)          │
│   📍 Medicine cabinet                   │
│   🔄 Changed from blue pill             │
│                                         │
│   ─────────────────────────────────     │
│   Changed on Jan 15, 2025               │
│   ─────────────────────────────────     │
│                                         │
│   Jan 14, 8:10 AM                       │
│   Metformin 500mg (blue)                │
│   📍 Medicine cabinet                   │
│                                         │
│                                         │
│   [View Full History]  [Done]           │
│                                         │
└─────────────────────────────────────────┘
```

**Interaction**: Click "Done" → Go to Screen 7 (Jump to 1 week later)

---

### Screen 7: Transition Card (1 Week Later)

```markdown
┌─────────────────────────────────────────┐
│                                         │
│         ⏰                               │
│                                         │
│   ONE WEEK LATER...                     │
│                                         │
│   Sarah has been taking the white       │
│   pill all week using MedShift's        │
│   memory-strengthening system.          │
│                                         │
│   Let's test if she remembers the       │
│   change...                             │
│                                         │
│         [Continue to Test]              │
│                                         │
└─────────────────────────────────────────┘
```

**Interaction**: Click "Continue to Test" → Go to Screen 8

---

### Screen 8: Memory Test - Part 1

```markdown
┌─────────────────────────────────────────┐
│                                  [×]    │
├─────────────────────────────────────────┤
│                                         │
│   MEMORY CHECK                          │
│                                         │
│   What medication do you take in        │
│   the morning?                          │
│                                         │
│   ┌───────────────────────────────┐     │
│   │ White pill - Metformin XR     │     │
│   │                               │     │
│   └───────────────────────────────┘     │
│                                         │
│         [Submit Answer]                 │
│                                         │
│                                         │
│                                         │
│                                         │
│                                         │
│                                         │
│  ───────────────────────────────────    │
│  This tests if Sarah remembers her      │
│  CURRENT medication                     │
└─────────────────────────────────────────┘
```

**Interactions**:
- User types in text field (demo: auto-fill "White pill - Metformin XR")
- Click "Submit Answer" → Go to Screen 9

**Data to capture**:
```javascript
{
  screen: "test_current_med",
  timestamp: Date.now(),
  user_answer: "White pill - Metformin XR",
  correct: true
}
```

---

### Screen 9: Memory Test - Part 2 (Change Detection)

```markdown
┌─────────────────────────────────────────┐
│  ← Back                          [×]    │
├─────────────────────────────────────────┤
│                                         │
│   ✓ Correct!                            │
│                                         │
│   Did this medication change            │
│   recently?                             │
│                                         │
│   ○ Yes                                 │
│   ○ No                                  │
│                                         │
│                                         │
│         [Submit Answer]                 │
│                                         │
│                                         │
│                                         │
│                                         │
│                                         │
│  ───────────────────────────────────    │
│  This tests CHANGE DETECTION -          │
│  does Sarah remember that her           │
│  medication changed?                    │
└─────────────────────────────────────────┘
```

**Interaction**: Select "Yes" → Click "Submit Answer" → Go to Screen 10

**Data to capture**:
```javascript
{
  screen: "test_change_detection",
  timestamp: Date.now(),
  detected_change: true
}
```

---

### Screen 10: Memory Test - Part 3 (Change Recollection)

```markdown
┌─────────────────────────────────────────┐
│  ← Back                          [×]    │
├─────────────────────────────────────────┤
│                                         │
│   ✓ Correct! It did change.             │
│                                         │
│   What was it before?                   │
│                                         │
│   ┌───────────────────────────────┐     │
│   │ Blue pill - Metformin 500mg   │     │
│   │                               │     │
│   └───────────────────────────────┘     │
│                                         │
│         [Submit Answer]                 │
│                                         │
│                                         │
│                                         │
│                                         │
│                                         │
│  ───────────────────────────────────    │
│  This tests CHANGE RECOLLECTION -       │
│  does Sarah remember WHAT it was        │
│  before?                                │
└─────────────────────────────────────────┘
```

**Interaction**: Type answer → Click "Submit Answer" → Go to Screen 11

**Data to capture**:
```javascript
{
  screen: "test_change_recollection",
  timestamp: Date.now(),
  user_answer: "Blue pill - Metformin 500mg",
  correct: true,
  full_recollection: true // remembered current + change + previous
}
```

---

### Screen 11: Results & Explanation

```markdown
┌─────────────────────────────────────────┐
│                                  [×]    │
├─────────────────────────────────────────┤
│                                         │
│   ✓ PERFECT! You remembered             │
│     everything correctly.               │
│                                         │
│   ✅ Current medication: White pill     │
│   ✅ It changed: Yes                    │
│   ✅ Previous medication: Blue pill     │
│                                         │
│   ─────────────────────────────────     │
│                                         │
│   WHY THIS MATTERS:                     │
│                                         │
│   Because you have a complete memory    │
│   of the change, you're much less       │
│   likely to:                            │
│   • Take the old medication by mistake  │
│   • Forget which pill is current        │
│   • Be confused at the pharmacy         │
│                                         │
│   ─────────────────────────────────     │
│                                         │
│   🧠 THE SCIENCE:                       │
│                                         │
│   Research shows that "recursive        │
│   memory encoding" - remembering the    │
│   old, the new, AND the change -        │
│   creates PROACTIVE FACILITATION:       │
│   Old memory helps rather than hurts.   │
│                                         │
│   [Learn More] [Restart Demo]           │
│                                         │
└─────────────────────────────────────────┘
```

**Interactions**:
- Click "Learn More" → Go to Screen 12 (Research explanation)
- Click "Restart Demo" → Go to Screen 0

---

### Screen 12: Research Background

```markdown
┌─────────────────────────────────────────┐
│  ← Back                          [×]    │
├─────────────────────────────────────────┤
│                                         │
│   📚 RESEARCH BACKGROUND                │
│                                         │
│   MedShift is based on Event Memory     │
│   Retrieval and Comparison (EMRC)       │
│   theory from cognitive neuroscience    │
│                                         │
│   Key Paper:                            │
│   Wahlheim & Zacks (2024)               │
│   "Memory updating and the structure    │
│   of event representations"             │
│   Trends in Cognitive Sciences          │
│                                         │
│   ─────────────────────────────────     │
│                                         │
│   KEY FINDINGS:                         │
│                                         │
│   ✓ Retrieving old memories BEFORE      │
│     new events strengthens updating     │
│                                         │
│   ✓ Making explicit predictions         │
│     creates prediction errors that      │
│     improve memory                      │
│                                         │
│   ✓ Encoding the full change sequence   │
│     prevents interference               │
│                                         │
│   ✓ "Recursive representations"         │
│     turn interference into facilitation │
│                                         │
│   [View Full Paper] [Back to Demo]      │
│                                         │
└─────────────────────────────────────────┘
```

**Interaction**: Click "Back to Demo" → Go to Screen 0

---

## Technical Specifications for Implementation

### Data Structure

```javascript
// Global state for demo
const demoState = {
  user: {
    name: "Sarah",
    age: 68
  },
  
  oldMedication: {
    name: "Metformin",
    dosage: "500mg",
    appearance: "Blue oval pill",
    imageUrl: "./assets/blue-pill.png",
    startDate: "2023-01-01",
    endDate: "2025-01-14"
  },
  
  newMedication: {
    name: "Metformin XR",
    dosage: "750mg",
    appearance: "White extended-release pill",
    imageUrl: "./assets/white-pill.png",
    startDate: "2025-01-15",
    changeReason: "Extended release for better blood sugar control"
  },
  
  interactions: {
    retrieval: null,     // Will store {timestamp, location, success}
    prediction: null,    // Will store {timestamp, predicted, confirmed}
    predictionError: null, // Will store {timestamp, acknowledged}
    integration: null,   // Will store {timestamp, reason, fullSequence}
    test: {
      currentMed: null,  // Will store {answer, correct}
      changeDetection: null,
      changeRecollection: null
    }
  },
  
  currentScreen: 0
};
```

### Screen Navigation

```javascript
const screens = [
  "landing",
  "reminder",
  "retrieval",
  "prediction",
  "predictionError",
  "integration",
  "confirmation",
  "weekLater",
  "testCurrent",
  "testChange",
  "testRecollection",
  "results",
  "research"
];

function goToScreen(screenIndex) {
  demoState.currentScreen = screenIndex;
  renderScreen(screens[screenIndex]);
}
```

### Styling Guidelines

```css
/* Color palette */
:root {
  --primary-blue: #4A90E2;
  --success-green: #7ED321;
  --warning-orange: #F5A623;
  --error-red: #D0021B;
  --text-dark: #333333;
  --text-light: #666666;
  --bg-light: #F8F9FA;
  --border-gray: #E1E4E8;
}

/* Card styling */
.demo-card {
  max-width: 400px;
  margin: 0 auto;
  padding: 24px;
  border: 1px solid var(--border-gray);
  border-radius: 12px;
  background: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* Pill images */
.pill-image {
  width: 120px;
  height: 120px;
  margin: 16px auto;
  display: block;
}

/* Science callout box */
.science-box {
  background: var(--bg-light);
  border-left: 4px solid var(--primary-blue);
  padding: 12px;
  margin-top: 20px;
  font-size: 0.9em;
  color: var(--text-light);
}
```

### Image Requirements

**Pill Images Needed** (can use placeholders or generate):
1. `blue-pill.png` - Blue oval pill
2. `white-pill.png` - White round pill

**Icons Needed**:
- Bell icon (🔔)
- Warning icon (⚠️)
- Checkmark icon (✓)
- Brain icon (🧠)
- Calendar icon (📅)
- Location pin icon (📍)
- Clock icon (⏰)

### Responsive Behavior

```css
/* Mobile-first design */
@media (max-width: 768px) {
  .demo-card {
    max-width: 100%;
    margin: 0 16px;
    padding: 16px;
  }
  
  .pill-image {
    width: 100px;
    height: 100px;
  }
}
```

### Analytics/Tracking (Optional)

```javascript
function trackInteraction(event, data) {
  // For demo purposes, just console.log
  console.log("Demo Event:", event, data);
  
  // In production, would send to analytics:
  // analytics.track(event, data);
}

// Example usage:
trackInteraction("retrieval_complete", {
  location: "medicine_cabinet",
  timestamp: Date.now()
});
```

---

## Implementation Checklist

### Phase 1: Basic Structure
- [ ] HTML page with basic structure
- [ ] CSS styling for cards and buttons
- [ ] Screen navigation system
- [ ] All 13 screens with static content

### Phase 2: Interactivity
- [ ] Button click handlers
- [ ] Form input handling (text fields, radio buttons)
- [ ] State management for tracking user journey
- [ ] Screen transitions

### Phase 3: Polish
- [ ] Pill images (placeholder or real)
- [ ] Icons
- [ ] Animations/transitions between screens
- [ ] Responsive design testing
- [ ] Science explanation boxes

### Phase 4: Deployment
- [ ] Host on GitHub Pages, Netlify, or Vercel
- [ ] Add meta tags for social sharing
- [ ] Test on mobile devices
- [ ] Add "Download concept PDF" option

---

## Sample HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MedShift Demo - Evidence-Based Medication Memory</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="app">
    <!-- Screens will render here -->
  </div>
  
  <script src="demo-state.js"></script>
  <script src="screens.js"></script>
  <script src="app.js"></script>
</body>
</html>
```

---

## Next Steps for LLM Agent

**To implement this demo, please:**

1. Create `index.html` with the basic structure
2. Create `styles.css` with the styling specifications above
3. Create `app.js` with screen rendering and navigation logic
4. Implement all 13 screens with exact text and layout as specified
5. Add interactive elements (buttons, form inputs)
6. Make it mobile-responsive
7. Add smooth transitions between screens

**Priority**: Focus on screens 0-6 first (the main intervention flow), then add screens 7-11 (testing), then screen 12 (research).

**Hosting**: Deploy to a static site host (GitHub Pages, Netlify, Vercel) for easy sharing.
