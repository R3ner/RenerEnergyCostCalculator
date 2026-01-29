#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import re
import time
import os

# ==== Function to clear console ====
def clear_console():
    # Windows: cls | Linux/Mac: clear
    os.system('cls' if os.name == 'nt' else 'clear')

# ==== Welcome banner ====
def welcome_banner():
    print("🟢==================================================🟢")
    print("💡 Rener Energy Cost Calculator (RECC) 💡")
    print("Created by: R3ner")
    print("Date & Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("🟢==================================================🟢\n")

    print("🔹 Units reference:")
    print("   s = seconds, m = minutes, h = hours, d = days, w = weeks, Mo = months")
    print("🔹 Example: '1d16h46m' means 1 day, 16 hours, 46 minutes\n")
    
    print("⚡ Tool Usage Instructions:")
    print("1️⃣ Access the following MODES on your energy meter:")
    print("   - MODE 2: Accumulated kWh and Elapsed Time")
    print("   - MODE 5 & 6: Min/Max Power (LO/HI) in Watts (Optional)")
    print("   - Price per kWh (€) and your local Tax/VAT %")
    print("2️⃣ Enter the data when prompted.")
    print("3️⃣ The tool will calculate professional energy consumption and costs.")
    print("\n❓ Confused about what MODES are? Check the documentation:")
    print("📚 https://github.com/R3ner/RenerEnergyCostCalculator")
    print("🟢==================================================🟢\n")

# ==== Function to parse time strings ====
def parse_time_string(time_str):
    pattern = r'(\d+\.?\d*)(s|m|h|d|w|Mo)'
    matches = re.findall(pattern, time_str)
    total_hours = 0
    if not matches: return 0
    for value, unit in matches:
        value = float(value)
        if unit == 's': total_hours += value / 3600
        elif unit == 'm': total_hours += value / 60
        elif unit == 'h': total_hours += value
        elif unit == 'd': total_hours += value * 24
        elif unit == 'w': total_hours += value * 24 * 7
        elif unit == 'Mo': total_hours += value * 24 * 30
    return total_hours

# ==== Function to calculate professional costs ====
def calculate_costs_pro(kwh_acc, time_h, price_kwh, tax_iva, low_w=None, high_w=None):
    kwh_per_hour = kwh_acc / time_h
    iee_factor = 1.0511  # Electricity Tax (5.11%)
    iva_factor = 1 + (tax_iva / 100)
    real_price_kwh = price_kwh * iee_factor * iva_factor
    
    cost_hour = kwh_per_hour * real_price_kwh
    cost_daily = cost_hour * 24
    
    results = {
        "💡 Average Consumption (kWh/h)": round(kwh_per_hour, 4),
        "💡 Real Price (with all Taxes)": f"{real_price_kwh:.4f} €/kWh",
        "💡 Daily cost (€)": round(cost_daily, 2),
        "💡 Weekly cost (€)": round(cost_daily * 7, 2),
        "💡 Monthly cost (€)": round(cost_daily * 30, 2),
        "💡 Monthly consumption (kWh)": round(kwh_per_hour * 24 * 30, 2),
    }

    # Optional LO/HI calculation
    if low_w is not None:
        cost_mo_lo = (low_w / 1000) * 24 * 30 * real_price_kwh
        results["📉 Idle/Low state cost (LO)"] = f"{cost_mo_lo:.2f} €/month"
    else:
        results["📉 Idle/Low state cost (LO)"] = "SKIPPED"

    if high_w is not None:
        cost_mo_hi = (high_w / 1000) * 24 * 30 * real_price_kwh
        results["📈 Peak/High state cost (HI)"] = f"{cost_mo_hi:.2f} €/month"
    else:
        results["📈 Peak/High state cost (HI)"] = "SKIPPED"

    return results

# ==== Main program ====
def main():
    welcome_banner()

    try:
        # Step 1: Consumption & Time
        kwh_acc = float(input("Enter accumulated kWh (Mode 2, e.g., 2.935): "))
        time_input = input("Enter elapsed time (e.g., 1d18h06m): ")
        
        # Step 2: Power Load (With Skip option)
        print("\n(Press Enter to skip if you don't have LO/HI values)")
        low_raw = input("Enter Min Power (LO) in Watts: ")
        high_raw = input("Enter Max Power (HI) in Watts: ")
        
        low_watts = float(low_raw) if low_raw.strip() else None
        high_watts = float(high_raw) if high_raw.strip() else None
        
        # Step 3: Billing
        price_per_kwh = float(input("\nEnter price per kWh (€, e.g., 0.17): "))
        iva_percent = float(input("Enter VAT/IVA % (e.g., 21): "))

        # Parsing time
        time_hours = parse_time_string(time_input)
        if time_hours == 0:
            print("❌ Error: Invalid time format.")
            return

        # "Think before cleanaing" 
        print("\n⏳ Calculating metrics...")
        time.sleep(2)
        clear_console()

        results = calculate_costs_pro(kwh_acc, time_hours, price_per_kwh, iva_percent, low_watts, high_watts)

        # Display results
        print("🟢==================================================🟢")
        print("💡 Rener Energy Cost Calculator (RECC) - RESULTS 💡")
        print("🟢==================================================🟢")
        for key, value in results.items():
            print(f"{key}: {value}")
        print("🟢==================================================🟢\n")

    except ValueError:
        print("❌ Error: Invalid input. Please make sure to enter numbers correctly.")

    # Final Footer
    print("🙏 Thank you for using RECC!")
    print("If you find this tool useful, give it a star⭐: https://github.com/R3ner/RenerEnergyCostCalculator\n")

if __name__ == "__main__":
    main()