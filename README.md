# 💡 Rener Energy Cost Calculator (RECC)

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**RECC** is a professional-grade CLI tool designed to bridge the gap between "what your energy meter says" and "what you actually pay." Specifically optimized for 24/7 hardware like **Minecraft Servers**, Home Labs, and Workstations.

Unlike basic calculators, RECC accounts for **cascading taxation** (Electricity Tax + VAT) and provides hardware load analysis based on real-time power peaks.

---

## 🚀 Features

* **Precise Time Parsing:** Supports complex formats like `1d18h06m` or `1w2d`.
* **Professional Taxation:** Automatically applies the **Spanish/EU Electricity Tax (IEE 5.11%)** and customizable **VAT/IVA**.
* **Hardware Load Range:** Optional analysis for Minimum (LO) and Maximum (HI) power states to predict budget boundaries.
* **Clean UI:** Features a streamlined interface with "Calculating..." visual effects and console management.
* **Universal Compatibility:** Works with most plug-in energy meters (Mode-based logic).

---


## 📸 Understanding Your Energy Meter
<img width="128" height="256" alt="Gemini_Generated_Image_rngqtfrngqtfrngq-removebg-preview" src="https://github.com/user-attachments/assets/f76b9d94-c4c2-494e-82ea-af0d022bbca8" />


<img width="798" height="313" alt="image-removebg-preview" src="https://github.com/user-attachments/assets/5fb7a5c0-c2e6-4967-a3a8-abaaf66fb64b" />

*Figure 1: Technical diagram of the standard energy meter interface used for RECC logic.*

> [!NOTE]  
> This documentation and the script's logic are based on the **generic high-precision energy meters** shown above. While most "white-label" devices follow this exact 7-Mode structure, your specific button layout or screen order might vary slightly. **RECC** specifically requires data from **MODE 2** (Accumulated Energy/Time) and optionally **MODE 5 & 6** (Power Peaks).

To get accurate results, you need to navigate through your device's **MODES**. While brands vary, most follow this standard:

| Mode | Metric | Description |
| :--- | :--- | :--- |
| **MODE 2** | **kWh & Time** | The most important data. Total energy consumed and total time elapsed. |
| **MODE 5** | **LO (Watts)** | The lowest power draw recorded (usually when your server is idle). |
| **MODE 6** | **HI (Watts)** | The highest power peak recorded (usually during startup or heavy load). |
| **MODE 7** | **Cost/kWh** | Your base electricity rate (e.g., 0.17 €/kWh). |

> [!IMPORTANT]  
> **Decimal Tip:** Always use a period `.` for decimals (e.g., `2.935` kWh). Entering `2935` without a decimal will result in astronomical cost projections!

---

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/R3ner/RenerEnergyCostCalculator.git
   cd RenerEnergyCostCalculator
2. **Run the script:**
  ```bash
  python recc.py
  ```
3. **Follow the prompts:**

Enter your accumulated kWh and time from Mode 2.

(Optional) Enter LO/HI Watts or press `Enter` to skip.

Enter your electricity price and local tax percentage.
