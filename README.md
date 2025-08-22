# 🚀 Game of Life Optimisation Leaderboard  

This repository is a **personal training project** to:  
- Improve my programming skills 👨‍💻  
- Explore **Python optimization techniques** ⚡  
- Learn the basics of **low-level languages** like C, C++, or Rust 🦀  

At first, it was simply a way for me to move beyond Python and try something new.  
My first version of the game in Python was made in less than a day, without AI or any form of optimization. I just wanted to have a basic reference implementation.  

---

## 🏆 Project Goal  
I want to keep track of two **leaderboards** for Conway’s Game of Life:  

1. **Python Leaderboard** → Compare different Python optimizations.  
2. **Multi-language Leaderboard** → Compare how fast different programming languages can run the simulation.  

---

## 📊 Python Leaderboard  

### Rules  
- Must be implemented in **Python**.  
- Grid size: **1280 × 720** with a cell size of **10 then 2 pixels**.  
- The game **must render to the screen** (e.g. with `pygame`) → ❌ terminal output not allowed.  
- Initial grid must be generated using **NumPy random integer generator** with **seed = 1337**.  
- The grid must **wrap around (no walls)** 🔄.  

### Python leaderboard  

| Author | Version / Technique | ⏱️ Time 500 steps (10px) | ⏱️ Time 500 steps (2px) |
|--------------------|----------|---------------------|-----------------------|
| Blast02 | V4: v3 + pre-draw grid + move variable to global | **3.073s (≈162.6 steps/s) +4.40X** | 30.407s (≈16.44 steps/s) +10.7X |
| Blast02 | V5: v4 2dconvolution instead of np.roll | 3.108s (≈160.8 steps/s) +4.35X | 26.685s (≈18.73 steps/s) +12.22X |
| Blast02 | V3: V2 + remove unnecessary code | 3.638s (≈137.4 steps/s) +3.72X | 32.860s (≈15.21 steps/s) +9.93X |
| Blast02 | GPT5-thinking-ask-to-opti-2-shot | 3.916s (≈127.6 steps/s) +3.45X | **8.006s (≈62.45 steps/s) +40.75X** |
| Blast02 | V2: Base version + numpy | 4.605s (≈108.5 steps/s) +2.94X | 34.972s (≈14.2 steps/s) +9.33X |
| Blast02 | V1: Base version | 13.549s (≈36.9 steps/s) -- | 326.304s (≈1.5 steps/s) -- |
| Blast02 | GPT5-thinking-no-opti-1-shot | 26.956s (≈18.5 steps/s) -1.36X | 36.376s (≈13.7 steps/s) +8.97X  |

# After the 500 steps 10px your grid should look like this:
<img width="1281" height="720" alt="image" src="https://github.com/user-attachments/assets/8765ca2f-44ef-48b6-bc18-caaa834d95fe" />


# After the 500 steps 2px your grid should look like this:
<img width="1283" height="717" alt="image" src="https://github.com/user-attachments/assets/2f2e3f39-a2e3-44e6-9cf7-cc83cf7e1e29" />

---

## 🌍 Multi-language Leaderboard  

### Rules  
- Grid size: **1280 × 720** with a cell size of **10 then 5 then 2 pixels**.  
- The game **must render to the screen** → ❌ terminal output not allowed.  
- Initial grid must be generated with a **random integers generator** using **seed = 1337**.  
- The grid must **wrap around (no walls)** 🔄.  

### Multi-language leaderboard  

| Author | Version / Technique | Language | ⏱️ Time 100,000 steps (10px) | ⏱️ Time 1,000,000 steps (5px) | ⏱️ Time 5,000,000 steps (2px) |
|---------|-----------|----------|-------------------------|---------------------------|---------------------------|
| –        |-          | –        | –                       | –                         | –                         |

---

## 🤝 How to Contribute  

Want to add your version to the leaderboard? Here’s how:  

1. **Fork** this repository.  
2. Add your implementation in a new folder with a clear name (e.g. `python_numpy_optim` or `rust_base`).  
3. Run your implementation with the rules described above and measure execution time.  
4. Update the corresponding **leaderboard table** in this README with your results.  
5. Submit a **pull request** 🚀.  

---

👉 The idea is not just competition, but also **learning from different implementations** and seeing how far optimization can go.  
