# Getting Started with GitHub
### Pushing Your `hr_data_pipeline` Project to the Cloud

This guide will walk you through creating a GitHub account, setting up a repository, and uploading your `hr_data_pipeline` folder from your computer to GitHub — step by step.

---

## Before You Begin

Make sure you have the following ready:

- Your `hr_data_pipeline` folder somewhere on your computer (Desktop, Documents, etc.)
- Git installed on your computer (see Step 0 below)

---

## Step 0 — Install Git

Git is the tool that actually sends your files to GitHub. You need it installed before anything else.

**Check if you already have it:**

Open your terminal (Mac) or Command Prompt (Windows) and type:

```
git --version
```

If you see something like `git version 2.39.0`, you're good — skip to Step 1.

If you get an error, download and install Git here: **https://git-scm.com/downloads**

> **What's a terminal?**
> - **Mac:** Press `Cmd + Space`, type `Terminal`, hit Enter
> - **Windows:** Press the Windows key, type `cmd`, hit Enter

---

## Step 1 — Create a GitHub Account

1. Go to **https://github.com**
2. Click **Sign up** in the top right corner
3. Enter your email address, create a password, and choose a username
   - Your username will be public — keep it professional (e.g. `jsmith` or `jane-smith`)
4. Follow the prompts to verify your email
5. Once logged in, you'll land on your GitHub dashboard

---

## Step 2 — Create a New Repository

A **repository** (or "repo") is like a project folder on GitHub where your code lives.

1. On your GitHub dashboard, click the **green "New"** button on the left sidebar, or go to **https://github.com/new**
2. Fill in the form:
   - **Repository name:** `hr_data_pipeline`
   - **Description:** *(optional)* e.g. `HR data pipeline project`
   - **Visibility:** Select **Public** or **Private** — Be sure to use the **Public** option.
   - **Do NOT check** "Add a README file" — leave all checkboxes unchecked
3. Click **Create repository**

You'll land on a page that looks mostly empty. That's expected — nothing is there yet. Keep this page open, you'll need it shortly.

---

## Step 3 — Tell Git Who You Are

Before Git can send anything, it needs to know your name and email. You only need to do this once.

In your terminal or Command Prompt, run these two commands one at a time. Replace the example name and email with your own:

```
git config --global user.name "Jane Smith"
```

```
git config --global user.email "janesmith@email.com"
```

> Use the same email address you signed up to GitHub with.

---

## Step 4 — Navigate to Your `hr_data_pipeline` Folder

Open your `hr_data_pipeline` folder in VSCode and open the terminal in VSCode. 

**Confirm you're in the right place** by running:

```
ls
```
*(Mac)* &nbsp; or &nbsp;
```
dir
```
*(Windows)*

You should see the files inside your `hr_data_pipeline` folder listed in the terminal.

---

## Step 5 — Initialize Git in Your Folder

Now tell Git to start tracking this folder:

```
git init
```

You should see a message like: `Initialized empty Git repository in .../hr_data_pipeline/.git/`

---

## Step 6 — Stage Your Files

"Staging" means telling Git which files you want to include in your upload. This command stages everything in the folder:

```
git add .
```

> The `.` means "everything in this folder." Don't forget the dot!

---

## Step 7 — Make Your First Commit

A **commit** is a saved snapshot of your files. Every commit gets a message describing what changed. This is your first one:

```
git commit -m "Initial commit - add hr_data_pipeline project"
```

You should see a list of the files that were included.

---

## Step 8 — Connect Your Folder to GitHub

Now you'll link your local folder to the GitHub repository you created in Step 2.

Go back to your GitHub repository page. Copy the URL from your browser — it will look like:

```
https://github.com/your-username/hr_data_pipeline
```

Then run this command in your terminal, replacing `your-username` with your actual GitHub username:

```
git remote add origin https://github.com/your-username/hr_data_pipeline.git
```

---

## Step 9 — Push Your Files to GitHub

This is the final step — sending your files up to GitHub:

```
git branch -M main
```

```
git push -u origin main
```

Git will ask for your GitHub **username** and **password**.

> **Important:** GitHub no longer accepts your regular password here. You need to use a **Personal Access Token** instead. See the section below if prompted.

---

## Troubleshooting — Personal Access Token (PAT)

If Git asks for your password and your regular GitHub password doesn't work, follow these steps to generate a token:

1. On GitHub, click your **profile photo** (top right) → **Settings**
2. Scroll down to **Developer settings** (bottom of the left sidebar)
3. Click **Personal access tokens** → **Tokens (classic)**
4. Click **Generate new token** → **Generate new token (classic)**
5. Give it a name (e.g. `my-laptop`) and set expiration to **90 days**
6. Under **Scopes**, check the box next to **repo**
7. Scroll down and click **Generate token**
8. **Copy the token immediately** — you won't be able to see it again

When Git asks for your password, paste this token instead of your regular password.

---

## Verify It Worked

1. Go to `https://github.com/your-username/hr_data_pipeline` in your browser
2. You should see all the files from your `hr_data_pipeline` folder listed there

If you can see your files — you did it! 🎉

---

## Quick Reference — Commands in Order

```
git --version
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
cd ~/Desktop/hr_data_pipeline
git init
git add .
git commit -m "Initial commit - add hr_data_pipeline project"
git remote add origin https://github.com/your-username/hr_data_pipeline.git
git branch -M main
git push -u origin main
```

---

## Common Errors & Fixes

**`cd: no such file or directory`**
Your folder path is wrong. Double-check the folder name and location.

**`git: command not found`**
Git is not installed. Go back to Step 0.

**`remote origin already exists`**
Run `git remote remove origin` and then redo the `git remote add origin ...` command.

**`failed to push — repository not found`**
Double-check the URL in your `git remote add` command matches your GitHub repository URL exactly.

**Files not showing on GitHub after push**
Refresh the page. If still empty, confirm you ran `git add .` and `git commit` before pushing.

---

*Questions? Bring them to the next class session or post in the Canvas discussion board.*
