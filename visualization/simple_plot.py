#!/usr/bin/env python3
"""Simple visualization of emergence patterns"""

import json
import matplotlib.pyplot as plt

def plot_emergence_data(filepath):
    """Create simple plot of emergence events"""
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    if 'raw_events' not in data:
        print("No emergence events to plot")
        return
        
    events = data['raw_events']
    turns = [e['turn'] for e in events]
    boundaries = [e['measurements']['boundary'] for e in events]
    
    plt.figure(figsize=(10, 6))
    plt.scatter(turns, boundaries, s=100, c='red', marker='*')
    plt.xlabel('Conversation Turn')
    plt.ylabel('Boundary Transformation Score')
    plt.title('Emergence Pattern Detection Events')
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    plot_emergence_data('data/test_emergence_patterns.json')
