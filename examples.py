"""
Example usage scenarios for the CrewAI Content Pipeline.

This file demonstrates how to use the content creation pipeline
with different topics and configurations.
"""

from main import run_content_pipeline


# ============================================
# EXAMPLE TOPICS & USE CASES
# ============================================

EXAMPLES = {
    "tech_trends": {
        "topic": "Latest Trends in Machine Learning",
        "style": "technical and detailed for industry professionals"
    },
    "health": {
        "topic": "The Benefits of Regular Exercise for Mental Health",
        "style": "friendly, practical, and motivating"
    },
    "business": {
        "topic": "How to Build a Successful Remote Team",
        "style": "professional, actionable, and business-focused"
    },
    "education": {
        "topic": "The Future of Online Learning",
        "style": "informative, balanced, and educational"
    },
}


def run_example(example_key: str):
    """
    Run a specific example from the EXAMPLES dictionary.
    
    Args:
        example_key: Key from EXAMPLES dict
    """
    if example_key not in EXAMPLES:
        print(f"Unknown example: {example_key}")
        print(f"Available examples: {', '.join(EXAMPLES.keys())}")
        return
    
    config = EXAMPLES[example_key]
    result = run_content_pipeline(
        topic=config["topic"],
        style=config["style"]
    )
    return result


def run_custom_topic(topic: str, style: str = "informative and engaging"):
    """
    Run the pipeline for a custom topic.
    
    Args:
        topic: The topic to research and write about
        style: The desired writing style
    """
    return run_content_pipeline(topic=topic, style=style)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # If argument provided, run that example
        example_key = sys.argv[1]
        run_example(example_key)
    else:
        # Otherwise, print available examples
        print("Available examples:")
        for key, config in EXAMPLES.items():
            print(f"  - {key}: {config['topic']}")
        print("\nUsage: python examples.py <example_key>")
        print("\nOr run main.py to use the default example.")
