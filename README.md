# GitHub-Backup-Assistant

## 🧭 Contents:

* [🗒️ Description](#description)
* [🧱 Dependencies](#dependencies)
* [➡️ Launching](#launching)

<a name="description"></a>

## 🗒️ Description

GitHub Backup Assistant can help you to make a backup of all repositories, that you own

<a name="dependencies"></a>

## 🧱 Dependencies

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Python 3.X](https://www.python.org/downloads/release/python-399/)

<a name="launching"></a>

## ➡️ Launching (Windows)

1. Create virtual environment:

```
python -m venv venv
```

2. Activate virtual environment:

```
.\venv\Scripts\activate
```

3. Install requirements:

```
pip install -r requirements.txt
```

4. Run script:

```
python make_backup.py
```

5. Enter your GitHub credentials

> Enter your GitHub username: USERNAME
>
> Enter your GitHub password or personal access token: PASSWORD_OR_PERSONAL_ACCESS_TOKEN

6. Script will show you a list of repositories. Clone them:

> Do you want to clone all these repositories? (Y/N): y


Done.
