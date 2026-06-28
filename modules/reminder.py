import requests
from datetime import datetime, timezone

from config import (
    CODEFORCES_HANDLE,
    LEETCODE_USERNAME,
    CF_GOAL,
    LC_GOAL,
)


# =====================================================
# PRIVATE FUNCTIONS
# =====================================================

def _codeforces_today():
    url = "https://codeforces.com/api/user.status"

    response = requests.get(
        url,
        params={
            "handle": CODEFORCES_HANDLE,
            "from": 1,
            "count": 200,
        },
        timeout=10,
    )

    data = response.json()

    if data["status"] != "OK":
        raise Exception("Codeforces API failed.")

    today = datetime.now(timezone.utc).date()
    solved = set()

    for submission in data["result"]:

        if submission["verdict"] != "OK":
            continue

        submission_time = datetime.fromtimestamp(
            submission["creationTimeSeconds"],
            tz=timezone.utc,
        )

        if submission_time.date() != today:
            continue

        problem = (
            submission["problem"]["contestId"],
            submission["problem"]["index"],
        )

        solved.add(problem)

    return len(solved)


def _leetcode_today():

    url = "https://leetcode.com/graphql"

    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
      recentAcSubmissionList(
        username: $username,
        limit: $limit
      ) {
        titleSlug
        timestamp
      }
    }
    """

    response = requests.post(
        url,
        json={
            "query": query,
            "variables": {
                "username": LEETCODE_USERNAME,
                "limit": 100,
            },
        },
        headers={
            "Content-Type": "application/json",
        },
        timeout=10,
    )

    data = response.json()

    today = datetime.now(timezone.utc).date()

    solved = set()

    for submission in data["data"]["recentAcSubmissionList"]:

        submission_time = datetime.fromtimestamp(
            int(submission["timestamp"]),
            tz=timezone.utc,
        )

        if submission_time.date() == today:
            solved.add(submission["titleSlug"])

    return len(solved)


# =====================================================
# PUBLIC FUNCTION
# =====================================================

def get_daily_stats():

    try:
        cf_done = _codeforces_today()
    except Exception:
        cf_done = 0

    try:
        lc_done = _leetcode_today()
    except Exception:
        lc_done = 0

    return {

        "codeforces": {
            "goal": CF_GOAL,
            "done": cf_done,
            "remaining": max(0, CF_GOAL - cf_done),
        },

        "leetcode": {
            "goal": LC_GOAL,
            "done": lc_done,
            "remaining": max(0, LC_GOAL - lc_done),
        },

        "total_remaining":
            max(0, CF_GOAL - cf_done)
            + max(0, LC_GOAL - lc_done),

    }