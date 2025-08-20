import json
from datetime import datetime, timezone
import uuid

def collect_feedback(user_id, feedback_type, description):
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "feedback_id": str(uuid.uuid4()),
        "user_id": user_id,
        "feedback_type": feedback_type,
        "description": description
    }

    with open("feedback_records.jsonl", "a") as f:
        f.write(json.dumps(record) + "\n")

    print("Feedback recorded:", record)

if __name__ == "__main__":
    # Example manual inputs
    collect_feedback("12345", "bug_report", "Bot gave wrong answer to refund request.")
    collect_feedback("67890", "feature_request", "Add support for billing FAQs.")
