# Git Workflow & Repository Structure

## Repository Structure

Organize your work by **week** and **day**.

```text
python-intern-training/
├── week-01/
│   ├── day-01/
│   │   ├── README.md
│   │   ├── exercises/
│   │   └── assignment/
│   ├── day-02/
│   └── ...
├── week-02/
├── week-03/
└── resources/
```

### Day Folder Guidelines

Each `day-XX` folder should contain:

- `README.md` – Summary of concepts learned.
- `exercises/` – Practice exercises completed during the day.
- `assignment/` – Assigned task(s) for the day.

---

# Branching Strategy

The repository follows a hierarchical branching model.

```text
main
└── month-01
    ├── week-01
    │   ├── day-01-python-fundamentals
    │   ├── day-02-core-language
    │   └── ...
    ├── week-02
    ├── week-03
    └── week-04
```

### Merge Flow

```text
Day Branch
    ↓
Week Branch
    ↓
Month Branch
    ↓
Main
```

---

# Daily Git Workflow

### 1. Update your local repository

```bash
git checkout week-01
git pull origin week-01
```

### 2. Create a branch for the day's work

```bash
git checkout -b day-01-python-fundamentals
```

> Branch naming convention:
>
> `day-<day-number>-<topic>`
>
> Examples:
>
> - `day-01-python-fundamentals`
> - `day-02-core-language`

### 3. Complete the assigned work

- Add your code under the appropriate `week-XX/day-XX/` directory.
- Commit frequently with meaningful commit messages.

Example:

```bash
git add .
git commit -m "Complete Day 1 exercises on virtual environments and syntax"
```

### 4. Push your branch

```bash
git push -u origin day-01-python-fundamentals
```

### 5. Create a Merge Request

Create a Merge Request targeting the **current week's branch**.

Example:

```text
day-01-python-fundamentals
            ↓
        week-01
```

Do **not** merge directly into `month-01` or `main`.

---

# Review & Promotion Workflow

At the end of each day:

```text
Day Branch
    ↓
Week Branch
```

At the end of each week:

```text
Week Branch
    ↓
Month Branch
```

At the end of each month:

```text
Month Branch
    ↓
Main
```
