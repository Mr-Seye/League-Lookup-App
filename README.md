# 🧩 League Lookup

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/Library-Requests-0077B5?logo=requests)](https://pypi.org/project/requests/)
[![JSON](https://img.shields.io/badge/Data-JSON-lightgrey)](https://www.json.org/)
[![GitHub](https://img.shields.io/badge/Repo-GitHub-181717?logo=github)](https://github.com/yourusername/league-lookup)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Riot Games](https://img.shields.io/badge/API-Riot%20Games-critical?logo=riot-games)](https://developer.riotgames.com/)

---

## 🧠 Description

**League Lookup** is a command-line interface (CLI) project written in Python that connects to the **Riot Games API**. It allows users to retrieve:

- Summoner profile details (rank, level, name, etc.)
- In-depth information on any champion in League of Legends

Originally written for **Season 9**, this project may require API updates due to Riot's changes in structure and content delivery.

---

## 🚀 Features

- Connects to Riot API (requires valid developer key)
- Looks up **champion information**: name, title, abilities, cooldowns, etc.
- Looks up **summoner profile**: rank, level, mastery, etc.
- Supports basic CLI navigation via user prompts

---

## 🧰 Technologies Used

- Python
- Riot Games API
- Requests
- JSON

---

## 🛠️ Installation

1. Clone or download the repository.
2. (Optional) Download and inspect [DataDragon](https://developer.riotgames.com/docs/lol#data-dragon) assets if desired.
3. Run the main script:

```bash
python riotAPIMain.py
```
⚠️ You must have a valid Riot Games API key to use this application.

---

## 💡 Usage

Upon running the script, the CLI will prompt:

    Enter a Summoner Name

    Choose between:

        Summoner Profile Lookup

        Champion Information Lookup

Example Outputs

    Summoner Profile

        Name, ID, Level, Region

        Total Mastery

        Ranked Tier/Division (if applicable)

    Champion Info

        Name, Title, Role

        Resource Type

        Passive and Ability descriptions (Q, W, E, R)

        Cooldowns and Costs

---

## 📦 Prerequisites

    Python 3.8+

    Riot Developer Account + API Key

Install required packages:
```bash
pip install -r requirements.txt
```

---

## 👤 Author

Jordan Ogunseye

---

## ⚠️ Notes

    Riot's API has changed since this project was created. Endpoint URLs and data formats may be outdated.

    This project currently does not support newer Riot titles (e.g., Teamfight Tactics, Valorant, etc.)


 ---
