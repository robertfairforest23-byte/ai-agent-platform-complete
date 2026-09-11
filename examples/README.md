# Examples Directory

This directory contains standalone example scripts demonstrating different features of the MIKE AI Agent Platform.

## Digital Clock Examples

### `digital_clock_demo.py` - Full-Featured Interactive Clock
A complete digital clock application with interactive menu and real-time updates.

**Features:**
- Real-time clock display (updates every second)
- View all time zones at once
- Display business hours status (9 AM - 5 PM)
- Compare specific time zones
- View detailed timezone information
- Switch between 12-hour and 24-hour formats
- Add custom time zones dynamically
- View statistics
- Automatic demo mode

**Run:**
```bash
python examples/digital_clock_demo.py
```

**Usage:**
1. Select startup mode (Interactive, Real-time, or Demo)
2. Choose from menu options
3. Press Ctrl+C to stop

---

### `simple_clock.py` - Minimal Clock Display
A simplified version for basic clock functionality.

**Features:**
- Display all time zones
- Show business hours
- Quick timezone details
- Format switching
- Minimal dependencies

**Run:**
```bash
python examples/simple_clock.py
```

---

### `clock_examples.py` - Programming Examples
Shows how to use the DigitalClock class in your own code.

**Included Examples:**
1. Basic clock usage
2. Adding custom time zones
3. Time format switching
4. Business hours status
5. Time zone comparison
6. Detailed timezone info
7. Programmatic usage
8. Real-time updates

**Run:**
```bash
python examples/clock_examples.py
```

**Code Example:**
```python
from src.digital_clock import DigitalClock, TimeFormat

# Create clock
clock = DigitalClock()

# Display all clocks
print(clock.display_all_clocks())

# Get time in specific zone
time_est = clock.get_current_time_in_zone('US/Eastern')
print(f"Time in EST: {time_est}")

# Check business hours
print(clock.display_business_hours())

# Switch format
clock.set_time_format(TimeFormat.TWENTY_FOUR_HOUR)
```

---

## To-Do List Examples

### `todo_examples.py` - Task Management Examples
Demonstrates all features of the TodoListManager.

**Included Examples:**
1. Basic task management
2. Task operations (update, complete, mark in progress)
3. Filter tasks by status and priority
4. Task statistics
5. Delete tasks
6. Programmatic usage

**Run:**
```bash
python examples/todo_examples.py
```

**Code Example:**
```python
from src.todo_list import TodoListManager

# Create manager
todo = TodoListManager()

# Add tasks
task1 = todo.add_task("Important task", "high", "Do this first")
task2 = todo.add_task("Regular task", "medium")

# Display tasks
print(todo.display_all_tasks())

# Mark complete
todo.mark_complete(task1.id)

# View statistics
print(todo.display_statistics())
```

---

## Quick Start

### Digital Clock Demo
```bash
cd examples
python digital_clock_demo.py
```

Select option `[3] Demo Mode` to see all features automatically.

### To-Do List Demo
```bash
cd examples
python todo_examples.py
```

Select option `[7] Run All Examples` to see all features.

---

## Time Zones Supported

**Major Zones:**
- UTC (Coordinated Universal Time)
- EST (US Eastern)
- CST (US Central)
- MST (US Mountain)
- PST (US Pacific)
- GMT (UK London)
- CET (Europe Central)
- IST (India Standard)
- JST (Japan Standard)
- AEST (Australia Eastern)
- SGT (Singapore)
- HKT (Hong Kong)
- NZST (New Zealand)
- Dubai (Gulf Standard)
- BRT (Brazil Brasília)

**And more!** You can add any pytz timezone.

---

## Task Priorities

- 🔴 **High** - Urgent, do first
- 🟡 **Medium** - Normal priority (default)
- 🟢 **Low** - Can wait

---

## Task Status

- ⏳ **Pending** - Not started (default)
- ⚙️ **In Progress** - Currently working on it
- ✅ **Completed** - Task is done

---

## Integration with MIKE

These modules are also used by MIKE AI Agent:

```bash
# Voice/text mode
python -m src.mike --text
python -m src.mike --voice

# Clock commands
You: Show all clocks
You: Business hours
You: What time in EST?

# Task commands
You: Add task Buy groceries
You: Show tasks
You: Complete task
You: Show statistics
```

---

## File Organization

```
examples/
├── digital_clock_demo.py      # Full-featured clock app
├── simple_clock.py            # Minimal clock
├── clock_examples.py          # Programming examples
├── todo_examples.py           # Task management examples
└── README.md                  # This file
```

---

## Requirements

All examples require:
- Python 3.9+
- Dependencies from `requirements.txt`

```bash
pip install -r requirements.txt
```

---

## Tips

1. **Time Zone Names**: Use full names like `US/Eastern`, not abbreviations
2. **Real-Time Updates**: Clock data refreshes every second when displayed
3. **Task Persistence**: Tasks are saved to `data/tasks.json`
4. **24-Hour Format**: Available in both 12-hour and 24-hour formats
5. **Business Hours**: Standard definition is 9 AM - 5 PM

---

**Start with `digital_clock_demo.py` for a guided tour!** 🎬
