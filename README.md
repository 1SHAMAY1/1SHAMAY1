<!-- HEADER -->
<h1 align="center">⚡ SHANKHARAJ DATTA (1SHAMAY1)</h1>
<h3 align="center">Systems & Silicon Engineer • C++ & SystemVerilog Developer • Low-Level & AI Architect</h3>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?size=22&duration=3500&color=00A3FF&center=true&vCenter=true&width=700&lines=RTL+Design+%26+Silicon+Architect;Embedded+Systems+%26+Driver+Developer;Gameplay+Systems+%26+Physics+Engineer;C%2B%2B+%26+SystemVerilog+Enthusiast;Building+High-Performance+Swarms" />
</p>

---

# 🧩 About Me
I design and implement **high-performance systems** across the entire stack—ranging from synthesizable **RTL SoC Interconnects** and **GPU vector architectures** to **low-level bare-metal device drivers**, **data-oriented physics engines (ECS)**, and **distributed machine learning models**.

**Focus Areas**
- **Hardware/Silicon Design** – Synthesizable SystemVerilog, AXI4 Network-on-Chip (NoC) crossbars, and SIMT GPU architectures
- **Systems & Embedded Programming** – Bare-metal C driver development, Memory-Mapped I/O (MMIO), ring buffers, and custom hardware/software co-design
- **Simulation & Engine Tech** – Data-Oriented Design (DOD), Entity-Component-Systems (ECS), custom XPBD physics engines, and procedural C++ locomotion
- **Distributed AI & Machine Learning** – Swarm intelligence frameworks, temporal/predictive ML pipelines, and agent consensus protocols

---

# 🛠 Tech Stack

### Languages & HDLs  
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=flat&logo=cplusplus&logoColor=white)
![SystemVerilog](https://img.shields.io/badge/SystemVerilog-1A5F7A?style=flat&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=flat&logo=c&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

### Hardware, VLSI & Embedded Systems
<img alt="AXI4 Protocol" src="https://img.shields.io/badge/AXI4_Protocol-007ACC?style=flat" />
<img alt="Yosys Synthesis" src="https://img.shields.io/badge/Yosys_Synthesis-FF6B6B?style=flat" />
<img alt="Riviera Pro" src="https://img.shields.io/badge/Riviera_PRO-00A86B?style=flat" />
<img alt="Bare-Metal C" src="https://img.shields.io/badge/Bare--Metal_C-8A2BE2?style=flat" />
<img alt="MMIO" src="https://img.shields.io/badge/MMIO_/_Register_Access-D2A200?style=flat" />

### Frameworks & Engines  
![Unreal Engine 5](https://img.shields.io/badge/Unreal_Engine_5-313131?style=flat&logo=unrealengine&logoColor=white)
![OpenGL](https://img.shields.io/badge/OpenGL-5586A4?style=flat&logo=opengl&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![Raylib](https://img.shields.io/badge/Raylib-1E78C7?style=flat)

### Concepts & Paradigms
<img alt="OOP" src="https://img.shields.io/badge/OOPs-007ACC?style=flat" />
<img alt="Data-Oriented Design (DOD)" src="https://img.shields.io/badge/DOD_/_ECS-00A86B?style=flat" />
<img alt="Parallel Programming" src="https://img.shields.io/badge/SIMT_/_Vector-8A2BE2?style=flat" />
<img alt="Deep Learning" src="https://img.shields.io/badge/Deep_Learning-E34F26?style=flat" />

---

# 🚀 Featured Projects  

## 🔌 Low-Level Systems & Silicon (RTL & Drivers)

### 🌐 UMA SoC Interconnect  
**Apple M-Series style Unified Memory Architecture (UMA) SoC Interconnect** designed in synthesizable SystemVerilog.  
[![UMA SoC](https://img.shields.io/badge/UMA_SoC_Interconnect-000000?style=for-the-badge&logo=github)](https://github.com/1SHAMAY1/UMA_SoC_Interconnect)

- **2x1 AXI4 Crossbar** – Custom Network-on-Chip (NoC) router arbitrating between CPU (M0) and GPU (M1) bus masters.
- **Fixed-Priority Arbitration** – Real-time priority arbiter guaranteeing high-bandwidth GPU access over CPU.
- **Transaction Routing** – Uses AXI transaction IDs (`s0_bid` / `s0_rid`) to route responses back to the correct initiator without bus stalls.
- **Wide UMA Memory Controller** – Connected to a 256-bit wide data bus to maximize throughput to a shared SRAM segment.
- **Gate-Level Synthesis** – Compiles via Yosys with full schematic generation mapping multiplexers and logic blocks.

---

### 🏎️ GPU Compute Core & Ray-Tracing Accelerator  
**SIMT GPU Streaming Multiprocessor (SM)** integrated with a dedicated **Ray-Tracing Compute Unit (RTCU)**.  
[![GPU Core](https://img.shields.io/badge/GPU_Compute_Core-000000?style=for-the-badge&logo=github)](https://github.com/1SHAMAY1/GPU_Compute_Core)

- **SIMT Architecture** – 32-lane vector streaming multiprocessor managing execution masks across a parallel warp.
- **Ray-Tracing Co-processor** – Dedicated hardware block executing parallel Bounding Volume Hierarchy (BVH) node traversals and Möller-Trumbore ray-triangle intersections.
- **Custom Graphics ISA** – Custom instruction decoder dispatching ray-tracing operations directly to the RTCU over a 1024-bit packed vector bus.
- **Architectural Simulator** – Cycle-accurate Python model (`gpu_sim.py`) that functionalizes camera ray generation and path-traces scenes.

---

### 💻 Graphics Driver API  
**Bare-metal C GPU device driver** engineered to interface a CPU application with the GPU Compute Core over a Unified Memory Interconnect.  
[![Graphics Driver](https://img.shields.io/badge/Graphics_Driver_API-000000?style=for-the-badge&logo=github)](https://github.com/1SHAMAY1/Graphics_Driver_API)

- **Command Ring Buffer** – Non-blocking, circular command queue allowing asynchronous graphics task submissions from CPU to GPU.
- **MMIO Doorbell Signaling** – Directly triggers hardware execution by writing CPU-written ring indexes to Memory-Mapped I/O registers.
- **Zero-Copy Memory Allocations** – Utilizes a shared UMA heap allocation (`uma_alloc`) to pass raw pointers directly to the GPU, bypassing expensive PCIe bus transfers.
- **Silicon Verification Test** – Standalone testing framework verifying physical queue operations and doorbell interrupts.

---

## 🦾 Physics & Simulation Engines

### ⚡ Velox  
**High-performance 2D physics engine** written in modern C++ utilizing Data-Oriented Design (DOD) and an XPBD solver.  
[![Velox](https://img.shields.io/badge/Velox-000000?style=for-the-badge&logo=github)](https://github.com/1SHAMAY1/Velox)

- **Data-Oriented ECS** – Custom Entity-Component-System architecture optimized for L1/L2 cache line locality.
- **XPBD Solver** – Extended Position-Based Dynamics solver for stable stacking, rigid body constraints, and stiff constraint resolution.
- **Broadphase Collision** – Spatial Hash Grid reducing comparison complexity from `O(N^2)` to `O(N)`.
- **Visualizer** – Built-in Real-time simulation demo powered by Raylib.

---

### 🦾 Character Locomotion System  
**Advanced UE5 Locomotion Plugin** implementing procedural and physics-based movement systems.  
[![CLS](https://img.shields.io/badge/Character_Locomotion_System-000000?style=for-the-badge&logo=github)](https://github.com/1SHAMAY1/Plugin-CharacterLocomotionSystem)

- **Modular Parkour Pipeline** – Clean C++ runtime execution handler for climbing, vaulting, mantling, and wall-running.
- **Physics Integration** – Blends keyframe animations with real-time physical constraints for realistic collisions.

---

## 🧠 Distributed AI & Machine Learning

### 🕸️ SYNAPSE  
**High-performance decentralized swarm intelligence framework** built for multi-agent coordination.  
[![SYNAPSE](https://img.shields.io/badge/SYNAPSE-000000?style=for-the-badge&logo=github)](https://github.com/1SHAMAY1/SYNAPSE)

- **Autonomous Agent Swarms** – Implements decentralized communication layers allowing agents to dynamically distribute workloads.
- **Consensus Protocols** – Integrates lightweight state synchronization and self-healing task routing between active nodes.
- **Event-Driven Pipeline** – Optimized async runtime architecture handling massive message passing between concurrent agents.

---

### 📈 ML Predictor  
**Swarm-based machine learning modeling and analytics platform**.  
[![ML Predictor](https://img.shields.io/badge/ML_Predictor-000000?style=for-the-badge&logo=github)](https://github.com/1SHAMAY1/ML_Predictor)

- **Collective Intelligence Models** – Leverages swarm intelligence to optimize model weights and parameters across distributed prediction nodes.
- **High-Fidelity Training** – Custom neural network topologies implemented to analyze temporal trends with optimized training epochs.

---

### 🔋 AI Battery Health  
**Deep learning predictive diagnostic tool** for evaluating State of Health (SoH) and Remaining Useful Life (RUL) of lithium-ion cells.  
[![AI Battery](https://img.shields.io/badge/AI_Battery_Health-000000?style=for-the-badge&logo=github)](https://github.com/1SHAMAY1/AI_Battery_Health)

- **Temporal Networks** – Employs recurrent networks (LSTM/GRU architectures) to model non-linear electrochemical degradation curves.
- **Thermodynamic Modeling** – Integrates real-time cell thermal profiles with current/voltage curves to predict thermal runaway risks.

---

# 📊 GitHub Stats & Badges (Unbreakable)

<p align="center">
  <img alt="Followers" src="https://img.shields.io/github/followers/1SHAMAY1?label=Followers&style=social" />
  <img alt="Stars" src="https://img.shields.io/github/stars/1SHAMAY1?label=Stars&style=social" />
  <img alt="Views" src="https://komarev.com/ghpvc/?username=1SHAMAY1&color=blue" />
</p>

**Top languages:**  
C++ • SystemVerilog • C • Python • GLSL/HLSL  

---

# 🎯 What I'm Building
- **Hardware Accelerators** – Extending SIMT GPU instruction pipelines to handle wider matrices for AI math operations.
- **Velox Engine Modules** – Further optimizations on Broadphase algorithms and multi-threaded constraint solvers.
- **Swarm Robotics & AI** – Applying Synapse algorithms to real-world edge controllers and simulation environments.

---

# 🔗 Connect  
<p>
  <a href="https://www.linkedin.com/in/shankharaj-datta-45921a28a/" target="_blank">
    <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white" />
  </a>
</p>

---

<h3 align="center">⭐ If you like my work, consider starring a repository!</h3>
