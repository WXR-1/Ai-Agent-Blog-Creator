"""
Writing Task - Create engaging blog post content based on research.
"""

from crewai import Task


def create_writing_task(agent, research_output: str, style: str = "informative and engaging"):
    """
    Creates a task for the writer agent to create content.
    
    Args:
        agent: The writer agent
        research_output: The research findings from the researcher
        style: The desired writing style
    """
    return Task(
        description=f"""Using the following research findings, write an engaging blog post.
        
        Research Findings:
        {research_output}
        
        Writing Requirements:
        1. Create a compelling headline and introduction that hooks the reader
        2. Organize content into clear sections with subheadings
        3. Write in a {style} style
        4. Include practical examples or case studies where relevant
        5. Use clear, accessible language
        6. Include a strong conclusion with key takeaways
        7. Target length: 1500-2000 words
        8. Ensure transitions between sections are smooth and logical
        
        Make the content engaging and valuable for the reader.""",
        expected_output="A well-written, structured blog post ready for fact-checking",
        agent=agent,
    )
