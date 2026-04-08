TASKS = {
    "easy": [
        {
            "log": "Multiple failed login attempts from IP 192.168.1.10",
            "context": "5 attempts in 1 minute",
            "answer": "flag"
        },
        {
            "log": "User logged in successfully",
            "context": "normal behavior",
            "answer": "ignore"
        }
    ],

    "medium": [
        {
            "log": "Login attempt from new location",
            "context": "first time from this country",
            "answer": "flag"
        },
        {
            "log": "File downloaded",
            "context": "large size unusual time",
            "answer": "flag"
        }
    ],

    "hard": [
        {
            "log": "Single failed login attempt",
            "context": "but from blacklisted IP",
            "answer": "escalate"
        },
        {
            "log": "Password changed",
            "context": "after suspicious login",
            "answer": "escalate"
        }
    ]
}