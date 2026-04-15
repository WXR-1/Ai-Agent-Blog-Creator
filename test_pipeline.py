"""
Test suite for the CrewAI Content Pipeline.

This demonstrates how the pipeline works with different scenarios.
Run with: python test_pipeline.py
"""

from main import run_content_pipeline


def test_basic_topic():
    """Test with a simple, general-interest topic."""
    print("\n" + "="*80)
    print("TEST 1: Basic General Interest Topic")
    print("="*80)
    
    result = run_content_pipeline(
        topic="The Power of Reading",
        style="inspirational and engaging"
    )
    
    assert len(result) > 100, "Output should be substantive"
    print("✅ TEST 1 PASSED")
    return result


def test_technical_topic():
    """Test with a technical topic."""
    print("\n" + "="*80)
    print("TEST 2: Technical Topic")
    print("="*80)
    
    result = run_content_pipeline(
        topic="Kubernetes Container Orchestration Basics",
        style="technical, precise, and detailed"
    )
    
    assert len(result) > 100, "Output should be substantive"
    print("✅ TEST 2 PASSED")
    return result


def test_business_topic():
    """Test with a business-focused topic."""
    print("\n" + "="*80)
    print("TEST 3: Business Topic")
    print("="*80)
    
    result = run_content_pipeline(
        topic="Digital Transformation in Retail",
        style="professional, actionable, and business-focused"
    )
    
    assert len(result) > 100, "Output should be substantive"
    print("✅ TEST 3 PASSED")
    return result


def test_educational_topic():
    """Test with an educational topic."""
    print("\n" + "="*80)
    print("TEST 4: Educational Topic")
    print("="*80)
    
    result = run_content_pipeline(
        topic="Climate Change: Causes and Solutions",
        style="educational, balanced, and research-backed"
    )
    
    assert len(result) > 100, "Output should be substantive"
    print("✅ TEST 4 PASSED")
    return result


def run_all_tests():
    """Run all tests."""
    print("\n" + "🧪 RUNNING CREWAI PIPELINE TESTS")
    
    try:
        results = []
        results.append(("General Interest", test_basic_topic()))
        # Uncomment to test more topics (be aware of API rate limits with free tiers)
        # results.append(("Technical", test_technical_topic()))
        # results.append(("Business", test_business_topic()))
        # results.append(("Educational", test_educational_topic()))
        
        print("\n" + "="*80)
        print("✅ ALL TESTS PASSED!")
        print("="*80)
        
        return results
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    run_all_tests()
