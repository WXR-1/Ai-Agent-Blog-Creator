"""
Editing Task - Polish and refine the final content.
"""

from crewai import Task


def create_editing_task(agent, content: str, feedback: str = ""):
    """
    Creates a task for the editor agent to polish content.
    
    Args:
        agent: The editor agent
        content: The content to edit
        feedback: Any feedback from fact-checking or previous reviews
    """
    feedback_section = f"\nFact-Checker Feedback:\n{feedback}" if feedback else ""
    
    return Task(
        description=f"""Review and edit the following blog post to polish it for publication:
        
        Content to Edit:
        {content}
        {feedback_section}
        
        Editing Requirements:
        1. Review grammar, spelling, and punctuation
        2. Improve sentence structure and readability
        3. Enhance clarity and eliminate ambiguity
        4. Check for consistency in tone and voice
        5. Optimize pacing and flow between sections
        6. Remove redundancy or repetitive phrasing
        7. Strengthen weak sentences or transitions
        8. Ensure headings are compelling and consistent
        9. Optimize for readability (paragraph length, etc.)
        10. Add polish and professional refinement
        
        Incorporate any feedback provided and deliver a publication-ready version.
        Preserve the original intent and voice while improving quality.""",
        expected_output="A polished, publication-ready blog post with all edits applied",
        agent=agent,
    )
