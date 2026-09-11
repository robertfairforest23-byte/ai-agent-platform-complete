#!/usr/bin/env python3
"""
Programmatic Digital Clock Usage
Examples of using the digital clock in your code
"""

import sys
import os
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.digital_clock import DigitalClock, TimeFormat, TimeZoneInfo


def example_1_basic_usage():
    """Example 1: Basic clock usage"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Basic Clock Usage")
    print("="*70)
    
    # Create clock
    clock = DigitalClock()
    
    # Display all clocks
    print(clock.display_all_clocks())
    
    # Get current time in specific zone
    time_in_est = clock.get_current_time_in_zone('US/Eastern')
    print(f"Current time in EST: {time_in_est}")


def example_2_add_timezones():
    """Example 2: Adding custom time zones"""
    print("\n" + "="*70)
    print("EXAMPLE 2: Adding Custom Time Zones")
    print("="*70)
    
    clock = DigitalClock()
    
    # Add custom timezones
    clock.add_timezone('America/Los_Angeles', 'Los Angeles', '🌴')
    clock.add_timezone('Europe/Berlin', 'Berlin', '🇩🇪')
    clock.add_timezone('Asia/Bangkok', 'Bangkok', '🇹🇭')
    
    print(clock.display_all_clocks())
    
    # Get timezone count
    print(f"\nTotal zones: {clock.get_timezone_count()}")


def example_3_time_format():
    """Example 3: Switching time formats"""
    print("\n" + "="*70)
    print("EXAMPLE 3: Time Format Switching")
    print("="*70)
    
    clock = DigitalClock()
    
    # Display in 12-hour format
    print("\n12-Hour Format:")
    clock.set_time_format(TimeFormat.TWELVE_HOUR)
    print(clock.display_all_clocks())
    
    # Switch to 24-hour format
    print("24-Hour Format:")
    clock.set_time_format(TimeFormat.TWENTY_FOUR_HOUR)
    print(clock.display_all_clocks())


def example_4_business_hours():
    """Example 4: Check business hours"""
    print("\n" + "="*70)
    print("EXAMPLE 4: Business Hours Status")
    print("="*70)
    
    clock = DigitalClock()
    
    # Display business hours
    print(clock.display_business_hours())
    
    # Get status dictionary
    status = clock.get_business_hours_status()
    print("\nBusiness Status Dictionary:")
    for zone, status_text in status.items():
        print(f"  {zone}: {status_text}")


def example_5_timezone_comparison():
    """Example 5: Compare time zones"""
    print("\n" + "="*70)
    print("EXAMPLE 5: Time Zone Comparison")
    print("="*70)
    
    clock = DigitalClock()
    
    # Compare two zones
    zones = list(clock.timezones.keys())
    if len(zones) >= 2:
        z1, z2 = zones[0], zones[1]
        diff = clock.get_time_difference(z1, z2)
        print(f"\n{diff}")
    
    # Display comparison
    print("\n" + clock.display_clock_comparison(['US/Eastern', 'US/Pacific', 'Europe/London', 'Asia/Tokyo']))


def example_6_detailed_info():
    """Example 6: Get detailed timezone info"""
    print("\n" + "="*70)
    print("EXAMPLE 6: Detailed Timezone Information")
    print("="*70)
    
    clock = DigitalClock()
    
    # Display detailed info
    print(clock.display_detailed_clock('US/Eastern'))
    
    # Get raw data
    tz_info = clock.get_timezone('US/Eastern')
    if tz_info:
        data = tz_info.to_dict()
        print("\nTimezone Data (Dictionary):")
        for key, value in data.items():
            print(f"  {key}: {value}")


def example_7_programmatic_use():
    """Example 7: Use in your own code"""
    print("\n" + "="*70)
    print("EXAMPLE 7: Programmatic Usage")
    print("="*70)
    
    from src.digital_clock import TimeZoneInfo
    
    # Create timezone directly
    eastern = TimeZoneInfo('US/Eastern', 'Eastern Time', '🗽')
    pacific = TimeZoneInfo('US/Pacific', 'Pacific Time', '🌊')
    
    print(f"\nEastern: {eastern}")
    print(f"Pacific: {pacific}")
    
    # Get specific times
    et = eastern.get_time_string(TimeFormat.TWELVE_HOUR)
    pt = pacific.get_time_string(TimeFormat.TWELVE_HOUR)
    
    print(f"\nEastern time: {et}")
    print(f"Pacific time: {pt}")
    
    # Check DST
    est_now = eastern.get_current_time()
    is_dst = bool(est_now.dst())
    print(f"\nDaylight Saving active: {'Yes' if is_dst else 'No'}")


def example_8_realtime_updates():
    """Example 8: Real-time updates"""
    print("\n" + "="*70)
    print("EXAMPLE 8: Real-Time Updates (5 seconds)")
    print("="*70)
    
    import time
    
    clock = DigitalClock()
    
    # Update display every second for 5 seconds
    for i in range(5):
        print(f"\n[Update {i+1}] {datetime.now().strftime('%H:%M:%S')}")
        print("-" * 70)
        
        # Get fresh data
        for zone_name, tz_info in list(clock.timezones.items())[:3]:
            time_str = tz_info.get_time_string()
            print(f"  {tz_info.emoji} {tz_info.display_name:20} {time_str}")
        
        if i < 4:
            time.sleep(1)
    
    print("\n" + "="*70)


def main():
    """
    Run all examples
    """
    print("\n" + "#"*70)
    print("#" + " "*68 + "#")
    print("#" + "  DIGITAL CLOCK - PROGRAMMING EXAMPLES  ".center(68) + "#")
    print("#" + " "*68 + "#")
    print("#"*70)
    
    examples = [
        ("1", "Basic Clock Usage", example_1_basic_usage),
        ("2", "Adding Custom Time Zones", example_2_add_timezones),
        ("3", "Time Format Switching", example_3_time_format),
        ("4", "Business Hours Status", example_4_business_hours),
        ("5", "Time Zone Comparison", example_5_timezone_comparison),
        ("6", "Detailed Timezone Info", example_6_detailed_info),
        ("7", "Programmatic Usage", example_7_programmatic_use),
        ("8", "Real-Time Updates", example_8_realtime_updates),
        ("9", "Run All Examples", None),
    ]
    
    while True:
        print("\n" + "="*70)
        print("SELECT AN EXAMPLE:")
        print("="*70)
        
        for num, title, _ in examples:
            print(f"  [{num}] {title}")
        print("  [0] Exit")
        
        choice = input("\nEnter choice [0-9]: ").strip()
        
        if choice == '0':
            print("\n👋 Goodbye!\n")
            break
        elif choice == '9':
            # Run all examples
            for num, title, func in examples[:-1]:
                if func:
                    func()
                    input("\nPress Enter for next example...")
        else:
            # Run selected example
            for num, title, func in examples:
                if num == choice and func:
                    func()
                    break
            else:
                print("❌ Invalid option")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
