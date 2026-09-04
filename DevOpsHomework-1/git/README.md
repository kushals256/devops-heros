# Git Homework

Practiced in a local demo repo (`/tmp/git-hw-demo`) so this course repo’s history stays clean. Commands and real output below.

---

## Task 1: `git commit -a -m` vs `git commit -m`

### Difference

| | `git commit -m "msg"` | `git commit -a -m "msg"` |
|---|---|---|
| What it commits | Only files already in the **staging area** (`git add`) | All **tracked** files that were modified or deleted |
| New (untracked) files | Ignored until `git add` | Still ignored — `-a` does **not** add new files |
| Typical use | After `git add` of chosen files | Quick save of edits to files git already knows |

`-a` means “stage all tracked changes, then commit.” It is not a substitute for `git add` on brand-new files.

### Test 1 — `git commit -m` without `git add`

Tracked file `notes.txt` was modified but not staged.

```text
$ git status
On branch main
Changes not staged for commit:
	modified:   notes.txt

no changes added to commit (use "git add" and/or "git commit -a")

$ git commit -m "this should fail or do nothing useful"
On branch main
Changes not staged for commit:
	modified:   notes.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

**Result:** `git commit -m` did **not** create a commit. Git told us to `git add` or use `git commit -a`.

### Test 2 — `git commit -a -m` on the same tracked file

```text
$ git commit -a -m "second commit: notes.txt via -a"
[main 2fe38f7] second commit: notes.txt via -a
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git log --oneline
2fe38f7 second commit: notes.txt via -a
d57bd44 first commit: add notes.txt
```

**Result:** `-a` staged the tracked edit and committed it. No separate `git add` needed.

### Test 3 — `git commit -a -m` does not pick up new files

```text
$ echo "brand new" > extra.txt
$ git status
Untracked files:
	extra.txt

$ git commit -a -m "third try: will ignore untracked extra.txt"
Untracked files:
	extra.txt
nothing added to commit but untracked files present (use "git add" to track)

$ git add extra.txt
$ git commit -m "third commit: extra.txt after git add + commit -m"
[main 822a9e8] third commit: extra.txt after git add + commit -m
 1 file changed, 1 insertion(+)
 create mode 100644 extra.txt
```

**Result:** New files still need `git add` + `git commit -m`.

---

## Task 2: Cherry-pick

Cherry-pick copies **one commit** onto the current branch. Other commits on the source branch stay there.

### 1. Commits on `main`

```text
$ git log --oneline
83c4229 main: update app.txt
13ede9f main: add app.txt
822a9e8 third commit: extra.txt after git add + commit -m
2fe38f7 second commit: notes.txt via -a
d57bd44 first commit: add notes.txt
```

### 2. New branch with 3 commits

```text
$ git checkout -b feature/login
Switched to a new branch 'feature/login'

$ git commit -m "feature: add login.txt"
[feature/login 988fd95] feature: add login.txt

$ git commit -a -m "feature: add login validation"
[feature/login 2dfb158] feature: add login validation

$ git commit -m "feature: add dark mode theme"
[feature/login 746cb64] feature: add dark mode theme

$ git log --oneline --decorate
746cb64 (HEAD -> feature/login) feature: add dark mode theme
2dfb158 feature: add login validation
988fd95 feature: add login.txt
83c4229 (main) main: update app.txt
```

### 3. Identify one commit

```text
$ git log --oneline --grep "dark mode"
746cb64 feature: add dark mode theme
```

Picked hash: **`746cb64`** (`feature: add dark mode theme`).

### 4. Cherry-pick it onto `main`

```text
$ git checkout main
Switched to branch 'main'

$ git log --oneline --decorate
83c4229 (HEAD -> main) main: update app.txt
13ede9f main: add app.txt
...

$ git cherry-pick 746cb64
[main 16ad535] feature: add dark mode theme
 1 file changed, 1 insertion(+)
 create mode 100644 theme.txt
```

Git created a **new** commit on main (`16ad535`) with the same change. The original on the branch is still `746cb64`.

### 5. Verify on `main`

```text
$ git log --oneline --decorate
16ad535 (HEAD -> main) feature: add dark mode theme
83c4229 main: update app.txt
13ede9f main: add app.txt
...

$ git show HEAD --stat
    feature: add dark mode theme
 theme.txt | 1 +

$ cat theme.txt
THIS is the cherry-pick target: dark mode

$ git show HEAD:login.txt
fatal: path 'login.txt' does not exist in 'HEAD'
```

**Result:** `theme.txt` (dark mode) is on `main`. `login.txt` is **not** — only the one cherry-picked commit moved. `feature/login` still has all three feature commits.

```text
$ git log --oneline feature/login
746cb64 feature: add dark mode theme
2dfb158 feature: add login validation
988fd95 feature: add login.txt
```

---

## What I understood

- `git commit -m` = commit what is staged.
- `git commit -a -m` = auto-stage tracked edits, then commit. Skips untracked files.
- `git cherry-pick <hash>` = copy one commit onto the current branch. Use it when you want one change from a feature branch without merging the whole branch.
