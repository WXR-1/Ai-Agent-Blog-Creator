"""
CrewAI Content Research & Writing Pipeline

Orchestrates 4 agents to automate the complete content creation workflow:
1. Researcher - Gathers information about a topic
2. Writer - Creates engaging blog post content
3. Fact Checker - Validates claims and accuracy
4. Editor - Polishes the final output

Usage:
    python main.py
"""

# Import config FIRST to set environment variables for all agents
import config  # noqa: F401

from crewai import Crew, Process
from agents import (
    create_researcher_agent,
    create_writer_agent,
    create_fact_checker_agent,
    create_editor_agent,
)
from tasks import (
    create_research_task,
    create_writing_task,
    create_checking_task,
    create_editing_task,
)


def build_content_crew():
    """
    Builds and returns the CrewAI crew with all agents and tasks configured.
    """
    
    # ============================================
    # 1. CREATE AGENTS
    # ============================================
    researcher = create_researcher_agent()
    writer = create_writer_agent()
    fact_checker = create_fact_checker_agent()
    editor = create_editor_agent()
    
    # ============================================
    # 2. CREATE TASKS
    # ============================================
    # Note: We'll define tasks dynamically in the kickoff to include inputs
    
    # ============================================
    # 3. CREATE CREW
    # ============================================
    crew = Crew(
        agents=[researcher, writer, fact_checker, editor],
        process=Process.sequential,  # Tasks execute one after another
        verbose=True,
    )
    
    return crew, researcher, writer, fact_checker, editor


def run_content_pipeline(topic: str, style: str = "informative and engaging"):
    """
    Runs the complete content creation pipeline.
    
    Args:
        topic: The topic to research and write about
        style: The desired writing style (default: "informative and engaging")
    
    Returns:
        The final output from the editor
    """
    
    print("\n" + "="*80)
    print(f"📝 STARTING CONTENT CREATION PIPELINE")
    print(f"📚 Topic: {topic}")
    print(f"✨ Style: {style}")
    print("="*80 + "\n")
    
    # Build the crew
    crew, researcher, writer, fact_checker, editor = build_content_crew()
    
    # ============================================
    # STEP 1: RESEARCH
    # ============================================
    print("\n🔍 STEP 1: RESEARCH")
    print("-" * 80)
    research_task = create_research_task(researcher, topic)
    research_crew = Crew(agents=[researcher], tasks=[research_task], verbose=True)
    research_output = research_crew.kickoff()
    
    # ============================================
    # STEP 2: WRITE
    # ============================================
    print("\n✍️  STEP 2: WRITING")
    print("-" * 80)
    writing_task = create_writing_task(writer, research_output, style)
    writing_crew = Crew(agents=[writer], tasks=[writing_task], verbose=True)
    writing_output = writing_crew.kickoff()
    
    # ============================================
    # STEP 3: FACT-CHECK
    # ============================================
    print("\n✔️  STEP 3: FACT-CHECKING")
    print("-" * 80)
    checking_task = create_checking_task(fact_checker, writing_output)
    checking_crew = Crew(agents=[fact_checker], tasks=[checking_task], verbose=True)
    checking_output = checking_crew.kickoff()
    
    # ============================================
    # STEP 4: EDIT
    # ============================================
    print("\n🎯 STEP 4: EDITING & POLISHING")
    print("-" * 80)
    editing_task = create_editing_task(editor, writing_output, checking_output)
    editing_crew = Crew(agents=[editor], tasks=[editing_task], verbose=True)
    final_output = editing_crew.kickoff()
    
    # ============================================
    # SUMMARY
    # ============================================
    print("\n" + "="*80)
    print("✅ PIPELINE COMPLETE!")
    print("="*80)
    print("\n📄 FINAL OUTPUT:\n")
    print(final_output)
    print("\n" + "="*80 + "\n")
    
    return final_output


if __name__ == "__main__":
    # Example 1: Create a blog post about AI in Healthcare
    result = run_content_pipeline(
        topic="Artificial Intelligence in Healthcare",
        style="informative, engaging, and accessible to general readers"
    )
    
    # Optionally, save the result to a file
    with open("output.md", "w", encoding="utf-8") as f:
        f.write("# Generated Blog Post\n\n")
        # Convert CrewOutput to string
        output_text = str(result) if hasattr(result, '__str__') else result
        f.write(output_text)
    
    print("✅ Output saved to output.md")
