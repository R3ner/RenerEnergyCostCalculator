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

## 🌐 Live Web Version

Don't want to run Python code? Use the professional web-based calculator directly in your browser. It features the same logic, real-time taxation, and a modern interface.

👉 **[Launch RECC Web App](https://r3ner.github.io/RenerEnergyCostCalculator/web-version/)**
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

## 🧮 How it Works: The Math Behind RECC

RECC doesn't just multiply values; it simulates a real utility bill breakdown. Here is the mathematical logic used for the calculations:

### 1. Consumption Metrics
First, we establish the hourly burn rate ($C_h$) based on your meter's accumulated data:

$$C_h = \frac{kWh_{acc}}{T_h}$$

Where:
* $kWh_{acc}$ = Total energy reported in Mode 2.
* $T_h$ = Total elapsed time converted to hours.

### 2. The Professional Cost Formula
Unlike basic calculators, we apply the **cascading tax effect** used in the EU/Spanish energy market. The final cost per kWh ($P_{final}$) is calculated as follows:

$$P_{final} = P_{base} \times (1 + IEE) \times (1 + VAT)$$

Where:
* $P_{base}$ = Your raw price per kWh (e.g., 0.17).
* $IEE$ = Electricity Tax (**5.11%** or 0.0511).
* $VAT$ = Value Added Tax (e.g., **21%** or 0.21).

### 3. Hardware Load Projections
For the **LO/HI** analysis, we calculate the theoretical monthly impact if the device stayed in that specific power state 24/7:

$$Cost_{month} = \left( \frac{W}{1000} \right) \times 24 \times 30 \times P_{final}$$

This allows you to see the "financial ceiling" and "financial floor" of your hardware's impact on your wallet.
