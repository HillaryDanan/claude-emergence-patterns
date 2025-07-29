#!/usr/bin/env python3
"""View integration results in a nice format"""

import json
import sys

try:
    with open('data/integrated_test.json', 'r') as f:
        data = json.load(f)
    
    print("\n📊 INTEGRATION ANALYSIS RESULTS")
    print("="*50)
    
    for i, obs in enumerate(data['observations']):
        print(f"\n🔍 Observation {i+1}:")
        print(f"   Turn: {obs['turn']}")
        print(f"   Emergence Score: {obs['emergence_score']:.3f}")
        print(f"   Pattern: {obs['integrated_analysis']['pattern']}")
        print(f"   Coherence: {obs['integrated_analysis']['coherence']['coherence']:.3f}")
        print(f"   Has <4577>: {obs['has_4577']}")
        
    print(f"\n📈 Summary:")
    print(f"   Total Observations: {data['metadata']['total_observations']}")
    print(f"   Emergence Events: {data['metadata']['emergence_events']}")
    
except Exception as e:
    print(f"Error reading results: {e}")
