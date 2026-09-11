#!/usr/bin/env python3
"""
Simple Digital Clock - Minimal Version
Displays current time in multiple time zones
"""

import sys
import os
import time
from datetime import datetime
import pytz

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.digital_clock import DigitalClock


def main():
    """
    Simple clock display
    """
    print("\n" + "="*70)
    print("\t⏰ SIMPLE DIGITAL CLOCK ⏰")
    print("="*70 + "\n")
    
    # Create clock
    clock = DigitalClock()
    
    # Display
    print(clock.display_all_clocks())
    
    # Show business hours
    print(clock.display_business_hours())
    
    # Interactive options
    while True:
        print("\nOptions:")
        print("  [1] Refresh clocks")
        print("  [2] Show detailed info for a timezone")
        print("  [3] Compare time zones")
        print("  [4] Switch format (12h/24h)")
        print("  [5] Exit")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n" + "="*70)
            print("\t⏰ SIMPLE DIGITAL CLOCK ⏰")
            print("="*70 + "\n")
            print(clock.display_all_clocks())
        
        elif choice == '2':
            zones = list(clock.timezones.keys())
            print("\nAvailable zones:")
            for i, zone in enumerate(zones, 1):
                tz_info = clock.get_timezone(zone)
                print(f"  [{i}] {tz_info.display_name}")
            
            try:
                idx = int(input("\nSelect zone: ")) - 1
                if 0 <= idx < len(zones):
                    print("\n" + clock.display_detailed_clock(zones[idx]))
            except ValueError:
                print("Invalid input")
        
        elif choice == '3':
            zones = list(clock.timezones.keys())
            if len(zones) >= 2:
                z1, z2 = zones[0], zones[1]
                diff = clock.get_time_difference(z1, z2)
                print(f"\n{diff}\n")
        
        elif choice == '4':
            from src.digital_clock import TimeFormat
            current = clock.time_format.value
            new = input(f"Current: {current}. Switch to [12h/24h]? ").strip().lower()
            if new == '24h':
                clock.set_time_format(TimeFormat.TWENTY_FOUR_HOUR)
                print("✅ Switched to 24-hour")
            elif new == '12h':
                clock.set_time_format(TimeFormat.TWELVE_HOUR)
                print("✅ Switched to 12-hour")
        
        elif choice == '5':
            print("\n👋 Goodbye!\n")
            break
        
        else:
            print("Invalid option")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
