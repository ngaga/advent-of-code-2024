# Advent of Code 2024

My solutions for Advent of Code 2024.
<img width="853" height="255" alt="Capture d’écran 2025-10-14 à 17 27 36" src="https://github.com/user-attachments/assets/1d9251f1-162a-43b8-9b7c-80af14a38277" />

## Installation and execution with Docker

### Prerequisites
- Docker
- Docker Compose

### Run tests and solutions
0) Clone the project (e.g. with git and ssh) and go to the root of the project

1) Get your session token from the Advent of Code (see [How to get your session token](#how-to-get-your-session-token) section below)

2) Create a `.env` file in the project root with your Advent of Code session token:
```bash
echo "ADVENT_OF_CODE_SESSION=your_session_token_here" > .env
```
3) Then run all tests and all solutions 

```bash
./run.sh
```

### How to get your session token

To get your session token:
1. Go to [Advent of Code](https://adventofcode.com/)
2. Log in to your account
3. Open browser developer tools (F12)
4. Go to Application/Storage tab → Cookies
5. Copy the value of the `session` cookie
6. Replace `your_session_token_here` with your actual token

Example:
```
ADVENT_OF_CODE_SESSION=53616c7465645f5ff2d**************************************************************f0849ef76b03
```

Your `.env` file should look exactly like this (with your actual token):
```
ADVENT_OF_CODE_SESSION=your_actual_token_here
```

**Important:** 
- No spaces around the `=`
- No quotes around the token
- One line only
- The file should be named exactly `.env` (with the dot at the beginning and nothing after)


