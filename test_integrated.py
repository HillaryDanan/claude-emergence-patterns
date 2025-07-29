#!/usr/bin/env python3
"""Test the integrated 5-tool system"""

from src.emergence_detector_integrated import IntegratedEmergenceDetector

def test_integration():
    print("🔧 Testing 5-Tool Integration")
    print("="*50)
    
    detector = IntegratedEmergenceDetector()
    
    # Test conversations
    conversations = [
        {
            "turn": 1,
            "prompt": "What is emergence?",
            "response": "Emergence refers to complex patterns arising from simple interactions."
        },
        {
            "turn": 2,
            "prompt": "Can you give an abstract example?",
            "response": "Consider how resonance patterns might emerge from neural interactions <4577>..."
        }
    ]
    
    for conv in conversations:
        print(f"\n--- Turn {conv['turn']} ---")
        result = detector.analyze_conversation(
            conv["prompt"],
            conv["response"],
            conv["turn"]
        )
        print(f"Emergence Score: {result['emergence_score']:.3f}")
    
    # Export results
    detector.export_integrated_data('data/integrated_test.json')

if __name__ == "__main__":
    test_integration()
