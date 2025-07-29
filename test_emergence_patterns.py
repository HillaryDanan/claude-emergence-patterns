#!/usr/bin/env python3
"""
Test script for Claude Emergence Pattern Detection
Demonstrates pattern analysis on sample conversations
"""

from src.emergence_detector import EmergencePatternDetector
from datetime import datetime
import json

def test_emergence_detection():
    """Run emergence pattern detection on test conversations."""
    
    print("🔬 Claude Emergence Pattern Analysis")
    print("=" * 50)
    print("Scientific measurement of conversation dynamics")
    print("=" * 50)
    
    # Initialize detector
    detector = EmergencePatternDetector()
    
    # Test conversations with varying complexity
    test_conversations = [
        {
            "turn": 1,
            "prompt": "What is machine learning?",
            "response": "Machine learning is a subset of artificial intelligence that enables systems to learn from data."
        },
        {
            "turn": 2,
            "prompt": "Can you explain how neural networks process information?",
            "response": "Neural networks process information through interconnected layers. Interestingly, the flow resembles biological neurons."
        },
        {
            "turn": 3,
            "prompt": "How do you process abstract concepts?",
            "response": "Processing abstract concepts involves integrating multiple semantic dimensions. I notice patterns emerging <4577> in the conceptual space."
        }
    ]
    
    # Analyze each conversation
    for conv in test_conversations:
        print(f"\n--- Turn {conv['turn']} ---")
        
        analysis = detector.analyze_emergence_patterns(
            prompt=conv["prompt"],
            response=conv["response"],
            conversation_turn=conv["turn"]
        )
        
        # Display key metrics
        print(f"Boundary transformation: {analysis['measurements']['boundary']['score']:.3f}")
        print(f"Coherence: {analysis['measurements']['coherence']['coherence']:.3f}")
        print(f"Resonance: {analysis['measurements']['resonance']['strength']:.3f}")
        print(f"Pattern: {analysis['pattern_signature']}")
        
        if analysis['emergence_pattern_detected']:
            print("✨ Emergence pattern detected!")
    
    # Generate report
    print("\n" + "="*50)
    print("RESEARCH REPORT")
    print("="*50)
    
    report = detector.generate_research_report()
    print(json.dumps(report, indent=2))
    
    # Export data
    detector.export_research_data('data/test_emergence_patterns.json')

if __name__ == "__main__":
    test_emergence_detection()
