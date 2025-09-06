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
```python
rng = numpy.random.default_rng(seed=1337) #seed set to 1337
current_grid = rng.integers(0, 2, size=(int(window_height / cell), int(window_width / cell)), dtype=int)
```
- The grid must **wrap around (no walls)** 🔄.  

### Python leaderboard  

| Author | Version / Technique | ⏱️ Time 500 steps (10px) | ⏱️ Time 500 steps (2px) |
|--------------------|----------|---------------------|-----------------------|
| Blast02 | V4: v3 + pre-draw grid + move variable to global | **`1.551s (322.3 steps/s) 792%`** | 25.641s (19.4 steps/s) 1228.5% |
| Blast02 | V5: v4 2dconvolution instead of np.roll | 1.561s (320.2 steps/s) 786.9% | 24.111s (20.7 steps/s) 1306.4% |
| Blast02 | GPT5-thinking-ask-to-opti-2-shot | 1.683s (297 steps/s) 729.8% | **`4.670s (107 steps/s) 6745.1%`** |
| Blast02 | V3: V2 + remove unnecessary code | 1.757s (284.5 steps/s) 699.1% | 27.613s (18.1 steps/s) 1140% |
| Blast02 | V2: Base version + numpy | 2.442s (204.6 steps/s) 503% | 28.162s (17.7 steps/s) 1118.5% |
| Blast02 | V1: Base version | 12.284s (40.7 steps/s) 100% | 315s (1.5 steps/s) 100% |
| Blast02 | GPT5-thinking-no-opti-1-shot | 19.760s (25.3 steps/s) 62.1% | 21.636s (23.1 steps/s) 1455.9%  |

# After the 500 steps 10px your grid should look like this:
<img width="1281" height="720" alt="image" src="https://github.com/user-attachments/assets/8765ca2f-44ef-48b6-bc18-caaa834d95fe" />


# After the 500 steps 2px your grid should look like this:
<img width="1283" height="717" alt="image" src="https://github.com/user-attachments/assets/2f2e3f39-a2e3-44e6-9cf7-cc83cf7e1e29" />

---

## 🌍 Multi-language Leaderboard  

### Rules  
- Grid size: **1280 × 720** with a cell size of **10 then 5 then 2 pixels**.  
- The game **must render to the screen** → ❌ terminal output not allowed.  
- Initial grid must be generated with mersenne twister **random integers generator** using **seed = 49**.
```cpp
std::mt19937 rng(49);
std::uniform_int_distribution<int> dist(0, 1);
```
- The grid must **wrap around (no walls)** 🔄.  

### Multi-language leaderboard  

| Author | Version / Technique | Language | ⏱️ Time 5,000 steps (10px) | ⏱️ Time 5,000 steps (5px) | ⏱️ Time 5,000 steps (2px) |
|---------|-----------|----------|-------------------------|---------------------------|---------------------------|
| Blast02 | V1: Base version | C++ | 1.156s (4324.5 steps/s) 100% | 3.0763s (1625.3 steps/s) 100% | 17.308 (288.8 steps/s) 100% |

# After the 5,000 steps 10px your grid should look like this:
<img width="1281" height="720" alt="image" src="https://github.com/user-attachments/assets/4ad1ae97-ba97-47e9-bbc2-2d2267f30d1c" />

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
