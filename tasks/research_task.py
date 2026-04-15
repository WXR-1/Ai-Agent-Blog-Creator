"""
Research Task - Gather and synthesize information about a topic.
"""

from crewai import Task


def create_research_task(agent, topic: str):
    """
    Creates a task for the researcher agent to investigate a topic.
    
    Args:
        agent: The researcher agent
        topic: The topic to research
    """
    return Task(
        description=f"""Conduct comprehensive research on the topic: "{topic}"
        
        Your research should include:
        1. Key facts and information about the topic
        2. Historical context and background
        3. Current trends and developments
        4. Different perspectives and viewpoints
        5. Notable experts, examples, or case studies
        6. Statistics and data points (if relevant)
        
        Organize your findings into clear sections and be thorough.""",
        expected_output="A comprehensive research report with well-organized findings and key insights",
        agent=agent,
    )
