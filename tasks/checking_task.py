"""
Fact Checking Task - Validate claims and ensure accuracy.
"""

from crewai import Task


def create_checking_task(agent, content: str):
    """
    Creates a task for the fact-checker agent to validate content.
    
    Args:
        agent: The fact-checker agent
        content: The content to fact-check
    """
    return Task(
        description=f"""Carefully review and fact-check the following blog post content:
        
        Content to Check:
        {content}
        
        Fact-Checking Requirements:
        1. Identify any claims that seem questionable or unsupported
        2. Check for logical consistency and coherence
        3. Look for potential misstatements or inaccuracies
        4. Verify that examples and statistics are accurate and properly contextualized
        5. Ensure quotes (if any) are correctly represented
        6. Check for any outdated information
        7. Identify areas that need additional clarification or evidence
        
        Provide detailed feedback on:
        - Any inaccuracies found
        - Claims that need better support
        - Suggestions for improvement
        - Overall assessment of accuracy""",
        expected_output="A detailed fact-checking report with findings and recommendations",
        agent=agent,
    )
