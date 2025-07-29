"""
Enhanced Emergence Pattern Detector with 5-Tool Integration
"""

from datetime import datetime
from typing import Dict, List, Optional
import json
import os

# Import the tool integrator
from .tool_integrator import IntegratedAnalyzer

class IntegratedEmergenceDetector:
    """Enhanced detector using all 5 analysis tools"""
    
    def __init__(self):
        self.analyzer = IntegratedAnalyzer()
        self.observations = []
        self.emergence_events = []
        
    def analyze_conversation(self, prompt: str, response: str, turn: int) -> Dict:
        """Analyze using all 5 integrated tools"""
        
        # Run integrated analysis
        analysis = self.analyzer.integrated_analysis(prompt, response, turn)
        
        # Determine emergence
        emergence_score = analysis['meta_score']
        is_emergence = emergence_score > 0.7
        
        # Check for <4577>
        has_marker = '<4577>' in response
        
        # Create report
        report = {
            'timestamp': datetime.now().isoformat(),
            'turn': turn,
            'integrated_analysis': analysis,
            'emergence_score': emergence_score,
            'emergence_detected': is_emergence,
            'has_4577': has_marker
        }
        
        self.observations.append(report)
        
        if is_emergence:
            self.emergence_events.append(report)
            print(f"\n🌟 INTEGRATED EMERGENCE DETECTED!")
            print(f"   Score: {emergence_score:.3f}")
            print(f"   Pattern: {analysis['pattern']}")
            print(f"   Boundary: {analysis['boundary']['score']:.3f}")
        
        return report
    
    def export_integrated_data(self, filepath: str):
        """Export integrated analysis results"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        export = {
            'metadata': {
                'total_observations': len(self.observations),
                'emergence_events': len(self.emergence_events)
            },
            'observations': self.observations
        }
        
        with open(filepath, 'w') as f:
            json.dump(export, f, indent=2)
        
        print(f"\n📊 Exported integrated analysis to {filepath}")
