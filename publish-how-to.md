##### 🚀 How To Use `publish.sh` — Generic Step-by-Step Guide

This is a **clean reusable usage document** with representative (example) names instead of your specific repo / folders.

---

##### ✅ Step 1 — Keep Required Files in Project Root

Your project should look like:

```bash id="9v8k1x"
my-data-project/
│
├── publish.sh
├── .env
├── notebooks/
├── src/
├── data/
└── deploy-repos/
```

---

##### ✅ Step 2 — Configure `.env`

Create / edit `.env`:

```bash id="m3k9qp"
DEST=deploy-repos/binder-repo
GIT_REMOTE_URL=https://github.com/<your-username>/<your-binder-repo>.git
GIT_REMOTE_NAME=origin
GIT_BRANCH=main

MAXSIZE=20M
COMMIT_PREFIX="Auto Publish"
DRY_RUN=true
```

This file controls **all behaviour of publish script**.

---

##### ✅ Step 3 — Clone Deployment Repo (First Time Only)

You must clone once so that `.git` exists.

```bash id="p7x2rb"
mkdir -p deploy-repos

git clone https://github.com/<your-username>/<your-binder-repo>.git \
deploy-repos/binder-repo
```

After this → script can perform git operations.

---

##### ✅ Step 4 — Make Script Executable (One Time)

```bash id="g2w4sd"
chmod +x publish.sh
```

---

##### ✅ Step 5 — Run Safe Test (Dry Run Mode)

```bash id="q6n5ta"
./publish.sh
```

Because:

```bash id="z4r8ul"
DRY_RUN=true
```

Script will:

* scan large files
* copy allowed files
* show git commands
* NOT commit or push

This lets you verify behaviour safely.

---

##### ✅ Step 6 — Enable Real Publish

Edit `.env`

```bash id="b1k7cm"
DRY_RUN=false
```

Then run:

```bash id="s8v3ye"
./publish.sh
```

Now script will automatically:

1️⃣ Sync project files to deployment repo
2️⃣ Stage changes
3️⃣ Commit
4️⃣ Pull with rebase
5️⃣ Push to remote

---

##### ✅ Step 7 — Normal Daily Workflow

Your typical usage becomes:

```bash id="u5y9hf"
Modify notebook / code
↓
Run ./publish.sh
↓
Deployment repo updated
↓
Remote platform rebuilds environment
```

---

##### ⭐ Optional Productivity Tip

Create alias:

```bash id="t2p6nw"
alias deployproject="./publish.sh"
```

Then simply run:

```bash id="r3m8cx"
deployproject
```

---

##### 🧠 Key Operational Notes

* Clone deployment repo **only once**
* Always validate using **dry-run first**
* Files larger than configured size are skipped
* Script must be run from **project root directory**
* `.env` makes script reusable across projects

---

