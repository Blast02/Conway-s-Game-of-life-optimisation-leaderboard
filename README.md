# 🚀 Game of Life Optimisation Leaderboard  

This repository is a **personal training project** to:  
- Improve my programming skills 👨‍💻  
- Explore **Python optimization techniques** ⚡  
- Learn the basics of **low-level languages** like C, C++, or Rust 🦀  

At first, it was simply a way for me to move beyond Python and try something new.  

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
- Initial grid must be generated using **NumPy random number generator** with **seed = 42**.  

### Table Example  

| Author / Technique | Language | ⏱️ Time (500 ticks) | ⏱️ Time (5,000 ticks) |
|--------------------|----------|---------------------|-----------------------|
| Blast02 / Base version | Python | 14.792s (≈33.8 tick/s) | Too long ❌ |

---

## 🌍 Multi-language Leaderboard  

### Rules  
- Grid size: **1280 × 720** with a cell size of **10 pixels**.  
- The game **must render to the screen** → ❌ terminal output not allowed.  
- Initial grid must be generated with a **random number generator** using **seed = 42**.  

### Table Example  

| Author / Technique | Language | ⏱️ Time (100,000 ticks) | ⏱️ Time (1,000,000 ticks) | ⏱️ Time (5,000,000 ticks) |
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
