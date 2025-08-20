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
- Grid size: **1280 × 720** with a cell size of **10 pixels**.  
- The game **must render to the screen** (e.g. with `pygame`) → ❌ terminal output not allowed.  
- Initial grid must be generated using **NumPy random integer generator** with **seed = 1337**.  
- The grid must **wrap around (no walls)** 🔄.  

### Python leaderboard  

| Author / Technique | Language | ⏱️ Time (500 steps) | ⏱️ Time (5,000 steps) |
|--------------------|----------|---------------------|-----------------------|
| Blast02 / Base version + numpy | Python | 4.605s (≈108.573 steps/s) 2,94X faster| 38.920s (≈128.468 steps/s) 3.44X faster |
| Blast02 / Base version | Python | 13.549s (≈36.901 steps/s) -- | 134.232s (≈37.248 steps/s) -- |
| Blast02 / GPT5 | Python | 26.956s (≈18,548 steps/s) 1.36X slower | 239.830s (≈20,848 steps/s) 1.78X slower |

# After the 500 steps your grid should look like this:
<img width="1601" height="896" alt="image" src="https://github.com/user-attachments/assets/191b551f-5e64-4b10-8fc8-a0e0900b52f4" />

# After the 5,000 steps your grid should look like this:
<img width="1599" height="900" alt="image" src="https://github.com/user-attachments/assets/d8387663-fe54-40fe-ae19-8cbad9d2682f" />

---

## 🌍 Multi-language Leaderboard  

### Rules  
- Grid size: **1280 × 720** with a cell size of **10 pixels**.  
- The game **must render to the screen** → ❌ terminal output not allowed.  
- Initial grid must be generated with a **random integers generator** using **seed = 1337**.  
- The grid must **wrap around (no walls)** 🔄.  

### Multi-language leaderboard  

| Author / Technique | Language | ⏱️ Time (100,000 steps) | ⏱️ Time (1,000,000 steps) | ⏱️ Time (5,000,000 steps) |
|--------------------|----------|-------------------------|---------------------------|---------------------------|
| –                  | –        | –                       | –                         | –                         |

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
