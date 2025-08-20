import re
import time
import logging
from datetime import datetime, timezone
import random

# Configure logging
logging.basicConfig(
    filename="chatbot_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Regex patterns for PII
EMAIL_PATTERN = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
PHONE_PATTERN = r'\b\d{4}[-.]?\d{4}[-.]?\d{4}\b'

def detect_pii(text: str) -> bool:
    """Return True if PII (email/phone) is detected."""
    return bool(re.search(EMAIL_PATTERN, text) or re.search(PHONE_PATTERN, text))

def simulate_chatbot_response(user_input: str) -> str:
    """Simulate chatbot responses (could be good, error, or slow)."""
    responses = [
        "Sure, I can help you with that!",
        "Please provide your email so I can send details.",
        "Our support number is 2519-1203-3567.",
        "Oops, something went wrong."
    ]
    # Simulate latency
    delay = random.uniform(0.1, 2.5)
    time.sleep(delay)
    return random.choice(responses), delay

def log_response(user_input: str):
    response, latency = simulate_chatbot_response(user_input)

    pii_flag = detect_pii(response)
    error_flag = "Oops" in response

    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "user_input": user_input,
        "response": response,
        "latency": latency,
        "pii_detected": pii_flag,
        "error": error_flag
    }

    logging.info(str(log_entry))
    print(log_entry)

if __name__ == "__main__":
    # Run sample test logs
    for query in ["Refund request", "Contact support", "Send me info"]:
        log_response(query)
